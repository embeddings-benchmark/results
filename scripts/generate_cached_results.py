#!/usr/bin/env python3
"""
Script to generate __cached_results.json.gz for the MTEB leaderboard.

This pre-generates the cached results file that the leaderboard uses,
which can save 100+ seconds on fresh leaderboard builds.

Usage:
    python generate_cached_results.py

Output:
    Creates __cached_results.json.gz and __cached_results.parquet in
    the remote repo root directory. The parquet file is published
    alongside the gzip JSON so the leaderboard loader in mteb can
    migrate to the smaller, columnar format without a flag day; older
    mteb releases keep reading the gzip JSON unchanged.
"""

import gzip
import json
import logging
import sys
import time
from pathlib import Path

import mteb
import pyarrow as pa
import pyarrow.parquet as pq
from mteb.cache import ResultCache
from mteb.results import BenchmarkResults

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)


# Columns for the flat one-row-per-(model x task x split x subset) layout.
# Kept in sync with the BenchmarkResults / ModelResult / TaskResult Pydantic
# schemas in mteb. This is intentionally lossless w.r.t. the only_main_score
# JSON dump produced below, so the parquet round-trips back into a
# BenchmarkResults object.
_PARQUET_SCHEMA = pa.schema(
    [
        ("model_name", pa.string()),
        ("model_revision", pa.string()),
        ("experiment_name", pa.string()),
        ("task_name", pa.string()),
        ("dataset_revision", pa.string()),
        ("mteb_version", pa.string()),
        ("evaluation_time", pa.float64()),
        ("kg_co2_emissions", pa.float64()),
        ("date", pa.timestamp("us", tz="UTC")),
        ("split", pa.string()),
        ("hf_subset", pa.string()),
        ("languages", pa.list_(pa.string())),
        ("main_score", pa.float64()),
    ]
)


def _benchmark_results_to_table(all_results: BenchmarkResults) -> pa.Table:
    """Flatten BenchmarkResults into a long Arrow table.

    One row per (model_result, task_result, split, subset_score) tuple. The
    flattening loops mirror BenchmarkResults._build_pre_agg_df in mteb but
    keep every per-row metadata field so the file is a true replacement
    for the JSON dump.
    """
    cols: dict[str, list] = {field.name: [] for field in _PARQUET_SCHEMA}

    for model_result in all_results.model_results:
        model_name = model_result.model_name
        model_revision = model_result.model_revision
        experiment_name = getattr(model_result, "experiment_name", None)
        for task_result in model_result.task_results:
            task_name = task_result.task_name
            dataset_revision = task_result.dataset_revision
            mteb_version = task_result.mteb_version
            evaluation_time = task_result.evaluation_time
            kg_co2_emissions = task_result.kg_co2_emissions
            date = task_result.date
            for split, score_list in task_result.scores.items():
                for score in score_list:
                    cols["model_name"].append(model_name)
                    cols["model_revision"].append(model_revision)
                    cols["experiment_name"].append(experiment_name)
                    cols["task_name"].append(task_name)
                    cols["dataset_revision"].append(dataset_revision)
                    cols["mteb_version"].append(mteb_version)
                    cols["evaluation_time"].append(evaluation_time)
                    cols["kg_co2_emissions"].append(kg_co2_emissions)
                    cols["date"].append(date)
                    cols["split"].append(split)
                    cols["hf_subset"].append(score.get("hf_subset", "default"))
                    cols["languages"].append(list(score.get("languages", [])))
                    cols["main_score"].append(score.get("main_score"))

    return pa.table(cols, schema=_PARQUET_SCHEMA)


def generate_cached_results():
    """Generate the cached results JSON file."""
    start_time = time.time()
    
    logger.info("Initializing ResultCache...")
    cache = ResultCache(Path(__file__).parent.parent)
    
    # The remote repo should already be cloned from previous runs
    logger.info("Using existing remote results repository...")
    
    # Load all model names
    logger.info("Getting all model names...")
    models_start = time.time()
    all_model_names = [model_meta.name for model_meta in mteb.get_model_metas()]
    models_time = time.time() - models_start
    logger.info(f"Found {len(all_model_names)} models in {models_time:.2f}s")
    
    # Load results for all models
    logger.info("Loading results from cache...")
    load_start = time.time()
    all_results = cache.load_results(
        models=all_model_names,
        only_main_score=True,
        require_model_meta=False,
        include_remote=True,
    )
    load_time = time.time() - load_start
    logger.info(f"Loaded results in {load_time:.2f}s")
    
    # Serialize to JSON and write to gzip file
    repo_root = Path(__file__).parent.parent
    output_path = repo_root / "__cached_results.json.gz"
    logger.info(f"Serializing to JSON and writing to {output_path}...")
    write_start = time.time()
    json_str = all_results.model_dump_json()
    with gzip.open(output_path, 'wt', encoding='utf-8') as f:
        f.write(json_str)
    write_time = time.time() - write_start
    logger.info(f"Serialized and written in {write_time:.2f}s")
    
    # Report file size
    file_size_mb = output_path.stat().st_size / (1024 * 1024)
    uncompressed_size_mb = len(json_str) / (1024 * 1024)
    compression_ratio = (1 - file_size_mb / uncompressed_size_mb) * 100
    logger.info(f"Generated {output_path} ({file_size_mb:.1f} MB)")
    logger.info(f"Uncompressed size: {uncompressed_size_mb:.1f} MB")
    logger.info(f"Compression ratio: {compression_ratio:.1f}%")

    logger.info("--------------------------------")
    # Also emit a Parquet file alongside the gzip JSON. This is purely
    # additive: nothing reads it yet. The leaderboard loader in mteb
    # (mteb/cache.py:_load_from_cache) keeps using the gzip JSON until a
    # follow-up release teaches it to prefer parquet.
    parquet_path = repo_root / "__cached_results.parquet"
    logger.info(f"Building Arrow table for {parquet_path}...")
    parquet_start = time.time()
    table = _benchmark_results_to_table(all_results)
    table_build_time = time.time() - parquet_start
    logger.info(
        f"Built Arrow table with {table.num_rows} rows in {table_build_time:.2f}s"
    )

    write_parquet_start = time.time()
    pq.write_table(
        table,
        parquet_path,
        compression="zstd",
        compression_level=3,
        use_dictionary=["model_name", "task_name", "split", "hf_subset"],
    )
    write_parquet_time = time.time() - write_parquet_start
    parquet_size_mb = parquet_path.stat().st_size / (1024 * 1024)
    logger.info(f"Wrote {parquet_path} in {write_parquet_time:.2f}s")
    logger.info(f"Generated {parquet_path} ({parquet_size_mb:.1f} MB)")

    # Smoke test: read back and assert row counts match. Cheap (sub-second)
    # and catches schema regressions before they hit the cached-data branch.
    read_back = pq.read_table(parquet_path)
    if read_back.num_rows != table.num_rows:
        raise RuntimeError(
            f"Parquet round-trip row mismatch: wrote {table.num_rows}, "
            f"read back {read_back.num_rows}"
        )
    logger.info(f"Parquet round-trip OK ({read_back.num_rows} rows)")

    total_time = time.time() - start_time
    logger.info(f"Total time: {total_time:.2f}s")

    return output_path, parquet_path


if __name__ == "__main__":
    try:
        json_gz_path, parquet_path = generate_cached_results()
        logger.info(f"✅ Success! Generated {json_gz_path} and {parquet_path}")
    except Exception as e:
        logger.error(f"❌ Failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

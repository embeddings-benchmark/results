#!/usr/bin/env python3
"""Push the leaderboard results to the HF dataset, one subset per scope.

* ``default`` — every result, deduped across benchmarks.
* one subset per benchmark (slug of ``benchmark.name``), already
  validated against the benchmark's tasks (eval splits + hf subsets).

Each subset goes up as its own HF dataset config via
``Dataset.push_to_hub(config_name=...)``. ``super_squash_history``
afterwards collapses the burst of per-subset commits into one so the
cache repo stays small.

Requires the destination dataset to flag ``*.parquet`` as LFS in its
``.gitattributes`` — otherwise commits fail with
``FileNotFoundError: tmpXXXX.parquet`` (see
:file:`scripts/PUSH_BUG_NOTES.md` for the upstream root cause).

The leaderboard API loads what it needs with
``load_dataset(repo_id, name=<slug> | "default", split="train")``.

Usage::

    # Local: rely on `hf auth login`'s cached token.
    python scripts/push_leaderboard_parquet.py

    # CI: pass the token explicitly.
    HF_TOKEN=hf_xxx python scripts/push_leaderboard_parquet.py

Environment:
    HF_TOKEN     write-scoped HF token. Optional — when unset,
                 huggingface_hub falls back to the cached login from
                 ``hf auth login``.
    RESULTS_DIR  path to the local results directory; defaults to
                 ``<repo root>/results``.
    REPO_ID      dataset repo to push to; defaults to ``mteb/results``.
"""

from __future__ import annotations

import logging
import os
from pathlib import Path

import mteb
from huggingface_hub import HfApi
from mteb.cache import ResultCache
from mteb.cache.result_cache import _slug_benchmark_name

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
logger = logging.getLogger(__name__)

DEFAULT_REPO_ID = "mteb/results"
DEFAULT_SPLIT = "default"


def main() -> int:
    # Optional: missing env var means huggingface_hub picks up the
    # token saved by `hf auth login`.
    token = os.environ.get("HF_TOKEN")
    repo_id = os.environ.get("REPO_ID", DEFAULT_REPO_ID)
    results_dir = Path(
        os.environ.get(
            "RESULTS_DIR",
            Path(__file__).resolve().parent.parent / "results",
        )
    ).resolve()
    if not results_dir.is_dir():
        logger.error("results dir not found: %s", results_dir)
        return 1

    # Point ResultCache at the checkout — `<cache_path>/results/` is
    # where the loader looks, and `results_dir.parent` is the checkout
    # root. `include_remote=False` keeps us off GitHub.
    cache = ResultCache(cache_path=results_dir.parent)

    # Load every result once. Per-benchmark splits below come from
    # `results.select_tasks(...)` on this same object, which runs
    # `validate_and_filter_scores` per task — so each per-benchmark
    # subset is already restricted to its tasks' eval_splits /
    # hf_subsets without re-walking the filesystem.
    logger.info("Loading all results from %s", cache.cache_path / "results")
    all_results = cache.load_results(
        require_model_meta=False,
        include_remote=False,
        only_main_score=True,
    )

    # 1. Default split = the full all-results dump.
    splits = {DEFAULT_SPLIT: all_results._to_dataset()}
    logger.info("  %s: %d rows", DEFAULT_SPLIT, len(splits[DEFAULT_SPLIT]))

    # 2. One split per benchmark via in-memory selection.
    benchmarks = mteb.get_benchmarks()
    logger.info("Building per-benchmark splits for %d benchmarks", len(benchmarks))
    for bench in benchmarks:
        ds = all_results.select_tasks(bench.tasks)._to_dataset()
        if len(ds) == 0:
            logger.info("  %s: 0 rows, skipping", bench.name)
            continue
        # HF split names disallow `(`, `,`, etc — slug to a safe form.
        # `_slug_benchmark_name` is the same transform the API uses to
        # recover the original benchmark name on the consumer side.
        splits[_slug_benchmark_name(bench.name)] = ds
        logger.info("  %s: %d rows", bench.name, len(ds))

    api = HfApi(token=token)
    api.create_repo(repo_id=repo_id, repo_type="dataset", exist_ok=True)

    logger.info("Pushing %d subsets to %s", len(splits), repo_id)
    for name, ds in splits.items():
        ds.push_to_hub(
            repo_id,
            config_name=name,
            token=token,
            commit_message=f"Update subset {name}",
        )

    # Squash so the repo stays at one commit; each per-subset push is
    # its own commit, and this dataset is purely a cache.
    api.super_squash_history(repo_id=repo_id, repo_type="dataset", branch="main")
    logger.info("Squashed %s@main to a single commit", repo_id)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

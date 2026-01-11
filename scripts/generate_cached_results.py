#!/usr/bin/env python3
"""
Script to generate __cached_results.json.gz for the MTEB leaderboard.

This pre-generates the cached results file that the leaderboard uses,
which can save 100+ seconds on fresh leaderboard builds.

Usage:
    python generate_cached_results.py

Output:
    Creates __cached_results.json.gz in the remote repo root directory
"""

import gzip
import json
import logging
import sys
import time
from pathlib import Path

import mteb
from mteb.cache import ResultCache

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)


def generate_cached_results():
    """Generate the cached results JSON file."""
    start_time = time.time()
    
    logger.info("Initializing ResultCache...")
    cache = ResultCache(Path(__file__).parent.parent)
    
    # The remote repo should already be cloned from previous runs
    logger.info("Using existing remote results repository...")
    
    # Load all model metas (not just names)
    # Passing ModelMeta objects ensures filtering uses both name AND revision,
    # which avoids loading no_revision_available folders when a proper revision exists
    logger.info("Getting all model metas...")
    models_start = time.time()
    all_model_metas = [
        model_meta
        for model_meta in mteb.get_model_metas()
        if model_meta.name is not None
    ]
    models_time = time.time() - models_start
    logger.info(f"Found {len(all_model_metas)} models in {models_time:.2f}s")

    # Load results for all models
    logger.info("Loading results from cache...")
    load_start = time.time()
    all_results = cache.load_results(
        models=all_model_metas,
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
    
    total_time = time.time() - start_time
    logger.info(f"Total time: {total_time:.2f}s")
    
    return output_path


if __name__ == "__main__":
    try:
        output_file = generate_cached_results()
        logger.info(f"✅ Success! Generated {output_file}")
    except Exception as e:
        logger.error(f"❌ Failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

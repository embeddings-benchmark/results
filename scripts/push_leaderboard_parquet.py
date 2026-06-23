#!/usr/bin/env python
from __future__ import annotations

import logging
from pathlib import Path

from mteb.cache import ResultCache

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
logger = logging.getLogger(__name__)

DEFAULT_REPO_ID = "mteb/results"


def main():
    results_dir = Path(
        Path(__file__).resolve().parent.parent
    ).resolve()
    if not results_dir.is_dir():
        raise RuntimeError(f"Results dir not found: {results_dir}")

    cache = ResultCache(cache_path=results_dir)
    logger.info("Loading all results from %s", cache.cache_path)
    all_results = cache.load_results(
        require_model_meta=False,
        include_remote=False,
        only_main_score=True,
    )

    ds = all_results._to_dataset()
    logger.info("  %d rows", len(ds))
    ds.push_to_hub(DEFAULT_REPO_ID)


if __name__ == "__main__":
    main()

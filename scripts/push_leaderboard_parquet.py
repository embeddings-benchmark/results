#!/usr/bin/env python
from __future__ import annotations

import logging
import os
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
        os.environ.get(
            "RESULTS_DIR",
            Path(__file__).resolve().parent.parent / "results",
        )
    ).resolve()
    if not results_dir.is_dir():
        raise RuntimeError(f"Results dir not found: {results_dir}")

    cache = ResultCache(cache_path=results_dir.parent)
    logger.info("Loading all results from %s", cache.cache_path / "results")
    all_results = cache.load_results(
        require_model_meta=False,
        include_remote=False,
        only_main_score=True,
    )

    ds = all_results._to_dataset()
    logger.info("  %s: %d rows", len(ds))
    ds.push_to_hub(DEFAULT_REPO_ID)


if __name__ == "__main__":
    main()

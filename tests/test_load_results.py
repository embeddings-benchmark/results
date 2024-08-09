import os
from pathlib import Path

import mteb


def test_load_results():
    """Ensures that files can be loaded using MTEB"""
    tests_path = Path(__file__).parent.parent / "results"

    os.environ["MTEB_CACHE"] = str(tests_path)

    results = mteb.load_results(download_latest=False)

    assert isinstance(results, dict)
    for model in results:
        assert isinstance(results[model], dict)
        for revision in results[model]:
            assert isinstance(results[model][revision], list)
            for result in results[model][revision]:
                assert isinstance(result, mteb.MTEBResults)

    known_model = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    known_revision = "bf3bf13ab40c3157080a7ab344c831b9ad18b5eb"
    assert known_model in results
    assert known_revision in results[known_model]

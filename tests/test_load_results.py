import os
from pathlib import Path

import mteb
from mteb import TaskResult


def test_load_results():
    """Ensures that files can be loaded using MTEB"""
    tests_path = Path(__file__).parent / "mock_cache_dir"

    os.environ["MTEB_CACHE"] = str(tests_path)

    results = mteb.load_results(download_latest=False)

    assert isinstance(results, mteb.BenchmarkResults)
    for model_results in results.model_results:
        for model_result in model_results:
            assert isinstance(model_result, TaskResult)


def test_load_results_mteb():
    test_model_meta = mteb.get_model_meta("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
    model_results = mteb.load_results(models=[test_model_meta])
    model_result = model_results[0]
    assert model_result.model_name == test_model_meta.name
    assert model_result.model_revision == test_model_meta.revision

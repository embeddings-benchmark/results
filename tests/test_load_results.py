import os
from pathlib import Path

import mteb
from mteb.load_results.task_results import TaskResult


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
    test_model_name = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    model_results = mteb.load_results(models=[test_model_name])
    model_result = model_results[0]
    assert model_result.model_name == test_model_name
    assert model_result.model_revision == "8d6b950845285729817bf8e1af1861502c2fed0c"

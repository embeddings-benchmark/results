from pathlib import Path
import pytest
from datasets import load_dataset
from results import MODELS


@pytest.mark.parametrize("model", MODELS)
@pytest.mark.skip(reason="If new model added this test will fail")
def test_load_results_from_datasets(model):
    """Ensures that all models can be imported from dataset"""
    path = Path(__file__).parent.parent / "results.py"
    ds = load_dataset(str(path.absolute()), model, trust_remote_code=True)

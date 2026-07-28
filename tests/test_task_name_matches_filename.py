import json
from pathlib import Path

import pytest

from tests.test_correct_folder_structure import results_folder

model_rev_pairs = [
    (model_folder, rev_folder)
    for model_folder in results_folder.glob("*")
    for rev_folder in model_folder.glob("*")
    if model_folder.name not in [".DS_Store"] and rev_folder.name not in [".DS_Store"]
]


@pytest.mark.parametrize("model_rev_pair", model_rev_pairs)
def test_task_name_matches_filename(model_rev_pair):
    """Verify that the filename (without extension) matches the 'task_name' field in each result JSON."""
    _, rev_folder = model_rev_pair

    for json_file in rev_folder.glob("*.json"):
        if json_file.name == "model_meta.json":
            continue

        with json_file.open("r") as f:
            data = json.load(f)

        task_name = data.get("task_name") or data.get("mteb_dataset_name")
        assert task_name is not None, (
            f"Missing 'task_name' (or legacy 'mteb_dataset_name') key in {json_file}"
        )
        assert json_file.stem == task_name, (
            f"Filename '{json_file.stem}' does not match task_name '{task_name}' in {json_file}"
        )

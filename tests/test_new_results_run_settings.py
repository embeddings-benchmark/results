import json
from pathlib import Path

import pytest

from tests.git_utils import REPO_ROOT, get_base_ref
from tests.run_settings_check import (
    MIN_MTEB_VERSION,
    RUN_SETTINGS_FILENAME,
    SUBMISSION_GUIDE,
    get_changed_result_files,
    validate_result_file,
)


def test_new_results_have_run_settings_and_mteb_version():
    try:
        base_ref = get_base_ref()
    except RuntimeError as e:
        pytest.skip(str(e))

    changed = get_changed_result_files(base_ref)
    if not changed:
        pytest.skip("No added or modified result JSON files found.")

    errors = []
    for relative_path in changed:
        errors += validate_result_file(REPO_ROOT / relative_path, relative_path)

    assert not errors, (
        "\n".join(f"  - {e}" for e in errors) + f"\n\nSee {SUBMISSION_GUIDE}"
    )


def write_result(
    directory: Path,
    *,
    subsets: tuple[str, ...] = ("default",),
    splits: tuple[str, ...] = ("test",),
    version: str = str(MIN_MTEB_VERSION),
) -> Path:
    blocks = [
        {"hf_subset": subset, "main_score": 0.5, "languages": ["eng-Latn"]}
        for subset in subsets
    ]
    path = directory / "DemoTask.json"
    path.write_text(
        json.dumps(
            {
                "dataset_revision": "abc123",
                "task_name": "DemoTask",
                "mteb_version": version,
                "evaluation_time": 1.0,
                "scores": dict.fromkeys(splits, blocks),
            }
        )
    )
    return path


def write_run_settings(directory: Path, **fields) -> None:
    (directory / RUN_SETTINGS_FILENAME).write_text(
        json.dumps({"task": "DemoTask", **fields}) + "\n"
    )


def validate(result_path: Path) -> list[str]:
    return validate_result_file(result_path, "results/model/revision/DemoTask.json")


@pytest.mark.parametrize(
    "fields",
    [
        pytest.param({"split": "test", "subset": "en"}, id="legacy-singular"),
        pytest.param(
            {"split": "test", "subsets": ["en", "de"]}, id="collapsed-subsets"
        ),
        pytest.param({"splits": ["test"], "subsets": ["en"]}, id="current-plural"),
        pytest.param({"splits": ["test"], "subset": "en"}, id="mixed"),
    ],
)
def test_accepts_every_run_settings_shape(tmp_path, fields):
    result_path = write_result(tmp_path, subsets=("en",))
    write_run_settings(tmp_path, **fields)

    assert validate(result_path) == []


def test_partial_coverage_is_reported_per_file(tmp_path):
    result_path = write_result(tmp_path, subsets=("en", "nl", "de", "fr"))
    write_run_settings(tmp_path, splits=["test"], subsets=["en", "de"])

    errors = validate(result_path)

    assert len(errors) == 1
    assert "2 split/subset(s) missing" in errors[0]
    assert "test/nl" in errors[0] and "test/fr" in errors[0]
    assert "test/en" not in errors[0] and "test/de" not in errors[0]


def test_coverage_is_per_split(tmp_path):
    result_path = write_result(tmp_path, splits=("test", "validation"))
    write_run_settings(tmp_path, splits=["test"], subsets=["default"])

    errors = validate(result_path)
    assert len(errors) == 1
    assert "validation/default" in errors[0]

    write_run_settings(tmp_path, splits=["test", "validation"], subsets=["default"])
    assert validate(result_path) == []

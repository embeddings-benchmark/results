import json
import os
import re
import subprocess
import sys
from pathlib import Path

import pytest


REPO_PATH = Path(__file__).parents[1]
MIN_MTEB_VERSION = (2, 0, 0)


def run_git_command(args: list[str]) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=REPO_PATH,
        text=True,
        capture_output=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {result.stderr}")
    return result.stdout


def get_base_ref() -> str:
    base_ref = os.environ.get("PR_BASE_SHA")
    if base_ref:
        return base_ref

    for ref in ("origin/main", "main"):
        result = subprocess.run(
            ["git", "merge-base", ref, "HEAD"],
            cwd=REPO_PATH,
            text=True,
            capture_output=True,
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()

    raise RuntimeError("Could not find a valid base ref.")


def get_added_result_files(base_ref: str) -> list[str]:
    changed_files = run_git_command(
        ["diff", "--name-only", "--diff-filter=A", base_ref, "HEAD", "--", "results"]
    ).splitlines()

    added_results = []
    for relative_path in changed_files:
        path = Path(relative_path)
        if path.suffix == ".json" and path.name != "model_meta.json":
            added_results.append(relative_path)
    return sorted(added_results)


def parse_version(value: object) -> tuple[int, int, int] | None:
    if not isinstance(value, str):
        return None

    parts = value.strip().split(".")
    version_parts = []
    for part in parts[:3]:
        match = re.match(r"^(\d+)", part)
        if not match:
            return None
        version_parts.append(int(match.group(1)))

    while len(version_parts) < 3:
        version_parts.append(0)

    return tuple(version_parts)


def validate_mteb_version(value: object, source: str) -> list[str]:
    parsed = parse_version(value)
    if parsed is None:
        return [f"{source} must have a parseable MTEB version, got {value!r}."]
    if parsed <= MIN_MTEB_VERSION:
        return [f"{source} must use MTEB >2.0.0, got {value!r}."]
    return []


def score_block_keys(
    result_data: dict,
    relative_path: str,
) -> tuple[list[tuple[str, str, str]], list[str]]:
    errors = []
    task_name = result_data.get("task_name") or result_data.get("mteb_dataset_name")
    if not isinstance(task_name, str) or not task_name:
        return [], [f"{relative_path} must define task_name."]

    scores = result_data.get("scores")
    if not isinstance(scores, dict):
        return [], [f"{relative_path} must define scores as an object."]

    keys = []
    for split, score_blocks in scores.items():
        if not isinstance(score_blocks, list):
            errors.append(f"{relative_path} scores[{split!r}] must be a list.")
            continue

        for index, score_block in enumerate(score_blocks):
            if not isinstance(score_block, dict):
                errors.append(
                    f"{relative_path} scores[{split!r}][{index}] must be an object."
                )
                continue

            subset = score_block.get("hf_subset")
            if not isinstance(subset, str) or not subset:
                errors.append(
                    f"{relative_path} scores[{split!r}][{index}] must define hf_subset."
                )
                continue

            keys.append((task_name, split, subset))
            errors.extend(
                validate_mteb_version(
                    score_block.get("mteb_version"),
                    f"{relative_path} scores[{split!r}][{index}].mteb_version",
                )
            )

    if not keys and not errors:
        errors.append(f"{relative_path} must contain at least one score block.")

    return keys, errors


def load_json(path: Path, relative_path: str) -> tuple[dict | None, list[str]]:
    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return None, [f"{relative_path} is not valid JSON: {e}"]
    except OSError as e:
        return None, [f"{relative_path} could not be read: {e}"]

    if not isinstance(data, dict):
        return None, [f"{relative_path} must contain a JSON object."]
    return data, []


def load_run_settings(
    path: Path,
    relative_path: str,
) -> tuple[dict[tuple[str, str, str], list[dict]], list[str]]:
    if not path.exists():
        return {}, [
            f"{relative_path} is missing run_settings.jsonl in the same directory."
        ]

    entries = {}
    errors = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as e:
        return {}, [f"{relative_path} run_settings.jsonl could not be read: {e}"]

    for line_number, line in enumerate(lines, start=1):
        if not line.strip():
            continue

        try:
            entry = json.loads(line)
        except json.JSONDecodeError as e:
            errors.append(
                f"{relative_path} run_settings.jsonl line {line_number} is not valid JSON: {e}"
            )
            continue

        if not isinstance(entry, dict):
            errors.append(
                f"{relative_path} run_settings.jsonl line {line_number} must be an object."
            )
            continue

        key = (entry.get("task"), entry.get("split"), entry.get("subset"))
        if not all(isinstance(value, str) and value for value in key):
            errors.append(
                f"{relative_path} run_settings.jsonl line {line_number} "
                "must define task, split, and subset."
            )
            continue

        entries.setdefault(key, []).append(entry)

    if not entries and not errors:
        errors.append(
            f"{relative_path} run_settings.jsonl must contain at least one entry."
        )

    return entries, errors


def validate_result_file(result_path: Path, relative_path: str) -> list[str]:
    result_data, errors = load_json(result_path, relative_path)
    if result_data is None:
        return errors

    errors.extend(
        validate_mteb_version(
            result_data.get("mteb_version"),
            f"{relative_path} mteb_version",
        )
    )

    score_keys, score_errors = score_block_keys(result_data, relative_path)
    errors.extend(score_errors)

    run_settings, run_settings_errors = load_run_settings(
        result_path.parent / "run_settings.jsonl",
        relative_path,
    )
    errors.extend(run_settings_errors)

    for key in score_keys:
        matching_entries = run_settings.get(key, [])
        if not matching_entries:
            errors.append(
                f"{relative_path} has no matching run_settings.jsonl entry for "
                f"task={key[0]!r}, split={key[1]!r}, subset={key[2]!r}."
            )
            continue

        for entry_index, entry in enumerate(matching_entries):
            version = entry.get("version")
            mteb_version = version.get("mteb") if isinstance(version, dict) else None
            errors.extend(
                validate_mteb_version(
                    mteb_version,
                    f"{relative_path} run_settings entry {entry_index} version.mteb",
                )
            )

    return errors


def test_added_result_files_have_run_settings_and_mteb_version():
    base_ref = get_base_ref()
    added_result_files = get_added_result_files(base_ref)

    if not added_result_files:
        pytest.skip("No newly added result JSON files found.")

    errors = []
    for relative_path in added_result_files:
        errors.extend(validate_result_file(REPO_PATH / relative_path, relative_path))

    assert not errors, "\n".join(errors)


def write_valid_result(directory: Path, *, version: str = "2.1.0") -> Path:
    result_path = directory / "DemoTask.json"
    result_path.parent.mkdir(parents=True, exist_ok=True)
    result_path.write_text(
        json.dumps(
            {
                "task_name": "DemoTask",
                "mteb_version": version,
                "scores": {
                    "test": [
                        {
                            "hf_subset": "default",
                            "main_score": 0.5,
                            "mteb_version": version,
                        }
                    ]
                },
            }
        ),
        encoding="utf-8",
    )
    return result_path


def write_run_settings(
    directory: Path,
    *,
    task: str = "DemoTask",
    version: str = "2.1.0",
) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    entry = {
        "task": task,
        "split": "test",
        "subset": "default",
        "version": {"mteb": version},
    }
    (directory / "run_settings.jsonl").write_text(
        json.dumps(entry) + "\n",
        encoding="utf-8",
    )


def test_validate_result_file_accepts_matching_v2_run_settings(tmp_path):
    result_path = write_valid_result(tmp_path)
    write_run_settings(tmp_path)

    assert validate_result_file(result_path, "results/model/revision/DemoTask.json") == []


def test_get_added_result_files_filters_to_task_result_json(monkeypatch):
    def fake_run_git_command(args):
        assert "--diff-filter=A" in args
        return "\n".join(
            [
                "results/model/revision/DemoTask.json",
                "results/model/revision/model_meta.json",
                "results/model/revision/run_settings.jsonl",
                "README.md",
            ]
        )

    monkeypatch.setattr(sys.modules[__name__], "run_git_command", fake_run_git_command)

    assert get_added_result_files("base") == ["results/model/revision/DemoTask.json"]


def test_validate_result_file_requires_run_settings(tmp_path):
    result_path = write_valid_result(tmp_path)

    errors = validate_result_file(result_path, "results/model/revision/DemoTask.json")

    assert any("missing run_settings.jsonl" in error for error in errors)


def test_validate_result_file_rejects_old_mteb_versions(tmp_path):
    result_path = write_valid_result(tmp_path, version="1.38.0")
    write_run_settings(tmp_path, version="1.38.0")

    errors = validate_result_file(result_path, "results/model/revision/DemoTask.json")

    assert any("mteb_version must use MTEB >2.0.0" in error for error in errors)
    assert any("version.mteb must use MTEB >2.0.0" in error for error in errors)


def test_validate_result_file_requires_matching_run_settings_tuple(tmp_path):
    result_path = write_valid_result(tmp_path)
    write_run_settings(tmp_path, task="OtherTask")

    errors = validate_result_file(result_path, "results/model/revision/DemoTask.json")

    assert any("no matching run_settings.jsonl entry" in error for error in errors)


def test_validate_result_file_rejects_malformed_run_settings(tmp_path):
    result_path = write_valid_result(tmp_path)
    (tmp_path / "run_settings.jsonl").write_text("{bad json\n", encoding="utf-8")

    errors = validate_result_file(result_path, "results/model/revision/DemoTask.json")

    assert any("run_settings.jsonl line 1 is not valid JSON" in error for error in errors)

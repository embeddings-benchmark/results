import json
from pathlib import Path

from mteb import TaskResult
from mteb.results.task_result import _expand_run_settings_entry
from packaging.version import Version

from tests.git_utils import _run_git

MIN_MTEB_VERSION = Version("2.0.0")
RUN_SETTINGS_FILENAME = "run_settings.jsonl"
SUBMISSION_GUIDE = "https://docs.mteb.org/contributing/submitting_results/"


def get_changed_result_files(base_ref: str) -> list[str]:
    result = _run_git(
        "diff",
        "--name-status",
        "-M",
        "--diff-filter=AMR",
        base_ref,
        "HEAD",
        "--",
        "*.json",
    )
    if result.returncode != 0:
        raise RuntimeError(f"git diff failed: {result.stderr}")

    paths = []
    for line in result.stdout.splitlines():
        fields = line.split("\t")
        if len(fields) < 2 or fields[0] == "R100":  # a pure move resubmits nothing
            continue
        paths.append(fields[-1])  # for a rename this is the destination
    return sorted(
        path
        for path in paths
        if path.startswith("results/") and not path.endswith("model_meta.json")
    )


def load_task_result(
    result_path: Path, relative_path: str
) -> tuple[TaskResult | None, list[str]]:
    try:
        return TaskResult.from_disk(result_path), []
    except Exception as e:  # noqa: BLE001
        return None, [f"{relative_path} is not a valid mteb TaskResult: {e}"]


def validate_mteb_version(version: str | None, relative_path: str) -> list[str]:
    parsed = TaskResult._parse_mteb_version_min(version) if version else None
    if parsed is None:
        return [f"{relative_path} has no usable mteb_version (got {version!r})."]
    if parsed < MIN_MTEB_VERSION:
        return [f"{relative_path} must use MTEB >={MIN_MTEB_VERSION}, got {version!r}."]
    return []


def load_run_settings(
    path: Path, relative_path: str
) -> tuple[set[tuple[str, str, str]], list[str]]:
    if not path.exists():
        return set(), [f"{relative_path} is missing {RUN_SETTINGS_FILENAME}."]

    covered: set[tuple[str, str, str]] = set()
    errors = []
    for line_number, line in enumerate(path.read_text().splitlines(), start=1):
        if not line.strip():
            continue

        source = f"{relative_path} {RUN_SETTINGS_FILENAME} line {line_number}"
        try:
            entry = json.loads(line)
        except json.JSONDecodeError as e:
            errors.append(f"{source} is not valid JSON: {e}")
            continue
        if not isinstance(entry, dict):
            errors.append(f"{source} must be an object.")
            continue

        keys = [key for key, _, _ in _expand_run_settings_entry(entry)]
        if not keys or any(not task for task, _, _ in keys):
            errors.append(f"{source} must define task, split(s) and subset(s).")
            continue
        covered.update(keys)

    if not covered and not errors:
        errors.append(f"{relative_path} {RUN_SETTINGS_FILENAME} has no entries.")
    return covered, errors


def validate_result_file(result_path: Path, relative_path: str) -> list[str]:
    task_result, errors = load_task_result(result_path, relative_path)
    if task_result is None:
        return errors

    errors += validate_mteb_version(task_result.mteb_version, relative_path)

    covered, run_settings_errors = load_run_settings(
        result_path.parent / RUN_SETTINGS_FILENAME, relative_path
    )
    errors += run_settings_errors
    if not covered:
        return errors

    submitted = {
        (task_result.task_name, split, block["hf_subset"])
        for split, blocks in task_result.scores.items()
        for block in blocks
    }
    missing = sorted(f"{split}/{subset}" for _, split, subset in submitted - covered)
    if missing:
        errors.append(
            f"{relative_path}: {len(missing)} split/subset(s) missing from "
            f"{RUN_SETTINGS_FILENAME}, e.g. {missing[:5]}"
        )
    return errors

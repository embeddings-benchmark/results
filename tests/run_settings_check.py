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


def load_run_settings(path: Path) -> set[tuple[str, str, str]]:
    covered: set[tuple[str, str, str]] = set()
    for line_number, line in enumerate(path.read_text().splitlines(), start=1):
        if not line.strip():
            continue
        try:
            entry = json.loads(line)
        except json.JSONDecodeError as e:
            raise ValueError(f"{path} line {line_number} is not valid JSON: {e}") from e
        covered.update(key for key, _, _ in _expand_run_settings_entry(entry))
    return covered


def validate_result_file(result_path: Path, relative_path: str) -> list[str]:
    task_result, errors = load_task_result(result_path, relative_path)
    if task_result is None:
        return errors

    errors += validate_mteb_version(task_result.mteb_version, relative_path)

    run_settings_path = result_path.parent / RUN_SETTINGS_FILENAME
    if not run_settings_path.exists():
        return errors + [f"{relative_path} is missing {RUN_SETTINGS_FILENAME}."]

    covered = load_run_settings(run_settings_path)

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

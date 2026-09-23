import json
from pathlib import Path

from mteb import TaskResult
from mteb.results.task_result import _expand_run_settings_entry
from packaging.version import Version

from tests.git_utils import REPO_ROOT, get_changed_json_files

# the release that introduced run_settings.jsonl
MIN_MTEB_VERSION = Version("2.14.0")
RUN_SETTINGS_FILENAME = "run_settings.jsonl"
SUBMISSION_GUIDE = (
    "https://docs.mteb.org/contributing/submitting_results/"
)
# one directory can hold tens of thousands of uncovered (task, split, subset)
MAX_ERRORS_PER_DIRECTORY = 10


def is_task_result_path(relative_path: str) -> bool:
    path = Path(relative_path)
    return (
        path.parts[:1] == ("results",)
        and path.suffix == ".json"
        and path.name != "model_meta.json"
    )


def get_changed_result_files(base_ref: str) -> list[str]:
    return [
        relative_path
        for relative_path in get_changed_json_files(base_ref)
        if is_task_result_path(relative_path) and (REPO_ROOT / relative_path).is_file()
    ]


def parse_version(value: object) -> Version | None:
    """Parse a recorded mteb version, or None if it is unusable."""
    if not isinstance(value, str):
        return None
    return TaskResult._parse_mteb_version_min(value)


def validate_mteb_version(value: object, source: str) -> list[str]:
    minimum = str(MIN_MTEB_VERSION)
    parsed = parse_version(value)
    if parsed is None:
        return [f"{source} must have a parseable MTEB version, got {value!r}."]
    if parsed < MIN_MTEB_VERSION:
        return [f"{source} must use MTEB >={minimum}, got {value!r}."]
    return []


def load_task_result(
    result_path: Path,
    relative_path: str,
) -> tuple[TaskResult | None, list[str]]:
    """Load through mteb, which validates the structure and backfills each score
    block's `mteb_version` from the top-level one."""
    try:
        return TaskResult.from_disk(result_path), []
    except Exception as e:  # noqa: BLE001 - pydantic/mteb raise a range of errors
        detail = " ".join(str(e).split())[:200]
        return None, [f"{relative_path} is not a valid mteb TaskResult: {detail}"]


def score_block_keys(
    task_result: TaskResult,
    relative_path: str,
) -> tuple[list[tuple[str, str, str]], list[str]]:
    """(task, split, subset) tuples for every score the result reports."""
    keys = []
    errors = []
    for split, score_blocks in task_result.scores.items():
        for score_block in score_blocks:
            # TaskResult guarantees hf_subset and main_score on every block
            subset = score_block["hf_subset"]
            keys.append((task_result.task_name, split, subset))
            errors.extend(
                validate_mteb_version(
                    score_block.get("mteb_version"),
                    f"{relative_path} scores[{split!r}][{subset!r}].mteb_version",
                )
            )

    return keys, errors


def load_run_settings(
    path: Path,
    relative_path: str,
) -> tuple[dict[tuple[str, str, str], list[dict]], list[str]]:
    """Index a run_settings.jsonl by the (task, split, subset) each row covers.

    Rows are expanded by mteb's own `_expand_run_settings_entry`, so the four
    shapes in the repository are read exactly as mteb reads them: `split`/`subset`
    before v2.18.17, `splits`/`subsets` after, and the `subsets` lists that
    `reduce_large_json_files.collapse_run_settings` merges rows into.
    """
    if not path.exists():
        return {}, [f"{relative_path} is missing {RUN_SETTINGS_FILENAME}."]

    entries: dict[tuple[str, str, str], list[dict]] = {}
    errors = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as e:
        return {}, [f"{relative_path} {RUN_SETTINGS_FILENAME} could not be read: {e}"]

    for line_number, line in enumerate(lines, start=1):
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

        ambiguous = [
            f"{singular}/{plural}"
            for singular, plural in (("split", "splits"), ("subset", "subsets"))
            if singular in entry and plural in entry
        ]
        if ambiguous:
            errors.append(
                f"{source} defines both {' and '.join(ambiguous)}; "
                "mteb writes one or the other."
            )
            continue

        keys = [
            key for key, _settings_key, _settings in _expand_run_settings_entry(entry)
        ]
        if not keys:
            errors.append(f"{source} must define split(s) and subset(s).")
            continue
        if any(not isinstance(task, str) or not task for task, _split, _subset in keys):
            errors.append(f"{source} must define task.")
            continue

        for key in keys:
            entries.setdefault(key, []).append(entry)

    if not entries and not errors:
        errors.append(
            f"{relative_path} {RUN_SETTINGS_FILENAME} must contain at least one entry."
        )

    return entries, errors


def validate_result_file(result_path: Path, relative_path: str) -> list[str]:
    task_result, errors = load_task_result(result_path, relative_path)
    if task_result is None:
        return errors

    errors.extend(
        validate_mteb_version(
            task_result.mteb_version,
            f"{relative_path} mteb_version",
        )
    )

    score_keys, score_errors = score_block_keys(task_result, relative_path)
    errors.extend(score_errors)

    run_settings, run_settings_errors = load_run_settings(
        result_path.parent / RUN_SETTINGS_FILENAME,
        relative_path,
    )
    errors.extend(run_settings_errors)

    if not run_settings:
        # nothing usable to match against; the file-level error above says why
        return errors

    for key in score_keys:
        matching_entries = run_settings.get(key, [])
        if not matching_entries:
            errors.append(
                f"{relative_path} has no matching {RUN_SETTINGS_FILENAME} entry for "
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


def summarize_errors(errors_by_directory: dict[str, list[str]]) -> str:
    """Group errors by result directory and cap them, so CI logs stay readable."""
    total = sum(len(messages) for messages in errors_by_directory.values())
    lines = [f"{total} problem(s) in {len(errors_by_directory)} result directory(ies):"]

    for directory in sorted(errors_by_directory):
        messages = errors_by_directory[directory]
        lines.append(f"\n{directory} ({len(messages)} problem(s)):")
        for message in messages[:MAX_ERRORS_PER_DIRECTORY]:
            lines.append(f"  - {message}")
        if len(messages) > MAX_ERRORS_PER_DIRECTORY:
            lines.append(
                f"  ... and {len(messages) - MAX_ERRORS_PER_DIRECTORY} more here"
            )

    minimum = str(MIN_MTEB_VERSION)
    lines.append(
        f"\n{RUN_SETTINGS_FILENAME} is written by `ResultCache.save_to_cache()` as of "
        f"mteb v{minimum}, but not by the deprecated `MTEB(...).run()` path. Scores "
        f"missing an entry were usually carried over from a cache written by an older "
        f"mteb, or from a run whose {RUN_SETTINGS_FILENAME} was not copied along with "
        f"them. See {SUBMISSION_GUIDE}"
    )

    return "\n".join(lines)

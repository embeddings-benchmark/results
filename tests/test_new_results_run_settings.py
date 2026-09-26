"""Tests for the new-result requirements, and the check itself.

`test_new_results_have_run_settings_and_mteb_version` is the guard that runs
against a PR's diff; everything below it exercises the validation in
`tests/run_settings_check.py` against the result shapes mteb actually writes.
"""

import json
import re
from pathlib import Path

import pytest
from packaging.version import Version

from tests.git_utils import get_base_ref
from tests.run_settings_check import (
    MAX_ERRORS_PER_DIRECTORY,
    REPO_ROOT,
    RUN_SETTINGS_FILENAME,
    get_changed_result_files,
    is_task_result_path,
    parse_version,
    summarize_errors,
    validate_result_file,
)


def test_new_results_have_run_settings_and_mteb_version():
    """The check itself: every result file this PR adds or modifies must be
    produced with mteb>=2.14 and be fully described by a run_settings.jsonl in
    its own directory. Results already on main are never revisited, so the
    requirements apply to new submissions only.
    """
    try:
        base_ref = get_base_ref()
    except RuntimeError as e:
        pytest.skip(str(e))

    changed_result_files = get_changed_result_files(base_ref)
    if not changed_result_files:
        pytest.skip("No added or modified result JSON files found.")

    errors_by_directory: dict[str, list[str]] = {}
    for relative_path in changed_result_files:
        file_errors = validate_result_file(REPO_ROOT / relative_path, relative_path)
        if file_errors:
            directory = str(Path(relative_path).parent)
            errors_by_directory.setdefault(directory, []).extend(file_errors)

    assert not errors_by_directory, summarize_errors(errors_by_directory)


# --- fixtures -------------------------------------------------------------
# run_settings.jsonl rows are shaped differently depending on the mteb version:
# `split`/`subset` before v2.18.17, `splits`/`subsets` after, and
# reduce_large_json_files.collapse_run_settings merges rows into `subsets`.

CURRENT_VERSION = "2.16.2"


def write_result(
    directory: Path,
    *,
    task_name: str = "DemoTask",
    subsets: tuple[str, ...] = ("default",),
    splits: tuple[str, ...] = ("test",),
    version: str = CURRENT_VERSION,
    block_version: str | None = None,
) -> Path:
    """A task result as mteb writes it: no per-block mteb_version by default."""
    blocks = []
    for subset in subsets:
        block = {"hf_subset": subset, "main_score": 0.5, "languages": ["eng-Latn"]}
        if block_version is not None:
            block["mteb_version"] = block_version
        blocks.append(block)

    result_path = directory / f"{task_name}.json"
    result_path.parent.mkdir(parents=True, exist_ok=True)
    result_path.write_text(
        json.dumps(
            {
                "dataset_revision": "abc123",
                "task_name": task_name,
                "mteb_version": version,
                "evaluation_time": 1.0,
                "scores": {split: blocks for split in splits},
            }
        ),
        encoding="utf-8",
    )
    return result_path


def write_run_settings(
    directory: Path,
    *,
    task: str = "DemoTask",
    split: str | None = None,
    splits: list[str] | None = None,
    subset: str | None = None,
    subsets: list[str] | None = None,
    version: str = CURRENT_VERSION,
) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    entry: dict = {"task": task}
    if splits is not None:
        entry["splits"] = splits
    else:
        entry["split"] = split if split is not None else "test"
    if subsets is not None:
        entry["subsets"] = subsets
    else:
        entry["subset"] = subset if subset is not None else "default"
    entry["version"] = {"mteb": version}
    (directory / RUN_SETTINGS_FILENAME).write_text(
        json.dumps(entry) + "\n", encoding="utf-8"
    )


def validate(result_path: Path, name: str = "DemoTask") -> list[str]:
    return validate_result_file(result_path, f"results/model/revision/{name}.json")


# --- run_settings.jsonl shapes --------------------------------------------


def test_accepts_legacy_split_and_subset(tmp_path):
    """The shape mteb wrote before v2.18.17: one row per (split, subset)."""
    result_path = write_result(tmp_path)
    write_run_settings(tmp_path, split="test", subset="default")

    assert validate(result_path) == []


def test_accepts_collapsed_subsets(tmp_path):
    """This repository's own reduce_large_json_files.collapse_run_settings merges
    rows sharing settings into one carrying a `subsets` list. A result naming any
    single subset from that list is covered by it."""
    result_path = write_result(tmp_path, subsets=("de",))
    write_run_settings(tmp_path, split="test", subsets=["de", "en"])

    assert validate(result_path) == []


def test_accepts_current_mteb_splits_and_subsets(tmp_path):
    """mteb >= 2.18.17 writes `splits` and `subsets` and never the singular
    forms, so this is the shape every new submission arrives in."""
    result_path = write_result(tmp_path, subsets=("en-en", "nl-nl"))
    write_run_settings(tmp_path, splits=["test"], subsets=["en-en", "nl-nl"])

    assert validate(result_path) == []


def test_accepts_splits_with_singular_subset(tmp_path):
    """Plural `splits` with a singular `subset` -- the two spellings are
    independent, so a row may mix them."""
    result_path = write_result(tmp_path)
    write_run_settings(tmp_path, splits=["test"], subset="default")

    assert validate(result_path) == []


def test_rejects_run_settings_without_any_split_field(tmp_path):
    """A row naming neither `split` nor `splits` cannot be matched to a score,
    so it is reported rather than silently ignored."""
    result_path = write_result(tmp_path)
    (tmp_path / RUN_SETTINGS_FILENAME).write_text(
        json.dumps(
            {
                "task": "DemoTask",
                "subset": "default",
                "version": {"mteb": CURRENT_VERSION},
            }
        )
        + "\n",
        encoding="utf-8",
    )

    errors = validate(result_path)

    assert any("must define split(s) and subset(s)" in error for error in errors)


def test_rejects_both_singular_and_plural(tmp_path):
    """`split` and `splits` together are ambiguous -- mteb writes one or the
    other -- so the row is rejected instead of guessing which wins."""
    result_path = write_result(tmp_path)
    (tmp_path / RUN_SETTINGS_FILENAME).write_text(
        json.dumps(
            {
                "task": "DemoTask",
                "split": "test",
                "splits": ["test"],
                "subset": "default",
                "version": {"mteb": CURRENT_VERSION},
            }
        )
        + "\n",
        encoding="utf-8",
    )

    errors = validate(result_path)

    assert any("defines both split/splits" in error for error in errors)


# --- mteb version ---------------------------------------------------------


def test_score_block_without_version_inherits_the_result_version(tmp_path):
    """Most results carry no per-block mteb_version -- only ~0.4% do. TaskResult
    backfills it from the top level on load, so its absence must not be an error.
    """
    result_path = write_result(tmp_path, block_version=None)
    write_run_settings(tmp_path, splits=["test"], subsets=["default"])

    assert validate(result_path) == []


def test_rejects_old_version_on_a_single_score_block(tmp_path):
    """A result merged from several runs can carry an old score among new ones.
    The per-block version catches that even when the top-level version is fine."""
    result_path = write_result(tmp_path, block_version="2.10.12")
    write_run_settings(tmp_path, splits=["test"], subsets=["default"])

    errors = validate(result_path)

    assert any(".mteb_version must use MTEB >=2.14.0" in error for error in errors)


def test_rejects_versions_below_the_run_settings_release(tmp_path):
    """2.13.x is a valid v2 release but predates run_settings.jsonl, so it could
    never satisfy the second requirement -- checked on both the result and the
    run settings entry."""
    result_path = write_result(tmp_path, version="2.13.9")
    write_run_settings(tmp_path, version="2.13.9")

    errors = validate(result_path)

    assert any("mteb_version must use MTEB >=2.14.0" in error for error in errors)
    assert any("version.mteb must use MTEB >=2.14.0" in error for error in errors)


def test_rejects_v1_results(tmp_path):
    """v1 results predate run settings entirely and are no longer accepted."""
    result_path = write_result(tmp_path, version="1.38.0")
    write_run_settings(tmp_path, version="1.38.0")

    errors = validate(result_path)

    assert any("mteb_version must use MTEB >=2.14.0" in error for error in errors)


def test_accepts_exactly_the_minimum_version(tmp_path):
    """2.14.0 itself is allowed: the bound is inclusive, since that release is
    the one that started writing run_settings.jsonl."""
    result_path = write_result(tmp_path, version="2.14.0")
    write_run_settings(tmp_path, version="2.14.0")

    assert validate(result_path) == []


@pytest.mark.parametrize(
    "value,expected",
    [
        ("2.16.2", Version("2.16.2")),
        # a range is written when a result's subsets disagree; the lower bound
        # is what must clear the minimum
        ("2.18.12-2.18.13", Version("2.18.12")),
        ("2.16", Version("2.16")),
        ("not-a-version", None),
        (None, None),
        (2, None),  # a non-string version is unusable, not a crash
    ],
)
def test_parse_version(value, expected):
    """Only the leading release segment matters. mteb writes a range like
    `2.18.12-2.18.13` when a result's subsets disagree; the lower bound is what
    the check must compare against."""
    assert parse_version(value) == expected


# --- run_settings coverage ------------------------------------------------


def test_requires_run_settings(tmp_path):
    """A result with no run_settings.jsonl beside it -- what the deprecated
    `MTEB(...).run()` path produces."""
    result_path = write_result(tmp_path)

    errors = validate(result_path)

    assert any("is missing run_settings.jsonl" in error for error in errors)


def test_requires_matching_run_settings_tuple(tmp_path):
    """run_settings.jsonl exists but describes a different task, so it says
    nothing about how this result was produced."""
    result_path = write_result(tmp_path)
    write_run_settings(tmp_path, task="OtherTask")

    errors = validate(result_path)

    assert any("has no matching run_settings.jsonl entry" in error for error in errors)


def uncovered_subsets(errors: list[str]) -> set[str]:
    """The subsets named by 'no matching entry' errors."""
    return set(re.findall(r"subset='([^']+)'", "\n".join(errors)))


def test_partial_coverage_reports_every_uncovered_subset(tmp_path):
    """run_settings.jsonl covers some subsets but not all of them.

    Matching is per (task, split, subset), so every uncovered subset is reported
    and no covered one is. More than one of each, because a single uncovered
    subset could not tell "reports them all" apart from "reports the first".
    This is the common real failure: a directory whose run settings were written
    by a later run than the scores.
    """
    result_path = write_result(tmp_path, subsets=("en", "nl", "de", "fr"))
    write_run_settings(tmp_path, splits=["test"], subsets=["en", "de"])

    errors = validate(result_path)

    assert uncovered_subsets(errors) == {"nl", "fr"}
    assert len(errors) == 2


def test_partial_coverage_across_splits_is_rejected(tmp_path):
    """Coverage is per split too: run settings naming only `test` say nothing
    about the same subset evaluated on `validation`."""
    result_path = write_result(tmp_path, subsets=("en",), splits=("test", "validation"))
    write_run_settings(tmp_path, splits=["test"], subsets=["en"])

    errors = validate(result_path)

    assert len(errors) == 1
    assert "split='validation'" in errors[0]


def test_full_coverage_across_splits_and_subsets(tmp_path):
    """The mirror case: one row listing every split and subset covers them all."""
    result_path = write_result(
        tmp_path, subsets=("en", "nl"), splits=("test", "validation")
    )
    write_run_settings(tmp_path, splits=["test", "validation"], subsets=["en", "nl"])

    assert validate(result_path) == []


def test_all_submitted_tasks_must_have_run_settings_entries(tmp_path):
    """Every task in the PR needs its own entry: covering one task does not
    vouch for the others submitted alongside it."""
    first = write_result(tmp_path, task_name="DemoTask")
    second = write_result(tmp_path, task_name="OtherTask")
    write_run_settings(tmp_path, task="DemoTask")

    errors = validate(first, "DemoTask") + validate(second, "OtherTask")

    assert any(
        "OtherTask" in error and "has no matching run_settings.jsonl entry" in error
        for error in errors
    )


def test_rejects_malformed_run_settings(tmp_path):
    """An unparseable line is reported with its line number rather than
    aborting the whole file."""
    result_path = write_result(tmp_path)
    (tmp_path / RUN_SETTINGS_FILENAME).write_text("{bad json\n", encoding="utf-8")

    errors = validate(result_path)

    assert any("line 1 is not valid JSON" in error for error in errors)


# --- diff scoping ---------------------------------------------------------


@pytest.mark.parametrize(
    "path,expected",
    [
        ("results/model/revision/DemoTask.json", True),
        ("results/model/revision/experiments/exp-a/ExperimentTask.json", True),
        ("results/model/revision/model_meta.json", False),
        ("results/model/revision/run_settings.jsonl", False),
        ("scripts/merge_same_model.py", False),
        ("paths.json", False),
    ],
)
def test_is_task_result_path(path, expected):
    """Which changed files are task results. Deliberately permissive about
    depth so a result in an unexpected place is still checked; model_meta.json
    and non-results paths are excluded."""
    assert is_task_result_path(path) is expected


# --- reporting ------------------------------------------------------------


def test_summarize_errors_caps_each_directory():
    """Every affected directory is reported, but each contributes a bounded
    number of lines -- one directory can hold tens of thousands of uncovered
    tuples."""
    errors_by_directory = {
        f"results/model{i}/revision": [f"problem {j}" for j in range(50)]
        for i in range(40)
    }

    summary = summarize_errors(errors_by_directory)

    assert "2000 problem(s) in 40 result directory(ies)" in summary
    # every directory is reported, but each contributes a bounded number of lines
    assert summary.count("... and 40 more here") == len(errors_by_directory)
    header_and_footer = 3
    per_directory = MAX_ERRORS_PER_DIRECTORY + 3
    assert (
        len(summary.splitlines())
        <= len(errors_by_directory) * per_directory + header_and_footer
    )

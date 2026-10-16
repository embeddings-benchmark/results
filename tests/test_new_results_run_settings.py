"""New results must be produced with a supported mteb and ship a run_settings.jsonl
covering every submitted (task, split, subset).

Results from models that produce low-precision (fp16/bf16) embeddings must also have
been scored in float32: sentence-transformers < 6 scores in the embedding dtype, which
collapses nearby scores into ties, and mteb only upcasts on every scoring path since
MIN_FP32_SCORING_MTEB_VERSION.

See https://github.com/embeddings-benchmark/mteb/issues/5031
and https://github.com/embeddings-benchmark/mteb/issues/5229
"""

import json
from pathlib import Path
from typing import Any

import mteb
import pytest
from mteb import TaskResult
from mteb.results.task_result import _expand_run_settings_entry
from packaging.version import Version

from tests.git_utils import REPO_ROOT, _run_git, get_base_ref

# requiring run_settings.jsonl is the stricter rule in practice: mteb only
# started writing it in v2.14, and `MTEB(...).run()` never does
MIN_MTEB_VERSION = Version("2.0.0")
# first release that scores in float32 on every path (embeddings-benchmark/mteb#5620)
MIN_FP32_SCORING_MTEB_VERSION = Version("2.24.6")
# sentence-transformers scores in float32 itself from v6
FP32_SCORING_SENTENCE_TRANSFORMERS_VERSION = Version("6.0.0")
LOW_PRECISION_DTYPES = {"float16", "bfloat16"}
RUN_SETTINGS_FILENAME = "run_settings.jsonl"
MODEL_META_FILENAME = "model_meta.json"
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


def validate_mteb_version(version: str | None, relative_path: str) -> list[str]:
    parsed = TaskResult._parse_mteb_version_min(version) if version else None
    if parsed is None:
        return [f"{relative_path} has no usable mteb_version (got {version!r})."]
    if parsed < MIN_MTEB_VERSION:
        return [f"{relative_path} must use MTEB >={MIN_MTEB_VERSION}, got {version!r}."]
    return []


def load_run_settings(path: Path) -> dict[tuple[str, str, str], dict[str, Any]]:
    """Settings of every (task, split, subset) in a run_settings.jsonl; later lines win."""
    covered: dict[tuple[str, str, str], dict[str, Any]] = {}
    for line_number, line in enumerate(path.read_text().splitlines(), start=1):
        if not line.strip():
            continue
        try:
            entry = json.loads(line)
        except json.JSONDecodeError as e:
            raise ValueError(f"{path} line {line_number} is not valid JSON: {e}") from e
        covered.update(
            (key, settings) for key, _, settings in _expand_run_settings_entry(entry)
        )
    return covered


def get_output_dtypes(result_path: Path) -> set[str]:
    """Embedding dtypes declared for the model, preferring mteb's current ModelMeta.

    The model_meta.json saved with the results is only a fallback: mteb versions before
    the dtypes were filled in (embeddings-benchmark/mteb#5620) did not record them.
    """
    meta_path = result_path.parent / MODEL_META_FILENAME
    saved_meta = json.loads(meta_path.read_text()) if meta_path.exists() else {}
    model_folder = result_path.relative_to(REPO_ROOT / "results").parts[0]
    model_name = saved_meta.get("name") or model_folder.replace("__", "/")
    try:
        dtypes = mteb.get_model_meta(model_name).output_dtypes
    except KeyError:
        dtypes = saved_meta.get("output_dtypes")
    if not dtypes:
        return set()
    if not isinstance(dtypes, list):
        dtypes = [dtypes]
    return {str(getattr(dtype, "value", dtype)) for dtype in dtypes}


def is_low_precision(dtypes: set[str]) -> bool:
    # only floats: API models list int8/binary as supported output formats
    return any(d in LOW_PRECISION_DTYPES or d.startswith("float8") for d in dtypes)


def validate_low_precision_scoring(
    relative_path: str,
    dtypes: set[str],
    settings: list[dict[str, Any]],
) -> list[str]:
    """Low-precision embeddings must have been scored by a version that upcasts to float32."""
    if not is_low_precision(dtypes):
        return []
    outdated = set()
    for setting in settings:
        versions = setting.get("version") or {}
        st_version = TaskResult._parse_mteb_version_min(
            versions.get("sentence-transformers")
        )
        if st_version and st_version >= FP32_SCORING_SENTENCE_TRANSFORMERS_VERSION:
            continue
        mteb_version = TaskResult._parse_mteb_version_min(versions.get("mteb"))
        if mteb_version is None or mteb_version < MIN_FP32_SCORING_MTEB_VERSION:
            outdated.add(
                f"mteb={versions.get('mteb')}, "
                f"sentence-transformers={versions.get('sentence-transformers')}"
            )
    if not outdated:
        return []
    return [
        (
            f"{relative_path}: the model produces {'/'.join(sorted(dtypes))} embeddings, "
            f"so it must be run with mteb>={MIN_FP32_SCORING_MTEB_VERSION} or "
            f"sentence-transformers>={FP32_SCORING_SENTENCE_TRANSFORMERS_VERSION} to "
            f"score in float32, got {sorted(outdated)}."
        )
    ]


def validate_result_file(result_path: Path, relative_path: str) -> list[str]:
    """Every problem with one submitted result file."""
    try:
        task_result = TaskResult.from_disk(result_path)
    except Exception as e:  # noqa: BLE001 - pydantic/mteb raise a range of errors
        return [f"{relative_path} is not a valid mteb TaskResult: {e}"]

    errors = validate_mteb_version(task_result.mteb_version, relative_path)

    run_settings_path = result_path.parent / RUN_SETTINGS_FILENAME
    if not run_settings_path.exists():
        return errors + [f"{relative_path} is missing {RUN_SETTINGS_FILENAME}."]

    # TaskResult guarantees hf_subset on every score block
    submitted = {
        (task_result.task_name, split, block["hf_subset"])
        for split, blocks in task_result.scores.items()
        for block in blocks
    }
    run_settings = load_run_settings(run_settings_path)
    missing = sorted(
        f"{split}/{subset}" for _, split, subset in submitted - run_settings.keys()
    )
    if missing:
        errors.append(
            f"{relative_path}: {len(missing)} split/subset(s) missing from "
            f"{RUN_SETTINGS_FILENAME}, e.g. {missing[:5]}"
        )
    errors += validate_low_precision_scoring(
        relative_path,
        get_output_dtypes(result_path),
        [run_settings[key] for key in submitted & run_settings.keys()],
    )
    return errors


def test_new_results_have_run_settings_and_mteb_version():
    changed = get_changed_result_files(get_base_ref())
    if not changed:
        pytest.skip("No added or modified result JSON files found.")

    errors = []
    for relative_path in changed:
        errors += validate_result_file(REPO_ROOT / relative_path, relative_path)

    assert not errors, (
        "\n".join(f"  - {e}" for e in errors) + f"\n\nSee {SUBMISSION_GUIDE}"
    )


@pytest.mark.parametrize(
    ("dtypes", "versions", "valid"),
    [
        ({"bfloat16"}, {"mteb": "2.24.5", "sentence-transformers": "5.4.1"}, False),
        ({"float16"}, {"mteb": "2.24.6", "sentence-transformers": "5.4.1"}, True),
        ({"bfloat16"}, {"mteb": "2.18.1", "sentence-transformers": "6.0.1"}, True),
        (set(), {"mteb": "2.18.1", "sentence-transformers": "5.4.1"}, True),
        # API models list quantized output formats, not the embedding dtype
        (
            {"int8", "binary"},
            {"mteb": "2.18.1", "sentence-transformers": "5.4.1"},
            True,
        ),
    ],
)
def test_validate_low_precision_scoring(dtypes, versions, valid):
    errors = validate_low_precision_scoring(
        "results/org__model/rev/Task.json", dtypes, [{"version": versions}]
    )
    assert (not errors) == valid

"""Regression tests for result files with known-bad task/dataset revisions."""

import json
from pathlib import Path

RESULTS_ROOT = Path(__file__).resolve().parents[1] / "results"

# Add entries here as (task_name, dataset_revision) pairs when a task dataset
# revision is known to be invalid and all corresponding results must be removed.
DISALLOWED_TASK_REVISION_PAIRS = {
    (
        "Vidore3NuclearNemotron35Embed8BReranking.v2",
        "2257498b70708115557fb03e5f3193beab4bffd1",
    ),
    (
        "Vidore3TelecomNemotron35Embed8BReranking.v2",
        "8cac8232b1113de3b06cf67e2cb482f3043a9979",
    ),
}


def test_no_results_use_disallowed_task_revision_pairs() -> None:
    disallowed_results: list[str] = []

    for task_name, disallowed_revision in DISALLOWED_TASK_REVISION_PAIRS:
        for result_file in RESULTS_ROOT.glob(f"*/*/{task_name}.json"):
            with result_file.open() as f:
                result = json.load(f)

            result_task_name = result.get("task_name") or result_file.stem
            dataset_revision = result.get("dataset_revision")
            if (result_task_name, dataset_revision) == (task_name, disallowed_revision):
                disallowed_results.append(str(result_file.relative_to(RESULTS_ROOT.parent)))

    assert not disallowed_results, (
        "Remove results with disallowed task/dataset revision pairs before merging: "
        + ", ".join(disallowed_results)
    )

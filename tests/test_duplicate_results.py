from collections import defaultdict
from pathlib import Path
from typing import Dict, List

import pytest
import mteb


def get_reference_revision(model_name: str) -> str | None:
    """Get the reference revision for a model from MTEB."""
    try:
        model_meta = mteb.get_model_meta(model_name)
        return model_meta.revision
    except Exception:
        return None


def find_duplicate_tasks() -> Dict[str, List[Dict]]:
    """
    Find all duplicate task results across revisions.

    Returns:
        A dictionary mapping model names to lists of duplicate task information.
    """
    results_folder = Path(__file__).parent.parent / "results"
    duplicates_found = {}

    for model_folder in sorted(results_folder.glob("*")):
        if not model_folder.is_dir() or model_folder.name.startswith(".") or model_folder.name == "Human":
            continue

        model_name = model_folder.name.replace("__", "/")
        task_to_revisions: Dict[str, List[Dict]] = defaultdict(list)

        # Collect all task files across revisions
        for revision_folder in model_folder.glob("*"):
            if not revision_folder.is_dir() or revision_folder.name.startswith("."):
                continue

            revision = revision_folder.name

            for task_file in revision_folder.glob("*.json"):
                if task_file.name == "model_meta.json":
                    continue

                task_name = task_file.stem
                task_to_revisions[task_name].append({
                    "revision": revision,
                    "file_path": task_file,
                    "revision_folder": revision_folder,
                })

        # Find tasks with duplicates
        model_duplicates = []
        for task_name, revision_list in sorted(task_to_revisions.items()):
            if len(revision_list) > 1:
                reference_revision = get_reference_revision(model_name)
                revisions_present = [r["revision"] for r in revision_list]

                to_delete = []
                retained_revision = None

                if reference_revision and reference_revision in revisions_present:
                    to_delete = [r for r in revision_list if r["revision"] != reference_revision]
                    retained_revision = reference_revision
                else:
                    priority_order = [
                        r for r in revision_list
                        if r["revision"] not in ["external", "no_revision_available"]
                    ]

                    if priority_order:
                        retained_revision = priority_order[0]["revision"]
                        to_delete = [r for r in revision_list if r["revision"] != retained_revision]
                    else:
                        # All are external/no_revision_available, keep first
                        retained_revision = revision_list[0]["revision"]
                        to_delete = revision_list[1:]

                if to_delete:
                    model_duplicates.append({
                        "task_name": task_name,
                        "revisions_present": revisions_present,
                        "retained_revision": retained_revision,
                        "to_delete": [r["revision"] for r in to_delete],
                        "files": to_delete,
                    })

        if model_duplicates:
            duplicates_found[model_name] = model_duplicates

    return duplicates_found


@pytest.fixture
def duplicate_check():
    """Fixture to find duplicates."""
    return find_duplicate_tasks()


def test_no_duplicate_task_results_exist(duplicate_check):
    """
    Test that no duplicate task results exist across revisions.

    A duplicate is when the same task exists in multiple revisions for the same model.
    These should be cleaned up by keeping only the reference revision or the first valid one.
    """
    if not duplicate_check:
        assert True
        return

    error_lines = [
        "Found duplicate task results that could be deleted:\n",
    ]

    for model_name, duplicates in sorted(duplicate_check.items()):
        reference_revision = get_reference_revision(model_name)
        error_lines.append(f"\n{model_name} (reference revision: {reference_revision}):")

        for dup in duplicates:
            error_lines.append(f"  Task: {dup['task_name']}")
            error_lines.append(f"    Revisions present: {dup['revisions_present']}")
            error_lines.append(f"    Retained revision: {dup['retained_revision']}")
            error_lines.append(f"    Should delete from revisions: {dup['to_delete']}")

    error_message = "\n".join(error_lines)
    pytest.fail(error_message)
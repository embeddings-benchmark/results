from collections import defaultdict
from pathlib import Path

import mteb
import pytest
import logging
import json

logger = logging.getLogger(__name__)


def get_reference_revision(path: Path, model_name: str) -> str | None:
    """Load model metadata from a JSON file."""
    try:
        model_meta = mteb.get_model_meta(model_name, fetch_from_hf=False)
        return model_meta.revision
    except KeyError:
        logger.info(
            f"Model metadata for '{model_name}' not found in MTEB registry."
            " Trying to load from local 'model_meta.json' file."
        )
    meta_file = path / "model_meta.json"
    if meta_file.exists():
        with open(meta_file, "r", encoding="utf-8") as f:

            meta_data = json.load(f)
        model_name = meta_data.get("name")
        if model_name:
            try:
                model_meta = mteb.get_model_meta(model_name, fetch_from_hf=False)
                return model_meta.revision
            except KeyError:
                logger.warning(
                    f"Model metadata for '{model_name}' from local file not found in MTEB registry."
                )
    raise KeyError(
        f"Could not determine reference revision for model '{model_name}'."
        f" On path: {path}"
    )


def find_duplicate_tasks() -> dict[str, list[dict]]:
    """
    Find all duplicate task results across revisions.

    Returns:
        A dictionary mapping model names to lists of duplicate task information.
    """
    results_folder = Path(__file__).parent.parent / "results"
    duplicates_found = {}

    for model_folder in sorted(results_folder.glob("*")):
        if (
            not model_folder.is_dir()
            or model_folder.name.startswith(".")
            or model_folder.name == "Human"
        ):
            continue

        model_name = model_folder.name.replace("__", "/")
        task_to_revisions: dict[str, list[str]] = defaultdict(list)

        reference_revision = None

        # Collect all task files across revisions
        for revision_folder in model_folder.glob("*"):
            if not revision_folder.is_dir() or revision_folder.name.startswith("."):
                continue

            revision = revision_folder.name
            if reference_revision is None:
                reference_revision = get_reference_revision(revision_folder, model_name)

            for task_file in revision_folder.glob("*.json"):
                if task_file.name == "model_meta.json":
                    continue

                task_name = task_file.stem
                task_to_revisions[task_name].append(revision)

        # Find tasks with duplicates
        model_duplicates = []
        for task_name, revision_list in sorted(task_to_revisions.items()):
            if len(revision_list) == 1:
                continue

            to_delete = []
            retained_revision = None

            if reference_revision and reference_revision in revision_list:
                to_delete = [r for r in revision_list if r != reference_revision]
                retained_revision = reference_revision
            else:
                priority_order = [
                    r
                    for r in revision_list
                    if r not in ["external", "no_revision_available"]
                ]

                if priority_order:
                    retained_revision = priority_order[0]
                    to_delete = [r for r in revision_list if r != retained_revision]
                else:
                    # All are external/no_revision_available, keep first
                    retained_revision = revision_list[0]
                    to_delete = revision_list[1:]

            if to_delete:
                model_duplicates.append(
                    {
                        "task_name": task_name,
                        "revisions_present": revision_list,
                        "retained_revision": retained_revision,
                        "to_delete": to_delete,
                    }
                )

        if model_duplicates:
            duplicates_found[model_name] = model_duplicates

    return duplicates_found


def test_no_duplicate_task_results_exist():
    """
    Test that no duplicate task results exist across revisions.

    A duplicate is when the same task exists in multiple revisions for the same model.
    These should be cleaned up by keeping only the reference revision or the first valid one.
    """
    duplicate_check = find_duplicate_tasks()
    if duplicate_check:
        error_lines = [
            "Found duplicate task results that could be deleted:\n",
        ]

        for model_name, duplicates in sorted(duplicate_check.items()):
            error_lines.append(
                f"\n{model_name}:"
            )

            for dup in duplicates:
                error_lines.append(f"  Task: {dup['task_name']}")
                error_lines.append(f"    Revisions present: {dup['revisions_present']}")
                error_lines.append(f"    Retained revision: {dup['retained_revision']}")
                error_lines.append(
                    f"    Should delete from revisions: {dup['to_delete']}"
                )

        error_message = "\n".join(error_lines)
        pytest.fail(error_message)

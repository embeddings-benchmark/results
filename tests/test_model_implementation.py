import json
from pathlib import Path

import pytest

import mteb


def find_unimplemented_models() -> dict[str, list[str]]:
    """
    Find all models in results that are not implemented in MTEB.
    """
    implementations = {meta.name for meta in mteb.get_model_metas() if meta.name}
    results_folder = Path(__file__).parent.parent / "results"
    unimplemented = {}
    exclude_models = {"jinaai/jina-clip-v2", "sentence-transformers/multi-qa-mpnet-base-dot-v1", "sentence-transformers/static-retrieval-mrl-en-v1"}

    for model_folder in sorted(results_folder.glob("*")):
        if not model_folder.is_dir() or model_folder.name.startswith("."):
            continue

        model_name_from_path = model_folder.name.replace("__", "/")
        if model_name_from_path in exclude_models:
            continue
        revisions = []

        # Check if model is implemented via model_meta.json files
        impl_exists = False
        meta_files = list(model_folder.glob("**/model_meta.json"))

        for meta_file in meta_files:
            try:
                with meta_file.open("r") as f:
                    model_meta = json.load(f)
                    model_name_from_meta = model_meta.get("name")

                    if model_name_from_meta and model_name_from_meta in implementations:
                        impl_exists = True
                        break
            except Exception as e:
                pytest.fail(f"Error reading {meta_file}: {e}")

        # Also check model name from path
        if not impl_exists and model_name_from_path in implementations:
            impl_exists = True

        # Collect revisions for unimplemented models
        if not impl_exists:
            for revision_folder in model_folder.glob("*"):
                if revision_folder.is_dir() and not revision_folder.name.startswith(
                    "."
                ):
                    revisions.append(revision_folder.name)

            if revisions:
                unimplemented[model_name_from_path] = revisions

    return unimplemented


def test_all_models_are_implemented_in_mteb():
    """
    Test that all models in the results folder are implemented in MTEB.

    A model is considered implemented if:
    1. Its name appears in mteb.get_model_metas(), OR
    2. Its model_meta.json file contains a name that appears in mteb.get_model_metas()
    """
    unimplemented_check = find_unimplemented_models()
    if unimplemented_check:
        error_lines = [
            "Found models in results that are not implemented in MTEB:\n",
        ]

        for model_name, revisions in sorted(unimplemented_check.items()):
            error_lines.append(f"  {model_name}")
            error_lines.append(f"    Revisions: {revisions}")

        error_lines.append(
            "\nThese models need to be added to MTEB's model implementations "
            "or the results should be removed."
        )

        error_message = "\n".join(error_lines)
        pytest.fail(error_message)

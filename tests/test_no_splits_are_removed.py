import json
from collections import defaultdict

from tests.git_utils import (
    REPO_ROOT,
    get_base_ref,
    get_changed_json_files,
    show_file_at_ref,
)


def get_splits_subsets(data: dict) -> dict[str, set[str]]:
    return {
        split: {r["hf_subset"] for r in results}
        for split, results in data.get("scores", {}).items()
    }


def test_no_splits_are_removed():
    # Compare every changed file against the *same* base commit that the list of
    # changed files was computed from. See tests/git_utils.py for why this must not be
    # PR_BASE_SHA or origin/main (embeddings-benchmark/mteb#5242).
    base_ref = get_base_ref()
    changed_files = get_changed_json_files(base_ref)

    errors = []
    for filepath_str in changed_files:
        filepath = REPO_ROOT / filepath_str
        if not filepath.exists() or filepath.name == "model_meta.json":
            continue

        old_content = show_file_at_ref(filepath_str, base_ref)
        if not old_content:
            # New file, nothing could have been removed
            continue

        old_data = json.loads(old_content)
        with filepath.open("r") as f:
            new_data = json.load(f)

        old_splits_subsets = get_splits_subsets(old_data)
        new_splits_subsets = get_splits_subsets(new_data)

        removed_split_subsets = defaultdict(list)
        for split, old_subsets in old_splits_subsets.items():
            for subset in sorted(old_subsets):
                if subset not in new_splits_subsets.get(split, set()):
                    removed_split_subsets[split].append(subset)

        if removed_split_subsets:
            errors.append(
                f"{filepath_str} has had splits/subsets removed: {dict(removed_split_subsets)}"
            )

    if errors:
        raise AssertionError("\n".join(errors))

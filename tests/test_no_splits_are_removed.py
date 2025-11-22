import json
import subprocess
from pathlib import Path


def test_no_splits_are_removed():
    # Get changed files from git diff between main and HEAD
    result = subprocess.run(
        ["git", "diff", "--name-only", "origin/main", "HEAD", "*.json"],
        capture_output=True,
        text=True,
    )

    changed_files = [f.strip() for f in result.stdout.split("\n") if f.strip()]

    for filepath in changed_files:
        # Get the file from main branch
        old_content = subprocess.run(
            ["git", "show", f"origin/main:{filepath}"], capture_output=True, text=True
        )

        if old_content.returncode != 0:
            # New file, skip
            continue

        # Load old version
        old_data = json.loads(old_content.stdout)

        # Load new version
        root = Path(__file__).parent.parent
        filepath = Path(filepath)
        with Path(filepath).open("r") as f:
            new_data = json.load(f)

        old_splits_subsets = {
            split: [r["hf_subset"] for r in results]
            for split, results in old_data["scores"].items()
        }

        new_splits_subsets = {
            split: set(r["hf_subset"] for r in results)
            for split, results in new_data["scores"].items()
        }

        for split, new_subsets in old_splits_subsets.items():
            assert (
                split in new_data["scores"]
            ), f"Split '{split}' was removed in file '{filepath}'"

            for subset in new_subsets:
                assert (
                    subset in new_splits_subsets[split]
                ), f"Subset '{subset}' from split '{split}' was removed in file '{filepath}'"

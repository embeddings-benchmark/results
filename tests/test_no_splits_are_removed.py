import json
import subprocess
from pathlib import Path


def test_no_splits_are_removed():
    # Find the merge-base (common ancestor) between main and current branch
    merge_base = subprocess.run(
        ["git", "merge-base", "main", "HEAD"],
        capture_output=True,
        text=True,
    ).stdout.strip()

    # Get changed files from git diff between main and HEAD
    result = subprocess.run(
        ["git", "diff", "--name-only", merge_base, "HEAD", "*.json"],
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
        filepath = root / Path(filepath)
        with filepath.open("r") as f:
            new_data = json.load(f)

        old_splits_subsets = {
            split: set(r["hf_subset"] for r in results)
            for split, results in old_data["scores"].items()
        }

        new_splits_subsets = {
            split: set(r["hf_subset"] for r in results)
            for split, results in new_data["scores"].items()
        }

        errors = []
        for split, old_subsets in old_splits_subsets.items():
            if split not in new_data["scores"]:
                errors.append(f"Split '{split}' was removed in file '{filepath}'")

            for subset in old_subsets:
                if subset not in new_splits_subsets.get(split, set()):
                    errors.append(
                        f"Subset '{subset}' from split '{split}' was removed in file '{filepath}'"
                    )

        if errors:
            raise AssertionError("\n".join(errors))

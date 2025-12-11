import json
import os
import subprocess
from collections import defaultdict
from pathlib import Path


def test_no_splits_are_removed():
    # In CI on PRs, use the PR base SHA; otherwise use merge-base with main
    pr_base_sha = os.environ.get("PR_BASE_SHA")

    if pr_base_sha:
        merge_base = pr_base_sha
    else:
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
    root = Path(__file__).parent.parent

    errors = []
    for filepath_str in changed_files:
        filepath = root / Path(filepath_str)
        if filepath.name == "model_meta.json":
            continue
        # Get the file from main branch
        old_content = subprocess.run(
            ["git", "show", f"origin/main:{filepath_str}"],
            capture_output=True,
            text=True,
        )

        if old_content.returncode != 0:
            # New file, skip
            continue

        # Load old version
        old_data = json.loads(old_content.stdout)

        # Load new version
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

        removed_split_subsets = defaultdict(list)
        for split, old_subsets in old_splits_subsets.items():
            for subset in old_subsets:
                if subset not in new_splits_subsets.get(split, set()):
                    removed_split_subsets[split].append(subset)

        if removed_split_subsets:
            errors.append(
                f"{filepath_str} has had splits/subsets removed: {removed_split_subsets}"
            )

    if errors:
        raise AssertionError("\n".join(errors))

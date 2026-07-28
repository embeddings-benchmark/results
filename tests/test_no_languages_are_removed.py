import json
import os
import subprocess
from collections import defaultdict
from pathlib import Path


def test_no_languages_are_removed():
    merge_base = os.environ.get("PR_BASE_SHA")
    if not merge_base:
        for ref in ("origin/main", "main"):
            res = subprocess.run(
                ["git", "merge-base", ref, "HEAD"],
                capture_output=True,
                text=True,
            )
            if res.returncode == 0:
                merge_base = res.stdout.strip()
                break
        if not merge_base:
            raise RuntimeError("Could not find a valid base ref (neither origin/main nor main exists).")

    diff_res = subprocess.run(
        ["git", "diff", "--name-only", merge_base, "HEAD", "*.json"],
        capture_output=True,
        text=True,
    )
    if diff_res.returncode != 0:
        raise RuntimeError(f"git diff failed with code {diff_res.returncode}: {diff_res.stderr}")

    changed_files = sorted(diff_res.stdout.splitlines())

    root = Path(__file__).parent.parent
    errors = []

    def get_languages(data):
        langs = defaultdict(set)
        for split, results in data.get("scores", {}).items():
            if isinstance(results, list):
                for r in results:
                    if isinstance(r, dict) and isinstance(r.get("languages"), list):
                        langs[(split, r.get("hf_subset", ""))].update(r["languages"])
        return langs

    for f_str in changed_files:
        filepath = root / f_str
        if not filepath.exists() or filepath.name == "model_meta.json":
            continue

        # Try to retrieve file from origin/main, falling back to merge_base
        old_content = None
        for ref in ("origin/main", merge_base):
            res = subprocess.run(
                ["git", "show", f"{ref}:{f_str}"],
                capture_output=True,
                text=True,
            )
            if res.returncode == 0:
                old_content = res.stdout
                break

        if not old_content:
            continue

        try:
            old_data = json.loads(old_content)
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse old JSON content for {f_str}: {e}")

        try:
            with filepath.open() as f:
                new_data = json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            raise ValueError(f"Failed to load/parse new JSON file {f_str}: {e}")

        old_langs = get_languages(old_data)
        new_langs = get_languages(new_data)

        removed_languages = defaultdict(list)
        for (split, subset), old_set in old_langs.items():
            missing = old_set - new_langs.get((split, subset), set())
            if missing:
                removed_languages[(split, subset)].extend(sorted(list(missing)))

        if removed_languages:
            sorted_keys = sorted(removed_languages.keys())
            removed_str = ", ".join(f"{split}/{subset}: {removed_languages[(split, subset)]}" for split, subset in sorted_keys)
            errors.append(f"{f_str} has had languages removed: {removed_str}")

    if errors:
        raise AssertionError("\n".join(sorted(errors)))

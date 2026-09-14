import json
from collections import defaultdict

from tests.git_utils import (
    REPO_ROOT,
    get_base_ref,
    get_changed_json_files,
    show_file_at_ref,
)


def get_languages(data: dict) -> dict[tuple[str, str], set[str]]:
    langs = defaultdict(set)
    for split, results in data.get("scores", {}).items():
        if isinstance(results, list):
            for r in results:
                if isinstance(r, dict) and isinstance(r.get("languages"), list):
                    langs[(split, r.get("hf_subset", ""))].update(r["languages"])
    return langs


def test_no_languages_are_removed():
    # Compare every changed file against the *same* base commit that the list of
    # changed files was computed from. See tests/git_utils.py for why this must not be
    # PR_BASE_SHA or origin/main (embeddings-benchmark/mteb#5242).
    base_ref = get_base_ref()
    changed_files = get_changed_json_files(base_ref)

    errors = []
    for f_str in changed_files:
        filepath = REPO_ROOT / f_str
        if not filepath.exists() or filepath.name == "model_meta.json":
            continue

        old_content = show_file_at_ref(f_str, base_ref)
        if not old_content:
            # New file, nothing could have been removed
            continue

        try:
            old_data = json.loads(old_content)
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse old JSON content for {f_str}: {e}")

        try:
            with filepath.open() as f:
                new_data = json.load(f)
        except (json.JSONDecodeError, OSError) as e:
            raise ValueError(f"Failed to load/parse new JSON file {f_str}: {e}")

        old_langs = get_languages(old_data)
        new_langs = get_languages(new_data)

        removed_languages = defaultdict(list)
        for (split, subset), old_set in old_langs.items():
            missing = old_set - new_langs.get((split, subset), set())
            if missing:
                removed_languages[(split, subset)].extend(sorted(missing))

        if removed_languages:
            sorted_keys = sorted(removed_languages.keys())
            removed_str = ", ".join(
                f"{split}/{subset}: {removed_languages[(split, subset)]}"
                for split, subset in sorted_keys
            )
            errors.append(f"{f_str} has had languages removed: {removed_str}")

    if errors:
        raise AssertionError("\n".join(sorted(errors)))

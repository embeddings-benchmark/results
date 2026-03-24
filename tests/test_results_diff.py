"""
Tests for result difference validation.

This test module reuses functions from create_pr_results_comment.py to:
1. Validate that main_score changes don't exceed configured thresholds
2. Provide a summary of all main_score changes in the PR
"""

import json
import os
import sys
import subprocess
from pathlib import Path
import pandas as pd
import pytest
from mteb import TaskResult

MTEB_SCORE_EPSILON=0.001 
repo_path = Path(__file__).parents[1]

def get_base_ref() -> str:
    """Get the base reference for comparison (PR_BASE_SHA env var or origin/main)."""
    return os.getenv("PR_BASE_SHA", "origin/main")

def get_diff_from_main() -> list[str]:
    differences = subprocess.run(
        ["git", "diff", "--name-only", "origin/main...HEAD"],
        cwd=repo_path,
        text=True,
        capture_output=True,
    ).stdout.splitlines()

    return differences

def load_json_from_git_ref(relative_path: str, git_ref: str) -> dict | None:
    """Load a JSON file from a specific git reference."""
    result = subprocess.run(
        ["git", "show", f"{git_ref}:{relative_path}"],
        cwd=repo_path,
        text=True,
        capture_output=True,
    )
    if result.returncode != 0 or not result.stdout.strip():
        return None
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        return None

def extract_main_score(task_result_dict: dict) -> dict[tuple[str, str], float]:
    """
    Extract main_score for each split/subset combination from task result.
    No aggregation - returns the main_score value for each (split, subset) pair.
    
    Returns:
        Dict mapping (split, subset) tuples to their main_score value.
        Example: {("test", "default"): 0.85, ("test", "en"): 0.90}
    """
    split_subset_scores: dict[tuple[str, str], float] = {}
    
    try:
        task_result = TaskResult.from_dict(task_result_dict)
        filtered_result = task_result.only_main_score()
        
        for split_name, split_scores in filtered_result.scores.items():
            for subset_score in split_scores:
                subset_name = subset_score.get("hf_subset")
                main_score = subset_score.get("main_score")
                
                if (subset_name is not None and main_score is not None 
                    and not pd.isna(main_score)):
                    value = float(main_score)
                    if value > 1:
                        value /= 100
                    split_subset_scores[(split_name, subset_name)] = value
        
        return split_subset_scores
    except Exception:
        return {}

def create_old_new_diff_table(differences: list[str], base_ref: str) -> pd.DataFrame:
    """Create DataFrame comparing old and new main_score for each split/subset."""
    columns = ["model_name", "task_name", "split", "subset", "old_revision", "old_value", "new_revision", "new_value", "delta", "pct_change"]
    rows: list[dict] = []

    for relative_path in differences:
        path = repo_path / relative_path
        if not path.exists() or path.suffix != ".json" or path.name == "model_meta.json":
            continue

        model_meta_path = path.parent / "model_meta.json"
        task_name = path.stem
        
        if not model_meta_path.exists():
            continue
            
        try:
            with model_meta_path.open("r") as f:
                model_meta = json.load(f)
                model_name = model_meta["name"]
                new_revision = model_meta["revision"]
        except (json.JSONDecodeError, IOError, KeyError):
            continue

        old_json = load_json_from_git_ref(relative_path, base_ref)
        if old_json is None:
            continue

        old_model_meta = load_json_from_git_ref(str(model_meta_path.relative_to(repo_path)), base_ref)
        if old_model_meta is None:
            old_revision = "unknown"
        else:
            try:
                old_revision = old_model_meta.get("revision", "unknown")
            except (AttributeError, TypeError):
                old_revision = "unknown"

        try:
            with path.open("r") as f:
                new_json = json.load(f)
        except (json.JSONDecodeError, IOError):
            continue

        old_scores = extract_main_score(old_json)
        new_scores = extract_main_score(new_json)
        
        if not old_scores or not new_scores:
            continue
        
        for (split, subset), new_value in new_scores.items():
            if (split, subset) not in old_scores:
                continue
            
            old_value = old_scores[(split, subset)]
            
            delta = new_value - old_value
            if delta == 0:
                continue
            
            pct_change = None if old_value == 0 else delta / old_value

            rows.append({
                "model_name": model_name,
                "task_name": task_name,
                "split": split,
                "subset": subset,
                "old_revision": old_revision,
                "old_value": old_value,
                "new_revision": new_revision,
                "new_value": new_value,
                "delta": delta,
                "pct_change": pct_change,
            })

    if not rows:
        return pd.DataFrame(columns=columns)

    return pd.DataFrame(rows, columns=columns).sort_values(
        ["model_name", "task_name", "split", "subset"]
    )

def test_result_diffs_within_threshold():
    """
    Fail if any main_score delta exceeds configured thresholds.
    """
    
    base_ref = get_base_ref()
    differences = get_diff_from_main()
    print(differences)
    
    # Skip test if no changes found
    if not differences:
        pytest.skip("No changes found between base and current branch")
    
    diff_table = create_old_new_diff_table(differences, base_ref)
    
    # Skip test if no comparable results found
    if diff_table.empty:
        pytest.skip("No comparable updated result files found")
    
    violations = []
    for _, row in diff_table.iterrows():
        delta = abs(row["delta"])
        
        model_task = f"{row['model_name']}/{row['task_name']}"
        
        if delta > MTEB_SCORE_EPSILON:
            violations.append(
            f"  {model_task}: The difference between the current score ({row['new_value']}) and the previous ({row['old_value']}) exceeds threshold of {MTEB_SCORE_EPSILON}"
            )
    
    assert not violations, (
        f"Main score changes exceed configured threshold "
        f"(MTEB_SCORE_EPSILON={MTEB_SCORE_EPSILON}):\n"
        + "\n".join(violations)
    )
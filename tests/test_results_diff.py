"""
Tests for result difference validation.

This test module reuses functions from create_pr_results_comment.py to:
1. Validate that main_score changes don't exceed configured thresholds
2. Provide a summary of all main_score changes in the PR
"""

import os
import sys
from pathlib import Path

import pytest

# Add scripts directory to path to import create_pr_results_comment
scripts_dir = Path(__file__).parents[1] / "scripts"
sys.path.insert(0, str(scripts_dir))

from create_pr_results_comment import (
    get_base_ref,
    get_diff_from_main,
    create_old_new_diff_table,
)

MTEB_SCORE_EPSILON=0.001 

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
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


def test_result_diffs_within_threshold():
    """
    Fail if any main_score delta exceeds configured thresholds.
    
    Environment variables:
    - MAX_ALLOWED_PCT_CHANGE: Maximum percent change allowed (default: 0.05 = 5%)
    """
    max_pct_change = float(os.getenv("MAX_ALLOWED_PCT_CHANGE", "0.05"))
    
    base_ref = get_base_ref()
    differences = get_diff_from_main()
    
    # Skip test if no changes found
    if not differences:
        pytest.skip("No changes found between base and current branch")
    
    diff_table = create_old_new_diff_table(differences, base_ref)
    
    # Skip test if no comparable results found
    if diff_table.empty:
        pytest.skip("No comparable updated result files found")
    
    violations = []
    for _, row in diff_table.iterrows():
        pct_change = abs(row["pct_change"]) if row["pct_change"] else 0
        
        model_task = f"{row['model_name']}/{row['task_name']}"
        
        if pct_change > max_pct_change:
            violations.append(
                f"  {model_task}: percent change {pct_change*100:.2f}% exceeds threshold {max_pct_change*100:.0f}%"
            )
    
    assert not violations, (
        f"Main score changes exceed configured thresholds "
        f"(MAX_ALLOWED_PCT_CHANGE={max_pct_change*100:.0f}%):\n"
        + "\n".join(violations)
    )
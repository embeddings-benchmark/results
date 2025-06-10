"""
Script to generate a Markdown comparison table for new model results in a pull request.

Usage:
    gh pr checkout {pr-number}
    scripts/create_pr_results_comment.py [--models MODEL1 MODEL2 ...]

Description:
    - Compares new model results (added in the current PR) against reference models.
    - Outputs a Markdown table with results for each new model and highlights the best scores.
    - By default, compares against: intfloat/multilingual-e5-large and google/gemini-embedding-001.
    - You can specify reference models with the --models argument.

Arguments:
    --models: List of reference models to compare against (default: intfloat/multilingual-e5-large google/gemini-embedding-001)

Example:
    scripts/create_pr_results_comment.py --models intfloat/multilingual-e5-large myorg/my-new-model
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
from collections import defaultdict
from pathlib import Path

import mteb
import pandas as pd

TaskName, ModelName = str, str


repo_path = Path(__file__).parents[1]
results_path = repo_path / "results"

os.environ["MTEB_CACHE"] = str(repo_path.parent)


default_reference_models = [
    "intfloat/multilingual-e5-large",
    "google/gemini-embedding-001",
]


def get_diff_from_main() -> list[str]:
    current_rev, origin_rev = subprocess.run(
        ["git", "rev-parse", "main", "origin/main"],
        cwd=repo_path,
        capture_output=True,
        check=True,
        text=True,
    ).stdout.splitlines()

    if current_rev != origin_rev:
        raise ValueError(
            f"Your main branch is not up-to-date ({current_rev} != {origin_rev}), please run `git fetch origin main`"
        )

    differences = subprocess.run(
        ["git", "diff", "--name-only", "origin/main...HEAD"],
        cwd=repo_path,
        text=True,
        capture_output=True,
    ).stdout.splitlines()

    return differences


def extract_new_models_and_tasks(
    differences: list[str],
) -> dict[ModelName, list[TaskName]]:
    diffs = [repo_path / diff for diff in differences]
    result_diffs = filter(
        lambda p: p.exists() and p.suffix == ".json" and p.name != "model_meta.json",
        diffs,
    )

    models = defaultdict(list)
    for diff in result_diffs:
        model_meta = diff.parent / "model_meta.json"
        task_name = diff.stem

        with model_meta.open("r") as f:
            model_name = json.load(f)["name"]

        models[model_name].append(task_name)

    return models


def create_comparison_table(models: list[str], tasks: list[str]) -> pd.DataFrame:
    results = mteb.load_results(models=models, tasks=tasks, download_latest=False)
    results = results.join_revisions()
    df = results.to_dataframe()

    # compute average pr. columns
    model_names = [c for c in df.columns if c != "task_name"]

    row = pd.DataFrame(
        {
            "task_name": ["**Average**"],
            **{
                model: df[model].mean() if model != "task_name" else None
                for model in model_names
            },
        }
    )
    df = pd.concat([df, row], ignore_index=True)
    return df


def highlight_max_bold(df, exclude_cols=["task_name"]):
    # result_df = df.copy().astype(str)
    # only 2 decimal places except for the excluded columns
    result_df = df.copy()
    result_df = result_df.applymap(lambda x: f"{x:.2f}" if isinstance(x, float) else x)
    tmp_df = df.copy()
    tmp_df = tmp_df.drop(columns=exclude_cols)
    for idx in df.index:
        max_col = tmp_df.loc[idx].idxmax()
        result_df.loc[idx, max_col] = f"**{result_df.loc[idx, max_col]}**"

    return result_df


def create_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Create PR comment with results comparison."
    )
    parser.add_argument(
        "--models",
        nargs="+",
        default=default_reference_models,
        help="List of reference models to compare against (default: %(default)s)",
    )
    return parser


def main(reference_models: list[str]):
    diff = get_diff_from_main()
    new_additions = extract_new_models_and_tasks(diff)

    for model, tasks in new_additions.items():
        print(f"**Results for `{model}`**")
        df = create_comparison_table(models=reference_models + [model], tasks=tasks)
        bold_df = highlight_max_bold(df)
        print(bold_df.to_markdown(index=False))


if __name__ == "__main__":
    parser = create_argparse()
    args = parser.parse_args()
    main(reference_models=args.models)

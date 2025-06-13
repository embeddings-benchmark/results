"""
Script to generate a Markdown comparison table for new model results in a pull request.

Usage:
    gh pr checkout {pr-number}
    python scripts/create_pr_results_comment.py [--models MODEL1 MODEL2 ...] [--output OUTPUT_FILE]

Description:
    - Compares new model results (added in the current PR) against reference models.
    - Outputs a Markdown file with results for each new model and highlights the best scores.
    - By default, compares against: intfloat/multilingual-e5-large and google/gemini-embedding-001.
    - You can specify reference models with the --models argument.

Arguments:
    --reference-models: List of reference models to compare against (default: intfloat/multilingual-e5-large google/gemini-embedding-001)
    --output: Output markdown file path (default: model-comparison.md)

Example:
    python scripts/create_pr_results_comment.py --models intfloat/multilingual-e5-large myorg/my-new-model
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import logging
from collections import defaultdict
from pathlib import Path

import mteb
import pandas as pd

TaskName, ModelName = str, str

# Default reference models to compare against
REFERENCE_MODELS: list[str] = [
    "intfloat/multilingual-e5-large",
    "google/gemini-embedding-001",
]

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

repo_path = Path(__file__).parents[1]

os.environ["MTEB_CACHE"] = str(repo_path.parent)


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


def create_comparison_table(
    model: str, tasks: list[str], reference_models: list[str]
) -> pd.DataFrame:
    models = [model] + reference_models
    max_col_name = "Max result"
    task_col_name = "task_name"
    results = mteb.load_results(models=models, tasks=tasks, download_latest=False)

    results = results.join_revisions()
    df = results.to_dataframe()

    if df.empty:
        raise ValueError(f"No results found for models {models} on tasks {tasks}")

    df[max_col_name] = None
    task_results = mteb.load_results(tasks=tasks, download_latest=False)
    task_results = task_results.join_revisions()
    max_dataframe = (
        task_results.to_dataframe(format="long").groupby(task_col_name).max()
    )
    if not max_dataframe.empty:
        for task_name, row in max_dataframe.iterrows():
            df.loc[df[task_col_name] == task_name, max_col_name] = (
                row["score"] / 100
            )  # scores are in percentage

    averages: dict[str, float | None] = {}
    for col in models + [max_col_name]:
        numeric = pd.to_numeric(df[col], errors="coerce")
        avg = numeric.mean()
        averages[col] = avg if not pd.isna(avg) else None

    avg_row = pd.DataFrame(
        {
            task_col_name: ["**Average**"],
            **{col: [val] for col, val in averages.items()},
        }
    )
    return pd.concat([df, avg_row], ignore_index=True)


def highlight_max_bold(
    df: pd.DataFrame, exclude_cols: list[str] = ["task_name"]
) -> pd.DataFrame:
    result_df = df.copy()
    for col in result_df.columns:
        if col not in exclude_cols:
            result_df[col] = result_df[col].apply(
                lambda x: f"{x:.2f}"
                if isinstance(x, (int, float)) and pd.notna(x)
                else x
            )

    tmp = df.drop(columns=exclude_cols)
    for idx in df.index:
        row = pd.to_numeric(tmp.loc[idx], errors="coerce")
        if row.isna().all():
            continue
        max_col = row.idxmax()
        if pd.notna(row[max_col]):
            result_df.at[idx, max_col] = f"**{result_df.at[idx, max_col]}**"

    return result_df


def generate_markdown_content(
    model_tasks: dict[str, list[str]], reference_models: list[str]
) -> str:
    if not model_tasks:
        return "# Model Results Comparison\n\nNo new model results found in this PR."

    all_tasks = sorted({t for tasks in model_tasks.values() for t in tasks})
    new_models = list(model_tasks.keys())

    parts: list[str] = [
        "# Model Results Comparison",
        "",
        f"**Reference models:** {', '.join(f'`{m}`' for m in reference_models)}",
        f"**New models evaluated:** {', '.join(f'`{m}`' for m in new_models)}",
        f"**Tasks:** {', '.join(f'`{t}`' for t in all_tasks)}",
        "",
    ]

    for model_name, tasks in model_tasks.items():
        parts.append(f"## Results for `{model_name}`")

        df = create_comparison_table(model_name, tasks, reference_models)
        bold_df = highlight_max_bold(df)
        parts.append(bold_df.to_markdown(index=False))

        parts.extend(["", "---", ""])

    return "\n".join(parts)


def create_argparse() -> argparse.ArgumentParser:
    """Create the argument parser for the script."""
    parser = argparse.ArgumentParser(
        description="Create PR comment with results comparison."
    )
    parser.add_argument(
        "--reference-models",
        nargs="+",
        default=REFERENCE_MODELS,
        help="List of reference models to compare against (default: %(default)s)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("model-comparison.md"),
        help="Output markdown file path",
    )
    return parser


def main(reference_models: list[str], output_path: Path) -> None:
    logger.info("Starting to create PR results comment...")
    logger.info(f"Using reference models: {', '.join(reference_models)}")
    diff = get_diff_from_main()

    model_tasks = extract_new_models_and_tasks(diff)
    markdown = generate_markdown_content(model_tasks, reference_models)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(markdown)


if __name__ == "__main__":
    parser = create_argparse()
    args = parser.parse_args()
    main(args.reference_models, args.output)

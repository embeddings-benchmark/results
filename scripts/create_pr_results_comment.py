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
import logging
import subprocess
from collections import defaultdict
from pathlib import Path

import mteb
import pandas as pd
from mteb import AbsTask
from mteb.cache import ResultCache

ModelName = str
ModelRevision = str

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

cache = ResultCache(repo_path)


def get_diff_from_main() -> list[str]:
    differences = subprocess.run(
        ["git", "diff", "--name-only", "origin/main...HEAD"],
        cwd=repo_path,
        text=True,
        capture_output=True,
    ).stdout.splitlines()

    return differences


def extract_new_models_and_tasks(
    differences: list[str],
) -> dict[tuple[ModelName, ModelRevision], list[AbsTask]]:
    diffs = [repo_path / diff for diff in differences]
    result_diffs = filter(
        lambda p: p.exists() and p.suffix == ".json" and p.name != "model_meta.json",
        diffs,
    )

    models_tasks = defaultdict(list)
    for diff in result_diffs:
        model_meta = diff.parent / "model_meta.json"
        task_name = diff.stem

        with model_meta.open("r") as f:
            model_meta = json.load(f)
            model_name = model_meta["name"]
            revision = model_meta["revision"]

        with diff.open("r") as f:
            task_result = json.load(f)

        splits = set()
        subsets = set()
        for split_name, split_results in task_result.get("scores", {}).items():
            splits.add(split_name)
            for subset_result in split_results:
                subsets.add(subset_result["hf_subset"])

        task = mteb.get_task(
            task_name, eval_splits=list(splits), hf_subsets=list(subsets)
        )
        models_tasks[(model_name, revision)].append(task)

    return models_tasks


def create_comparison_table(
    model: ModelName,
    new_model_revision: str,
    tasks: list[AbsTask],
    reference_models: list[ModelName],
    models_in_pr: list[ModelName],
) -> tuple[pd.DataFrame, list[str]]:
    models = [model] + reference_models
    max_col_name = "Max result"
    max_model_col_name = "Model with max result"
    task_col_name = "task_name"
    results = cache.load_results(models=models, tasks=tasks)
    df = results.to_dataframe(include_model_revision=True)
    new_df_columns = []
    columns_to_merge = defaultdict(list)
    new_model_revisions = []
    for model_name, revision in df.columns:
        col_with_revision = f"{model_name}__{revision}"
        new_df_columns.append(col_with_revision)
        if model_name != model:
            columns_to_merge[model_name].append(col_with_revision)
        else:
            new_model_revisions.append(col_with_revision)
    # if only one revision of the new model exists, then no need to show revision in the column name
    if len(new_model_revisions) == 1:
        columns_to_merge[model] = new_model_revisions

    df.columns = new_df_columns

    # Merge columns with the same model name by taking the maximum value
    for model_name, cols in columns_to_merge.items():
        if len(cols) > 1:
            df[model_name] = df[cols].max(axis=1)
            df.drop(columns=cols, inplace=True)
        else:
            df.rename(columns={cols[0]: model_name}, inplace=True)

    if df.empty:
        raise ValueError(f"No results found for models {models} on tasks {tasks}")

    df[max_col_name] = None
    df[max_model_col_name] = ''
    df["Training Datasets"] = ''
    task_results = cache.load_results(tasks=tasks)
    task_results = task_results.join_revisions()

    for _, row in task_results.iterrows():
        task_name = row["task_name"]
        df.loc[df[task_col_name] == task_name, max_col_name] = row["score"]
        df.loc[df[task_col_name] == task_name, max_model_col_name] = row[
            "model_name"
        ]
        
        # Get training datasets for the model
        try:
            model_meta = mteb.get_model_meta(row["model_name"])
            training_datasets = model_meta.get_training_datasets()
            if training_datasets:
                df.loc[df[task_col_name] == task_name, "Training Datasets"] = ", ".join(sorted(training_datasets))
        except (ValueError, KeyError):
            pass

    task_results_df = task_results.to_dataframe(format="long")
    # some scores are in percentage, convert them to decimal
    task_results_df.loc[task_results_df["score"] > 1, "score"] /= 100
    # remove results of models in this pr from max score calculation
    task_results_df = task_results_df[~task_results_df["model_name"].isin(models_in_pr)]
    max_dataframe = task_results_df.sort_values(
        "score", ascending=False
    ).drop_duplicates(subset=task_col_name, keep="first")
    high_model_performance_tasks = []

    model_select_colum = (
        model if model in df.columns else f"{model}__{new_model_revision}"
    )
    if not max_dataframe.empty:
        for _, row in max_dataframe.iterrows():
            task_name = row["task_name"]
            df.loc[df[task_col_name] == task_name, max_col_name] = row["score"]
            df.loc[df[task_col_name] == task_name, max_model_col_name] = row[
                "model_name"
            ]
            model_score = df.loc[
                df[task_col_name] == task_name, model_select_colum
            ].values[0]
            if model_score > row["score"]:
                high_model_performance_tasks.append(task_name)

    averages: dict[str, float | None] = {}
    index_columns = defaultdict(list)
    # models with revisions if exists
    for col in df.columns:
        index_columns[col.split("__")[0]].append(col)
    for col in models + [max_col_name]:
        available_columns = index_columns.get(col)
        if available_columns is None:
            continue
        for cur_col in available_columns:
            numeric = pd.to_numeric(df[cur_col], errors="coerce")
            avg = numeric.mean()
            averages[cur_col] = avg if not pd.isna(avg) else None

    avg_row = pd.DataFrame(
        {
            task_col_name: ["**Average**"],
            **{col: [val] for col, val in averages.items()},
        }
    )
    return pd.concat([df, avg_row], ignore_index=True), high_model_performance_tasks


def highlight_max_bold(
    df: pd.DataFrame, exclude_cols: list[str] = ["task_name"]
) -> pd.DataFrame:
    result_df = df.copy()
    for col in result_df.columns:
        if col not in exclude_cols:
            result_df[col] = result_df[col].apply(
                lambda x: f"{x:.4f}"
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

    # add revisions row if at least one column has revision
    revisions = []
    new_df_columns = []
    at_least_one_revision = False
    for col in result_df.columns:
        if "__" in col:
            at_least_one_revision = True
            model_name, revision = col.split("__")
            revisions.append(revision)
            new_df_columns.append(model_name)
        elif col == "task_name":
            revisions.append("**Revisions**")
            new_df_columns.append(col)
        else:
            revisions.append("")
            new_df_columns.append(col)

    if at_least_one_revision:
        # add row with revisions after the header
        revisions_row = pd.DataFrame(
            {col: [rev] for col, rev in zip(result_df.columns, revisions)}
        )
        result_df = pd.concat(
            [revisions_row, result_df], ignore_index=True
        ).reset_index(drop=True)
        result_df.columns = new_df_columns

    return result_df


def generate_markdown_content(
    model_tasks: dict[ModelName, list[AbsTask]], reference_models: list[str]
) -> str:
    if not model_tasks:
        return "# Model Results Comparison\n\nNo new model results found in this PR."

    all_tasks = sorted(
        {t.metadata.name for tasks in model_tasks.values() for t in tasks}
    )
    new_models = [model_name for model_name, revision in model_tasks.keys()]

    parts: list[str] = [
        "# Model Results Comparison",
        "",
        f"**Reference models:** {', '.join(f'`{m}`' for m in reference_models)}",
        f"**New models evaluated:** {', '.join(f'`{m}`' for m in new_models)}",
        f"**Tasks:** {', '.join(f'`{t}`' for t in all_tasks)}",
        "",
    ]

    for (model_name, revision), tasks in model_tasks.items():
        parts.append(f"## Results for `{model_name}`")

        df, high_model_performance_tasks = create_comparison_table(
            model_name, revision, tasks, reference_models, new_models
        )
        bold_df = highlight_max_bold(df)
        parts.append(bold_df.to_markdown(index=False))

        if len(high_model_performance_tasks) > 0:
            parts.extend(
                [
                    "",
                    "Model have high performance on these tasks: "
                    + ",".join([f"`{task}`" for task in high_model_performance_tasks]),
                    "",
                ]
            )

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

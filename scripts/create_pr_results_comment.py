"""
Script to generate a Markdown comparison table for new model results in a pull request.

Usage:
    gh pr checkout {pr-number}
    python scripts/create_pr_results_comment.py [--models MODEL1 MODEL2 ...] [--output-comparison FILE] [--output-diff FILE]

Description:
    - Compares new model results (added in the current PR) against reference models.
    - Outputs a Markdown file with results for each new model and highlights the best scores.
    - Also generates a table comparing old (base branch) vs new (PR) scores for updated result files.
    - By default, compares against: intfloat/multilingual-e5-large and google/gemini-embedding-001.
    - You can specify reference models with the --models argument.

Arguments:
    --reference-models: List of reference models to compare against (default: intfloat/multilingual-e5-large google/gemini-embedding-001)
    --output-comparison: Output markdown file for reference model comparison (default: model-comparison.md)
    --output-diff: Output markdown file for old vs new results diff (default: model-diff.md)

Example:
    python scripts/create_pr_results_comment.py --models intfloat/multilingual-e5-large myorg/my-new-model --output-comparison model-comparison.md --output-diff model-diff.md
"""

from __future__ import annotations

import argparse
import json
import os
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
    

def extract_all_metrics(task_result: dict) -> dict[tuple[str, str, str], float]:
    """
    Extract all metrics from task result for each split/subset/metric combination.
    Returns dict with key (split, subset, metric_name) -> value
    """
    extracted: dict[tuple[str, str, str], float] = {}
    for split_name, split_results in task_result.get("scores", {}).items():
        for subset_result in split_results:
            subset = subset_result.get("hf_subset", "default")
            # Extract all numeric metrics (skip non-numeric fields)
            for metric_name, metric_value in subset_result.items():
                if metric_name in ["hf_subset", "languages", "scores_per_experiment"]:
                    continue
                if not isinstance(metric_value, (int, float)):
                    continue
                # Normalize percentage scores to decimal
                value = float(metric_value)
                if value > 1:
                    value /= 100
                extracted[(split_name, subset, metric_name)] = value
    return extracted


def create_old_new_diff_table(differences: list[str], base_ref: str) -> pd.DataFrame:
    """Create a DataFrame comparing old and new results for all changed metrics."""
    columns = [
        "model_name",
        "revision",
        "task_name",
        "split",
        "hf_subset",
        "metric",
        "old_value",
        "new_value",
        "delta",
        "pct_change",
    ]
    rows: list[dict] = []

    for relative_path in differences:
        path = repo_path / relative_path
        # Skip non-result files
        if (
            not path.exists()
            or path.suffix != ".json"
            or path.name == "model_meta.json"
        ):
            continue

        # Load model metadata from model_meta.json (same approach as extract_new_models_and_tasks)
        model_meta_path = path.parent / "model_meta.json"
        task_name = path.stem
        
        if not model_meta_path.exists():
            continue
            
        try:
            with model_meta_path.open("r") as f:
                model_meta = json.load(f)
                model_name = model_meta["name"]
                revision = model_meta["revision"]
        except (json.JSONDecodeError, IOError, KeyError):
            continue

        # Load old version from base ref
        old_json = load_json_from_git_ref(relative_path, base_ref)
        if old_json is None:
            continue  # File is new in this PR, skip comparison

        # Load new version
        try:
            with path.open("r") as f:
                new_json = json.load(f)
        except (json.JSONDecodeError, IOError):
            continue

        # Extract all metrics
        old_metrics = extract_all_metrics(old_json)
        new_metrics = extract_all_metrics(new_json)
        common_keys = sorted(set(old_metrics).intersection(new_metrics))
        if not common_keys:
            continue

        # Create row for each split/subset/metric combination
        for split_name, subset_name, metric_name in common_keys:
            old_value = old_metrics[(split_name, subset_name, metric_name)]
            new_value = new_metrics[(split_name, subset_name, metric_name)]
            
            # Skip if either value is None or NaN
            if old_value is None or new_value is None or pd.isna(old_value) or pd.isna(new_value):
                continue
            
            delta = new_value - old_value
            
            # Only include if there's an actual change
            if delta == 0:
                continue
            
            pct_change = None if old_value == 0 else delta / old_value

            rows.append(
                {
                    "model_name": model_name,
                    "revision": revision,
                    "task_name": task_name,
                    "split": split_name,
                    "hf_subset": subset_name,
                    "metric": metric_name,
                    "old_value": old_value,
                    "new_value": new_value,
                    "delta": delta,
                    "pct_change": pct_change,
                }
            )

    if not rows:
        return pd.DataFrame(columns=columns)

    return pd.DataFrame(rows, columns=columns).sort_values(
        ["model_name", "revision", "task_name", "split", "hf_subset", "metric"]
    )


def generate_old_new_diff_markdown(diff_df: pd.DataFrame, base_ref: str) -> str:
    """Generate markdown table from old vs new comparison DataFrame."""
    parts = [
        "# Updated Results: Old vs New Comparison",
        "",
        f"**Comparing against:** `{base_ref}`",
        "",
    ]

    if diff_df.empty:
        parts.append("No comparable updated result files found between base and PR.")
        return "\n".join(parts)

    # Format display DataFrame
    display_df = diff_df.copy()
    for col in ["old_value", "new_value", "delta"]:
        display_df[col] = display_df[col].apply(lambda x: f"{x:.6f}")
    display_df["pct_change"] = display_df["pct_change"].apply(
        lambda x: "-" if x is None or pd.isna(x) else f"{x * 100:+.2f}%"
    )

    # Add summary by model
    parts.append(f"**Total metric changes:** {len(display_df)}")
    parts.append("")
    
    # Group by model for easier navigation
    for model in display_df["model_name"].unique():
        model_df = display_df[display_df["model_name"] == model]
        parts.append(f"### {model}")
        parts.append(f"Revision: `{model_df['revision'].iloc[0]}`")
        parts.append("")
        parts.append(model_df.to_markdown(index=False))
        parts.append("")

    return "\n".join(parts)


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
) -> tuple[pd.DataFrame, list[str], set[str]]:
    models = [model] + reference_models
    max_col_name = "Max result"
    max_model_col_name = "Model with max result"
    task_col_name = "task_name"
    in_training_col_name = "In Training Data"

    results = cache.load_results(models=models, tasks=tasks, validate_and_filter=True)
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
    df[in_training_col_name] = False
    task_results = cache.load_results(tasks=tasks, validate_and_filter=True)
    task_results = task_results.join_revisions()

    task_results_df = task_results.to_dataframe(format="long")
    # some scores are in percentage, convert them to decimal
    task_results_df.loc[task_results_df["score"] > 1, "score"] /= 100
    # remove results of models in this pr from max score calculation
    task_results_df = task_results_df[~task_results_df["model_name"].isin(models_in_pr)]

    model_meta = mteb.get_model_meta(model)
    all_training_datasets: set[str] = model_meta.get_training_datasets()

    if all_training_datasets:
        df.loc[
            df[task_col_name].isin(all_training_datasets),
            in_training_col_name
        ] = True

    max_dataframe = task_results_df.sort_values(
        "score", ascending=False
    ).drop_duplicates(subset=task_col_name, keep="first")
    high_model_performance_tasks = []

    model_select_column = (
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
                df[task_col_name] == task_name, model_select_column
            ].values[0]
            if model_score > row["score"]:
                high_model_performance_tasks.append(task_name)

    averages: dict[str, float | None] = {}
    index_columns = defaultdict(list)
    # models with revisions if exists
    for col in df.columns:
        if col != in_training_col_name:
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
            in_training_col_name: ["-"],
            **{col: [val] for col, val in averages.items()},
        }
    )
    return pd.concat([df, avg_row], ignore_index=True), high_model_performance_tasks, all_training_datasets


def highlight_max_bold(
    df: pd.DataFrame, exclude_cols: list[str] = ["task_name"]
) -> pd.DataFrame:
    result_df = df.copy()

    for col in result_df.columns:
        if col not in exclude_cols and col != "In Training Data":
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

        df, high_model_performance_tasks, all_training_datasets = create_comparison_table(
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
        
        if all_training_datasets:
            datasets_list = ", ".join(f"`{d}`" for d in sorted(all_training_datasets))
            parts.extend([
                "",  # need blank line before to not merge with table
                f"**Training datasets:** {datasets_list}",
                "",
                "",
            ])

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
        "--output-comparison",
        type=Path,
        default=Path("model-comparison.md"),
        help="Output markdown file for reference model comparison (default: model-comparison.md)",
    )
    parser.add_argument(
        "--output-diff",
        type=Path,
        default=Path("model-diff.md"),
        help="Output markdown file for old vs new results diff (default: model-diff.md)",
    )
    return parser


def main(reference_models: list[str], output_comparison: Path, output_diff: Path) -> None:
    logger.info("Starting to create PR results comment...")
    logger.info(f"Using reference models: {', '.join(reference_models)}")
    diff = get_diff_from_main()
    base_ref = get_base_ref()

    output_comparison.parent.mkdir(parents=True, exist_ok=True)
    output_diff.parent.mkdir(parents=True, exist_ok=True)
    
    model_tasks = extract_new_models_and_tasks(diff)
    markdown = generate_markdown_content(model_tasks, reference_models)
    output_comparison.write_text(markdown)

    diff_table_df = create_old_new_diff_table(diff, base_ref)
    old_new_markdown = generate_old_new_diff_markdown(diff_table_df, base_ref)
    output_diff.write_text(old_new_markdown)


if __name__ == "__main__":
    parser = create_argparse()
    args = parser.parse_args()
    main(args.reference_models, args.output_comparison, args.output_diff)
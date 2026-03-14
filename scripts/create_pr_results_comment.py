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
import sys

import mteb
import pandas as pd
from mteb import AbsTask, TaskResult
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
    

def extract_main_score(task_result_dict: dict) -> float | None:
    """
    Extract main_score from task result dictionary using TaskResult.
    Returns the normalized main_score or None if not found.
    """
    try:
        task_result = TaskResult.from_dict(task_result_dict)
        filtered_result = task_result.only_main_score()
        # Get the main_score from the first split/subset
        for split_scores in filtered_result.scores.values():
            for subset_score in split_scores:
                main_score = subset_score.get("main_score")
                if main_score is not None and not pd.isna(main_score):
                    value = float(main_score)
                    # Normalize percentage scores to decimal
                    if value > 1:
                        value /= 100
                    return value
        return None
    except Exception:
        return None


def create_old_new_diff_table(differences: list[str], base_ref: str) -> pd.DataFrame:
    """Create DataFrame comparing old and new main_score with old and new revisions."""
    columns = ["model_name", "task_name", "old_revision", "old_value", "new_revision", "new_value", "delta", "pct_change"]
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

        # Load old version from base ref
        old_json = load_json_from_git_ref(relative_path, base_ref)
        if old_json is None:
            continue

        # Load old revision from model_meta.json in base ref
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

        old_value = extract_main_score(old_json)
        new_value = extract_main_score(new_json)
        
        if old_value is None or new_value is None:
            continue
        
        if pd.isna(old_value) or pd.isna(new_value):
            continue
        
        delta = new_value - old_value
        if delta == 0:
            continue
        
        pct_change = None if old_value == 0 else delta / old_value

        rows.append({
            "model_name": model_name,
            "task_name": task_name,
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
        ["model_name", "task_name"]
    )


def generate_old_new_diff_markdown(diff_df: pd.DataFrame, base_ref: str) -> str:
    """Generate markdown table with merged model_name rows and revisions on right."""
    parts = [
        "# Updated Results: Old vs New Comparison",
        "",
        f"**Comparing against:** `{base_ref}`",
        "",
    ]

    if diff_df.empty:
        parts.append("No comparable updated result files found.")
        return "\n".join(parts)

    parts.append(f"**Total tasks updated:** {len(diff_df)}")
    parts.append("")
    
    # Build markdown table with merged model_name rows, revisions on right
    table_rows = [
        "| Model | Task Name | Old Score | New Score | Δ Score | % Change | Old Revision | New Revision |",
        "|-------|-----------|-----------|-----------|---------|----------|--------------|--------------|",
    ]
    
    current_model = None
    for _, row in diff_df.iterrows():
        model_name = row["model_name"]
        task_name = row["task_name"]
        old_value = f"{row['old_value']:.6f}"
        new_value = f"{row['new_value']:.6f}"
        delta = f"{row['delta']:+.6f}"
        pct_change = "-" if row["pct_change"] is None or pd.isna(row["pct_change"]) else f"{row['pct_change']*100:+.2f}%"
        old_revision = row["old_revision"]
        new_revision = row["new_revision"]
        
        # Show model name only for the first row of each model (merged rows effect)
        if model_name != current_model:
            display_model = model_name
            current_model = model_name
        else:
            display_model = ""
        
        table_rows.append(
            f"| {display_model} | {task_name} | {old_value} | {new_value} | {delta} | {pct_change} | {old_revision} | {new_revision} |"
        )
    
    parts.extend(table_rows)
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


def main(reference_models: list[str], output_comparison: Path, output_diff: Path) -> int:
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
    if diff_table_df.empty:
        logger.info("No result changes detected. Skipping comment generation.")
        return 1
    
    output_diff.write_text(old_new_markdown)
    return 0


if __name__ == "__main__":
    parser = create_argparse()
    args = parser.parse_args()
    exit_code = main(args.reference_models, args.output_comparison, args.output_diff)
    sys.exit(exit_code)
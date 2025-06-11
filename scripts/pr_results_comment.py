"""
Script to generate a Markdown comparison table for model results from file paths.

The script takes a list of result files and extracts:
- Model name from the folder structure (results/model_name/...)
- Task name from the filename (without .json extension)

Usage:
    python scripts/pr_results_comment.py file1.json file2.json --output results.md

Arguments:
    files: List of result files to process
    --output: Output markdown file path (required)

Example:
    python scripts/create_pr_results_comment.py \
        results/my-new-model/revision/task1.json \
        results/my-new-model/revision/task2.json \
        results/another-model/revision/task1.json \
        --output comparison.md
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from collections import defaultdict
from pathlib import Path

import mteb
import pandas as pd

repo_path = Path(__file__).parents[1]
results_path = repo_path / "results"

# Set MTEB cache
os.environ["MTEB_CACHE"] = str(repo_path.parent)

# Hardcoded reference models to compare against
REFERENCE_MODELS = [
    "intfloat/multilingual-e5-large",
    "google/gemini-embedding-001",
]


def extract_model_and_task_from_path(file_path: str) -> tuple[str, str]:
    """
    Extract model name and task name from file path.

    Expected structure: results/model_name/revision/task_name.json
    Returns: (model_name, task_name)
    """
    path = Path(file_path)

    if not path.suffix == '.json':
        raise ValueError(f"File must be a JSON file: {file_path}")

    task_name = path.stem
    parts = path.parts
    try:
        results_idx = parts.index('results')
        if results_idx + 1 < len(parts):
            model_dir = parts[results_idx + 1].replace("__", "/")

            # Try to get model name from model_meta.json
            model_meta_path = path.parent / "model_meta.json"
            if model_meta_path.exists():
                try:
                    with open(model_meta_path) as f:
                        meta = json.load(f)
                        model_name = meta.get("name", model_dir)
                except (json.JSONDecodeError, KeyError):
                    model_name = model_dir
            else:
                model_name = model_dir

            return model_name, task_name
        else:
            raise ValueError(f"Invalid path structure: {file_path}")
    except ValueError:
        raise ValueError(f"Path must contain 'results' directory: {file_path}")


def group_files_by_model(file_paths: list[str]) -> dict[str, list[str]]:
    """Group files by model and extract task names."""
    model_tasks = defaultdict(list)

    for file_path in file_paths:
        try:
            model_name, task_name = extract_model_and_task_from_path(file_path)
            model_tasks[model_name].append(task_name)
            print(f"✓ Found: {model_name} -> {task_name}")
        except ValueError as e:
            print(f"⚠ Warning: Skipping {file_path}: {e}")
            continue

    # Remove duplicates and sort
    for model in model_tasks:
        model_tasks[model] = sorted(list(set(model_tasks[model])))

    return dict(model_tasks)


def create_comparison_table(model: str, tasks: list[str]) -> pd.DataFrame:
    """Create comparison table for given models and tasks."""
    try:
        print(f"Loading results for model: {model}")
        print(f"Tasks: {tasks}")

        try:
            results = mteb.load_results(models=[model]+REFERENCE_MODELS, tasks=tasks, download_latest=False)
        except Exception as e:
            # if model in reference don't have results on task
            results = mteb.load_results(models=[model], tasks=tasks, download_latest=False)
        results = results.join_revisions()
        df = results.to_dataframe()

        if df.empty:
            raise ValueError("No results found for the specified models and tasks")

        # Compute average per columns
        model_names = [c for c in df.columns if c != "task_name"]

        # Calculate averages only for numeric columns
        averages = {}
        for model in model_names:
            if model in df.columns:
                numeric_values = pd.to_numeric(df[model], errors='coerce')
                avg_value = numeric_values.mean()
                averages[model] = avg_value if not pd.isna(avg_value) else None
            else:
                averages[model] = None

        # Add average row
        avg_row = pd.DataFrame({
            "task_name": ["**Average**"],
            **{model: [avg_val] for model, avg_val in averages.items()},
        })

        df = pd.concat([df, avg_row], ignore_index=True)
        return df
    except Exception as e:
        print(f"❌ Error creating comparison table: {e}")
        raise


def highlight_max_bold(df: pd.DataFrame, exclude_cols=["task_name"]) -> pd.DataFrame:
    """Highlight maximum values in bold for each row."""
    result_df = df.copy()

    # Format numeric values to 2 decimal places
    for col in result_df.columns:
        if col not in exclude_cols:
            result_df[col] = result_df[col].apply(
                lambda x: f"{x:.2f}" if isinstance(x, (int, float)) and pd.notna(x) else str(x)
            )

    # Create a temporary dataframe for finding max values
    tmp_df = df.copy()
    tmp_df = tmp_df.drop(columns=exclude_cols)

    for idx in df.index:
        # Skip rows with no numeric data
        numeric_row = pd.to_numeric(tmp_df.loc[idx], errors='coerce')
        if numeric_row.isna().all():
            continue

        max_col = numeric_row.idxmax()
        if pd.notna(numeric_row[max_col]):
            current_value = result_df.loc[idx, max_col]
            result_df.loc[idx, max_col] = f"**{current_value}**"

    return result_df


def generate_markdown_content(model_tasks: dict[str, list[str]]) -> str:
    """Generate the complete markdown content with comparison tables."""

    if not model_tasks:
        return "# Model Results Comparison\n\nNo valid model results found."

    # Get all unique tasks across all models
    all_tasks = []
    for tasks in model_tasks.values():
        all_tasks.extend(tasks)
    all_tasks = sorted(list(set(all_tasks)))

    # Get all models
    new_models = list(model_tasks.keys())

    markdown_parts = [
        "# Model Results Comparison",
        "",
        f"**New models evaluated:** {', '.join(f'`{m}`' for m in new_models)}",
        f"**Tasks:** {', '.join(f'`{t}`' for t in all_tasks)}",
        "",
    ]

    # Create comparison tables for each new model
    for model_name, model_tasks_list in model_tasks.items():
        markdown_parts.extend([
            f"## Results for `{model_name}`",
        ])

        try:
            # Compare this model against reference models
            df = create_comparison_table(model_name, tasks=model_tasks_list)
            bold_df = highlight_max_bold(df)
            markdown_table = bold_df.to_markdown(index=False)
            markdown_parts.append(markdown_table)
        except Exception as e:
            print(f"❌ Error generating comparison table for {model_name}: {e}")

        markdown_parts.extend(["", "---", ""])

    return "\n".join(markdown_parts)


def create_argparse() -> argparse.ArgumentParser:
    """Create argument parser."""
    parser = argparse.ArgumentParser(
        description="Generate markdown comparison table for model results from file paths."
    )
    parser.add_argument(
        "files",
        nargs="+",
        help="List of result JSON files to process",
    )
    parser.add_argument(
        "--output",
        type=Path,
        required=True,
        help="Output markdown file path (required)",
    )
    return parser


def main():
    """Main function."""
    parser = create_argparse()
    args = parser.parse_args()

    print(f"Processing {len(args.files)} files...")

    # Group files by model
    try:
        model_tasks = group_files_by_model(args.files)
        print(f"\nFound {len(model_tasks)} models:")
        for model, tasks in model_tasks.items():
            print(f"  {model}: {len(tasks)} tasks ({', '.join(tasks)})")
    except Exception as e:
        print(f"❌ Error processing files: {e}")
        raise e

    if not model_tasks:
        print("❌ No valid model results found")
        raise e

    # Generate markdown content
    try:
        markdown_content = generate_markdown_content(model_tasks)
    except Exception as e:
        print(f"❌ Error generating markdown: {e}")
        raise e

    # Write to output file
    try:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(markdown_content)
        print(f"✅ Markdown written to {args.output}")
    except Exception as e:
        print(f"❌ Error writing to {args.output}: {e}")
        raise e


if __name__ == "__main__":
    main()

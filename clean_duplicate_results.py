"""
Script to clean duplicate task results for models.

For each model:
    For each task:
        If multiple results exist:
            - If reference revision is present, delete other revisions
            - Otherwise, only delete 'external' and 'no_revision_available' revisions
"""

import shutil
from pathlib import Path
from collections import defaultdict
from typing import Dict, List
import mteb
import csv

def get_reference_revision(model_name: str) -> str | None:
    try:
        model_meta = mteb.get_model_meta(model_name)
        return model_meta.revision
    except Exception:
        return None

def clean_duplicate_results():
    results_folder = Path(__file__).parent / "results"
    deletions = []
    model_deleted_revisions = defaultdict(set)
    model_retained_revisions = defaultdict(set)
    stats = {
        'models_processed': 0,
        'tasks_with_duplicates': 0,
        'files_deleted': 0,
        'folders_removed': 0
    }
    
    for model_folder in sorted(results_folder.glob("*")):
        if not model_folder.is_dir() or model_folder.name.startswith("."):
            continue
            
        model_name = model_folder.name.replace("__", "/")
        reference_revision = get_reference_revision(model_name)
        
        stats['models_processed'] += 1
        task_to_revisions: Dict[str, List[Dict]] = defaultdict(list)
        
        for revision_folder in model_folder.glob("*"):
            if not revision_folder.is_dir() or revision_folder.name.startswith("."):
                continue
                
            revision = revision_folder.name
            
            # Get all task result files (excluding model_meta.json)
            for task_file in revision_folder.glob("*.json"):
                if task_file.name == "model_meta.json":
                    continue
                    
                task_name = task_file.stem
                task_to_revisions[task_name].append({
                    'revision': revision,
                    'file_path': task_file,
                    'revision_folder': revision_folder
                })
        
        # Process each task with multiple results
        for task_name, revision_list in sorted(task_to_revisions.items()):
            if len(revision_list) <= 1:
                continue  
                
            stats['tasks_with_duplicates'] += 1
            revisions_present = [r['revision'] for r in revision_list]
            
            to_delete = []
            retained_revision = None
            
            if reference_revision and reference_revision in revisions_present:
                # Reference revision exists - delete all others
                to_delete = [r for r in revision_list if r['revision'] != reference_revision]
                retained_revision = reference_revision
            else:
                # Reference revision not present - only delete external and no_revision_available
                to_delete = [
                    r for r in revision_list 
                    if r['revision'] in ['external', 'no_revision_available']
                ]
                # Find retained revision (the one not deleted)
                retained_revisions = [r['revision'] for r in revision_list if r not in to_delete]
                if retained_revisions:
                    retained_revision = retained_revisions[0]  # Take first if multiple
            
            # Delete the files
            for item in to_delete:
                revision = item['revision']
                file_path = item['file_path']
                relative_path = file_path.relative_to(results_folder)

                # file_path.unlink()
                stats['files_deleted'] += 1
                deletions.append(str(relative_path))
                model_deleted_revisions[model_name].add(revision)
            
            # Track retained revision
            if retained_revision:
                model_retained_revisions[model_name].add(retained_revision)
        
        # Clean up empty revision folders
        for revision_folder in model_folder.glob("*"):
            if not revision_folder.is_dir():
                continue
                
            # Check if folder only has model_meta.json or is empty
            json_files = list(revision_folder.glob("*.json"))
            if len(json_files) == 0 or (
                len(json_files) == 1 and json_files[0].name == "model_meta.json"
            ):
                relative_path = revision_folder.relative_to(results_folder)

                # shutil.rmtree(revision_folder)
                stats['folders_removed'] += 1
    
    print(f"\n{'='*80}")
    print(f"SUMMARY")
    print(f"{'='*80}")
    print(f"Models processed: {stats['models_processed']}")
    print(f"Tasks with duplicates: {stats['tasks_with_duplicates']}")
    print(f"Files deleted: {stats['files_deleted']}")
    print(f"Folders removed: {stats['folders_removed']}")

    if model_deleted_revisions:
        csv_folder = Path(__file__).parent
        csv_file = csv_folder / "deleted_revisions.csv"
        with csv_file.open("w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["model", "revision_retained", "deleted_revisions", "num_deleted_revisions"])
            
            for model_name in sorted(model_deleted_revisions.keys()):
                deleted_revs = sorted(model_deleted_revisions[model_name])
                retained_revs = sorted(model_retained_revisions[model_name])
                retained_revs_str = ", ".join(retained_revs) if retained_revs else "N/A"
                
                writer.writerow([
                    model_name,
                    retained_revs_str,
                    ", ".join(deleted_revs),
                    len(deleted_revs)
                ])
        
        print(f"Deleted revisions CSV saved to: {csv_file}")
        print(f"Models with deleted revisions: {len(model_deleted_revisions)}")

if __name__ == "__main__":
    clean_duplicate_results()
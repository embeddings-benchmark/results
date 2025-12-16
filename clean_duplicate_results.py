import shutil
from pathlib import Path
from collections import defaultdict
from typing import Dict, List
import mteb
from datetime import datetime

def get_reference_revision(model_name: str) -> str | None:
    try:
        model_meta = mteb.get_model_meta(model_name)
        return model_meta.revision
    except Exception:
        return None

def clean_duplicate_results():
    results_folder = Path(__file__).parent / "results"
    deletions = []
    stats = {
        'models_processed': 0,
        'tasks_with_duplicates': 0,
        'files_deleted': 0,
        'folders_removed': 0
    }
    
    # Setup log file
    log_folder = Path(__file__).parent
    log_file = log_folder / "deletion_log.txt"
    log_lines = []
    log_lines.append(f"Deduplication Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log_lines.append("="*80)
    log_lines.append("")
    
    for model_folder in sorted(results_folder.glob("*")):
        if not model_folder.is_dir() or model_folder.name.startswith(".") or model_folder.name == "Human":
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
        model_has_duplicates = False
        model_log_lines = []  # Temporary storage for this model's logs
        
        for task_name, revision_list in sorted(task_to_revisions.items()):
            if len(revision_list) <= 1:
                continue  
                
            if not model_has_duplicates:
                model_has_duplicates = True
                # Add model header only when first duplicate is found
                model_log_lines.append(f"=== Deduplicating model ({model_name}) ===")
                model_log_lines.append(f'reference revision "{reference_revision if reference_revision else "None"}"')
                model_log_lines.append("")
                
            stats['tasks_with_duplicates'] += 1
            revisions_present = [r['revision'] for r in revision_list]
            
            to_delete = []
            retained_revision = None
            
            if reference_revision and reference_revision in revisions_present:
                # Reference revision exists - delete task from all other revisions
                to_delete = [r for r in revision_list if r['revision'] != reference_revision]
                retained_revision = reference_revision
            else:
                # Reference revision not present - keep first non-external/non-no_revision_available
                # Priority: any valid revision > external > no_revision_available
                priority_order = []
                for r in revision_list:
                    if r['revision'] not in ['external', 'no_revision_available']:
                        priority_order.append(r)
                
                if priority_order:
                    retained_revision = priority_order[0]['revision']
                    to_delete = [r for r in revision_list if r['revision'] != retained_revision]
                else:
                    # All are external/no_revision_available, keep first
                    retained_revision = revision_list[0]['revision']
                    to_delete = revision_list[1:]
            
            # Log duplicate found
            model_log_lines.append(f"Found duplicates for {task_name}")
            
            # Delete the task files (not entire revision folders)
            for item in to_delete:
                revision = item['revision']
                file_path = item['file_path']
                relative_path1 = file_path.relative_to(results_folder)
                
                retained_path = f"{retained_revision}/{task_name}.json"
                deleted_path = f"{revision}/{task_name}.json"
                
                model_log_lines.append(f"    deleting {deleted_path} as {retained_path} already exists")
                
                file_path.unlink()
                stats['files_deleted'] += 1
                deletions.append(str(relative_path1))
        
        # Only add model logs if there were duplicates
        if model_has_duplicates:
            log_lines.extend(model_log_lines)
            log_lines.append("")
        
        # Clean up empty revision folders
        for revision_folder in model_folder.glob("*"):
            if not revision_folder.is_dir():
                continue
                
            # Check if folder only has model_meta.json or is empty
            json_files = list(revision_folder.glob("*.json"))
            if len(json_files) == 0 or (
                len(json_files) == 1 and json_files[0].name == "model_meta.json"
            ):
                relative_path2 = revision_folder.relative_to(results_folder)
                
                # Only log if this model had duplicates (to keep log clean)
                if model_has_duplicates:
                    if log_lines and log_lines[-1] == "":
                        log_lines.pop()
                    log_lines.append(f"Removing empty revision folder: {relative_path2}")
                    log_lines.append("")
                
                shutil.rmtree(revision_folder)
                print(f"Removed empty folder: {revision_folder}")
                stats['folders_removed'] += 1
    
    with log_file.open("w") as f:
        f.write("\n".join(log_lines))
    
    print(f"\n{'='*80}")
    print(f"SUMMARY")
    print(f"{'='*80}")
    print(f"Models processed: {stats['models_processed']}")
    print(f"Tasks with duplicates: {stats['tasks_with_duplicates']}")
    print(f"Files deleted: {stats['files_deleted']}")
    print(f"Folders removed: {stats['folders_removed']}")
    print(f"Log file saved to: {log_file}")

if __name__ == "__main__":
    clean_duplicate_results()
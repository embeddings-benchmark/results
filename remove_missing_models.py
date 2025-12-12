import pandas as pd
import shutil
from pathlib import Path

# Read the CSV with missing implementations
csv_path = Path(__file__).parent / "missing_implementations.csv"
df = pd.read_csv(csv_path)

res = Path(__file__).parent / "results"

# Preview what will be deleted
print(f"Found {len(df)} models without implementations")
print("\nModels to be deleted:")
print("=" * 80)

models_to_delete = []
for idx, row in df.iterrows():
    model_name = row['model']
    # Convert model name back to folder format
    folder_name = model_name.replace("/", "__")
    model_path = res / folder_name
    
    if model_path.exists():
        models_to_delete.append(model_path)
        print(f"{idx + 1}. {model_name} ({folder_name})")

print("=" * 80)
print(f"\nTotal directories to delete: {len(models_to_delete)}")

# Ask for confirmation
response = input("\nDo you want to proceed with deletion? (yes/no): ")

if response.lower() == "yes":
    deleted_count = 0
    failed_deletions = []
    
    for model_path in models_to_delete:
        try:
            shutil.rmtree(model_path)
            deleted_count += 1
            print(f"Deleted: {model_path.name}")
        except Exception as e:
            failed_deletions.append((model_path.name, str(e)))
            print(f"Failed to delete {model_path.name}: {e}")
    
    print(f"\n✓ Successfully deleted {deleted_count} model directories")
    
    if failed_deletions:
        print(f"\n✗ Failed to delete {len(failed_deletions)} directories:")
        for name, error in failed_deletions:
            print(f"  - {name}: {error}")
else:
    print("\nDeletion cancelled.")
import os
import glob


for folder in glob.glob("results/*"):
    if not os.path.isdir(folder):
        continue

    if "__" in folder:
        # remove the first part of the model name
        new_folder = folder.split("__")[1]
        os.system(f"mv {folder} results/{new_folder}-1")


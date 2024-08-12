import glob
import json
import os

for file in glob.glob("results/*/*/*.json"):
    if os.path.getsize(file) >= 9.5 * 1024 * 1024:
        print(f"Resizing {file} to have no indentations")
        # read it in as json and write it out with no indent
        with open(file, "r") as f:
            data = json.load(f)

        with open(file, "w") as f:
            json.dump(data, f, indent=None)

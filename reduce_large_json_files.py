import glob
import json
import os
from pathlib import Path

import mteb


def resize_flores():
    """
    includes only relevant splits from the FloresBitextMining.json files
    """
    paths = Path(__file__).parent.glob("**/FloresBitextMining.json")

    for p in paths:
        try:
            res = mteb.MTEBResults.from_disk(p)
            res.validate_and_filter_scores()
            res.to_disk(p)
        except Exception:
            pass


def remove_spaces():
    """
    removes spaces from the json files
    """

    for file in glob.glob("results/*/*/*.json"):
        # if the file is greater than 9 MB, compress it with gzip
        if os.path.getsize(file) >= 9.5 * 1024 * 1024:
            print(f"Resizing {file} to have no indentations")
            # read it in as json and write it out with no indent
            with open(file, "r") as f:
                data = json.load(f)

            with open(file, "w") as f:
                json.dump(data, f, indent=None)


if __name__ == "__main__":
    resize_flores()
    remove_spaces()

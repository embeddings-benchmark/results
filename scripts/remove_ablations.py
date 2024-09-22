import glob
import os
import json
import tqdm


for file in tqdm.tqdm(glob.glob("results/*/*.json")):
    print(file)
    if "Instruction" not in file:
        continue
    with open(file, "r") as fin:
        data = json.load(fin)
        if "individual" in data["test"]:
            del data["test"]["individual"]

    with open(file, "w") as fout:
        json.dump(data, fout, indent=2)

import os
import glob
import tqdm


def line_count(file):
    with open(file) as f:
        return sum(1 for _ in f)


for folder in glob.glob("results/*"):
    if not os.path.isdir(folder):
        continue

    print(f"Processing {folder}")

    # create the subfolder if it doesn't exist
    for subfolder in glob.glob(os.path.join(folder + "-1", "*")):
        if not os.path.isdir(subfolder):
            continue

        # if it doesn't exist in the original, create it
        if not os.path.isdir(subfolder.replace("-1", "")):
            os.makedirs(subfolder.replace("-1", ""), exist_ok=True)

    # if there is the same folder name but with -1 at the end, we need a merge
    if os.path.isdir(folder + "-1"):
        # copy each file over, unless it is already there, in which case choose the longest one
        for file in tqdm.tqdm(glob.glob(os.path.join(folder + "-1", "*", "*.json"))):
            if os.path.exists(file.replace("-1", "")):
                line_count_1 = line_count(file)
                line_count_2 = line_count(file.replace("-1", ""))
                if line_count_1 > line_count_2:
                    os.system(f"mv {file} {file.replace('-1', '')}")

            else:
                os.system(f"mv {file} {file.replace('-1', '')}")


"""
This script merges two model directories that are the same except one ends with "-1"

I renamed all files to end with "-1" because we can't have duplicate filenames. Then we need some script to merge their contents (which is this). So first rename all model folders then run this. 

Then go through and remove the -1 from ones that are new and thus werent merged
"""

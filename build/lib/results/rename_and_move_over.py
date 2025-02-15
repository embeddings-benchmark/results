import os
import glob
import tqdm

for folder in tqdm.tqdm(glob.glob("results/*")):
    if not os.path.isdir(folder):
        continue

    # move all files in that folder into a new folder called "no_revision_available"
    os.makedirs(os.path.join(folder, "no_revision_available"), exist_ok=True)
    os.system(f"mv {os.path.join(folder, '*')} {os.path.join(folder, 'no_revision_available')}")

    # now move it over to /home/hltcoe/oweller/my_exps/mteb_public/results
    os.system(f"mv {folder} /home/hltcoe/oweller/my_exps/mteb_public/results")

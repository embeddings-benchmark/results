import json
import pandas as pd
from pathlib import Path

import mteb

print(mteb.__version__) # should be latest

implementations = {meta.name for meta in mteb.get_model_metas() if meta.name}
with open("implementations.json", "w") as f:
    json.dump(list(implementations), f, indent=2)

print(f"Total implementations: {len(implementations)}")
print(f"Total Results models: {len(list((Path(__file__).parent / 'results').glob('*')))}")
model_list = []

res = Path(__file__).parent / "results"
for mdl_path in res.glob("*"):
    revisions = [r.name for r in mdl_path.glob("*")]

    # see if there is any model_meta.json file
    imp_exists = False
    meta_files = list(mdl_path.glob("**/model_meta.json"))
    for meta_file in meta_files:
        with meta_file.open("r") as f:
            mdl_meta = json.load(f)
            mdl_name = mdl_meta["name"]
            if mdl_name in implementations:
                imp_exists = True
                break
    mdl_name = mdl_path.name.replace("__", "/")
    imp_exists = imp_exists or (mdl_name in implementations)

    if not imp_exists:
        # print(f"Implementation missing for {mdl_name} with revisions {revisions}")
        model_list.append((mdl_name, revisions))


print(f"Total missing implementations: {len(model_list)}")
df = pd.DataFrame(model_list, columns=["model", "revisions"])
df.to_csv("missing_implementations.csv", index=False)

print(df['revisions'].explode().value_counts())
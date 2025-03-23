# /// script
# requires-python = "==3.12"
# dependencies = [
#     "mteb[codecarbon]>=1.36.10",
# ]
# ///

"""
runs a set of predefined models on all benchmarks.

Can be reproduced by running:

```
uv run scripts/run_model_suite.py
```

which installs the required dependencies (based on the file header) in a new environement and runs the script.  
"""


from __future__ import annotations

import mteb

apis = [] # would require some sort of CI setup (to having to share APIs keys)

# a set of small and efficient models that we can reasonably maintain
baseline_models = [
    "sentence-transformers/static-similarity-mrl-multilingual-v1",
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
    "intfloat/multilingual-e5-small",
    #"intfloat/multilingual-e5-base",
    #"intfloat/multilingual-e5-large",
] + apis

benchmarks = mteb.get_benchmarks()
for bench in benchmarks:
    print("Running", bench.name)

    if bench.name == "CodeRAG":
        continue


    for model_name in baseline_models:
        try:
            model = mteb.get_model(model_name)
            runner = mteb.MTEB(tasks=bench)
            runner.run(
                model,
                # output_folder= ..., # should point to the results repo to not rerun results
                overwrite_results=False,
                co2_tracker=False, # model_name not in apis,  # only tracks co2 for non-api models
                raise_on_error=False,
            )
        except:
            pass


# ERRORS
# ERROR:mteb.evaluation.MTEB:Error while evaluating PubChemSMILESPC: PubChemSMILESPC.load_data() got an unexpected keyword argument 'raise_on_error'
# 
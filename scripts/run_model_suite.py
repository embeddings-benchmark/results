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
    "intfloat/multilingual-e5-small",
    "intfloat/multilingual-e5-base",
    "intfloat/multilingual-e5-large",
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
] + apis

benchmarks = mteb.get_benchmarks()
for model_name in baseline_models:
    for bench in benchmarks:

        try:
            runner = mteb.MTEB(tasks=bench)
            model = mteb.get_model(model_name)
            runner.run(
                model,
                # output_folder= ..., # should point to the results repo to not rerun results
                overwrite_results=False,
                co2_tracker=model_name not in apis,  # only tracks co2 for non-api models
                raise_on_error=False,
            )
        except:
            pass
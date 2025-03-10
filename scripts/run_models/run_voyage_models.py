# /// script
# requires-python = "==3.12"
# dependencies = [
#     "mteb>=1.36.10",
#     "voyageai",
# ]
# ///

import mteb

voyage_models = [
    "voyageai/voyage-3",
    "voyageai/voyage-3-lite",
    "voyageai/voyage-3-m-exp",
    "voyageai/voyage-multilingual-2",
    "voyageai/voyage-2",
    "voyage-large-2",
    "voyageai/voyage-code-3",
    "voyageai/voyage-code-2",
    "voyageai/voyage-law-2",
    "voyageai/voyage-finance-2",
    "voyageai/voyage-large-2-instruct",
    "voyageai/voyage-multimodal-3",
]
benchmarks = mteb.get_benchmarks()


for bench in benchmarks:
    for mdl_name in voyage_models:
        print(f"Running {mdl_name} on {bench.name}")
        model = mteb.get_model(mdl_name)

        runner = mteb.MTEB(tasks=[bench.tasks])
        runner.run(
            model, co2_tracker=False, raise_on_error=True
        )  # a we are using an API

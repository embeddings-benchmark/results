import json
import os

REPLACE_MAP = {
    "NDCG": 'ndcg',
    "MAP": 'map',
    "MRR": 'mrr',
    "RECALL": 'recall',
    "P": 'precision',
}

MODEL_TO_MODEL = {
    "bm25": "bm25",
    "bge": "bge-large-en-v1.5",
    "cohere": "Cohere-embed-english-v3.0",
    "e5": "e5-mistral-7b-instruct",
    "google": "google-gecko.text-embedding-preview-0409",
    "grit": "GritLM-7B",
    "inst-l": "instructor-large",
    "inst-xl": "instructor-xl",
    "openai": "text-embedding-3-large",
    "qwen2": "gte-Qwen2-7B-instruct",
    "qwen": "gte-Qwen1.5-7B-instruct",
    "sbert": "all-mpnet-base-v2",
    "sf": "SFR-Embedding-Mistral",
    "voyage": "voyage-large-2-instruct",
}
folders = os.listdir('bright_scores')
print(folders)
models = set([x.split("_")[-3] for x in folders if os.path.isdir('bright_scores/' + x)])
for model in models:
    print(f"Converting {model}")
    result_template = {
        "dataset_revision": "a75a0eb",
        "mteb_version": "1.12.79",
        "scores": {
            "standard": []
        },
        "task_name": "BrightRetrieval",
    }
    for folder in [x for x in folders if (os.path.isdir('bright_scores/' + x)) and (x.split("_")[-3] == model)]:
        results_path = 'bright_scores/' + folder + '/results.json'
        if len(folder.split("_")) == 4:
            split = folder.split("_")[0]
        elif len(folder.split("_")) == 5:
            split = folder.split("_")[0] + "_" + folder.split("_")[1]
        with open(results_path) as f:
            results = json.load(f)
        result_template['scores']['standard'].append(
            {
                "hf_subset": split,
                "languages": ["eng-Latn"],
                "main_score": results["NDCG@10"],
                **{"_at_".join([REPLACE_MAP.get(x, x) for x in k.split("@")]): v for k,v in results.items()}
            }
        )
    
    model_folder = MODEL_TO_MODEL[model]
    os.makedirs(f"results/{model_folder}/no_revision_available", exist_ok=True)
    print(f"Writing to: results/{model_folder}/no_revision_available/BrightRetrieval.json")
    with open(f"results/{model_folder}/no_revision_available/BrightRetrieval.json", "w") as f:
        json.dump(result_template, f, indent=4)



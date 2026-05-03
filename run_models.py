# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "mteb[peft]>=2.12.37",
# ]
#
# [tool.uv.sources]
# mteb = { git = "https://github.com/embeddings-benchmark/mteb" }
# ///
"""
requires login:
uv pip install huggingface_hub
hf auth login

install from git should not be nec., but the latest version does not seem to be in pypi (will check later)
"""

from pathlib import Path

import mteb

task = mteb.get_tasks(
    [
        "LexRetrieval.v1",
        "GlobalNewsRetrieval",
        "PublicNewsRetrieval",
        "ElasticKBRetrieval",
    ]
)

model_names = [
    "microsoft/harrier-oss-v1-0.6b",
    "Qwen/Qwen3-Embedding-0.6B",
    "jinaai/jina-embeddings-v5-text-small",
    "Octen/Octen-Embedding-0.6B",
    # "nvidia/llama-nemotron-embed-1b-v2",
    
    "BAAI/bge-m3",
    "intfloat/multilingual-e5-large",
]

cache_path = Path(__file__).parent
cache = mteb.ResultCache(cache_path)
assert cache.get_models()

# model_metas = mteb.get_model_metas(model_names)

# for model_meta in model_metas:
#     model_meta._check_requirements() # peft

# not implemented in mteb yet, so directly get model and evaluate here - sentence trf. compatible though.
model_name= "nvidia/llama-nemotron-embed-1b-v2"
model = mteb.get_model("nvidia/llama-nemotron-embed-1b-v2", trust_remote_code=True)
print(model_name)
res = mteb.evaluate(model, task, cache=cache)

# for model in model_metas:
#     print(model.name)
#     res = mteb.evaluate(model, task, cache=cache)

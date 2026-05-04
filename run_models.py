# /// script
# requires-python = "==3.12.*"
# dependencies = [
#     "mteb[peft]>=2.12.37",
#     "torch",
#     "flash-attn @ https://github.com/mjun0812/flash-attention-prebuild-wheels/releases/download/v0.7.16/flash_attn-2.8.3+cu128torch2.7-cp312-cp312-linux_x86_64.whl",
# ]
#
# [tool.uv.sources]
# mteb = { git = "https://github.com/embeddings-benchmark/mteb"}
# torch = { index = "pytorch-cu128" }
#
# [[tool.uv.index]]
# name = "pytorch-cu128"
# url = "https://download.pytorch.org/whl/cu128"
# explicit = true
# ///
"""
requires login:
uv pip install huggingface_hub
hf auth login

install from git should not be nec., but the latest version does not seem to be in pypi (will check later)
also missed had to fix the private sets (so using branch fix-private-sets)
"""
import logging
from pathlib import Path

import mteb

# setup logger:
# logging.basicConfig(
#     format="%(asctime)s - %(levelname)s - %(message)s",
#     level=logging.INFO,
# )

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
    "nvidia/llama-nemotron-embed-1b-v2",
    
    "BAAI/bge-m3",
    "intfloat/multilingual-e5-large",
]

cache_path = Path(__file__).parent
cache = mteb.ResultCache(cache_path)
assert cache.get_models()

model_metas = mteb.get_model_metas(model_names)

# for model_meta in model_metas:
#     model_meta._check_requirements() # peft

# not implemented in mteb yet, so directly get model and evaluate here - sentence trf. compatible though.
model_name= "nvidia/llama-nemotron-embed-1b-v2"
model = mteb.get_model("nvidia/llama-nemotron-embed-1b-v2", trust_remote_code=True, device="cuda")
print(model_name)
res = mteb.evaluate(model, task, cache=cache, raise_error=False, encode_kwargs={"batch_size": 8})

for model in model_metas:
    print(model.name)
    mdl = model.load_model(device="cuda")
    res = mteb.evaluate(mdl, task, cache=cache, encode_kwargs={"batch_size": 8}, raise_error=False)


for model in model_metas:
    print(model.name)
    mdl = model.load_model(device="cuda")
    res = mteb.evaluate(mdl, task, cache=cache, encode_kwargs={"batch_size": 1}, raise_error=False)

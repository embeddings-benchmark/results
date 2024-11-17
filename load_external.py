from __future__ import annotations

import json
import logging
import math
import re
from pathlib import Path
from typing import Any

from huggingface_hub import HfApi, get_hf_file_metadata, hf_hub_download, hf_hub_url
from huggingface_hub.errors import NotASafetensorsRepoError
from huggingface_hub.hf_api import ModelInfo
from huggingface_hub.repocard import metadata_load
from mteb import ModelMeta, get_task

API = HfApi()
logger = logging.getLogger(__name__)


library_mapping = {
    "sentence-transformers": "Sentence Transformers",
}


def get_model_dir(model_id: str) -> Path:
    external_result_dir = Path("results") / model_id.replace("/", "__") / "external"
    return external_result_dir


def simplify_dataset_name(name: str) -> str:
    return name.replace("MTEB ", "").split()[0]


def get_model_parameters_memory(model_info: ModelInfo) -> tuple[int| None, float|None]:
    try:
        safetensors = API.get_safetensors_metadata(model_info.id)
        num_parameters = sum(safetensors.parameter_count.values())
        return num_parameters, round(num_parameters * 4 / 1024 ** 3, 2)
    except NotASafetensorsRepoError as e:
        logger.info(f"Could not find SafeTensors metadata for {model_info.id}")

    filenames = [sib.rfilename for sib in model_info.siblings]
    if "pytorch_model.bin" in filenames:
        url = hf_hub_url(model_info.id, filename="pytorch_model.bin")
        meta = get_hf_file_metadata(url)
        bytes_per_param = 4
        num_params = round(meta.size / bytes_per_param)
        size_gb = round(meta.size * (4 / bytes_per_param) / 1024 ** 3, 2)
        return num_params, size_gb
    if "pytorch_model.bin.index.json" in filenames:
        index_path = hf_hub_download(model_info.id, filename="pytorch_model.bin.index.json")
        size = json.load(open(index_path))
        bytes_per_param = 4
        if "metadata" in size and "total_size" in size["metadata"]:
            return round(size["metadata"]["total_size"] / bytes_per_param), round(size["metadata"]["total_size"] / 1024 ** 3, 2)
    logger.info(f"Could not find the model parameters for {model_info.id}")
    return None, None


def get_dim_seq_size(model: ModelInfo) -> tuple[str | None, str | None, int, float]:
    siblings = model.siblings or []
    filenames = [sib.rfilename for sib in siblings]
    dim, seq = None, None
    for filename in filenames:
        if re.match(r"\d+_Pooling/config.json", filename):
            st_config_path = hf_hub_download(model.id, filename=filename)
            dim = json.load(open(st_config_path)).get("word_embedding_dimension", None)
            break
    for filename in filenames:
        if re.match(r"\d+_Dense/config.json", filename):
            st_config_path = hf_hub_download(model.id, filename=filename)
            dim = json.load(open(st_config_path)).get("out_features", dim)
    if "config.json" in filenames:
        config_path = hf_hub_download(model.id, filename="config.json")
        config = json.load(open(config_path))
        if not dim:
            dim = config.get("hidden_dim", config.get("hidden_size", config.get("d_model", None)))
        seq = config.get("n_positions", config.get("max_position_embeddings", config.get("n_ctx", config.get("seq_length", None))))

    parameters, memory = get_model_parameters_memory(model)
    return dim, seq, parameters, memory


def create_model_meta(model_info: ModelInfo) -> ModelMeta | None:
    readme_path = hf_hub_download(model_info.id, filename="README.md", etag_timeout=30)
    meta = metadata_load(readme_path)
    dim, seq, parameters, memory = None, None, None, None
    try:
        dim, seq, parameters, memory = get_dim_seq_size(model_info)
    except Exception as e:
        logger.error(f"Error getting model parameters for {model_info.id}, {e}")

    release_date = str(model_info.created_at.date()) if model_info.created_at else ""
    library = [library_mapping[model_info.library_name]] if model_info.library_name in library_mapping else []
    languages = meta.get("language", [])
    if not isinstance(languages, list) and isinstance(languages, str):
        languages = [languages]
    # yaml transforms norwegian `no` to False
    for i in range(len(languages)):
        if languages[i] is False:
            languages[i] = "no"

    model_meta = ModelMeta(
        name=model_info.id,
        revision=model_info.sha,
        release_date=release_date,
        open_weights=True,
        framework=library,
        license=meta.get("license", None),
        embed_dim=dim,
        max_tokens=seq,
        n_parameters=parameters,
        languages=languages,
    )
    return model_meta


def parse_readme(model_info: ModelInfo) -> dict[str, dict[str, Any]] | None:
    model_id = model_info.id
    try:
        readme_path = hf_hub_download(model_info.id, filename="README.md", etag_timeout=30)
    except Exception:
        logger.warning(f"ERROR: Could not fetch metadata for {model_id}, trying again")
        readme_path = hf_hub_download(model_id, filename="README.md", etag_timeout=30)
    meta = metadata_load(readme_path)
    if "model-index" not in meta:
        logger.info(f"Could not find model-index in {model_id}")
        return
    model_index = meta["model-index"][0]
    model_name_from_readme = model_index.get("name", None)
    orgs = ["Alibaba-NLP", "HIT-TMG", "McGill-NLP", "Snowflake", "facebook", "jinaai", "nomic-ai"]
    is_org = any([model_id.startswith(org) for org in orgs])
    # There a lot of reuploads with tunes, quantization, etc. We only want the original model
    # to prevent this most of the time we can check if the model name from the readme is the same as the model id
    # but some orgs have a different naming in their readme
    if model_name_from_readme and not model_info.id.endswith(model_name_from_readme) and not is_org:
        logger.warning(f"Model name mismatch: {model_info.id} vs {model_name_from_readme}")
        return
    results = model_index.get("results", [])
    model_results = {}
    for result in results:
        dataset = result["dataset"]
        dataset_type = dataset["type"]  # type is repo of the dataset
        if dataset_type not in model_results:
            output_dict = {
                "dataset_revision": dataset.get("revision", ""),
                "task_name": simplify_dataset_name(dataset["name"]),
                "evaluation_time": None,
                "mteb_version": None,
                "scores": {},
            }
        else:
            output_dict = model_results[dataset_type]

        try:
            mteb_task = get_task(output_dict["task_name"])
        except Exception:
            logger.warning(f"Error getting task for {model_id} {output_dict['task_name']}")
            continue

        mteb_task_metadata = mteb_task.metadata
        mteb_task_eval_languages = mteb_task_metadata.eval_langs

        scores_dict = output_dict["scores"]
        current_split = dataset["split"]
        current_config = dataset.get("config", "")
        cur_split_metrics = {
            "hf_subset": current_config,
            "languages": mteb_task_eval_languages if isinstance(mteb_task_eval_languages, list) else mteb_task_eval_languages.get(current_config, ["None"]),
        }
        for metric in result["metrics"]:
            if isinstance(metric["value"], (float, int)):
                cur_split_metrics[metric["type"]] = metric["value"] / 100
            else:
                cur_split_metrics[metric["type"]] = metric["value"]

        main_score_str = "main_score"
        if main_score_str not in cur_split_metrics:
            # old sts and sum_eval have cos_sim_pearson, but in model_meta cosine_spearman is main_score
            for old_metric, new_metric in zip(["cos_sim_pearson", "cos_sim_spearman"], ["cosine_pearson", "cosine_spearman"]):
                if old_metric in cur_split_metrics:
                    cur_split_metrics[new_metric] = cur_split_metrics[old_metric]

            if mteb_task.metadata.main_score not in cur_split_metrics:
                logger.warning(f"Could not find main score for {model_id} {output_dict['task_name']}, mteb task {mteb_task.metadata.name}. Main score: {mteb_task.metadata.main_score}. Metrics: {cur_split_metrics}, result {result['metrics']}")
                continue

            cur_split_metrics[main_score_str] = cur_split_metrics.get(mteb_task.metadata.main_score, None)
        split_metrics = scores_dict.get(current_split, [])
        split_metrics.append(cur_split_metrics)
        scores_dict[current_split] = split_metrics
        model_results[dataset_type] = output_dict
    return model_results


def get_mteb_data() -> None:
    models = sorted(list(API.list_models(filter="mteb", full=True)), key=lambda x: x.id)
    # models = [model for model in models if model.id == "intfloat/multilingual-e5-large"]
    for i, model_info in enumerate(models, start=1):
        logger.info(f"[{i}/{len(models)}] Processing {model_info.id}")
        model_path = get_model_dir(model_info.id)
        if (model_path / "model_meta.json").exists() and len(list(model_path.glob("*.json"))) > 1:
            logger.info(f"Model meta already exists for {model_info.id}")
            # continue
        if model_info.id.lower().endswith("gguf"):
            logger.info(f"Skipping {model_info.id} GGUF model")
            continue

        spam_users = ["ILKT", "fine-tuned", "mlx-community"]
        is_spam = False
        for spam_user in spam_users:
            if model_info.id.startswith(spam_user):
                logger.info(f"Skipping {model_info.id}")
                is_spam = True
                continue
        if is_spam:
            continue
        model_meta = create_model_meta(model_info)
        model_results = parse_readme(model_info)

        if not model_meta or not model_results:
            logger.warning(f"Could not get model meta or results for {model_info.id}")
            continue

        if not model_path.exists():
            model_path.mkdir(parents=True, exist_ok=True)

        model_meta_path = model_path / "model_meta.json"
        with model_meta_path.open("w") as f:
            json.dump(model_meta.model_dump(), f, indent=4)

        for model_result in model_results:
            task_name = model_results[model_result]["task_name"]
            result_file = model_path / f"{task_name}.json"
            with result_file.open("w") as f:
                json.dump(model_results[model_result], f, indent=4)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    get_mteb_data()

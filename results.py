"""MTEB Results"""
from __future__ import annotations

import json

import datasets


logger = datasets.logging.get_logger(__name__)


_CITATION = """@article{muennighoff2022mteb,
  doi = {10.48550/ARXIV.2210.07316},
  url = {https://arxiv.org/abs/2210.07316},
  author = {Muennighoff, Niklas and Tazi, Nouamane and Magne, Lo{\"\i}c and Reimers, Nils},
  title = {MTEB: Massive Text Embedding Benchmark},
  publisher = {arXiv},
  journal={arXiv preprint arXiv:2210.07316},
  year = {2022}
}
"""

_DESCRIPTION = """Results on MTEB"""

URL = "https://huggingface.co/datasets/mteb/results/resolve/main/paths.json"
VERSION = datasets.Version("1.0.1")
EVAL_LANGS = ['af', 'afr-eng', 'am', "amh", 'amh-eng', 'ang-eng', 'ar', 'ar-ar', 'ara-eng', 'arq-eng', 'arz-eng', 'ast-eng', 'awa-eng', 'az', 'aze-eng', 'bel-eng', 'ben-eng', 'ber-eng', 'bn', 'bos-eng', 'bre-eng', 'bul-eng', 'cat-eng', 'cbk-eng', 'ceb-eng', 'ces-eng', 'cha-eng', 'cmn-eng', 'cor-eng', 'csb-eng', 'cy', 'cym-eng', 'da', 'dan-eng', 'de', 'de-fr', 'de-pl', 'deu-eng', 'dsb-eng', 'dtp-eng', 'el', 'ell-eng', 'en', 'en-ar', 'en-de', 'en-en', 'en-tr', 'eng', 'epo-eng', 'es', 'es-en', 'es-es', 'es-it', 'est-eng', 'eus-eng', 'fa', 'fao-eng', 'fi', 'fin-eng', 'fr', 'fr-en', 'fr-pl', 'fra', 'fra-eng', 'fry-eng', 'gla-eng', 'gle-eng', 'glg-eng', 'gsw-eng', 'hau', 'he', 'heb-eng', 'hi', 'hin-eng', 'hrv-eng', 'hsb-eng', 'hu', 'hun-eng', 'hy', 'hye-eng', 'ibo', 'id', 'ido-eng', 'ile-eng', 'ina-eng', 'ind-eng', 'is', 'isl-eng', 'it', 'it-en', 'ita-eng', 'ja', 'jav-eng', 'jpn-eng', 'jv', 'ka', 'kab-eng', 'kat-eng', 'kaz-eng', 'khm-eng', 'km', 'kn', 'ko', 'ko-ko', 'kor-eng', 'kur-eng', 'kzj-eng', 'lat-eng', 'lfn-eng', 'lit-eng', 'lin', 'lug', 'lv', 'lvs-eng', 'mal-eng', 'mar-eng', 'max-eng', 'mhr-eng', 'mkd-eng', 'ml', 'mn', 'mon-eng', 'ms', 'my', 'nb', 'nds-eng', 'nl', 'nl-ende-en', 'nld-eng', 'nno-eng', 'nob-eng', 'nov-eng', 'oci-eng', 'orm', 'orv-eng', 'pam-eng', 'pcm', 'pes-eng', 'pl', 'pl-en', 'pms-eng', 'pol-eng', 'por-eng', 'pt', 'ro', 'ron-eng', 'ru', 'run', 'rus-eng', 'sl', 'slk-eng', 'slv-eng', 'spa-eng', 'sna', 'som', 'sq', 'sqi-eng', 'srp-eng', 'sv', 'sw', 'swa', 'swe-eng', 'swg-eng', 'swh-eng', 'ta', 'tam-eng', 'tat-eng', 'te', 'tel-eng', 'tgl-eng', 'th', 'tha-eng', 'tir', 'tl', 'tr', 'tuk-eng', 'tur-eng', 'tzl-eng', 'uig-eng', 'ukr-eng', 'ur', 'urd-eng', 'uzb-eng', 'vi', 'vie-eng', 'war-eng', 'wuu-eng', 'xho', 'xho-eng', 'yid-eng', 'yor', 'yue-eng', 'zh', 'zh-CN', 'zh-TW', 'zh-en', 'zsm-eng']

# v_measures key is somehow present in voyage-2-law results and is a list
SKIP_KEYS = ["std", "evaluation_time", "main_score", "threshold", "v_measures", "scores_per_experiment"]

# Use "train" split instead
TRAIN_SPLIT = ["DanishPoliticalCommentsClassification"]
# Use "validation" split instead
VALIDATION_SPLIT = ["AFQMC", "Cmnli", "IFlyTek", "LEMBSummScreenFDRetrieval", "MSMARCO", "MSMARCO-PL", "MultilingualSentiment", "Ocnli", "TNews"]
# Use "dev" split instead
DEV_SPLIT = ["CmedqaRetrieval", "CovidRetrieval", "DuRetrieval", "EcomRetrieval", "MedicalRetrieval", "MMarcoReranking", "MMarcoRetrieval", "MSMARCO", "MSMARCO-PL", "T2Reranking", "T2Retrieval", "VideoRetrieval", "TERRa", "MIRACLReranking", "MIRACLRetrieval"]
# Use "test.full" split
TESTFULL_SPLIT = ["OpusparcusPC"]
# Use "standard" split
STANDARD_SPLIT = ["BrightRetrieval"]
# Use "devtest" split
DEVTEST_SPLIT = ["FloresBitextMining"]

TEST_AVG_SPLIT = {
    "LEMBNeedleRetrieval": ["test_256", "test_512", "test_1024", "test_2048", "test_4096", "test_8192", "test_16384", "test_32768"],
    "LEMBPasskeyRetrieval": ["test_256", "test_512", "test_1024", "test_2048", "test_4096", "test_8192", "test_16384", "test_32768"],
}

MODELS = [
    "Baichuan-text-embedding",
    "Cohere-embed-english-v3.0",
    "Cohere-embed-english-v3.0-instruct",
    "Cohere-embed-multilingual-light-v3.0",
    "Cohere-embed-multilingual-v3.0",
    "DanskBERT",
    "FollowIR-7B",
    "GritLM-7B",
    "GritLM-7B-noinstruct",
    "LASER2",
    "LLM2Vec-Llama-2-supervised",
    "LLM2Vec-Llama-2-unsupervised",
    "LLM2Vec-Meta-Llama-3-supervised",
    "LLM2Vec-Meta-Llama-3-unsupervised",
    "LLM2Vec-Mistral-supervised",
    "LLM2Vec-Mistral-unsupervised",
    "LLM2Vec-Sheared-Llama-supervised",
    "LLM2Vec-Sheared-Llama-unsupervised",
    "LaBSE",
    "OpenSearch-text-hybrid",
    "SFR-Embedding-Mistral",
    "all-MiniLM-L6-v2",
    "all-MiniLM-L6-v2-instruct",
    "all-mpnet-base-v2",
    "all-mpnet-base-v2-instruct",
    "allenai-specter",
    "bert-base-10lang-cased",
    "bert-base-15lang-cased",
    "bert-base-25lang-cased",
    "bert-base-multilingual-cased",
    "bert-base-multilingual-uncased",
    "bert-base-swedish-cased",
    "bert-base-uncased",
    "bge-base-en-v1.5",
    "bge-base-en-v1.5-instruct",
    "bge-base-en",
    "bge-base-zh",
    "bge-base-zh-v1.5",
    "bge-large-en",
    "bge-large-en-v1.5",
    "bge-large-en-v1.5-instruct",
    "bge-large-zh",
    "bge-large-zh-noinstruct",
    "bge-large-zh-v1.5",
    "bge-m3",
    "bge-m3-instruct",
    "bge-small-en-v1.5",
    "bge-small-en-v1.5-instruct",
    "bge-small-zh",
    "bge-small-zh-v1.5",
    "bm25",
    "bm25s",
    "camembert-base",
    "camembert-large",
    "contriever",
    "contriever-instruct",
    "contriever-base-msmarco",
    "cross-en-de-roberta-sentence-transformer",
    "dfm-encoder-large-v1",
    "distilbert-base-25lang-cased",
    "distilbert-base-en-fr-cased",
    "distilbert-base-en-fr-es-pt-it-cased",
    "distilbert-base-fr-cased",
    "distilbert-base-uncased",
    "distiluse-base-multilingual-cased-v2",
    "dragon-plus",
    "dragon-plus-instruct",
    "e5-base",
    "e5-base-4k",
    "e5-base-v2",
    "e5-large",
    "e5-large-v2",
    "e5-mistral-7b-instruct",
    "e5-mistral-7b-instruct-noinstruct",
    "e5-small",
    "e5-small-v2",
    "electra-small-nordic",
    "electra-small-swedish-cased-discriminator",
    "elser-v2",
    "embedder-100p",
    "facebook-dpr-ctx_encoder-multiset-base",
    "facebookdragon-plus-context-encoder",
    "flan-t5-base",
    "flan-t5-large",
    "flaubert_base_cased",
    "flaubert_base_uncased",
    "flaubert_large_cased",
    "gbert-base",
    "gbert-large",
    "gelectra-base",
    "gelectra-large",
    "glove.6B.300d",
    "google-gecko-256.text-embedding-preview-0409",
    "google-gecko.text-embedding-preview-0409",
    "gottbert-base",
    "gte-Qwen1.5-7B-instruct",
    "gte-Qwen2-7B-instruct",
    "gtr-t5-base",
    "gtr-t5-large",
    "gtr-t5-xl",
    "gtr-t5-xxl",
    "herbert-base-retrieval-v2",
    "instructor-base",
    "instructor-large",
    "instructor-xl",
    "jina-embeddings-v2-base-en",
    "komninos",
    "llama-2-7b-chat",
    "luotuo-bert-medium",
    "m3e-base",
    "m3e-large",
    "mistral-7b-instruct-v0.2",
    "mistral-embed",
    "monobert-large-msmarco",
    "monot5-3b-msmarco-10k",
    "monot5-base-msmarco-10k",
    "msmarco-bert-co-condensor",
    "multi-qa-MiniLM-L6-cos-v1",
    "multilingual-e5-base",
    "multilingual-e5-large",
    "multilingual-e5-large-instruct",
    "multilingual-e5-small",
    "mxbai-embed-large-v1",
    "nb-bert-base",
    "nb-bert-large",
    "nomic-embed-text-v1",
    "nomic-embed-text-v1.5-128",
    "nomic-embed-text-v1.5-256",
    "nomic-embed-text-v1.5-512",
    "nomic-embed-text-v1.5-64",
    "norbert3-base",
    "norbert3-large",
    "paraphrase-multilingual-MiniLM-L12-v2",
    "paraphrase-multilingual-mpnet-base-v2",
    "rubert-tiny",
    "rubert-tiny2",
    "sbert_large_mt_nlu_ru",
    "sbert_large_nlu_ru",
    "sentence-bert-swedish-cased",
    "sentence-camembert-base",
    "sentence-camembert-large",
    "sentence-croissant-llm-base",
    "sentence-t5-base",
    "sentence-t5-large",
    "sentence-t5-xl",
    "sentence-t5-xxl",
    "all-MiniLM-L12-v2",
    "sgpt-bloom-1b7-nli",
    "sgpt-bloom-7b1-msmarco",
    "SGPT-125M-weightedmean-nli-bitfit",
    "SGPT-1.3B-weightedmean-msmarco-specb-bitfit",
    "SGPT-5.8B-weightedmean-msmarco-specb-bitfit-que",
    "SGPT-5.8B-weightedmean-msmarco-specb-bitfit",
    "SGPT-5.8B-weightedmean-nli-bitfit",
    "SGPT-2.7B-weightedmean-msmarco-specb-bitfit",
    "SGPT-125M-weightedmean-msmarco-specb-bitfit-que",
    "SGPT-125M-weightedmean-msmarco-specb-bitfit-doc",
    "SGPT-125M-weightedmean-msmarco-specb-bitfit",
    "silver-retriever-base-v1",
    "st-polish-paraphrase-from-distilroberta",
    "st-polish-paraphrase-from-mpnet",
    "sup-simcse-bert-base-uncased",
    "tart-dual-contriever-msmarco",
    "tart-full-flan-t5-xl",
    "text-embedding-3-large",
    "text-embedding-3-large-instruct",
    "text-embedding-3-large-256",
    "text-embedding-3-small",
    "text-embedding-3-small-instruct",
    "text-embedding-ada-002",
    "text-embedding-ada-002-instruct",
    "text-search-ada-001",
    "text-search-ada-doc-001",
    "text-search-babbage-001",
    "text-search-curie-001",
    "text-search-davinci-001",
    "text-similarity-ada-001",
    "text-similarity-babbage-001",
    "text-similarity-curie-001",
    "text-similarity-davinci-001",
    "text2vec-base-chinese",
    "text2vec-base-multilingual",
    "text2vec-large-chinese",
    "titan-embed-text-v1",
    "udever-bloom-1b1",
    "udever-bloom-560m",
    "universal-sentence-encoder-multilingual-3",
    "universal-sentence-encoder-multilingual-large-3",
    "unsup-simcse-bert-base-uncased",
    "use-cmlm-multilingual",
    "voyage-2",
    "voyage-code-2",
    "voyage-large-2-instruct",
    "voyage-law-2",
    "voyage-lite-01-instruct",
    "voyage-lite-02-instruct",
    "voyage-multilingual-2",
    "xlm-roberta-base",
    "xlm-roberta-large",
    "deberta-v1-base",
    "USER-bge-m3",
    "USER-base",
    "rubert-tiny-turbo",
    "LaBSE-ru-turbo",
    "distilrubert-small-cased-conversational",
    "rubert-base-cased",
    "rubert-base-cased-sentence",
    "LaBSE-en-ru",
]


def get_model_for_current_dir(dir_name: str) -> str | None:
    for model in MODELS:
        if model == dir_name or ("__" in dir_name and dir_name.split("__")[1] == model):
            return model
    return None


# Needs to be run whenever new files are added
def get_paths():
    import collections, json, os
    files = collections.defaultdict(list)
    for model_dir in os.listdir("results"):
        results_model_dir = os.path.join("results", model_dir)
        if not os.path.isdir(results_model_dir):
            print(f"Skipping {results_model_dir}")
            continue
        model_name = get_model_for_current_dir(model_dir)
        if model_name is None:
            print(f"Skipping {model_dir} model dir")
            continue
        for revision_folder in os.listdir(results_model_dir):
            if not os.path.isdir(os.path.join(results_model_dir, revision_folder)):
                continue
            for res_file in os.listdir(os.path.join(results_model_dir, revision_folder)):
                if (res_file.endswith(".json")) and not(res_file.endswith(("overall_results.json", "model_meta.json"))):
                    results_model_file = os.path.join(results_model_dir, revision_folder, res_file)
                    files[model_name].append(results_model_file)
    with open("paths.json", "w") as f:
        json.dump(files, f, indent=2)
    return files


class MTEBResults(datasets.GeneratorBasedBuilder):
    """MTEBResults"""

    BUILDER_CONFIGS = [
        datasets.BuilderConfig(
            name=model,
            description=f"{model} MTEB results",
            version=VERSION,
        )
        for model in MODELS
    ]

    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(
                {
                    "mteb_dataset_name": datasets.Value("string"),
                    "eval_language": datasets.Value("string"),
                    "metric": datasets.Value("string"),
                    "score": datasets.Value("float"),
                    "split": datasets.Value("string"),
                    "hf_subset": datasets.Value("string"),
                }
            ),
            supervised_keys=None,
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        path_file = dl_manager.download_and_extract(URL)
        # Local debugging help
        # with open("/path/to/local/paths.json") as f:
        with open(path_file) as f:
            files = json.load(f)
        downloaded_files = dl_manager.download_and_extract(files[self.config.name])
        return [
            datasets.SplitGenerator(
                name=datasets.Split.TEST,
                gen_kwargs={'filepath': downloaded_files}
            )
        ]

    def _generate_examples(self, filepath):
        """This function returns the examples in the raw (text) form."""
        logger.info(f"Generating examples from {filepath}")
        out = []

        for path in filepath:
            with open(path, encoding="utf-8") as f:
                res_dict = json.load(f)
                # Naming changed from mteb_dataset_name to task_name
                ds_name = res_dict.get("mteb_dataset_name", res_dict.get("task_name"))
                # New MTEB format uses scores
                res_dict = res_dict.get("scores", res_dict)

                split = "test"
                if (ds_name in TRAIN_SPLIT) and ("train" in res_dict):
                    split = "train"
                elif (ds_name in VALIDATION_SPLIT) and ("validation" in res_dict):
                    split = "validation"
                elif (ds_name in DEV_SPLIT) and ("dev" in res_dict):
                    split = "dev"
                elif (ds_name in TESTFULL_SPLIT) and ("test.full" in res_dict):
                    split = "test.full"
                elif (ds_name in STANDARD_SPLIT):
                    split = []
                    if "standard" in res_dict:
                        split += ["standard"]
                    if "long" in res_dict:
                        split += ["long"]
                elif (ds_name in DEVTEST_SPLIT) and ("devtest" in res_dict):
                    split = "devtest"
                elif (ds_name in TEST_AVG_SPLIT):
                    # Average splits
                    res_dict = {}
                    for split in TEST_AVG_SPLIT[ds_name]:
                        # Old MTEB format
                        if isinstance(res_dict.get(split), dict):
                            for k, v in res_dict.get(split, {}).items():
                                if k in ["hf_subset", "languages"]:
                                    res_dict[k] = v

                                v /= len(TEST_AVG_SPLIT[ds_name])
                                if k not in res_dict:
                                    res_dict[k] = v
                                else:
                                    res_dict[k] += v
                        # New MTEB format
                        elif isinstance(res_dict.get(split), list):
                            assert len(res_dict[split]) == 1, "Only single-lists supported for now"
                            for k, v in res_dict[split][0].items():
                                if k in ["hf_subset", "languages"]:
                                    res_dict[k] = v
                                if not isinstance(v, float): continue
                                v /= len(TEST_AVG_SPLIT[ds_name])
                                if k not in res_dict:
                                    res_dict[k] = v
                                else:
                                    res_dict[k] += v
                    split = "test_avg"
                    res_dict = {split: [res_dict]}
                elif "test" not in res_dict:
                    print(f"Skipping {ds_name} as split {split} not present.")
                    continue

                splits = [split] if not isinstance(split, list) else split
                full_res_dict = res_dict
                for split in splits:
                    res_dict = full_res_dict.get(split)

                    ### New MTEB format ###
                    if isinstance(res_dict, list):
                        for res in res_dict:
                            lang = res.pop("languages", [""])
                            subset = res.pop("hf_subset", "")
                            if len(lang) == 1:
                                lang = lang[0].replace("eng-Latn", "")
                            else:
                                lang = "_".join(lang)
                            if not lang:
                                lang = subset
                            for metric, score in res.items():
                                if metric in SKIP_KEYS: continue
                                if isinstance(score, dict):
                                    # Legacy format with e.g. {cosine: {spearman: ...}}
                                    # Now it is {cosine_spearman: ...}
                                    for k, v in score.items():
                                        if not isinstance(v, float):
                                            print(f'WARNING: Expected float, got {v} for {ds_name} {lang} {metric} {k}')
                                            continue
                                        if metric in SKIP_KEYS: continue
                                        out.append({
                                            "mteb_dataset_name": ds_name,
                                            "eval_language": lang,
                                            "metric": metric + "_" + k,
                                            "score": v * 100,
                                            "hf_subset": subset,
                                        })
                                else:
                                    if not isinstance(score, float):
                                        print(f'WARNING: Expected float, got {score} for {ds_name} {lang} {metric}')
                                        continue
                                    out.append({
                                        "mteb_dataset_name": ds_name,
                                        "eval_language": lang,
                                        "metric": metric,
                                        "score": score * 100,
                                        "split": split,
                                        "hf_subset": subset,
                                    })

                    ### Old MTEB format ###
                    else:
                        is_multilingual = any(x in res_dict for x in EVAL_LANGS)
                        langs = res_dict.keys() if is_multilingual else ["en"]
                        for lang in langs:
                            if lang in SKIP_KEYS: continue
                            test_result_lang = res_dict.get(lang) if is_multilingual else res_dict
                            subset = test_result_lang.pop("hf_subset", "")
                            if subset == "" and is_multilingual:
                                subset = lang
                            for metric, score in test_result_lang.items():
                                if not isinstance(score, dict):
                                    score = {metric: score}
                                for sub_metric, sub_score in score.items():
                                    if any(x in sub_metric for x in SKIP_KEYS): continue
                                    if isinstance(sub_score, dict): continue
                                    out.append({
                                        "mteb_dataset_name": ds_name,
                                        "eval_language": lang if is_multilingual else "",
                                        "metric": f"{metric}_{sub_metric}" if metric != sub_metric else metric,
                                        "score": sub_score * 100,
                                        "split": split,
                                        "hf_subset": subset,
                                    })
        for idx, row in enumerate(sorted(out, key=lambda x: x["mteb_dataset_name"])):
            yield idx, row


# NOTE: for generating the new paths
if __name__ == "__main__":
    get_paths()

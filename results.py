"""MTEB Results"""

from __future__ import annotations

import json
import os
from pathlib import Path

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
EVAL_LANGS = [
    "af",
    "afr-eng",
    "am",
    "amh",
    "amh-eng",
    "ang-eng",
    "ar",
    "ar-ar",
    "ara-eng",
    "arq-eng",
    "arz-eng",
    "ast-eng",
    "awa-eng",
    "az",
    "aze-eng",
    "bel-eng",
    "ben-eng",
    "ber-eng",
    "bn",
    "bos-eng",
    "bre-eng",
    "bul-eng",
    "cat-eng",
    "cbk-eng",
    "ceb-eng",
    "ces-eng",
    "cha-eng",
    "cmn-eng",
    "cor-eng",
    "csb-eng",
    "cy",
    "cym-eng",
    "da",
    "dan-eng",
    "de",
    "de-fr",
    "de-pl",
    "deu-eng",
    "dsb-eng",
    "dtp-eng",
    "el",
    "ell-eng",
    "en",
    "en-ar",
    "en-de",
    "en-en",
    "en-tr",
    "eng",
    "epo-eng",
    "es",
    "es-en",
    "es-es",
    "es-it",
    "est-eng",
    "eus-eng",
    "fa",
    "fas-Arab",
    "fao-eng",
    "fi",
    "fin-eng",
    "fr",
    "fr-en",
    "fr-pl",
    "fra",
    "fra-eng",
    "fry-eng",
    "gla-eng",
    "gle-eng",
    "glg-eng",
    "gsw-eng",
    "hau",
    "he",
    "heb-eng",
    "hi",
    "hin-eng",
    "hrv-eng",
    "hsb-eng",
    "hu",
    "hun-eng",
    "hy",
    "hye-eng",
    "ibo",
    "id",
    "ido-eng",
    "ile-eng",
    "ina-eng",
    "ind-eng",
    "is",
    "isl-eng",
    "it",
    "it-en",
    "ita-eng",
    "ja",
    "jav-eng",
    "jpn-eng",
    "jv",
    "ka",
    "kab-eng",
    "kat-eng",
    "kaz-eng",
    "khm-eng",
    "km",
    "kn",
    "ko",
    "ko-ko",
    "kor-eng",
    "kur-eng",
    "kzj-eng",
    "lat-eng",
    "lfn-eng",
    "lit-eng",
    "lin",
    "lug",
    "lv",
    "lvs-eng",
    "mal-eng",
    "mar-eng",
    "max-eng",
    "mhr-eng",
    "mkd-eng",
    "ml",
    "mn",
    "mon-eng",
    "ms",
    "my",
    "nb",
    "nds-eng",
    "nl",
    "nl-ende-en",
    "nld-eng",
    "nno-eng",
    "nob-eng",
    "nov-eng",
    "oci-eng",
    "orm",
    "orv-eng",
    "pam-eng",
    "pcm",
    "pes-eng",
    "pl",
    "pl-en",
    "pms-eng",
    "pol-eng",
    "por-eng",
    "pt",
    "ro",
    "ron-eng",
    "ru",
    "run",
    "rus-eng",
    "sl",
    "slk-eng",
    "slv-eng",
    "spa-eng",
    "sna",
    "som",
    "sq",
    "sqi-eng",
    "srp-eng",
    "sv",
    "sw",
    "swa",
    "swe-eng",
    "swg-eng",
    "swh-eng",
    "ta",
    "tam-eng",
    "tat-eng",
    "te",
    "tel-eng",
    "tgl-eng",
    "th",
    "tha-eng",
    "tir",
    "tl",
    "tr",
    "tuk-eng",
    "tur-eng",
    "tzl-eng",
    "uig-eng",
    "ukr-eng",
    "ur",
    "urd-eng",
    "uzb-eng",
    "vi",
    "vie-eng",
    "war-eng",
    "wuu-eng",
    "xho",
    "xho-eng",
    "yid-eng",
    "yor",
    "yue-eng",
    "zh",
    "zh-CN",
    "zh-TW",
    "zh-en",
    "zsm-eng",
]

# v_measures key is somehow present in voyage-2-law results and is a list
SKIP_KEYS = ["std", "evaluation_time", "main_score", "threshold", "v_measures", "scores_per_experiment"]

# Use "train" split instead
TRAIN_SPLIT = ["DanishPoliticalCommentsClassification"]
# Use "validation" split instead
VALIDATION_SPLIT = [
    "AFQMC",
    "Cmnli",
    "IFlyTek",
    "LEMBSummScreenFDRetrieval",
    "MSMARCO",
    "MSMARCO-PL",
    "MSMARCO-Fa",
    "MultilingualSentiment",
    "Ocnli",
    "TNews",
]
# Use "dev" split instead
DEV_SPLIT = [
    "CmedqaRetrieval",
    "CovidRetrieval",
    "DuRetrieval",
    "EcomRetrieval",
    "MedicalRetrieval",
    "MMarcoReranking",
    "MMarcoRetrieval",
    "MSMARCO",
    "MSMARCO-PL",
    "MSMARCO-Fa",
    "T2Reranking",
    "T2Retrieval",
    "VideoRetrieval",
    "TERRa",
    "MIRACLReranking",
    "MIRACLRetrieval",
]
# Use "test.full" split
TESTFULL_SPLIT = ["OpusparcusPC"]
# Use "standard" split
STANDARD_SPLIT = ["BrightRetrieval"]
# Use "devtest" split
DEVTEST_SPLIT = ["FloresBitextMining"]

TEST_AVG_SPLIT = {
    "LEMBNeedleRetrieval": [
        "test_256",
        "test_512",
        "test_1024",
        "test_2048",
        "test_4096",
        "test_8192",
        "test_16384",
        "test_32768",
    ],
    "LEMBPasskeyRetrieval": [
        "test_256",
        "test_512",
        "test_1024",
        "test_2048",
        "test_4096",
        "test_8192",
        "test_16384",
        "test_32768",
    ],
}

MODELS = sorted(list(set([str(file).split('/')[-1] for file in (Path(__file__).parent / "results").glob("*") if file.is_dir()])))

# Needs to be run whenever new files are added
def get_paths():
    import collections, json, os

    files = collections.defaultdict(list)
    for model_dir in MODELS:
        results_model_dir = os.path.join("results", model_dir)
        if not os.path.isdir(results_model_dir):
            print(f"Skipping {results_model_dir}")
            continue
        for revision_folder in os.listdir(results_model_dir):
            if not os.path.isdir(os.path.join(results_model_dir, revision_folder)):
                continue
            if revision_folder == "external":
                continue
            for res_file in os.listdir(os.path.join(results_model_dir, revision_folder)):
                if (res_file.endswith(".json")) and not (
                    res_file.endswith(("overall_results.json", "model_meta.json"))
                ):
                    results_model_file = os.path.join(results_model_dir, revision_folder, res_file)
                    files[model_dir].append(results_model_file)
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
        return [datasets.SplitGenerator(name=datasets.Split.TEST, gen_kwargs={"filepath": downloaded_files})]

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
                elif ds_name in STANDARD_SPLIT:
                    split = []
                    if "standard" in res_dict:
                        split += ["standard"]
                    if "long" in res_dict:
                        split += ["long"]
                elif (ds_name in DEVTEST_SPLIT) and ("devtest" in res_dict):
                    split = "devtest"
                elif ds_name in TEST_AVG_SPLIT:
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
                                if not isinstance(v, float):
                                    continue
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
                                if metric in SKIP_KEYS:
                                    continue
                                if isinstance(score, dict):
                                    # Legacy format with e.g. {cosine: {spearman: ...}}
                                    # Now it is {cosine_spearman: ...}
                                    for k, v in score.items():
                                        if not isinstance(v, float):
                                            print(f"WARNING: Expected float, got {v} for {ds_name} {lang} {metric} {k}")
                                            continue
                                        if metric in SKIP_KEYS:
                                            continue
                                        out.append(
                                            {
                                                "mteb_dataset_name": ds_name,
                                                "eval_language": lang,
                                                "metric": metric + "_" + k,
                                                "score": v * 100,
                                                "hf_subset": subset,
                                            }
                                        )
                                else:
                                    if not isinstance(score, float):
                                        print(f"WARNING: Expected float, got {score} for {ds_name} {lang} {metric}")
                                        continue
                                    out.append(
                                        {
                                            "mteb_dataset_name": ds_name,
                                            "eval_language": lang,
                                            "metric": metric,
                                            "score": score * 100,
                                            "split": split,
                                            "hf_subset": subset,
                                        }
                                    )

                    ### Old MTEB format ###
                    else:
                        is_multilingual = any(x in res_dict for x in EVAL_LANGS)
                        langs = res_dict.keys() if is_multilingual else ["en"]
                        for lang in langs:
                            if lang in SKIP_KEYS:
                                continue
                            test_result_lang = res_dict.get(lang) if is_multilingual else res_dict
                            subset = test_result_lang.pop("hf_subset", "")
                            if subset == "" and is_multilingual:
                                subset = lang
                            for metric, score in test_result_lang.items():
                                if not isinstance(score, dict):
                                    score = {metric: score}
                                for sub_metric, sub_score in score.items():
                                    if any(x in sub_metric for x in SKIP_KEYS):
                                        continue
                                    if isinstance(sub_score, dict):
                                        continue
                                    out.append(
                                        {
                                            "mteb_dataset_name": ds_name,
                                            "eval_language": lang if is_multilingual else "",
                                            "metric": f"{metric}_{sub_metric}" if metric != sub_metric else metric,
                                            "score": sub_score * 100,
                                            "split": split,
                                            "hf_subset": subset,
                                        }
                                    )
        for idx, row in enumerate(sorted(out, key=lambda x: x["mteb_dataset_name"])):
            yield idx, row


# NOTE: for generating the new paths
if __name__ == "__main__":
    get_paths()

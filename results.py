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

MODELS = [
"ai-forever__sbert_large_mt_nlu_ru",
    "ai-forever__sbert_large_nlu_ru",
    "Alibaba-NLP__gte-base-en-v1.5",
    "Alibaba-NLP__gte-base-en-v1.5-instruct",
    "Alibaba-NLP__gte-large-en-v1.5",
    "Alibaba-NLP__gte-large-en-v1.5-instruct",
    "Alibaba-NLP__gte-multilingual-base",
    "Alibaba-NLP__gte-Qwen1.5-7B-instruct",
    "Alibaba-NLP__gte-Qwen2-1.5B",
    "Alibaba-NLP__gte-Qwen2-1.5B-instruct",
    "Alibaba-NLP__gte-Qwen2-7B-instruct",
    "aliyun__OpenSearch-text-hybrid",
    "almanach__camembert-base",
    "almanach__camembert-large",
    "amazon__titan-embed-text-v1",
    "BAAI__bge-base-en",
    "BAAI__bge-base-en-v1.5",
    "BAAI__bge-base-en-v1.5-instruct",
    "BAAI__bge-base-zh",
    "BAAI__bge-base-zh-v1.5",
    "BAAI__bge-large-en",
    "BAAI__bge-large-en-v1.5",
    "BAAI__bge-large-en-v1.5-instruct",
    "BAAI__bge-large-zh",
    "BAAI__bge-large-zh-noinstruct",
    "BAAI__bge-large-zh-v1.5",
    "BAAI__bge-m3",
    "BAAI__bge-m3-instruct",
    "BAAI__bge-reranker-v2-gemma",
    "BAAI__bge-reranker-v2-gemma-instruct",
    "BAAI__bge-reranker-v2-m3",
    "BAAI__bge-reranker-v2-m3-instruct",
    "BAAI__bge-small-en-v1.5",
    "BAAI__bge-small-en-v1.5-instruct",
    "BAAI__bge-small-zh",
    "BAAI__bge-small-zh-v1.5",
    "baichuan-ai__text-embedding",
    "bigscience-data__sgpt-bloom-1b7-nli",
    "bigscience-data__sgpt-bloom-7b1-msmarco",
    "bm25",
    "bm25s",
    "castorini__mdpr-tied-pft-msmarco",
    "castorini__monobert-large-msmarco",
    "castorini__monot5-3b-msmarco-10k",
    "castorini__monot5-base-msmarco-10k",
    "chcaa__dfm-encoder-large-v1",
    "Cohere__Cohere-embed-english-v3.0",
    "Cohere__Cohere-embed-english-v3.0-instruct",
    "Cohere__Cohere-embed-multilingual-light-v3.0",
    "Cohere__Cohere-embed-multilingual-v3.0",
    "cointegrated__LaBSE-en-ru",
    "cointegrated__rubert-tiny",
    "cointegrated__rubert-tiny2",
    "dangvantuan__sentence-camembert-base",
    "dangvantuan__sentence-camembert-large",
    "deepfile__embedder-100p",
    "DeepPavlov__distilrubert-small-cased-conversational",
    "DeepPavlov__rubert-base-cased",
    "DeepPavlov__rubert-base-cased-sentence",
    "deepset__gbert-base",
    "deepset__gbert-large",
    "deepset__gelectra-base",
    "deepset__gelectra-large",
    "deepvk__deberta-v1-base",
    "deepvk__USER-base",
    "deepvk__USER-bge-m3",
    "distilbert__distilbert-base-uncased",
    "dunzhang__stella_en_1.5B_v5",
    "dunzhang__stella_en_400M_v5",
    "dwzhu__e5-base-4k",
    "elastic__elser-v2",
    "FacebookAI__xlm-roberta-base",
    "FacebookAI__xlm-roberta-large",
    "facebookresearch__dragon-plus",
    "facebookresearch__dragon-plus-instruct",
    "facebookresearch__LASER2",
    "facebook__contriever",
    "facebook__contriever-instruct",
    "facebook__contriever-msmarco",
    "facebook__dpr-ctx_encoder-multiset-base",
    "facebook__dragon-plus-context-encoder",
    "facebook__tart-full-flan-t5-xl",
    "flaubert__flaubert_base_cased",
    "flaubert__flaubert_base_uncased",
    "flaubert__flaubert_large_cased",
    "Geotrend__bert-base-10lang-cased",
    "Geotrend__bert-base-15lang-cased",
    "Geotrend__bert-base-25lang-cased",
    "Geotrend__distilbert-base-25lang-cased",
    "Geotrend__distilbert-base-en-fr-cased",
    "Geotrend__distilbert-base-en-fr-es-pt-it-cased",
    "Geotrend__distilbert-base-fr-cased",
    "google-bert__bert-base-multilingual-cased",
    "google-bert__bert-base-multilingual-uncased",
    "google-bert__bert-base-uncased",
    "google-gecko__text-embedding-004",
    "google-gecko__text-embedding-004-256",
    "google__flan-t5-base",
    "google__flan-t5-large",
    "gpt-3.5-turbo",
    "gpt-3.5-turbo-instruct",
    "gpt-4o-instruct",
    "gpt-4o-mini-2-instruct",
    "gpt-4o-mini-instruct",
    "GritLM__GritLM-7B",
    "GritLM__GritLM-7B-instruct",
    "GritLM__GritLM-7B-noinstruct",
    "GritLM__GritLM-8x7B",
    "hkunlp__instructor-base",
    "hkunlp__instructor-large",
    "hkunlp__instructor-xl",
    "intfloat__e5-base",
    "intfloat__e5-base-v2",
    "intfloat__e5-base-v2-instruct",
    "intfloat__e5-large",
    "intfloat__e5-large-v2",
    "intfloat__e5-large-v2-instruct",
    "intfloat__e5-mistral-7b",
    "intfloat__e5-mistral-7b-instruct",
    "intfloat__e5-mistral-7b-instruct-noinstruct",
    "intfloat__e5-small",
    "intfloat__e5-small-v2",
    "intfloat__e5-small-v2-instruct",
    "intfloat__multilingual-e5-base",
    "intfloat__multilingual-e5-large",
    "intfloat__multilingual-e5-large-instruct",
    "intfloat__multilingual-e5-small",
    "ipipan__herbert-base-retrieval-v2",
    "ipipan__silver-retriever-base-v1",
    "izhx__udever-bloom-1b1",
    "izhx__udever-bloom-560m",
    "jhu-clsp__FollowIR-7B",
    "jinaai__jina-embeddings-v2-base-en",
    "jinaai__jina-embeddings-v3",
    "jinaai__jina-reranker-v2-base-multilingual",
    "jinaai__jina-reranker-v2-base-multilingual-instruct",
    "jonfd__electra-small-nordic",
    "KBLab__electra-small-swedish-cased-discriminator",
    "KBLab__sentence-bert-swedish-cased",
    "KB__bert-base-swedish-cased",
    "ltg__norbert3-base",
    "ltg__norbert3-large",
    "McGill-NLP__LLM2Vec-Llama-2-7b-chat-hf-mntp-supervised",
    "McGill-NLP__LLM2Vec-Llama-2-unsupervised",
    "McGill-NLP__LLM2Vec-Meta-Llama-3-8B-Instruct-mntp-supervised",
    "McGill-NLP__LLM2Vec-Meta-Llama-3-supervised",
    "McGill-NLP__LLM2Vec-Meta-Llama-3-unsupervised",
    "McGill-NLP__LLM2Vec-Mistral-supervised",
    "McGill-NLP__LLM2Vec-Mistral-unsupervised",
    "McGill-NLP__LLM2Vec-Sheared-Llama-supervised",
    "McGill-NLP__LLM2Vec-Sheared-Llama-unsupervised",
    "meta-llama__llama-2-7b-chat",
    "mistralai__mistral-7b-instruct-v0.2",
    "mistral__mistral-embed",
    "mixedbread-ai__mxbai-embed-large-v1",
    "mixedbread-ai__mxbai-rerank-large-v1",
    "mixedbread-ai__mxbai-rerank-large-v1-instruct",
    "moka-ai__m3e-base",
    "moka-ai__m3e-large",
    "monot5",
    "monot5-instruct",
    "Muennighoff__SGPT-1.3B-weightedmean-msmarco-specb-bitfit",
    "Muennighoff__SGPT-125M-weightedmean-msmarco-specb-bitfit",
    "Muennighoff__SGPT-125M-weightedmean-msmarco-specb-bitfit-doc",
    "Muennighoff__SGPT-125M-weightedmean-msmarco-specb-bitfit-que",
    "Muennighoff__SGPT-125M-weightedmean-nli-bitfit",
    "Muennighoff__SGPT-2.7B-weightedmean-msmarco-specb-bitfit",
    "Muennighoff__SGPT-5.8B-weightedmean-msmarco-specb-bitfit",
    "Muennighoff__SGPT-5.8B-weightedmean-msmarco-specb-bitfit-que",
    "Muennighoff__SGPT-5.8B-weightedmean-nli-bitfit",
    "NbAiLab__nb-bert-base",
    "NbAiLab__nb-bert-large",
    "nomic-ai__nomic-embed-text-v1",
    "nomic-ai__nomic-embed-text-v1.5",
    "nomic-ai__nomic-embed-text-v1.5-128",
    "nomic-ai__nomic-embed-text-v1.5-256",
    "nomic-ai__nomic-embed-text-v1.5-512",
    "nomic-ai__nomic-embed-text-v1.5-64",
    "nthakur__contriever-base-msmarco",
    "nthakur__mcontriever-base-msmarco",
    "nvidia__NV-Embed-v1",
    "nvidia__NV-Embed-v1-instruct",
    "openai__text-embedding-3-large",
    "openai__text-embedding-3-large-256",
    "openai__text-embedding-3-large-instruct",
    "openai__text-embedding-3-small",
    "openai__text-embedding-3-small-instruct",
    "openai__text-embedding-ada-002",
    "openai__text-embedding-ada-002-instruct",
    "openai__text-search-ada-001",
    "openai__text-search-ada-doc-001",
    "openai__text-search-babbage-001",
    "openai__text-search-curie-001",
    "openai__text-search-davinci-001",
    "openai__text-similarity-ada-001",
    "openai__text-similarity-babbage-001",
    "openai__text-similarity-curie-001",
    "openai__text-similarity-davinci-001",
    "orionweller__tart-dual-contriever-msmarco",
    "princeton-nlp__sup-simcse-bert-base-uncased",
    "princeton-nlp__unsup-simcse-bert-base-uncased",
    "Salesforce__SFR-Embedding-2_R",
    "Salesforce__SFR-Embedding-Mistral",
    "sdadas__st-polish-paraphrase-from-distilroberta",
    "sdadas__st-polish-paraphrase-from-mpnet",
    "sentence-transformers__all-MiniLM-L12-v2",
    "sentence-transformers__all-MiniLM-L6-v2",
    "sentence-transformers__all-MiniLM-L6-v2-instruct",
    "sentence-transformers__all-mpnet-base-v2",
    "sentence-transformers__all-mpnet-base-v2-instruct",
    "sentence-transformers__allenai-specter",
    "sentence-transformers__average_word_embeddings_glove.6B.300d",
    "sentence-transformers__average_word_embeddings_komninos",
    "sentence-transformers__distiluse-base-multilingual-cased-v2",
    "sentence-transformers__gtr-t5-base",
    "sentence-transformers__gtr-t5-large",
    "sentence-transformers__gtr-t5-xl",
    "sentence-transformers__gtr-t5-xxl",
    "sentence-transformers__LaBSE",
    "sentence-transformers__msmarco-bert-co-condensor",
    "sentence-transformers__multi-qa-MiniLM-L6-cos-v1",
    "sentence-transformers__paraphrase-multilingual-MiniLM-L12-v2",
    "sentence-transformers__paraphrase-multilingual-mpnet-base-v2",
    "sentence-transformers__sentence-t5-base",
    "sentence-transformers__sentence-t5-large",
    "sentence-transformers__sentence-t5-xl",
    "sentence-transformers__sentence-t5-xxl",
    "sentence-transformers__use-cmlm-multilingual",
    "sergeyzh__LaBSE-ru-turbo",
    "sergeyzh__rubert-tiny-turbo",
    "shibing624__text2vec-base-chinese",
    "shibing624__text2vec-base-multilingual",
    "shibing624__text2vec-large-chinese",
    "silk-road__luotuo-bert-medium",
    "Snowflake__snowflake-arctic-embed-m-v1.5",
    "T-Systems-onsite__cross-en-de-roberta-sentence-transformer",
    "text-embedding-3-small",
    "text-embedding-3-small-instruct",
    "uklfr__gottbert-base",
    "vesteinn__DanskBERT",
    "voyage-multilingual-2",
    "voyageai__voyage-2",
    "voyageai__voyage-3",
    "voyageai__voyage-3-lite",
    "voyageai__voyage-code-2",
    "voyageai__voyage-large-2-instruct",
    "voyageai__voyage-law-2",
    "voyageai__voyage-lite-01-instruct",
    "voyageai__voyage-lite-02-instruct",
    "voyageai__voyage-multilingual-2",
    "vprelovac__universal-sentence-encoder-multilingual-3",
    "vprelovac__universal-sentence-encoder-multilingual-large-3",
    "WhereIsAI__UAE-Large-V1",
    "Wissam42__sentence-croissant-llm-base",
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
                if (res_file.endswith(".json")) and not (
                    res_file.endswith(("overall_results.json", "model_meta.json"))
                ):
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

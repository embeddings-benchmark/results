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
    "aari1995__German_Semantic_STS_V2",
    "AbderrahmanSkiredj1__Arabic_text_embedding_for_sts",
    "AbderrahmanSkiredj1__arabic_text_embedding_sts_arabertv02_arabicnlitriplet",
    "abhinand__MedEmbed-small-v0.1",
    "AdrienB134__llm2vec-occiglot-mntp",
    "ai-forever__ru-en-RoSBERTa",
    "ai-forever__sbert_large_mt_nlu_ru",
    "ai-forever__sbert_large_nlu_ru",
    "aiacademyvn__multilingual-e5-large-instruct",
    "akarum__cloudy-large-zh",
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
    "amazon__Titan-text-embeddings-v2",
    "Amu__tao",
    "andersonbcdefg__bge-small-4096",
    "arcdev__e5-mistral-7b-instruct",
    "arcdev__SFR-Embedding-Mistral",
    "arkohut__jina-embeddings-v2-base-zh",
    "arkohut__jina-embeddings-v3",
    "aspire__acge_text_embedding",
    "atian-chapters__Chapters-SFR-Embedding-Mistral",
    "avsolatorio__GIST-all-MiniLM-L6-v2",
    "avsolatorio__GIST-Embedding-v0",
    "avsolatorio__GIST-large-Embedding-v0",
    "avsolatorio__GIST-small-Embedding-v0",
    "avsolatorio__NoInstruct-small-Embedding-v0",
    "BAAI__bge-base-en",
    "BAAI__bge-base-en-v1.5",
    "BAAI__bge-base-en-v1.5-instruct",
    "BAAI__bge-base-zh",
    "BAAI__bge-base-zh-v1.5",
    "BAAI__bge-en-icl",
    "BAAI__bge-large-en",
    "BAAI__bge-large-en-v1.5",
    "BAAI__bge-large-en-v1.5-instruct",
    "BAAI__bge-large-zh",
    "BAAI__bge-large-zh-noinstruct",
    "BAAI__bge-large-zh-v1.5",
    "BAAI__bge-m3",
    "BAAI__bge-m3-instruct",
    "BAAI__bge-multilingual-gemma2",
    "BAAI__bge-reranker-base",
    "BAAI__bge-small-en",
    "BAAI__bge-small-en-v1.5",
    "BAAI__bge-small-en-v1.5-instruct",
    "BAAI__bge-small-zh",
    "BAAI__bge-small-zh-v1.5",
    "baichuan-ai__text-embedding",
    "barisaydin__bge-base-en",
    "barisaydin__bge-large-en",
    "barisaydin__bge-small-en",
    "barisaydin__gte-base",
    "barisaydin__gte-large",
    "barisaydin__gte-small",
    "barisaydin__text2vec-base-multilingual",
    "beademiguelperez__sentence-transformers-multilingual-e5-small",
    "BeastyZ__e5-R-mistral-7b",
    "bennegeek__stella_en_1.5B_v5",
    "biggunnyso4__stella_en_400M_v5_cpu",
    "bigscience-data__sgpt-bloom-1b7-nli",
    "bigscience-data__sgpt-bloom-7b1-msmarco",
    "bigscience__sgpt-bloom-7b1-msmarco",
    "bijaygurung__stella_en_400M_v5",
    "biswa921__bge-m3",
    "bm25",
    "bm25s",
    "brahmairesearch__slx-v0.1",
    "castorini__mdpr-tied-pft-msmarco",
    "castorini__monobert-large-msmarco",
    "castorini__monot5-3b-msmarco-10k",
    "castorini__monot5-base-msmarco-10k",
    "chcaa__dfm-encoder-large-v1",
    "chuxin-llm__Chuxin-Embedding",
    "ClayAtlas__winberta-large",
    "Cohere__Cohere-embed-english-light-v3.0",
    "Cohere__Cohere-embed-english-v3.0",
    "Cohere__Cohere-embed-english-v3.0-instruct",
    "Cohere__Cohere-embed-multilingual-light-v3.0",
    "Cohere__Cohere-embed-multilingual-v3.0",
    "cointegrated__LaBSE-en-ru",
    "cointegrated__rubert-tiny",
    "cointegrated__rubert-tiny2",
    "consciousAI__cai-lunaris-text-embeddings",
    "consciousAI__cai-stellaris-text-embeddings",
    "d0rj__e5-large-en-ru",
    "dangvantuan__sentence-camembert-base",
    "dangvantuan__sentence-camembert-large",
    "davidpeer__gte-small",
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
    "DivineNnamdi__jina-embeddings-v3",
    "djovak__multi-qa-MiniLM-L6-cos-v1",
    "DMetaSoul__Dmeta-embedding-zh-small",
    "DMetaSoul__sbert-chinese-general-v1",
    "dumyy__sft-bge-small",
    "dunzhang__stella-large-zh-v3-1792d",
    "dunzhang__stella-mrl-large-zh-v3.5-1792d",
    "dunzhang__stella_en_1.5B_v5",
    "dunzhang__stella_en_400M_v5",
    "dwzhu__e5-base-4k",
    "EdwardBurgin__paraphrase-multilingual-mpnet-base-v2",
    "ekorman-strive__bge-large-en-v1.5",
    "elastic__elser-v2",
    "Erin__IYun-large-zh",
    "Erin__mist-zh",
    "FacebookAI__xlm-roberta-base",
    "FacebookAI__xlm-roberta-large",
    "facebookresearch__dragon-plus",
    "facebookresearch__dragon-plus-instruct",
    "facebookresearch__LASER2",
    "facebook__contriever",
    "facebook__contriever-instruct",
    "facebook__dpr-ctx_encoder-multiset-base",
    "facebook__dragon-plus-context-encoder",
    "facebook__SONAR",
    "facebook__tart-full-flan-t5-xl",
    "fangxq__XYZ-embedding-zh",
    "fangxq__XYZ-embedding-zh-v2",
    "GameScribes__stella_en_400M_v5",
    "Gameselo__STS-multilingual-mpnet-base-v2",
    "Geotrend__bert-base-10lang-cased",
    "Geotrend__bert-base-15lang-cased",
    "Geotrend__bert-base-25lang-cased",
    "Geotrend__distilbert-base-25lang-cased",
    "Geotrend__distilbert-base-en-fr-cased",
    "Geotrend__distilbert-base-en-fr-es-pt-it-cased",
    "Geotrend__distilbert-base-fr-cased",
    "ggrn__e5-small-v2",
    "gizmo-ai__Cohere-embed-multilingual-v3.0",
    "goldenrooster__multilingual-e5-large",
    "gpt-4o-instruct",
    "GritLM__GritLM-7B",
    "GritLM__GritLM-7B-instruct",
    "GritLM__GritLM-7B-noinstruct",
    "GritLM__GritLM-8x7B",
    "Haon-Chen__speed-embedding-7b-instruct",
    "HIT-TMG__KaLM-embedding-multilingual-mini-instruct-v1",
    "HIT-TMG__KaLM-embedding-multilingual-mini-v1",
    "Hum-Works__lodestone-base-4096-v1",
    "iampanda__zpoint_large_embedding_zh",
    "IEITYuan__Yuan-embedding-1.0",
    "ildodeltaRule__multilingual-e5-large",
    "infgrad__stella-base-en-v2",
    "infgrad__stella-base-zh",
    "infgrad__stella-base-zh-v2",
    "infgrad__stella-base-zh-v3-1792d",
    "infgrad__stella-large-zh",
    "infgrad__stella-large-zh-v2",
    "Intel__neural-embedding-v1",
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
    "izhx__udever-bloom-3b",
    "izhx__udever-bloom-560m",
    "izhx__udever-bloom-7b1",
    "jamesgpt1__sf_model_e5",
    "Jaume__gemma-2b-embeddings",
    "jhu-clsp__FollowIR-7B",
    "jinaai__jina-embedding-b-en-v1",
    "jinaai__jina-embedding-l-en-v1",
    "jinaai__jina-embedding-s-en-v1",
    "jinaai__jina-embeddings-v2-base-de",
    "jinaai__jina-embeddings-v2-base-en",
    "jinaai__jina-embeddings-v2-base-es",
    "jinaai__jina-embeddings-v2-base-zh",
    "jinaai__jina-embeddings-v2-small-en",
    "jinaai__jina-embeddings-v3",
    "jingyeom__korean_embedding_model",
    "jonfd__electra-small-nordic",
    "jxm__cde-small-v1",
    "karsar__gte-multilingual-base-hu",
    "karsar__paraphrase-multilingual-MiniLM-L12-hu-v2",
    "karsar__paraphrase-multilingual-MiniLM-L12-hu_v1",
    "katanemo__bge-large-en-v1.5",
    "KBLab__electra-small-swedish-cased-discriminator",
    "KBLab__sentence-bert-swedish-cased",
    "KB__bert-base-swedish-cased",
    "keeeeenw__MicroLlama-text-embedding",
    "khoa-klaytn__bge-small-en-v1.5-angle",
    "krilecy__e5-mistral-7b-instruct",
    "Labib11__MUG-B-1.6",
    "Lajavaness__bilingual-embedding-base",
    "Lajavaness__bilingual-embedding-large",
    "Lajavaness__bilingual-embedding-large-8k",
    "Lajavaness__bilingual-embedding-small",
    "Lenovo-Zhihui__Zhihui_LLM_Embedding",
    "lier007__xiaobu-embedding",
    "Linq-AI-Research__Linq-Embed-Mistral",
    "ltg__norbert3-base",
    "ltg__norbert3-large",
    "maiyad__multilingual-e5-small",
    "malenia1__ternary-weight-embedding",
    "manu__bge-m3-custom-fr",
    "manu__sentence_croissant_alpha_v0.2",
    "manu__sentence_croissant_alpha_v0.3",
    "manu__sentence_croissant_alpha_v0.4",
    "markaw__NV-Embed-v2",
    "Marqo__dunzhang-stella_en_400M_v5",
    "McGill-NLP__LLM2Vec-Llama-2-7b-chat-hf-mntp-supervised",
    "McGill-NLP__LLM2Vec-Llama-2-7b-chat-hf-mntp-unsup-simcse",
    "McGill-NLP__LLM2Vec-Llama-2-unsupervised",
    "McGill-NLP__LLM2Vec-Meta-Llama-3-8B-Instruct-mntp-supervised",
    "McGill-NLP__LLM2Vec-Meta-Llama-3-8B-Instruct-mntp-unsup-simcse",
    "McGill-NLP__LLM2Vec-Meta-Llama-3-supervised",
    "McGill-NLP__LLM2Vec-Meta-Llama-3-unsupervised",
    "McGill-NLP__LLM2Vec-Mistral-7B-Instruct-v2-mntp-supervised",
    "McGill-NLP__LLM2Vec-Mistral-7B-Instruct-v2-mntp-unsup-simcse",
    "McGill-NLP__LLM2Vec-Mistral-supervised",
    "McGill-NLP__LLM2Vec-Mistral-unsupervised",
    "McGill-NLP__LLM2Vec-Sheared-LLaMA-mntp-supervised",
    "McGill-NLP__LLM2Vec-Sheared-LLaMA-mntp-unsup-simcse",
    "McGill-NLP__LLM2Vec-Sheared-Llama-supervised",
    "McGill-NLP__LLM2Vec-Sheared-Llama-unsupervised",
    "meta-llama__llama-2-7b-chat",
    "michaelfeil__ct2fast-bge-base-en-v1.5",
    "michaelfeil__ct2fast-bge-large-en-v1.5",
    "michaelfeil__ct2fast-bge-small-en-v1.5",
    "michaelfeil__ct2fast-e5-large",
    "michaelfeil__ct2fast-e5-large-v2",
    "michaelfeil__ct2fast-e5-small",
    "michaelfeil__ct2fast-e5-small-v2",
    "michaelfeil__ct2fast-gte-base",
    "michaelfeil__ct2fast-gte-large",
    "Mihaiii__Bulbasaur",
    "Mihaiii__gte-micro",
    "Mihaiii__gte-micro-v4",
    "Mihaiii__Ivysaur",
    "Mihaiii__Squirtle",
    "Mihaiii__Venusaur",
    "Mihaiii__Wartortle",
    "minishlab__M2V_base_glove",
    "minishlab__M2V_base_glove_subword",
    "minishlab__M2V_base_output",
    "minishlab__potion-base-2M",
    "minishlab__potion-base-4M",
    "minishlab__potion-base-8M",
    "mistralai__mistral-7b-instruct-v0.2",
    "mistral__mistral-embed",
    "mixedbread-ai__mxbai-embed-2d-large-v1",
    "mixedbread-ai__mxbai-embed-large-v1",
    "mixedbread-ai__mxbai-embed-xsmall-v1",
    "moka-ai__m3e-base",
    "moka-ai__m3e-large",
    "Muennighoff__SGPT-1.3B-weightedmean-msmarco-specb-bitfit",
    "Muennighoff__SGPT-125M-weightedmean-msmarco-specb-bitfit",
    "Muennighoff__SGPT-125M-weightedmean-msmarco-specb-bitfit-doc",
    "Muennighoff__SGPT-125M-weightedmean-msmarco-specb-bitfit-que",
    "Muennighoff__SGPT-125M-weightedmean-nli-bitfit",
    "Muennighoff__SGPT-2.7B-weightedmean-msmarco-specb-bitfit",
    "Muennighoff__SGPT-5.8B-weightedmean-msmarco-specb-bitfit",
    "Muennighoff__SGPT-5.8B-weightedmean-msmarco-specb-bitfit-que",
    "Muennighoff__SGPT-5.8B-weightedmean-nli-bitfit",
    "Narsil__bge-base-en",
    "NbAiLab__nb-bert-base",
    "NbAiLab__nb-bert-large",
    "neofung__bge-reranker-large-1k",
    "neofung__LdIR-Qwen2-reranker-1.5B",
    "neofung__LdIR-reranker-large",
    "neofung__m3e-ernie-xbase-zh",
    "neuralmagic__bge-base-en-v1.5-quant",
    "neuralmagic__bge-base-en-v1.5-sparse",
    "neuralmagic__bge-large-en-v1.5-quant",
    "neuralmagic__bge-large-en-v1.5-sparse",
    "neuralmagic__bge-small-en-v1.5-quant",
    "neuralmagic__bge-small-en-v1.5-sparse",
    "Nextcloud-AI__multilingual-e5-large-instruct",
    "nickprock__mmarco-bert-base-italian-uncased",
    "nickprock__mmarco-sentence-flare-it",
    "nickprock__stsbm-sentence-flare-it",
    "NLPArtisan__qwen-1.8b-retrieval-test",
    "nomic-ai__nomic-embed-text-v1",
    "nomic-ai__nomic-embed-text-v1-ablated",
    "nomic-ai__nomic-embed-text-v1-unsupervised",
    "nomic-ai__nomic-embed-text-v1.5",
    "nomic-ai__nomic-embed-text-v1.5-128",
    "nomic-ai__nomic-embed-text-v1.5-256",
    "nomic-ai__nomic-embed-text-v1.5-512",
    "nomic-ai__nomic-embed-text-v1.5-64",
    "nthakur__contriever-base-msmarco",
    "nthakur__mcontriever-base-msmarco",
    "nvidia__NV-Embed-v1",
    "nvidia__NV-Embed-v1-instruct",
    "nvidia__NV-Embed-v2",
    "nvidia__NV-Retriever-v1",
    "odunola__e5-base-v2",
    "omarelshehy__arabic-english-sts-matryoshka",
    "omarelshehy__Arabic-STS-Matryoshka",
    "Omartificial-Intelligence-Space__Arabert-all-nli-triplet-Matryoshka",
    "Omartificial-Intelligence-Space__Arabic-all-nli-triplet-Matryoshka",
    "Omartificial-Intelligence-Space__Arabic-labse-Matryoshka",
    "Omartificial-Intelligence-Space__Arabic-MiniLM-L12-v2-all-nli-triplet",
    "Omartificial-Intelligence-Space__Arabic-mpnet-base-all-nli-triplet",
    "Omartificial-Intelligence-Space__GATE-AraBert-v1",
    "Omartificial-Intelligence-Space__Marbert-all-nli-triplet-Matryoshka",
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
    "openbmb__MiniCPM-Embedding",
    "OrcaDB__cde-small-v1",
    "OrcaDB__gte-base-en-v1.5",
    "OrdalieTech__Solon-embeddings-large-0.1",
    "orionweller__tart-dual-contriever-msmarco",
    "OrlikB__KartonBERT-USE-base-v1",
    "OrlikB__st-polish-kartonberta-base-alpha-v1",
    "pengql__checkpoint-9000",
    "princeton-nlp__sup-simcse-bert-base-uncased",
    "princeton-nlp__unsup-simcse-bert-base-uncased",
    "Pristinenlp__alime-embedding-large-zh",
    "Pristinenlp__alime-reranker-large-zh",
    "qinxianliu__FAB-Ramy-v1",
    "qinxianliu__FAE-v1",
    "qinxianliu__FUE-v1",
    "radames__e5-large",
    "raghavlight__SE_v1",
    "rlsChapters__Chapters-SFR-Embedding-Mistral",
    "RookieHX__bge_m3e_stella",
    "Salesforce__SFR-Embedding-2_R",
    "Salesforce__SFR-Embedding-Mistral",
    "sdadas__mmlw-e5-base",
    "sdadas__mmlw-e5-large",
    "sdadas__mmlw-e5-small",
    "sdadas__mmlw-roberta-base",
    "sdadas__mmlw-roberta-large",
    "sdadas__st-polish-paraphrase-from-distilroberta",
    "sdadas__st-polish-paraphrase-from-mpnet",
    "sensenova__piccolo-base-zh",
    "sensenova__piccolo-large-zh",
    "sensenova__piccolo-large-zh-v2",
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
    "shanghung__stella-base-zh-v3-1792d",
    "shhy1995__AGE_Hybrid",
    "shibing624__text2vec-base-chinese",
    "shibing624__text2vec-base-multilingual",
    "shibing624__text2vec-large-chinese",
    "silk-road__luotuo-bert-medium",
    "silma-ai__silma-embeddding-matryoshka-v0.1",
    "silverjam__jina-embeddings-v2-base-zh",
    "sionic-ai__sionic-ai-v1",
    "sionic-ai__sionic-ai-v2",
    "Snowflake__snowflake-arctic-embed-l",
    "Snowflake__snowflake-arctic-embed-m",
    "Snowflake__snowflake-arctic-embed-m-long",
    "Snowflake__snowflake-arctic-embed-m-v1.5",
    "Snowflake__snowflake-arctic-embed-s",
    "Snowflake__snowflake-arctic-embed-xs",
    "srikanthmalla__BAAI-bge-reranker-large",
    "T-Systems-onsite__cross-en-de-roberta-sentence-transformer",
    "tanmaylaud__ret-phi2-v0",
    "thenlper__gte-base",
    "thenlper__gte-base-zh",
    "thenlper__gte-large",
    "thenlper__gte-large-zh",
    "thenlper__gte-small",
    "thenlper__gte-small-zh",
    "thtang__ALL_862873",
    "tomaarsen__bge-base-en-v1.5",
    "towing__gte-small-zh",
    "TownsWu__PEG",
    "tsirif__BinGSE-Meta-Llama-3-8B-Instruct",
    "uklfr__gottbert-base",
    "vectoriseai__bge-base-en-v1.5",
    "vectoriseai__bge-large-en-v1.5",
    "vectoriseai__bge-small-en",
    "vectoriseai__bge-small-en-v1.5",
    "vectoriseai__e5-base",
    "vectoriseai__e5-base-v2",
    "vectoriseai__e5-large",
    "vectoriseai__e5-large-v2",
    "vectoriseai__e5-small-v2",
    "vectoriseai__gte-base",
    "vectoriseai__gte-large",
    "vectoriseai__gte-small",
    "vectoriseai__multilingual-e5-large",
    "VectorStackAI__vstackai-law-1",
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
    "vprelovac__universal-sentence-encoder-4",
    "vprelovac__universal-sentence-encoder-large-5",
    "vprelovac__universal-sentence-encoder-multilingual-3",
    "vprelovac__universal-sentence-encoder-multilingual-large-3",
    "WhereIsAI__UAE-Large-V1",
    "Wissam42__sentence-croissant-llm-base",
    "woody72__multilingual-e5-base",
    "zeroshot__gte-large-quant",
    "zeroshot__gte-large-sparse",
    "zeroshot__gte-small-quant",
    "zeta-alpha-ai__Zeta-Alpha-E5-Mistral",
]

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

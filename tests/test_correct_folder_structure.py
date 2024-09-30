import json
from pathlib import Path


def test_correct_folder_structure():
    """
    the folders should be structured as follows:
    results/model_name/revision/*json
    """
    results_folder = Path(__file__).parent.parent / "results"
    meta_files = results_folder.glob("**/model_meta.json")
    meta_files = list(meta_files)

    for meta_file in meta_files:
        with open(meta_file, "r") as f:
            meta = json.load(f)

        mdl_name, revision = meta["name"], meta["revision"]

        mdl_name = mdl_name.replace(" ", "_").replace("/", "__")

        if revision is None:
            revision = meta_file.parent.name

        expected_path = results_folder / mdl_name / revision
        assert expected_path == meta_file.parent
        assert expected_path.exists()
        assert len(list(expected_path.glob("*.json"))) > 0
        for file in expected_path.glob("*.json"):
            assert file.exists()
            assert file.is_file()
            assert file.parent == expected_path
            assert file.suffix == ".json"


folders_without_meta = [  # please do not add to this list it is only intended for backwards compatibility. Future results should have a model_meta.json file
    ("openai__text-search-davinci-001", "no_revision_available"),
    ("McGill-NLP__LLM2Vec-Llama-2-unsupervised", "no_revision_available"),
    ("openai__text-search-babbage-001", "no_revision_available"),
    ("hkunlp__instructor-base", "no_revision_available"),
    ("deepfile__embedder-100p", "no_revision_available"),
    ("openai__text-embedding-ada-002-instruct", "no_revision_available"),
    ("BAAI__bge-m3-instruct", "5617a9f61b028005a4858fdac845db406aefb181"),
    ("FacebookAI__xlm-roberta-large", "no_revision_available"),
    ("voyageai__voyage-2", "no_revision_available"),
    ("openai__text-search-ada-001", "no_revision_available"),
    ("sentence-transformers__gtr-t5-large", "no_revision_available"),
    ("sentence-transformers__sentence-t5-xxl", "no_revision_available"),
    ("openai__text-embedding-3-small-instruct", "no_revision_available"),
    ("BAAI__bge-m3", "no_revision_available"),
    ("voyageai__voyage-lite-02-instruct", "no_revision_available"),
    ("openai__text-similarity-ada-001", "no_revision_available"),
    ("McGill-NLP__LLM2Vec-Sheared-Llama-supervised", "no_revision_available"),
    ("intfloat__e5-base", "no_revision_available"),
    ("BAAI__bge-small-zh-v1.5", "no_revision_available"),
    ("BAAI__bge-base-en", "no_revision_available"),
    ("KBLab__electra-small-swedish-cased-discriminator", "no_revision_available"),
    ("nomic-ai__nomic-embed-text-v1.5-512", "no_revision_available"),
    ("McGill-NLP__LLM2Vec-Mistral-unsupervised", "no_revision_available"),
    ("voyageai__voyage-law-2", "no_revision_available"),
    ("dwzhu__e5-base-4k", "no_revision_available"),
    ("T-Systems-onsite__cross-en-de-roberta-sentence-transformer", "no_revision_available"),
    ("dangvantuan__sentence-camembert-base", "no_revision_available"),
    ("Muennighoff__SGPT-5.8B-weightedmean-nli-bitfit", "no_revision_available"),
    ("almanach__camembert-large", "no_revision_available"),
    ("Muennighoff__SGPT-125M-weightedmean-msmarco-specb-bitfit-doc", "no_revision_available"),
    ("baichuan-ai__text-embedding", "no_revision_available"),
    ("sentence-transformers__LaBSE", "e34fab64a3011d2176c99545a93d5cbddc9a91b7"),
    ("sentence-transformers__LaBSE", "no_revision_available"),
    ("Wissam42__sentence-croissant-llm-base", "no_revision_available"),
    ("Geotrend__bert-base-25lang-cased", "no_revision_available"),
    ("bigscience-data__sgpt-bloom-7b1-msmarco", "no_revision_available"),
    ("jonfd__electra-small-nordic", "no_revision_available"),
    ("Muennighoff__SGPT-5.8B-weightedmean-msmarco-specb-bitfit", "no_revision_available"),
    ("distilbert__distilbert-base-uncased", "no_revision_available"),
    ("McGill-NLP__LLM2Vec-Meta-Llama-3-supervised", "no_revision_available"),
    ("openai__text-embedding-3-large", "no_revision_available"),
    ("Geotrend__bert-base-10lang-cased", "no_revision_available"),
    ("sentence-transformers__sentence-t5-large", "no_revision_available"),
    ("moka-ai__m3e-base", "no_revision_available"),
    ("intfloat__e5-mistral-7b-instruct", "no_revision_available"),
    ("almanach__camembert-base", "no_revision_available"),
    ("vprelovac__universal-sentence-encoder-multilingual-3", "no_revision_available"),
    ("dangvantuan__sentence-camembert-large", "no_revision_available"),
    ("deepset__gelectra-large", "no_revision_available"),
    ("intfloat__e5-large-v2", "no_revision_available"),
    ("intfloat__e5-large-v2", "b322e09026e4ea05f42beadf4d661fb4e101d311"),
    ("moka-ai__m3e-large", "no_revision_available"),
    ("meta-llama__llama-2-7b-chat", "no_revision_available"),
    ("bigscience-data__sgpt-bloom-1b7-nli", "no_revision_available"),
    ("sentence-transformers__all-mpnet-base-v2", "84f2bcc00d77236f9e89c8a360a00fb1139bf47d"),
    ("sentence-transformers__sentence-t5-xl", "no_revision_available"),
    ("Geotrend__distilbert-base-en-fr-cased", "no_revision_available"),
    ("openai__text-embedding-ada-002", "no_revision_available"),
    ("BAAI__bge-small-en-v1.5-instruct", "5c38ec7c405ec4b44b94cc5a9bb96e735b38267a"),
    ("shibing624__text2vec-base-multilingual", "no_revision_available"),
    ("sentence-transformers__multi-qa-MiniLM-L6-cos-v1", "no_revision_available"),
    ("jinaai__jina-embeddings-v2-base-en", "no_revision_available"),
    ("mistralai__mistral-7b-instruct-v0.2", "no_revision_available"),
    ("castorini__monot5-3b-msmarco-10k", "no_revision_available"),
    ("Alibaba-NLP__gte-Qwen2-7B-instruct", "no_revision_available"),
    ("google-bert__bert-base-multilingual-uncased", "no_revision_available"),
    ("sentence-transformers__distiluse-base-multilingual-cased-v2", "no_revision_available"),
    ("sentence-transformers__distiluse-base-multilingual-cased-v2", ".gitkeep"),
    ("BAAI__bge-base-zh-v1.5", "no_revision_available"),
    ("google-gecko__text-embedding-preview-004", "no_revision_available"),
    ("openai__text-search-curie-001", "no_revision_available"),
    ("princeton-nlp__sup-simcse-bert-base-uncased", "no_revision_available"),
    ("BAAI__bge-base-en-v1.5-instruct", "a5beb1e3e68b9ab74eb54cfd186867f64f240e1a"),
    ("GritLM__GritLM-7B", "no_revision_available"),
    ("GritLM__GritLM-7B", "13f00a0e36500c80ce12870ea513846a066004af"),
    ("Cohere__Cohere-embed-multilingual-light-v3.0", "no_revision_available"),
    ("BAAI__bge-base-zh", "no_revision_available"),
    ("voyageai__voyage-code-2", "no_revision_available"),
    ("sentence-transformers__sentence-t5-base", "no_revision_available"),
    ("flaubert__flaubert_large_cased", "no_revision_available"),
    ("Cohere__Cohere-embed-english-v3.0-instruct", "no_revision_available"),
    ("Salesforce__SFR-Embedding-Mistral", "no_revision_available"),
    ("facebookresearch__dragon-plus", "no_revision_available"),
    ("McGill-NLP__LLM2Vec-Sheared-Llama-unsupervised", "no_revision_available"),
    ("openai__text-embedding-3-small", "no_revision_available"),
    ("google__flan-t5-base", "no_revision_available"),
    ("openai__text-search-ada-doc-001", "no_revision_available"),
    ("google-bert__bert-base-multilingual-cased", "no_revision_available"),
    ("McGill-NLP__LLM2Vec-Meta-Llama-3-unsupervised", "no_revision_available"),
    ("ipipan__silver-retriever-base-v1", "no_revision_available"),
    ("facebook__dpr-ctx_encoder-multiset-base", "no_revision_available"),
    ("bm25s", "0_1_10"),
    ("sentence-transformers__all-MiniLM-L12-v2", "a05860a77cef7b37e0048a7864658139bc18a854"),
    ("facebookresearch__dragon-plus-instruct", "no_revision_available"),
    ("elastic__elser-v2", "no_revision_available"),
    ("facebook__contriever-instruct", "2bd46a25019aeea091fd42d1f0fd4801675cf699"),
    ("BAAI__bge-small-en-v1.5", "5c38ec7c405ec4b44b94cc5a9bb96e735b38267a"),
    ("Muennighoff__SGPT-125M-weightedmean-msmarco-specb-bitfit", "no_revision_available"),
    ("BAAI__bge-large-zh-noinstruct", "no_revision_available"),
    ("izhx__udever-bloom-560m", "no_revision_available"),
    ("sdadas__st-polish-paraphrase-from-distilroberta", "no_revision_available"),
    ("sentence-transformers__gtr-t5-base", "no_revision_available"),
    ("intfloat__e5-mistral-7b-instruct-noinstruct", "07163b72af1488142a360786df853f237b1a3ca1"),
    ("Muennighoff__SGPT-2.7B-weightedmean-msmarco-specb-bitfit", "no_revision_available"),
    ("FacebookAI__xlm-roberta-base", "no_revision_available"),
    ("BAAI__bge-large-zh-v1.5", "no_revision_available"),
    ("orionweller__tart-dual-contriever-msmarco", "no_revision_available"),
    ("openai__text-embedding-preview-004-768", "no_revision_available"),
    ("vesteinn__DanskBERT", "no_revision_available"),
    ("deepset__gbert-large", "no_revision_available"),
    ("openai__text-similarity-davinci-001", "no_revision_available"),
    ("sentence-transformers__use-cmlm-multilingual", "no_revision_available"),
    ("KBLab__sentence-bert-swedish-cased", "no_revision_available"),
    ("nomic-ai__nomic-embed-text-v1", "no_revision_available"),
    ("openai__text-similarity-babbage-001", "no_revision_available"),
    ("mistral__mistral-embed", "no_revision_available"),
    ("voyageai__voyage-large-2-instruct", "no_revision_available"),
    ("flaubert__flaubert_base_uncased", "no_revision_available"),
    ("nomic-ai__nomic-embed-text-v1.5-256", "no_revision_available"),
    ("intfloat__e5-large", "no_revision_available"),
    ("BAAI__bge-large-zh", "no_revision_available"),
    ("Geotrend__distilbert-base-en-fr-es-pt-it-cased", "no_revision_available"),
    ("Muennighoff__SGPT-5.8B-weightedmean-msmarco-specb-bitfit-que", "no_revision_available"),
    ("voyageai__voyage-multilingual-2", "no_revision_available"),
    ("sentence-transformers__all-mpnet-base-v2-instruct", "84f2bcc00d77236f9e89c8a360a00fb1139bf47d"),
    ("Muennighoff__SGPT-125M-weightedmean-msmarco-specb-bitfit-que", "no_revision_available"),
    ("sentence-transformers__average_word_embeddings_glove.6B.300d", "no_revision_available"),
    ("aliyun__OpenSearch-text-hybrid", "no_revision_available"),
    ("deepset__gelectra-base", "no_revision_available"),
    ("BAAI__bge-small-zh", "no_revision_available"),
    ("sdadas__st-polish-paraphrase-from-mpnet", "no_revision_available"),
    ("bm25", "no_revision_available"),
    ("nomic-ai__nomic-embed-text-v1.5-128", "no_revision_available"),
    ("voyageai__voyage-lite-01-instruct", "no_revision_available"),
    ("hkunlp__instructor-large", "no_revision_available"),
    ("facebook__contriever", "2bd46a25019aeea091fd42d1f0fd4801675cf699"),
    ("Alibaba-NLP__gte-Qwen1.5-7B-instruct", "no_revision_available"),
    ("sentence-transformers__msmarco-bert-co-condensor", "no_revision_available"),
    ("shibing624__text2vec-large-chinese", "no_revision_available"),
    ("intfloat__multilingual-e5-small", "e4ce9877abf3edfe10b0d82785e83bdcb973e22e"),
    ("intfloat__multilingual-e5-small", "no_revision_available"),
    ("castorini__monot5-3b-msmarco-10k", "no_revision_available"),
    ("castorini__monot5-base-msmarco-10k", "no_revision_available"),
    ("jhu-clsp__FollowIR-7B", "no_revision_available"),
    ("ipipan__herbert-base-retrieval-v2", "no_revision_available"),
    ("izhx__udever-bloom-1b1", "no_revision_available"),
    ("openai__text-embedding-3-large-instruct", "no_revision_available"),
    ("McGill-NLP__LLM2Vec-Llama-2-supervised", "no_revision_available"),
    ("McGill-NLP__LLM2Vec-Llama-2-7b-chat-hf-mntp-supervised", "no_revision_available"),
    ("Cohere__Cohere-embed-multilingual-v3.0", "no_revision_available"),
    ("ltg__norbert3-large", "no_revision_available"),
    ("facebook__tart-full-flan-t5-xl", "no_revision_available"),
    ("nomic-ai__nomic-embed-text-v1.5-64", "no_revision_available"),
    ("NbAiLab__nb-bert-base", "no_revision_available"),
    ("Geotrend__distilbert-base-fr-cased", "no_revision_available"),
    ("hkunlp__instructor-xl", "no_revision_available"),
    ("shibing624__text2vec-base-chinese", "no_revision_available"),
    ("BAAI__bge-large-en", "no_revision_available"),
    ("BAAI__bge-large-en-v1.5-instruct", "d4aa6901d3a41ba39fb536a557fa166f842b0e09"),
    ("google-bert__bert-base-uncased", "no_revision_available"),
    ("sentence-transformers__all-MiniLM-L6-v2", "8b3219a92973c328a8e22fadcfa821b5dc75636a"),
    ("sentence-transformers__all-MiniLM-L6-v2", "no_revision_available"),
    ("intfloat__e5-base-v2", "no_revision_available"),
    ("intfloat__e5-base-v2", "1c644c92ad3ba1efdad3f1451a637716616a20e8"),
    ("sentence-transformers__gtr-t5-xl", "no_revision_available"),
    ("ltg__norbert3-base", "no_revision_available"),
    ("openai__text-embedding-3-large-256", "no_revision_available"),
    ("intfloat__e5-small", "no_revision_available"),
    ("sentence-transformers__average_word_embeddings_komninos", "no_revision_available"),
    ("castorini__monobert-large-msmarco", "no_revision_available"),
    ("uklfr__gottbert-base", "no_revision_available"),
    ("NbAiLab__nb-bert-large", "no_revision_available"),
    ("princeton-nlp__unsup-simcse-bert-base-uncased", "no_revision_available"),
    ("Geotrend__bert-base-15lang-cased", "no_revision_available"),
    ("flaubert__flaubert_base_cased", "no_revision_available"),
    ("sentence-transformers__paraphrase-multilingual-MiniLM-L12-v2", "no_revision_available"),
    (
        "sentence-transformers__paraphrase-multilingual-MiniLM-L12-v2",
        "bf3bf13ab40c3157080a7ab344c831b9ad18b5eb",
    ),
    ("sentence-transformers__all-MiniLM-L6-v2-instruct", "8b3219a92973c328a8e22fadcfa821b5dc75636a"),
    ("Geotrend__distilbert-base-25lang-cased", "no_revision_available"),
    ("facebookresearch__LASER2", "no_revision_available"),
    ("Cohere__Cohere-embed-english-v3.0", "no_revision_available"),
    ("Muennighoff__SGPT-125M-weightedmean-nli-bitfit", "no_revision_available"),
    ("amazon__titan-embed-text-v1", "no_revision_available"),
    ("nthakur__contriever-base-msmarco", "no_revision_available"),
    ("KB__bert-base-swedish-cased", "no_revision_available"),
    ("intfloat__multilingual-e5-large", "no_revision_available"),
    ("intfloat__multilingual-e5-large", "4dc6d853a804b9c8886ede6dda8a073b7dc08a81"),
    ("openai__text-similarity-curie-001", "no_revision_available"),
    ("silk-road__luotuo-bert-medium", "no_revision_available"),
    ("facebook__dragon-plus-context-encoder", "no_revision_available"),
    ("BAAI__bge-large-en-v1.5", "no_revision_available"),
    ("BAAI__bge-large-en-v1.5", "d4aa6901d3a41ba39fb536a557fa166f842b0e09"),
    ("chcaa__dfm-encoder-large-v1", "no_revision_available"),
    ("GritLM__GritLM-7B-noinstruct", "13f00a0e36500c80ce12870ea513846a066004af-temp"),
    ("sentence-transformers__gtr-t5-xxl", "no_revision_available"),
    ("google-gecko__text-embedding-preview-004-256", "no_revision_available"),
    ("intfloat__-e5-base", "no_revision_available"),
    ("intfloat__multilingual-e5-base", "d13f1b27baf31030b7fd00460d60d909913633f"),
    ("intfloat__multilingual-e5-base", "no_revision_available"),
    (
        "sentence-transformers__paraphrase-multilingual-mpnet-base-v2",
        "79f2382ceacceacdf38563d7c5d16b9ff8d725d6",
    ),
    ("sentence-transformers__paraphrase-multilingual-mpnet-base-v2", "no_revision_available"),
    ("google__flan-t5-large", "no_revision_available"),
    ("sergeyzh__rubert-tiny-turbo", "8ce0cf757446ce9bb2d5f5a4ac8103c7a1049054"),
    ("Muennighoff__SGPT-1.3B-weightedmean-msmarco-specb-bitfit", "no_revision_available"),
    ("vprelovac__universal-sentence-encoder-multilingual-large-3", "no_revision_available"),
    ("deepset__gbert-base", "no_revision_available"),
    ("sentence-transformers__allenai-specter", "no_revision_available"),
    ("McGill-NLP__LLM2Vec-Mistral-supervised", "no_revision_available"),
]


def test_model_meta_in_folders():
    """
    the folders should contain a model_meta.json file
    """
    results_folder = Path(__file__).parent.parent / "results"

    for model_folder in results_folder.glob("*"):
        for rev_folder in model_folder.glob("*"):
            if (model_folder.name, rev_folder.name) in folders_without_meta:
                continue

            meta_file = rev_folder / "model_meta.json"
            assert meta_file.exists()
            assert meta_file.is_file()
            assert meta_file.parent == rev_folder
            assert meta_file.suffix == ".json"
            assert meta_file.stem == "model_meta"

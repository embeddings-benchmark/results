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
    ("text-search-davinci-001", "no_revision_available"),
    ("LLM2Vec-Llama-2-unsupervised", "no_revision_available"),
    ("text-search-babbage-001", "no_revision_available"),
    ("instructor-base", "no_revision_available"),
    ("embedder-100p", "no_revision_available"),
    ("text-embedding-ada-002-instruct", "no_revision_available"),
    ("bge-m3-instruct", "5617a9f61b028005a4858fdac845db406aefb181"),
    ("xlm-roberta-large", "no_revision_available"),
    ("voyage-2", "no_revision_available"),
    ("text-search-ada-001", "no_revision_available"),
    ("gtr-t5-large", "no_revision_available"),
    ("sentence-t5-xxl", "no_revision_available"),
    ("text-embedding-3-small-instruct", "no_revision_available"),
    ("bge-m3", "no_revision_available"),
    ("voyage-lite-02-instruct", "no_revision_available"),
    ("text-similarity-ada-001", "no_revision_available"),
    ("LLM2Vec-Sheared-Llama-supervised", "no_revision_available"),
    ("e5-base", "no_revision_available"),
    ("bge-small-zh-v1.5", "no_revision_available"),
    ("bge-base-en", "no_revision_available"),
    ("electra-small-swedish-cased-discriminator", "no_revision_available"),
    ("nomic-embed-text-v1.5-512", "no_revision_available"),
    ("LLM2Vec-Mistral-unsupervised", "no_revision_available"),
    ("voyage-law-2", "no_revision_available"),
    ("e5-base-4k", "no_revision_available"),
    ("cross-en-de-roberta-sentence-transformer", "no_revision_available"),
    ("sentence-camembert-base", "no_revision_available"),
    ("SGPT-5.8B-weightedmean-nli-bitfit", "no_revision_available"),
    ("camembert-large", "no_revision_available"),
    ("SGPT-125M-weightedmean-msmarco-specb-bitfit-doc", "no_revision_available"),
    ("Baichuan-text-embedding", "no_revision_available"),
    ("LaBSE", "e34fab64a3011d2176c99545a93d5cbddc9a91b7"),
    ("LaBSE", "no_revision_available"),
    ("sentence-croissant-llm-base", "no_revision_available"),
    ("bert-base-25lang-cased", "no_revision_available"),
    ("sgpt-bloom-7b1-msmarco", "no_revision_available"),
    ("electra-small-nordic", "no_revision_available"),
    ("SGPT-5.8B-weightedmean-msmarco-specb-bitfit", "no_revision_available"),
    ("distilbert-base-uncased", "no_revision_available"),
    ("LLM2Vec-Meta-Llama-3-supervised", "no_revision_available"),
    ("text-embedding-3-large", "no_revision_available"),
    ("bert-base-10lang-cased", "no_revision_available"),
    ("sentence-t5-large", "no_revision_available"),
    ("m3e-base", "no_revision_available"),
    ("e5-mistral-7b-instruct", "no_revision_available"),
    ("camembert-base", "no_revision_available"),
    ("universal-sentence-encoder-multilingual-3", "no_revision_available"),
    ("sentence-camembert-large", "no_revision_available"),
    ("gelectra-large", "no_revision_available"),
    ("e5-large-v2", "no_revision_available"),
    ("e5-large-v2", "b322e09026e4ea05f42beadf4d661fb4e101d311"),
    ("m3e-large", "no_revision_available"),
    ("llama-2-7b-chat", "no_revision_available"),
    ("sgpt-bloom-1b7-nli", "no_revision_available"),
    ("all-mpnet-base-v2", "84f2bcc00d77236f9e89c8a360a00fb1139bf47d"),
    ("sentence-t5-xl", "no_revision_available"),
    ("distilbert-base-en-fr-cased", "no_revision_available"),
    ("text-embedding-ada-002", "no_revision_available"),
    ("bge-small-en-v1.5-instruct", "5c38ec7c405ec4b44b94cc5a9bb96e735b38267a"),
    ("text2vec-base-multilingual", "no_revision_available"),
    ("multi-qa-MiniLM-L6-cos-v1", "no_revision_available"),
    ("jina-embeddings-v2-base-en", "no_revision_available"),
    ("mistral-7b-instruct-v0.2", "no_revision_available"),
    ("monot5-base-msmarco-10k", "no_revision_available"),
    ("gte-Qwen2-7B-instruct", "no_revision_available"),
    ("bert-base-multilingual-uncased", "no_revision_available"),
    ("distiluse-base-multilingual-cased-v2", "no_revision_available"),
    ("distiluse-base-multilingual-cased-v2", ".gitkeep"),
    ("bge-base-zh-v1.5", "no_revision_available"),
    ("google-gecko.text-embedding-preview-0409", "no_revision_available"),
    ("text-search-curie-001", "no_revision_available"),
    ("sup-simcse-bert-base-uncased", "no_revision_available"),
    ("bge-base-en-v1.5-instruct", "a5beb1e3e68b9ab74eb54cfd186867f64f240e1a"),
    ("GritLM-7B", "no_revision_available"),
    ("GritLM-7B", "13f00a0e36500c80ce12870ea513846a066004af"),
    ("Cohere-embed-multilingual-light-v3.0", "no_revision_available"),
    ("bge-base-zh", "no_revision_available"),
    ("voyage-code-2", "no_revision_available"),
    ("sentence-t5-base", "no_revision_available"),
    ("flaubert_large_cased", "no_revision_available"),
    ("Cohere-embed-english-v3.0-instruct", "no_revision_available"),
    ("SFR-Embedding-Mistral", "no_revision_available"),
    ("dragon-plus", "no_revision_available"),
    ("LLM2Vec-Sheared-Llama-unsupervised", "no_revision_available"),
    ("text-embedding-3-small", "no_revision_available"),
    ("flan-t5-base", "no_revision_available"),
    ("text-search-ada-doc-001", "no_revision_available"),
    ("bert-base-multilingual-cased", "no_revision_available"),
    ("LLM2Vec-Meta-Llama-3-unsupervised", "no_revision_available"),
    ("silver-retriever-base-v1", "no_revision_available"),
    ("facebook-dpr-ctx_encoder-multiset-base", "no_revision_available"),
    ("bm25s", "0_1_10"),
    ("all-MiniLM-L12-v2", "a05860a77cef7b37e0048a7864658139bc18a854"),
    ("dragon-plus-instruct", "no_revision_available"),
    ("elser-v2", "no_revision_available"),
    ("contriever-instruct", "2bd46a25019aeea091fd42d1f0fd4801675cf699"),
    ("bge-small-en-v1.5", "5c38ec7c405ec4b44b94cc5a9bb96e735b38267a"),
    ("SGPT-125M-weightedmean-msmarco-specb-bitfit", "no_revision_available"),
    ("bge-large-zh-noinstruct", "no_revision_available"),
    ("udever-bloom-560m", "no_revision_available"),
    ("st-polish-paraphrase-from-distilroberta", "no_revision_available"),
    ("gtr-t5-base", "no_revision_available"),
    ("e5-mistral-7b-instruct-noinstruct", "07163b72af1488142a360786df853f237b1a3ca1"),
    ("SGPT-2.7B-weightedmean-msmarco-specb-bitfit", "no_revision_available"),
    ("xlm-roberta-base", "no_revision_available"),
    ("bge-large-zh-v1.5", "no_revision_available"),
    ("tart-dual-contriever-msmarco", "no_revision_available"),
    ("text-embedding-preview-0409-768", "no_revision_available"),
    ("DanskBERT", "no_revision_available"),
    ("gbert-large", "no_revision_available"),
    ("text-similarity-davinci-001", "no_revision_available"),
    ("use-cmlm-multilingual", "no_revision_available"),
    ("sentence-bert-swedish-cased", "no_revision_available"),
    ("nomic-embed-text-v1", "no_revision_available"),
    ("text-similarity-babbage-001", "no_revision_available"),
    ("mistral-embed", "no_revision_available"),
    ("voyage-large-2-instruct", "no_revision_available"),
    ("flaubert_base_uncased", "no_revision_available"),
    ("nomic-embed-text-v1.5-256", "no_revision_available"),
    ("e5-large", "no_revision_available"),
    ("bge-large-zh", "no_revision_available"),
    ("distilbert-base-en-fr-es-pt-it-cased", "no_revision_available"),
    ("SGPT-5.8B-weightedmean-msmarco-specb-bitfit-que", "no_revision_available"),
    ("voyage-multilingual-2", "no_revision_available"),
    ("all-mpnet-base-v2-instruct", "84f2bcc00d77236f9e89c8a360a00fb1139bf47d"),
    ("SGPT-125M-weightedmean-msmarco-specb-bitfit-que", "no_revision_available"),
    ("glove.6B.300d", "no_revision_available"),
    ("OpenSearch-text-hybrid", "no_revision_available"),
    ("gelectra-base", "no_revision_available"),
    ("bge-small-zh", "no_revision_available"),
    ("st-polish-paraphrase-from-mpnet", "no_revision_available"),
    ("bm25", "no_revision_available"),
    ("nomic-embed-text-v1.5-128", "no_revision_available"),
    ("voyage-lite-01-instruct", "no_revision_available"),
    ("instructor-large", "no_revision_available"),
    ("contriever", "2bd46a25019aeea091fd42d1f0fd4801675cf699"),
    ("gte-Qwen1.5-7B-instruct", "no_revision_available"),
    ("msmarco-bert-co-condensor", "no_revision_available"),
    ("text2vec-large-chinese", "no_revision_available"),
    ("multilingual-e5-small", "e4ce9877abf3edfe10b0d82785e83bdcb973e22e"),
    ("multilingual-e5-small", "no_revision_available"),
    ("monot5-3b-msmarco-10k", "no_revision_available"),
    ("FollowIR-7B", "no_revision_available"),
    ("herbert-base-retrieval-v2", "no_revision_available"),
    ("udever-bloom-1b1", "no_revision_available"),
    ("text-embedding-3-large-instruct", "no_revision_available"),
    ("LLM2Vec-Llama-2-supervised", "no_revision_available"),
    ("Cohere-embed-multilingual-v3.0", "no_revision_available"),
    ("norbert3-large", "no_revision_available"),
    ("tart-full-flan-t5-xl", "no_revision_available"),
    ("nomic-embed-text-v1.5-64", "no_revision_available"),
    ("nb-bert-base", "no_revision_available"),
    ("distilbert-base-fr-cased", "no_revision_available"),
    ("instructor-xl", "no_revision_available"),
    ("text2vec-base-chinese", "no_revision_available"),
    ("bge-large-en", "no_revision_available"),
    ("bge-large-en-v1.5-instruct", "d4aa6901d3a41ba39fb536a557fa166f842b0e09"),
    ("bert-base-uncased", "no_revision_available"),
    ("all-MiniLM-L6-v2", "8b3219a92973c328a8e22fadcfa821b5dc75636a"),
    ("all-MiniLM-L6-v2", "no_revision_available"),
    ("e5-base-v2", "no_revision_available"),
    ("e5-base-v2", "1c644c92ad3ba1efdad3f1451a637716616a20e8"),
    ("gtr-t5-xl", "no_revision_available"),
    ("norbert3-base", "no_revision_available"),
    ("text-embedding-3-large-256", "no_revision_available"),
    ("e5-small", "no_revision_available"),
    ("komninos", "no_revision_available"),
    ("monobert-large-msmarco", "no_revision_available"),
    ("gottbert-base", "no_revision_available"),
    ("nb-bert-large", "no_revision_available"),
    ("unsup-simcse-bert-base-uncased", "no_revision_available"),
    ("bert-base-15lang-cased", "no_revision_available"),
    ("flaubert_base_cased", "no_revision_available"),
    ("paraphrase-multilingual-MiniLM-L12-v2", "no_revision_available"),
    (
        "paraphrase-multilingual-MiniLM-L12-v2",
        "bf3bf13ab40c3157080a7ab344c831b9ad18b5eb",
    ),
    ("all-MiniLM-L6-v2-instruct", "8b3219a92973c328a8e22fadcfa821b5dc75636a"),
    ("distilbert-base-25lang-cased", "no_revision_available"),
    ("LASER2", "no_revision_available"),
    ("Cohere-embed-english-v3.0", "no_revision_available"),
    ("SGPT-125M-weightedmean-nli-bitfit", "no_revision_available"),
    ("titan-embed-text-v1", "no_revision_available"),
    ("contriever-base-msmarco", "no_revision_available"),
    ("bert-base-swedish-cased", "no_revision_available"),
    ("multilingual-e5-large", "no_revision_available"),
    ("multilingual-e5-large", "4dc6d853a804b9c8886ede6dda8a073b7dc08a81"),
    ("text-similarity-curie-001", "no_revision_available"),
    ("luotuo-bert-medium", "no_revision_available"),
    ("facebookdragon-plus-context-encoder", "no_revision_available"),
    ("bge-large-en-v1.5", "no_revision_available"),
    ("bge-large-en-v1.5", "d4aa6901d3a41ba39fb536a557fa166f842b0e09"),
    ("dfm-encoder-large-v1", "no_revision_available"),
    ("GritLM-7B-noinstruct", "13f00a0e36500c80ce12870ea513846a066004af-temp"),
    ("gtr-t5-xxl", "no_revision_available"),
    ("google-gecko-256.text-embedding-preview-0409", "no_revision_available"),
    ("multilingual-e5-base", "no_revision_available"),
    ("multilingual-e5-base", "d13f1b27baf31030b7fd040960d60d909913633f"),
    (
        "paraphrase-multilingual-mpnet-base-v2",
        "79f2382ceacceacdf38563d7c5d16b9ff8d725d6",
    ),
    ("paraphrase-multilingual-mpnet-base-v2", "no_revision_available"),
    ("flan-t5-large", "no_revision_available"),
    ("rubert-tiny-turbo", "8ce0cf757446ce9bb2d5f5a4ac8103c7a1049054"),
    ("SGPT-1.3B-weightedmean-msmarco-specb-bitfit", "no_revision_available"),
    ("universal-sentence-encoder-multilingual-large-3", "no_revision_available"),
    ("gbert-base", "no_revision_available"),
    ("allenai-specter", "no_revision_available"),
    ("LLM2Vec-Mistral-supervised", "no_revision_available"),
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

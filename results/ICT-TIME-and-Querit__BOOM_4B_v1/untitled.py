from mteb.models import ModelMeta, sentence_transformers_loader

my_model = ModelMeta(
    name="hengranZhang/BOOM_4B_v1",
    loader=sentence_transformers_loader,
    languages=["eng-Latn"], # follows ISO 639-3 and BCP-47
    open_weights=True,
    revision="no_revision_available",
    release_date="2026-01-30",
    n_parameters=4021774336,
    memory_usage_mb=7671.0,
    embed_dim=2560,
    license="apache-2.0",
    max_tokens=32768.0,
    reference="https://huggingface.co/user-or-org/model-name",
    similarity_fn_name="cosine",
    framework=["Sentence Transformers", "PyTorch"],
    use_instructions=False,
    public_training_code="https://github.com/hengran/Bagging-Based-Model-Merging",
    public_training_data=null,
    training_datasets=null
    # training_datasets=["FEVER", "CornStack", "DuRetrieval", "HotpotQA", "MSMARCO", "T2Ranking", "NQ", "MIRACLRetrieval", "MrTidyRetrieval", "Amazon_counterfactual", "Amazon_reviews", "Banking", "Emotion", "IMDB", "Mtop_Intent", "Toxic Conversations", "Tweet Sentiment", "ArXiv", "Biorxiv", "Medrxiv", "Reddit", "Stack_exchange", "twenty_news", "ELI5", "FiQA", "NLI", "Squad", "Stack Overflow Dup questions", "Trivial", "STS"], 
)
# training_datasets=["FEVER", "CornStack", "DuRetrieval", "HotpotQA", "MSMARCO", "T2Ranking", "NQ", "MIRACLRetrieval", "MrTidyRetrieval", "Amazon_counterfactual", "Amazon_reviews", "Banking", "Emotion", "IMDB", "Mtop_Intent", "Toxic Conversations", "Tweet Sentiment", "ArXiv", "Biorxiv", "Medrxiv", "Reddit", "Stack_exchange", "twenty_news", "ELI5", "FiQA", "NLI", "Squad", "Stack Overflow Dup questions", "Trivial", "STS"], 

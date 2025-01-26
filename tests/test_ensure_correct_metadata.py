import json

import pytest

from tests.test_correct_folder_structure import folders_without_meta, results_folder

model_rev_pairs = [
    (model_folder, rev_folder)
    for model_folder in results_folder.glob("*")
    for rev_folder in model_folder.glob("*")
    if model_folder.name not in [".DS_Store"]
    and rev_folder.name not in [".DS_Store"]
    and ((model_folder.name, rev_folder.name) not in folders_without_meta)
]


@pytest.mark.parametrize("model_rev_pair", model_rev_pairs)
def test_model_meta_in_folders(model_rev_pair):
    """
    Models added after the 26th of November should contain a model_meta.json file
    """
    model_folder, rev_folder = model_rev_pair

    meta_file = rev_folder / "model_meta.json"
    assert meta_file.exists()
    assert meta_file.is_file()
    assert meta_file.parent == rev_folder
    assert meta_file.suffix == ".json"
    assert meta_file.stem == "model_meta"


# please do not add to this list, this is only for historic results, all new results should include a revision ID
revision_exceptions = [
    ("castorini__mdpr-tied-pft-msmarco", "no_revision_available"),
    ("voyageai__voyage-3", "no_revision_available"),
    ("sentence-transformers__all-mpnet-base-v2", "no_revision_available"),
    ("Snowflake__snowflake-arctic-embed-m-v1.5", "no_revision_available"),
    ("sentence-transformers__all-MiniLM-L12-v2", "no_revision_available"),
    ("nthakur__mcontriever-base-msmarco", "no_revision_available"),
    ('voyageai__voyage-3-lite', 'no_revision_available'),
    ("google-bert__bert-base-uncased", "no_revision_available"),
    ("google-bert__bert-large-uncased", "no_revision_available"),
    ("google-gecko__text-embedding-004", "no_revision_available"),
    ("hkunlp__instructor-large", "no_revision_available"),
    ("hkunlp__instructor-base", "no_revision_available"),
    ("flaubert__flaubert_base_cased", "no_revision_available"),
    ("google-bert__bert-base-multilingual-cased", "no_revision_available"),
    ("google-bert__bert-base-multilingual-uncased", "no_revision_available"),
    ("hkunlp__instructor-xl", "no_revision_available"),
    ("google-gecko__text-embedding-004-256", "no_revision_available"),
    ("google__flan-t5-large", "no_revision_available"),
    ("flaubert__flaubert_large_cased", "no_revision_available"),
    ("flaubert__flaubert_base_uncased", "no_revision_available"),
    ("google__flan-t5-base", "no_revision_available"),
]


@pytest.mark.parametrize("model_rev_pair", model_rev_pairs)
def test_revision_is_specified_for_new_additions(model_rev_pair):
    """
    Models added after 26th of November should include a revision ID and can not use the "no_revision_available" fallback.
    """
    model_folder, rev_folder = model_rev_pair
    if (model_folder.name, rev_folder.name) not in revision_exceptions:
        meta_file = rev_folder / "model_meta.json"
        with meta_file.open("r") as f:
            meta = json.load(f)
        assert meta["revision"].lower() not in [
            "no_revision_available",
            "",
            "na",
            "no-revision-available",
        ]


@pytest.mark.parametrize("model_rev_pair", model_rev_pairs)
def test_organization_is_specified_for_new_additions(model_rev_pair):
    """
    Models added after 26th of November should include a organization ID within their name, e.g. "myorg/my_embedding_model".

    This is to avoid mispecified names such as "myorg__my_embedding_model" and similar.
    """
    model_folder, rev_folder = model_rev_pair
    meta_file = rev_folder / "model_meta.json"
    with meta_file.open("r") as f:
        meta = json.load(f)
    assert "/" in meta["name"]

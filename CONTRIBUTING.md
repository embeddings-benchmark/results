# Contributing results

This repository stores evaluation results produced by [MTEB](https://github.com/embeddings-benchmark/mteb). Submit results through a pull request to this repository. See the [MTEB submission guide](https://docs.mteb.org/contributing/submitting_results/) for the full evaluation and submission workflow.

## Prepare your model

- Add your model's metadata and reference implementation to MTEB by following the [adding a model guide](https://docs.mteb.org/contributing/adding_a_model/). If the implementation is still under review, link its pull request in your results PR.
- Provide a model sheet, report, or similar documentation, and make the model available through public weights or a publicly accessible API.
- Disclose any training on evaluation datasets, including their training splits, in the PR and model metadata.

## Run the evaluation

Use the model's reference implementation in MTEB to evaluate the tasks or benchmarks you want to submit. For example, in an environment with MTEB and your model's dependencies installed:

```sh
mteb run -m sentence-transformers/all-MiniLM-L6-v2 -t ArguAna
```

Replace the example model and task with your own. Keep the generated result files, model metadata, and run settings together. New submissions must include:

- Task result JSON files generated with MTEB >= 2.0.0.
- A `model_meta.json` file identifying the evaluated model and revision.
- A `run_settings.jsonl` file covering every submitted task, split, and subset. Use the current `mteb.evaluate` API or `mteb run` CLI to generate these settings; the legacy `MTEB(...).run()` API does not write them.

For models producing low-precision embeddings, scoring must use float32. The submission checks require MTEB >= 2.24.6 or sentence-transformers >= 6.0.0 for these runs. Rerun evaluations with supported versions if necessary; do not edit recorded version numbers to bypass validation.

## Prepare the submission

MTEB can prepare a submission from your cached results:

```sh
mteb submit-results -m sentence-transformers/all-MiniLM-L6-v2 -t ArguAna
```

Follow the manual submission instructions printed by the command and review the prepared changes before submitting. See the [submission guide](https://docs.mteb.org/contributing/submitting_results/) for Python and automated submission options.

If copying results into a fork of this repository manually, preserve this layout:

```text
results/
└── organization__model-name/
    └── model-revision/
        ├── model_meta.json
        ├── run_settings.jsonl
        └── TaskName.json
```

The model folder must match the metadata's model name with `/` replaced by `__` and spaces replaced by `_`. The revision folder must match the evaluated model revision. Task filenames must match the task names in the generated results. Copy the generated files rather than writing scores or metadata by hand.

Preserve existing results, languages, and splits when adding evaluations. Explain any intentional corrections or replacements in your PR. Keep changes focused on the models and tasks you evaluated.

## Validate the results

Use Python 3.11 or later and [uv](https://docs.astral.sh/uv/) to install the repository's test dependencies and run its checks:

```sh
make install-for-tests
make test
```

Some checks compare committed result files in `HEAD` against the base branch, so local checks of uncommitted files alone do not validate the complete submission. The pull request's CI checks validate the submitted changes.

Each submitted file must be at most 10 MiB (10,485,760 bytes). If a JSON file is too large, compact its formatting without changing the scores. The repository also provides `uv run python reduce_large_json_files.py` to reduce large result and run-settings files; review its diff because it scans the entire results directory. Do not remove valid scores, splits, or subsets just to meet the size limit.

## Pull requests

When creating or updating a pull request, use [the pull request template](.github/pull_request_template.md) for the PR body. Read the template before drafting the body, fill in the description, and retain the full checklist. This also applies when submitting through a CLI or API, where the template may not be inserted automatically.

Include the model name and revision, evaluated tasks or benchmarks, a link to the model documentation and reference implementation (or its PR), and any relevant evaluation settings or training-data disclosures. Mention whether you are adding new results or correcting existing ones, and report the validation you ran.

Check an item only when it is supported by evidence or confirmed by the contributor. Leave unverified items unchecked and explain any items that do not apply. Review CI failures and address them before requesting review.

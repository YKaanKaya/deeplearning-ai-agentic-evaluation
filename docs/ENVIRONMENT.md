# Environment and reproduction

Audit: 14 November 2026. Facts below come from notebook metadata/imports, not fresh hosted execution.

| Evidence | Observed configuration |
| --- | --- |
| Module 1 Python tracing notebook | Python metadata 3.12.16; pandas and IPython; standard-library tracing utilities |
| Graded notebooks, Modules 1-5 | Python metadata 3.11.13; Python 3 ipykernel; pandas and Phoenix APIs |
| Modules 2-5 | Anthropic model access directly or through course helpers / Phoenix evaluators |
| Module 3 | `phoenix.evals`, OpenInference tracing suppression, scikit-learn classification metrics and train/test split |
| Module 4 | Phoenix LLM/classification evaluators, OpenInference tracing suppression |
| Module 5 | Phoenix async experiments/client; `anthropic/claude-sonnet-4-6` judge in cell 9 |

No requirements file, pyproject, package lock, `pip freeze` or complete helper tree accompanies the course capture. Installed versions and exact seeded-data versions cannot be inferred from imports. Saved model names describe snapshots, not guaranteed API availability or deterministic reproduction.

## Hosted course route

Open a module's linked lesson and use its supplied runtime. Preserve notebook names, cell order, working directories, helpers and relative imports. Save a baseline before edits; execute in order, inspect exceptions and final outputs, then export the notebook, supporting tree and environment versions. This is guidance, not a tested reinstall procedure.

The notebooks import missing packages such as `apparel_agent`, `dlai_utils`, `trace_display`, `utils` and `unittests`. Some assume course-provided model credentials/proxies and a local Phoenix service. Installing similarly named packages will not reconstruct these course modules. The M2 notebook retains a `RateLimitError`.

## Included local examples

The five-stage [technical companion](TECHNICAL_WALKTHROUGH.md) is also independently authored and uses only the Python standard library. It replays new synthetic requests, constructs trace-linked cases, validates fixed label vectors, evaluates actions/state and compares protected layers. It starts no Phoenix server and calls no model. Its synthetic duration fields are fixture data, not measured latency. Run it from the repository root:

```powershell
python -m technical_companion
python -m unittest technical_companion.test_pipeline -v
```

`experiments/identity_alignment.py` uses only the Python standard library. It verifies reordered rows, duplicate/missing identities and paired aggregation. The notebook contains the same separately authored example with synthetic data and outputs generated during publication.

```powershell
python experiments/identity_alignment.py
```

Tested with Python **3.11.9**. Expected final line: `PASS: identity alignment, invariant scores, and duplicate/missing-case checks`.

This example explains a comparison bug. It does not execute Northwind, call an LLM, reproduce a course grade or measure agent quality. No credentials or environment files are published.

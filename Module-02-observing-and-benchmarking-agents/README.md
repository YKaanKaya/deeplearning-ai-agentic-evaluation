# Module 2: Observing and Benchmarking Agents

**Educational module notes** from DeepLearning.AI coursework, using the fictional Northwind Apparel scenario. Course exercises and results are learning examples rather than a production reliability assessment.

Original synthesis from saved local artifacts, reviewed on 14 November 2026. This review did not run the labs or verify unseen lectures.

## What this module demonstrates

A useful benchmark starts with observable failures and application requirements. Northwind traces are reduced to one row per agent run, reviewed for category and severity, expanded with curated synthetic questions, and saved with span IDs so a label can be traced back to its evidence.

The saved assignment contains implementations for Phoenix client initialization, root-span extraction, label joins and failure-dataset creation. The course supplies the agent, assignment structure and test harness. A separate practice capture documents AI-assisted query curation and annotation; it is not an independent human labeling study.

## Observed evidence

- The practice capture records 43 traces and a final four-case regression set: two manual and two synthetic scope violations. Its notes explicitly dispute several labels and distinguish factual grounding from useful task completion.
- The graded notebook records 32 manual labeled rows and 11 manual failures. It generated 48 candidates, selected 29, and later reports 28 synthetic labeled rows and 10 synthetic failures.
- A `RateLimitError` remains in the synthetic batch cell. The final saved dataset reports 21 failures, but this notebook cannot be described as a clean, uninterrupted execution.

These are two different saved lab artifacts. Their counts must not be merged. A deliberately adversarial, failures-only dataset also cannot estimate the agent's production error rate.

## Artifacts and limits

Local-only originals: `labs/m2-graded-lab-error-analysis-and-synthetic-test-data/C1M2_Assignment.ipynb` and `labs/lab-1-build-the-northwind-benchmark/M2_Northwind_Benchmark_Capture.zip`. The archive includes original curation and labeling notes, four trace-linked benchmark entries, six screenshots and a GIF. A standalone copy of that GIF is also present. See the [artifact manifest](../docs/ARTIFACTS.json) and [saved results](../docs/RESULTS.md).

No runnable practice notebook, agent package, helper modules or dependency lock is preserved here. The archive is a learning capture rather than a complete application export. No new execution or platform-grade verification is claimed.

## Published learning material

| Resource | What to explore |
| --- | --- |
| [Lab 1: Build the Northwind Benchmark](labs/lab-1-build-the-northwind-benchmark/CAPTURE.md) | Lab analysis of saved visual evidence |
| [M2 Graded Lab: Error analysis and synthetic test data](labs/m2-graded-lab-error-analysis-and-synthetic-test-data/CAPTURE.md) | Lab analysis of saved notebook outputs |

For the full teaching sequence, use the [official course](https://www.deeplearning.ai/courses/evaluating-and-improving-agentic-applications). This repository presents selected educational explanations and saved evidence, rather than a complete set of lecture notes.

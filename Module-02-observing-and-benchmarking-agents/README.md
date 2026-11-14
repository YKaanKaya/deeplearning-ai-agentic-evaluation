# Module 2: Observing and Benchmarking Agents

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

No runnable practice notebook, agent package, helper modules or dependency lock is preserved here. The archive is a learning capture rather than a complete application export. Lesson-note templates remain incomplete; no new execution or platform-grade verification is claimed.

## Lesson index

The syllabus order follows the course capture of 4 November 2026. Documentation status is independent of platform completion.

| # | Lesson | Format | Capture status |
| --- | --- | --- | --- |
| 01 | [Define Application Requirements](notes/01-define-application-requirements.md) | Video | Pending verification |
| 02 | [Turn Requirements into Test Cases](notes/02-turn-requirements-into-test-cases.md) | Video | Pending verification |
| 03 | [Analyze and Label Failures](notes/03-analyze-and-label-failures.md) | Video | Pending verification |
| 04 | [Build a Test Set You Can Trust](notes/04-build-a-test-set-you-can-trust.md) | Video | Pending verification |
| 05 | [Build the Northwind Benchmark](notes/05-build-the-northwind-benchmark.md) | Video | Pending verification |
| 06 | [Lab 1: Build the Northwind Benchmark](labs/lab-1-build-the-northwind-benchmark/CAPTURE.md) | Code Example | Archive and media inspected |
| 07 | [M2 Graded Lab: Error analysis and synthetic test data](labs/m2-graded-lab-error-analysis-and-synthetic-test-data/CAPTURE.md) | Graded・Code Assignment | Saved notebook; retained error |
| 08 | [Module 2 Quiz](notes/08-module-2-quiz.md) | Graded・Quiz | Pending verification |
| 09 | [Module 2 Resources](notes/09-module-2-resources.md) | Reading | Pending verification |

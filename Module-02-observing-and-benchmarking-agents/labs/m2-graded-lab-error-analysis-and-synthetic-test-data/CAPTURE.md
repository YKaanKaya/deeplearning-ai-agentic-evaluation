# M2 Graded Lab: Error analysis and synthetic test data

[Course lesson](https://learn.deeplearning.ai/courses/evaluating-and-improving-agentic-applications/lesson/i1bmot/m2-graded-lab%3A-error-analysis-and-synthetic-test-data) · M2-07

Status: saved notebook inspected on 14 November 2026; retained execution error; no new run or platform-grade verification.

## Problem and method

Build a failure benchmark from Phoenix root spans, apply category and severity labels, expand coverage with generated questions and register trace-linked datasets. Completed exercise regions implement client initialization, root-span extraction, label joins and dataset creation. The surrounding application and grading harness are supplied by the course.

## Saved outputs

Local-only original: `C1M2_Assignment.ipynb` (82 cells, including 35 code cells). All code cells have execution counts, but cell 72 retains a `RateLimitError` from the curated synthetic batch. Execution counts therefore do not establish a clean run.

- Cell 48: 32 manual labeled rows.
- Cells 55-61: 11 manual failures: six format inconsistencies, three scope violations and two faithfulness drifts.
- Cell 68: 48 generated queries using `claude-sonnet-4-6`.
- Cell 70: 29 curated queries.
- Cell 76: 28 synthetic labeled rows, with 18 passes, eight scope violations, one hallucination and one faithfulness drift.
- Cell 80: final dataset with 21 failures, comprising 11 manual and ten synthetic examples.

Four exercise-test outputs pass at cells 18, 31, 50 and 63. These are local saved test results, not platform grades. The missing synthetic row and retained rate-limit failure remain explicit limitations; no clean rerun has been substituted.

## Interpretation and reproduction

The label join uses query text, so repeated questions require deliberate handling to keep labels attached to the intended outputs. Category labels and generated stress tests do not independently establish real-world error frequency. These graded-assignment counts are distinct from the separate four-case practice capture.

Notebook metadata records Python 3.11.13. Course `utils`, `unittests`, the agent, database and a requirements/lock file are absent from this capture. The assignment and solutions remain local-only. See [the artifact manifest](../../../docs/ARTIFACTS.json), [saved results](../../../docs/RESULTS.md) and [environment documentation](../../../docs/ENVIRONMENT.md).

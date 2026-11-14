# M3 Graded Lab: Building and trusting evaluators

[Course lesson](https://learn.deeplearning.ai/courses/evaluating-and-improving-agentic-applications/lesson/x7gfw63j/m3-graded-lab%3A-building-and-trusting-evaluators) · M3-07

Status: saved notebook and five Phoenix GIFs inspected on 14 November 2026; no new execution or platform-grade verification.

## Problem and implementation

Check the reliability of evaluators before using their scores to steer agent changes. The course workflow combines a catalog code check, correctness judging and a policy rubric, with stratified development/validation/test splits. Completed exercise regions implement the splits, policy evaluator construction, reference-label updates and Cohen's kappa measurement. The surrounding application and tests are course-provided.

## Saved results

Local-only original: `C1M3_Assignment.ipynb` (76 cells; 35 code cells, all with execution counts and no retained error outputs). Cell 15 defines 57 queries; cell 20 reports 56 labeled runs. The cause of the missing run is not established by the saved capture. Cell 24 reports splits of 33 development, 11 validation and 12 final-test examples.

| Zero-based cell | Comparison | Saved result |
| --- | --- | --- |
| 49 | v1 vs initial validation labels, n=11 | accuracy 0.636; kappa 0.312 |
| 57 | v1 after reference-label changes, n=11 | accuracy 1.000; kappa 1.000 |
| 66 | v2 vs revised validation labels, n=11 | accuracy 0.636; kappa 0.312 |
| 73 | v1 final test, n=12 | accuracy 0.750; kappa 0.400 |
| 74 | v2 final test, n=12 | accuracy 0.750; kappa 0.400 |

Both final-test confusion matrices are `[[2, 1], [2, 7]]`, with rows and columns ordered non-compliant, compliant. Only three final-test examples are non-compliant. Four exercise-test outputs pass at cells 26, 43, 59 and 68; those tests are not assignment grades.

## Interpretation

The perfect intermediate validation score follows reference-label changes in the exercise. It is not evidence of an improved judge. The update is not an independent blinded annotation study, and a high agreement score cannot establish that either the judge or the reference is correct. The saved final aggregates provide no evidence that policy v2 outperformed v1.

Cell 34 records an Anthropic `claude-sonnet-4-6` judge; metadata records Python 3.11.13. Five graded GIFs show Phoenix overview, traces, code checks, correctness and policy annotations. They support navigation through the evidence rather than replacing the notebook's held-out results.

## Reproduction and publication

No dependency lock, course `utils`/`unittests`, agent package or database export is preserved. The notebook and solutions remain local-only, and no local rerun is claimed. See [the artifact manifest](../../../docs/ARTIFACTS.json), [saved results](../../../docs/RESULTS.md) and [environment documentation](../../../docs/ENVIRONMENT.md).

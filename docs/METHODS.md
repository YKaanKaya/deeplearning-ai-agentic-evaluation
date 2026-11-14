# Methods index

This index distinguishes methods observed in saved artifacts from lecture review. All original notebooks remain local; hashes and saved execution state are in [ARTIFACTS.json](ARTIFACTS.json). Most lesson-note templates are still pending.

| Method | What it measures / procedure | Evidence and failure mode |
| --- | --- | --- |
| Explicit success criteria | Define expected behavior before a test; separate user outcome, policy and factual support | Module 1 opening summary; Module 5 practice predeclared criterion. A grade or fluent answer is not agent success. |
| Local spans and Phoenix tracing | Record parent/child operations, inputs, outputs, errors and elapsed time | [Module 1](../Module-01-foundations-of-evals/README.md). A trace explains an execution; it does not validate correctness. |
| Manual error analysis | Label failures by requirement and curate realistic examples | [Module 2](../Module-02-observing-and-benchmarking-agents/README.md). Subjective labels and ambiguous usefulness/grounding need review. |
| Synthetic benchmark curation | Generate candidates, filter duplicates, preserve representative cases and labels | M2 practice archive and graded notebook are different datasets. Failure-only sets cannot estimate prevalence. |
| Deterministic code checks | Apply explicit expected-tool, argument or catalog rules | [Module 3](../Module-03-building-evaluators-you-can-trust/README.md), [Module 4](../Module-04-evaluating-agent-actions-and-outcomes/README.md). Literal matching may reject valid alternatives. |
| Model judges and custom rubrics | Score saved inputs, responses or trajectories against a defined rubric | M3/M4 policy and correctness annotations. Rubric ambiguity, model stochasticity and no-tool grounding passes need inspection. |
| Reference-label validation | Hold out cases, inspect disagreements, report classification metrics and Cohen's kappa | M3 splits 33/11/12; both final policy judges .750 accuracy, kappa 0.400. Changing references invalidates simple before/after claims. |
| Layered action/outcome evaluation | Score tool selection, invocation, identity-before-refund, policy and final outcome separately | M4 n=12. Failures overlap; final-answer quality can hide action failures. |
| Paired experiment comparison | Compare identical unique cases across versions; protect known-good behavior | [M5 analysis](RESULTS.md), [synthetic implementation](../experiments/identity-alignment.ipynb). Positional joins fabricate case changes. |
| Operational tradeoffs | Inspect tool calls and timing alongside quality and outcome | M5 snapshots only; no controlled repeated trials or reliable monetary cost export. |
| Production-to-regression feedback | Annotate failures, curate new cases, grow the test set and rerun | M5 saves 5 production samples and appends 2 cases to reach 7; no later 7-case run is saved. |

Proposed extension, not completed work: apply this workflow to an independently authored agent with public/synthetic data, fixed dataset identifiers, versioned rubrics and repeated trials.

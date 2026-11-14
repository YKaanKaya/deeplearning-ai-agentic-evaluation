# Results with evidence and limits

**Educational evidence from the fictional Northwind support-agent labs.** These small course exercises illustrate how evaluation methods reveal different kinds of failure.

Audit: 14 November 2026. Notebook cell indices are **zero-based**. Originals remain local and are fingerprinted in [ARTIFACTS.json](ARTIFACTS.json). These are saved outputs, not freshly replicated measurements.

## Module 3 - validate the policy judge

The graded notebook defines 57 queries, saves 56 labeled runs and reports development/validation/test splits of **33/11/12**. The missing run is unexplained.

| Cell | Comparison | Accuracy | Cohen's kappa |
| --- | --- | ---: | ---: |
| 49 | v1 vs initial validation labels, n=11 | 0.636 | 0.312 |
| 57 | v1 after reference-label changes, n=11 | 1.000 | 1.000 |
| 66 | v2 vs revised validation labels, n=11 | 0.636 | 0.312 |
| 73 | v1 final test, n=12 | 0.750 | 0.400 |
| 74 | v2 final test, n=12 | 0.750 | 0.400 |

Both final-test confusion matrices are `[[2, 1], [2, 7]]`, ordered non-compliant/compliant, human rows and judge columns. Only three test examples are non-compliant. The perfect intermediate agreement follows label changes, not an improved judge. Neither judge nor reference becomes ground truth through agreement alone. [Module 3 capture](../Module-03-building-evaluators-you-can-trust/labs/m3-graded-lab-building-and-trusting-evaluators/CAPTURE.md).

## Module 4 - separate the layers

Saved graded test table, **n=12**:

| Layer | Passed | Failed |
| --- | ---: | ---: |
| Tool selection | 6 | 6 |
| Tool invocation | 4 | 8 |
| Task outcome | 11 | 1 |
| Policy compliance | 11 | 1 |

Counts overlap across layers. They cannot be added as distinct failed cases or treated as production prevalence. Expected-tool/argument rules, outcome checks and model policy judgments measure different properties. [Module 4 capture](../Module-04-evaluating-agent-actions-and-outcomes/labs/m4-graded-lab-multi-layer-agent-evaluation/CAPTURE.md).

## Module 5 - two separate evidence sets

### Graded notebook: compare by identity

Source: local `C1M5_Assignment.ipynb`, SHA-256 `b933579d4819986a7492b35706c33d93cc174febedd8041d3b58695aac6e3526`. Cell 53 outputs 1/5/9 contain failure frames for v1/v2/v3; outputs 3/7/11 contain known-good frames. Row order changes. Cell 55's positional summary swaps v3 merino/hiking scores. Cell 57 has the same issue for per-case latency.

Matching saved failure frames by `case` gives:

| Case | v1 grounding | v2 grounding | v3 grounding |
| --- | ---: | ---: | ---: |
| Raincoat waterproofing | 1 | 1 | 1 |
| Beanie care | 0 | 0 | 0 |
| Denim jacket care | 1 | 1 | 1 |
| Hiking shoes materials | 1 | 1 | 1 |
| Merino wool care | 0 | 0 | 0 |
| **Grounded / 5** | **3/5** | **3/5** | **3/5** |

Known-good frames show 4/5 grounded in each version, with order status failing each time. Each uses seven tool calls in aggregate; mean saved latencies are about **1.38s, 0.20s, 0.21s**. Row misalignment corrupts case attribution, even when totals stay equal. Timing lacks repeats and cache/proxy controls; it cannot establish a causal speedup.

The original notebook remains unchanged. The [independent synthetic example](../experiments/identity-alignment.ipynb) requires unique case keys, rejects missing cases and aligns identity before comparing. This is publication-time analysis, not a corrected course notebook download.

Production cell 68 saves five compliant labels and four grounded labels. Four cases call no tools; some grounding passes only mean unsupported product facts were avoided, not that the task was completed. Cell 72 records five matched spans and five annotations for each of two evaluators. Cell 79 appends two production cases, growing the failure set from five to seven. No later seven-case experiment output is saved.

### Practice recording: protect known-good outcomes

Source: `M5_04_Data_Fix_and_Final_Comparison.gif`, frame 6; a **different practice snapshot** of three failure and three known-good cases. No corresponding practice notebook is local.

| Version | Failure grounding | Known-good grounding | Known-good selection / outcome | Known-good policy | Tool calls | Mean latency |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| v1 | 1/3 | 2/3 | 3/3 | 3/3 | 8 | 4.57s |
| v2 | 3/3 | 3/3 | 3/3 | 3/3 | 8 | 4.78s |
| v3 | 3/3 | 3/3 | 2/3 | 3/3 | 9 | 5.43s |

These values are transcribed from the recording, not recomputed. Its 36/36 evaluator scores per version describe score coverage, not 36 successful outcomes. The [Phoenix excerpt](../assets/m5-comparison.gif) shows v2 processing a $98 refund while v3 requests confirmation: v3 remains grounded/policy-compliant but fails selection and outcome.

A data-fix stage changes grounding from 1/3 to 2/3, but the recording identifies the merino change as stochastic with no catalog edit. It does not isolate a causal data-fix benefit. The snapshot supports selecting v2 within this tiny test, without overriding the graded notebook or proving general improvement. A reliable monetary cost comparison was not exported.

## Completion and missing evidence

The [public certificate](https://www.deeplearning.ai/certificates/03976233-64c4-4195-a504-d5676a73f825) was checked in the browser on 14 November 2026: Kaan KAYA, this course, completion date November 14, 2026. Kaan reports final lab **30/30** and quiz **10/10**. No grade screen was independently inspected. Grade percentages are not agent-performance measurements.

Six notebooks and 22 standalone recordings are preserved locally, versus eleven listed labs. The public pages curate substantive analysis and selected visual evidence. M2 retains a `RateLimitError`; complete execution counts do not establish a clean run. [Environment gaps](ENVIRONMENT.md) and [publication exclusions](ATTRIBUTION.md) remain explicit.

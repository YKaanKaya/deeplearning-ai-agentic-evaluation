# Lab 1: Evaluate What the Agent Does

[Course lesson](https://learn.deeplearning.ai/courses/evaluating-and-improving-agentic-applications/lesson/ldijcwt7i/lab-1%3A-evaluate-what-the-agent-does) · M5-07

Status: four existing recordings inspected on 14 November 2026. This audit did not execute the lab. The recording UI calls this practice exercise **“Fix a Failure and Test the Result”**; its original syllabus title and folder are retained.

## Objective and method

The recordings show an evaluation cycle for unsupported product claims: define three targeted failure cases and three known-good cases; establish a baseline; add a strict grounding rule in v2; compare a narrower rule in v3; and test a catalog-data intervention. Six evaluation dimensions appear: tool selection, tool invocation, outcome, identity before refund, policy compliance, and response grounding.

The acceptance check in the final recording requires all three failure cases to be grounded, no known-good evaluator regressions, and at most one extra tool call per known-good case. The recorded comparison selects v2 for this lab. This is an educational decision on six cases, not a production release recommendation.

## Files and structure

The four source GIFs are present locally in this folder. Each is 1920 × 1080. Frame numbers below are zero-based.

| Local source artifact | Frames / duration | Evidence locator |
| --- | --- | --- |
| `M5_01_Build_Test_Datasets.gif` | 5 / 18.5 s | Frame 1 shows the two three-case sets, generated 11 November 2026, 11:08:44 UTC. |
| `M5_02_Baseline_Evaluation.gif` | 4 / 24 s | Frame 1 shows all six baseline rows; frames 2–3 show Phoenix results and a grounding failure. |
| `M5_03_Prompt_Rule_Comparison.gif` | 3 / 21 s | Frame 1 shows baseline/v2 responses and evaluator labels; frame 2 shows known-good case comparisons. |
| `M5_04_Data_Fix_and_Final_Comparison.gif` | 7 / 46 s | Frame 0 shows the data comparison; frames 3–4 show Phoenix regression evidence; frame 6 shows the final summary. |

No practice notebook, helper modules, database, environment export, raw experiment tables, or before/after script baseline was found in this module. Names visible in recordings, such as `task4b_v3.py` and `data_f.pkl`, identify hosted artifacts; they are not files supplied by this checkout. Reviewed publication media is indexed in the [artifact inventory](../../../docs/ARTIFACTS.json).

## Lab explanation

The failure set concerns merino care, hiking-shoe materials, and denim-jacket care. Known-good cases cover tee availability, an eligible refund, and an out-of-window refusal. Phoenix experiment labels distinguish `baseline-v1`, `grounding-rule-v2`, and `scoped-rule-v3`, with `failures` and `known-good` suffixes. These sets and six evaluators differ from the [graded notebook](../m5-graded-lab-improving-an-agent-with-evals/CAPTURE.md).

The practice grounding rubric treats a hedge or general-advice preface as insufficient support for care instructions. That differs from the graded notebook's rubric, which explicitly allows clearly labeled general advice. Scores across the two labs are not directly comparable.

## Saved final comparison

Source: `M5_04_Data_Fix_and_Final_Comparison.gif`, frame 6, with Phoenix corroboration in frames 3–4. The displayed percentages are rounded from three cases in each set.

| Version | Failure grounding | Known-good grounding | Known-good tool selection | Known-good outcome | Known-good policy | Known-good total calls | Known-good mean latency |
| --- | --- | --- | --- | --- | --- | --- | --- |
| v1 | 1/3 | 2/3 | 3/3 | 3/3 | 3/3 | 8 | 4.57 s |
| v2 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 | 8 | 4.78 s |
| v3 | 3/3 | 3/3 | 2/3 | 2/3 | 3/3 | 9 | 5.43 s |

The final terminal summary reports all 36 evaluator scores present for each version. The Phoenix view shows the v3 eligible-refund response asks for confirmation instead of processing the requested refund: outcome and tool selection score zero while grounding and policy score one. This is a concrete example of why groundedness does not establish task completion. v3 also makes three calls for tee availability, against one in v1/v2.

## Findings and debugging

The catalog-data comparison records denim 0→0, hiking-shoe materials 1→1, and merino 0→1, raising grounding from one to two of three cases. The final recording states that the merino catalog entry was unchanged and identifies its changed label as stochastic. It also preserves a judge explanation for the denim failure: the answer goes beyond the catalog's care steps. These observations do not show that the data change caused a grounding improvement.

The final recording describes a transport repair using Anthropic's `between_tools` thinking mode for structured extraction. Its supporting code, package versions, exception trace, and environment are absent locally, so the repair is recorded as a statement visible in the source, not a locally reproduced fix.

No evidence in these GIFs establishes that the separate graded notebook's row-position comparison was corrected. The graded notebook still contains that defect; its results are documented separately.

## Reproduction

Use the linked hosted course lesson for the original environment. No local install or execution command for this practice lab has been validated. Reproduction would require its original application, datasets, catalog/database, evaluator definitions, prompts, service configuration, and dependency versions. Latency values are single saved observations without repeated trials or confidence intervals; no monetary experiment cost was available in Phoenix.

## Publication review

The recordings contain course UI, prompts, and synthetic Northwind interactions. This document provides original analysis with attribution to DeepLearning.AI and Arize AI. Full course prompts, original solutions, and downloaded course files remain local. Selected Phoenix/table views may be curated as reviewed visual evidence; do not infer publication permission for the rest of the workspace from their inclusion. The inspected GIF frames do not display credential values or authenticated URLs.

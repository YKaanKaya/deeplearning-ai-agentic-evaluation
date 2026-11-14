# Module 5: Improving Agentic Applications

**Educational module notes** from DeepLearning.AI coursework, using the fictional Northwind Apparel scenario. Course exercises and results are learning examples rather than a production reliability assessment.

The final module connects targeted failure analysis, prompt experiments, regression checks, and production feedback. This educational summary draws on saved artifacts inspected on 14 November 2026.

## Problem, method, and implementation

Northwind's support agent can call the appropriate product tool and still add unsupported care advice. The workflow separates a targeted grounding failure set from known-good cases, evaluates both, compares prompt versions, and checks tool use, policy, outcomes, and latency before choosing a change. Representative production requests then become regression candidates.

The saved practice recordings and graded notebook are **different experiments**. The practice lab uses three failure cases and three known-good cases with six evaluators. The graded notebook uses five cases in each set and four evaluators. Their scores must not be combined.

| Evidence | What it supports | Limitation |
| --- | --- | --- |
| [Practice capture](labs/lab-1-evaluate-what-the-agent-does/CAPTURE.md) | Four recordings show dataset creation, baseline evaluation, prompt comparison, and the final regression check. The final practice comparison favors v2 under that lab's acceptance criterion. | Recordings preserve selected views; the supporting practice scripts, tables, and environment were not downloaded here. |
| [Graded capture](labs/m5-graded-lab-improving-an-agent-with-evals/CAPTURE.md) | A saved executed notebook contains three passing test outputs, six experiment tables, five simulated production requests, and two appended regression cases. | The original comparison aligns rows by position. Joining the saved raw tables by case identity removes its apparent v3 improvement. |

## Observed results and lessons

- In the **practice recording**, v2 grounds all three failure cases and retains all three known-good outcomes with eight total known-good tool calls. v3 also grounds all three failure cases but completes only two of the three known-good outcomes and uses nine calls. The refund comparison makes the difference visible: a policy-compliant, grounded answer can still leave the requested refund unfinished.
- In the **graded notebook's raw result tables**, all three versions ground the same three of five failure cases. Its row-position comparison incorrectly presents a merino improvement and hiking-shoe regression when v3's row order changes. Case identity must survive asynchronous execution and comparison.
- A recorded catalog-data experiment improves one of three grounding labels, but the final recording explicitly identifies the merino change as stochastic because that catalog entry did not change. This is not evidence of a causal data improvement.
- Production-shaped questions expose coverage gaps. The graded notebook adds two representative requests to the failure dataset, increasing it from five to seven cases. A useful regression candidate need not have failed every evaluator.

These are small educational samples, not estimates of production reliability. The practice and graded grounding rubrics also differ in their treatment of general advice. Revalidate judges against representative human-reviewed labels when behavior changes. Tool counts and recorded latency describe operational tradeoffs; neither recording nor notebook establishes a dollar cost saving.

See [central results and source locators](../docs/RESULTS.md) and the [artifact inventory](../docs/ARTIFACTS.json). Course notebooks, slides, and solution cells remain local; this publication contains original analysis and reviewed visual evidence, with course attribution.

## Runnable technical companion

The independent [Module 5 source](../technical_companion/m5_compare.py) takes Module 4 score vectors for the same cases in two versions and produces identity-paired layer regressions and a gate decision. [Follow the code, data handoff and recorded output](../docs/TECHNICAL_WALKTHROUGH.md#module-5).

This deterministic $42 demo was authored during publication with AI assistance. Its outputs are separate from the saved course runs and Phoenix recordings discussed above.

## Published learning material

| Resource | What to explore |
| --- | --- |
| [Lab 1: Evaluate What the Agent Does](labs/lab-1-evaluate-what-the-agent-does/CAPTURE.md) | Lab analysis of saved visual evidence |
| [M5 Graded Lab: Improving an Agent with Evals](labs/m5-graded-lab-improving-an-agent-with-evals/CAPTURE.md) | Lab analysis of saved notebook outputs |

For the full teaching sequence, use the [official course](https://www.deeplearning.ai/courses/evaluating-and-improving-agentic-applications). This repository presents selected educational explanations and saved evidence, rather than a complete set of lecture notes.

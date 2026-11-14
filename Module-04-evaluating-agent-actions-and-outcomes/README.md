# Module 4: Evaluating Agent Actions and Outcomes

**Educational module notes** from DeepLearning.AI coursework, using the fictional Northwind Apparel scenario. Course exercises and results are learning examples rather than a production reliability assessment.

Original synthesis from saved local artifacts, reviewed on 14 November 2026. This review did not run the labs or verify unseen lectures.

## What this module demonstrates

An agent can produce a plausible answer while selecting the wrong tool, supplying incorrect arguments or failing to make the requested state change. This module separates those questions by reconstructing ordered tool trajectories and evaluating selection, invocation, refund outcomes and policy compliance independently.

The saved assignment contains completed exercise regions for required-tool coverage, expected-argument checks and identity-before-refund ordering. Phoenix annotations bring those layers back to the corresponding traces. The agent, database and surrounding lab workflow are course-provided.

## Observed evidence

The saved graded run contains 12 agent runs and 15 tool calls. All 20 code cells have execution counts, three exercise-test outputs pass, and no error output remains.

| Evaluation layer | Saved result |
| --- | --- |
| Required tool selection | 6 failures / 12 cases |
| Expected tool arguments | 8 failures / 12 cases |
| Refund outcome | 1 failure / 12 cases |
| LLM policy judgment | 11 compliant, 1 non-compliant |
| Phoenix logging | 5 annotations per span |

These layers measure different properties. The identity rule passes when no refund is attempted, so that pass does not prove task completion. The argument checker applies the lab's declared tool names and argument keys; its failure count is not a general measure of all possible valid tool strategies. The saved refund check consults shared database state; the database itself was not downloaded into this capture.

![Layered Phoenix annotations](../assets/m4-layered.gif)

*Compare the same request across action, argument, outcome and policy annotations. A passing layer can coexist with a failure elsewhere in the workflow.*

## Artifacts and limits

Local-only original: `labs/m4-graded-lab-multi-layer-agent-evaluation/C1M4_Assignment.ipynb`. Five practice walkthrough GIFs and four graded Phoenix GIFs are present. See the [artifact manifest](../docs/ARTIFACTS.json), [saved results](../docs/RESULTS.md) and [environment limits](../docs/ENVIRONMENT.md).

No runnable practice notebook, course helper tree, database snapshot or dependency lock is present. The media demonstrates a separate practice capture; its numbers should not be substituted for the graded notebook's results. No platform grade or new rerun is claimed.

## Runnable technical companion

The independent [Module 4 source](../technical_companion/m4_outcomes.py) takes a benchmark expectation and its replayed run and produces separate tool, ordering, policy and outcome checks. [Follow the code, data handoff and recorded output](../docs/TECHNICAL_WALKTHROUGH.md#module-4).

This deterministic $42 demo was authored during publication with AI assistance. Its outputs are separate from the saved course runs and Phoenix recordings discussed above.

## Published learning material

| Resource | What to explore |
| --- | --- |
| [Lab 1: Evaluate What the Agent Does](labs/lab-1-evaluate-what-the-agent-does/CAPTURE.md) | Lab analysis of saved visual evidence |
| [M4 Graded Lab: Multi-Layer Agent Evaluation](labs/m4-graded-lab-multi-layer-agent-evaluation/CAPTURE.md) | Lab analysis of saved notebook outputs |

For the full teaching sequence, use the [official course](https://www.deeplearning.ai/courses/evaluating-and-improving-agentic-applications). This repository presents selected educational explanations and saved evidence, rather than a complete set of lecture notes.

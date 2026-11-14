# Module 5: Improving Agentic Applications

The final module connects targeted failure analysis, prompt experiments, regression checks, and production feedback. This page summarizes the saved artifacts inspected on 14 November 2026; it does not claim that the placeholder lecture notes below have been reviewed.

## Problem, method, and implementation

Northwind's support agent can call the appropriate product tool and still add unsupported care advice. The workflow separates a targeted grounding failure set from known-good cases, evaluates both, compares prompt versions, and checks tool use, policy, outcomes, and latency before choosing a change. Representative production requests then become regression candidates.

The saved practice recordings and graded notebook are **different experiments**. The practice lab uses three failure cases and three known-good cases with six evaluators. The graded notebook uses five cases in each set and four evaluators. Their scores must not be combined.

| Evidence | What it supports | Limitation |
| --- | --- | --- |
| [Practice capture](labs/lab-1-evaluate-what-the-agent-does/CAPTURE.md) | Four recordings show dataset creation, baseline evaluation, prompt comparison, and the final regression check. The final practice comparison favors v2 under that lab's acceptance criterion. | Recordings preserve selected views; the supporting practice scripts, tables, and environment were not downloaded here. |
| [Graded capture](labs/m5-graded-lab-improving-an-agent-with-evals/CAPTURE.md) | A saved executed notebook contains three passing test outputs, six experiment tables, five simulated production requests, and two appended regression cases. | The original comparison aligns rows by position. Joining the saved raw tables by case identity removes its apparent v3 improvement. |
| [Quiz record](notes/09-module-5-quiz.md) | The learner reports 10/10 on 14 November 2026. | No grade screenshot was present in this module. |

## Observed results and lessons

- In the **practice recording**, v2 grounds all three failure cases and retains all three known-good outcomes with eight total known-good tool calls. v3 also grounds all three failure cases but completes only two of the three known-good outcomes and uses nine calls. The refund comparison makes the difference visible: a policy-compliant, grounded answer can still leave the requested refund unfinished.
- In the **graded notebook's raw result tables**, all three versions ground the same three of five failure cases. Its row-position comparison incorrectly presents a merino improvement and hiking-shoe regression when v3's row order changes. Case identity must survive asynchronous execution and comparison.
- A recorded catalog-data experiment improves one of three grounding labels, but the final recording explicitly identifies the merino change as stochastic because that catalog entry did not change. This is not evidence of a causal data improvement.
- Production-shaped questions expose coverage gaps. The graded notebook adds two representative requests to the failure dataset, increasing it from five to seven cases. A useful regression candidate need not have failed every evaluator.

These are small educational samples, not estimates of production reliability. The practice and graded grounding rubrics also differ in their treatment of general advice. Revalidate judges against representative human-reviewed labels when behavior changes. Tool counts and recorded latency describe operational tradeoffs; neither recording nor notebook establishes a dollar cost saving.

See [central results and source locators](../docs/RESULTS.md) and the [artifact inventory](../docs/ARTIFACTS.json). Course notebooks, slides, and solution cells remain local; this publication contains original analysis and reviewed visual evidence, with course attribution.

## Lesson index

The index follows the syllabus observed on 4 November 2026. Lecture-note capture status is independent of course completion and of the artifact audit above.

| # | Lesson | Format | Capture status |
| --- | --- | --- | --- |
| 01 | [Planning an Improvement Test](notes/01-planning-an-improvement-test.md) | Video | Pending verification |
| 02 | [Comparing Versions and Assessing Tradeoffs](notes/02-comparing-versions-and-assessing-tradeoffs.md) | Video | Pending verification |
| 03 | [Choosing Where to Intervene](notes/03-choosing-where-to-intervene.md) | Video | Pending verification |
| 04 | [Refining a Change After a Regression](notes/04-refining-a-change-after-a-regression.md) | Video | Pending verification |
| 05 | [Improving Agents After Deployment](notes/05-improving-agents-after-deployment.md) | Video | Pending verification |
| 06 | [Turning Production Failures into Regression Tests](notes/06-turning-production-failures-into-regression-tests.md) | Video | Pending verification |
| 07 | [Lab 1: Evaluate What the Agent Does](labs/lab-1-evaluate-what-the-agent-does/CAPTURE.md) | Code Example | Saved recordings inspected |
| 08 | [M5 Graded Lab: Improving an Agent with Evals](labs/m5-graded-lab-improving-an-agent-with-evals/CAPTURE.md) | Graded・Code Assignment | Saved notebook outputs inspected; grade learner-reported |
| 09 | [Module 5 Quiz](notes/09-module-5-quiz.md) | Graded・Quiz | 10/10 learner-reported |
| 10 | [Module 5 Resources](notes/10-module-5-resources.md) | Reading | Pending verification |
| 11 | [Acknowledgments](notes/11-acknowledgments.md) | Reading | Pending verification |

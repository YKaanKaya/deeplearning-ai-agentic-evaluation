# M4 Graded Lab: Multi-Layer Agent Evaluation

[Course lesson](https://learn.deeplearning.ai/courses/evaluating-and-improving-agentic-applications/lesson/cno79gi0z/m4-graded-lab%3A-multi-layer-agent-evaluation) · M4-08

Status: saved notebook and four Phoenix GIFs inspected on 14 November 2026; no new execution or platform-grade verification.

## Problem and implementation

Evaluate the actions behind the response as well as the outcome. The notebook groups tool spans by parent agent run, orders them by start time and constructs trajectories containing tools, arguments and results. Completed exercise regions implement required-tool selection, expected-argument comparison and identity-before-refund ordering. The course supplies the agent, seeded database and surrounding workflow.

## Saved results

Local-only original: `C1M4_Assignment.ipynb` (57 cells; 20 code cells, all with execution counts and no retained error outputs). Cell 18 reports 12 agent runs and 15 tool calls. Three exercise tests pass at cells 26, 30 and 50; these are not assignment grades.

| Zero-based cell | Layer | Saved result |
| --- | --- | --- |
| 32 | Required tool selection | 6 failures / 12 |
| 32 | Expected arguments | 8 failures / 12 |
| 36 | Refund outcome | 1 failure / 12 |
| 48 | LLM policy compliance | 11 compliant; 1 non-compliant |
| 53 | Phoenix annotation logging | 5 annotations per span |

Cell 55 displays the combined scores. One request can pass the outcome and identity rules while receiving a non-compliant policy judgment. A different return request has no refund call and fails the expected-outcome layer.

## Interpretation and limits

Selection checks whether all required tools occur. Invocation checks the declared keys on the first matching call and leaves missing-tool detection to selection. An identity check that is not engaged passes; that is not evidence that identity was verified or the task completed. These semantics matter when interpreting the aggregate counts.

The outcome check consults the shared refunds table and the trace's refund calls. The database snapshot is absent, so the saved notebook is the evidence for this result; state changes cannot be independently inspected now. A future extension could tie persistent records to exact run IDs and inspect alternate valid tool strategies.

Metadata records Python 3.11.13. Four `M4_*.gif` files show Phoenix trace inspection, tool calls, evaluation results and layered annotations. The course helper modules, agent package and dependency lock are absent. The notebook and solutions remain local-only; no local rerun is claimed. See [the artifact manifest](../../../docs/ARTIFACTS.json), [saved results](../../../docs/RESULTS.md) and [environment documentation](../../../docs/ENVIRONMENT.md).

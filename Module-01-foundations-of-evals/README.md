# Module 1: Foundations of Evals

Original synthesis from saved local artifacts, reviewed on 14 November 2026. This review did not run the labs or verify unseen lectures.

## What this module demonstrates

A final answer hides the work that produced it. The saved labs expose Northwind Apparel's agent requests, model calls and tools as linked spans, first with a small Python tracer and then with Phoenix.

The Python walkthrough records parent/child relationships, timing, inputs, outputs and errors, and sanitizes serialized trace data. The graded assignment contains completed exercise implementations for tracer registration, tool instrumentation and a traced agent entry point. The agent and its ecommerce tools are provided by the course; no baseline diff establishes authorship of every surrounding cell.

## Observed evidence

- Two local notebooks and two screenshot-based GIFs are present. The Python walkthrough has 16 executed code cells and no retained error outputs; an intentionally failing tool is caught and recorded as a span.
- Its saved analysis covers seven agent questions, with 15 model calls, 11 tool calls and zero recorded span errors. This is a small lab observation, not an agent quality benchmark.
- The graded notebook retains three passing exercise-test outputs. Its final Phoenix-link cell is unexecuted; the notebook does not establish a platform grade.

![Phoenix trace walkthrough](../assets/m1-tracing.gif)

*Follow an agent request into its child tool spans. Tracing makes the supporting work inspectable; a trace without an error does not establish a correct answer.*

## Artifacts and limits

Local-only originals: `labs/lab-1-trace-an-agent-with-python/local_traces_walkthrough.ipynb` and `labs/m1-graded-lab-tracing-the-northwind-apparel-agent-with-phoenix/C1M1_Assignment.ipynb`. The Phoenix practice lab has media but no saved notebook. Their paths and hashes belong in the [artifact manifest](../docs/ARTIFACTS.json).

The imported agent package, helper modules, trace JSON files and dependency lock are absent from this capture. No local rerun is claimed. See [environment limits](../docs/ENVIRONMENT.md) and the lab captures below. Lesson-note templates remain explicitly incomplete.

## Lesson index

The syllabus order follows the course capture of 4 November 2026. Documentation status is independent of platform completion.

| # | Lesson | Format | Capture status |
| --- | --- | --- | --- |
| 01 | [A conversation between Laurie Voss and Andrew Ng](notes/01-a-conversation-between-laurie-voss-and-andrew-ng.md) | Video | Transcript notes drafted |
| 02 | [Why Evals Matter](notes/02-why-evals-matter.md) | Video | Pending verification |
| 03 | [The Evals Process Part 1](notes/03-the-evals-process-part-1.md) | Video | Pending verification |
| 04 | [The Evals Process Part 2](notes/04-the-evals-process-part-2.md) | Video | Pending verification |
| 05 | [Traces](notes/05-traces.md) | Video | Pending verification |
| 06 | [Reading Lab 1: How Tracing Works](notes/06-reading-lab-1-how-tracing-works.md) | Reading | Pending verification |
| 07 | [Lab 1: Trace an Agent with Python](labs/lab-1-trace-an-agent-with-python/CAPTURE.md) | Code Example | Saved notebook inspected |
| 08 | [Lab 2: Trace an Agent with Phoenix](labs/lab-2-trace-an-agent-with-phoenix/CAPTURE.md) | Code Example | Media only; notebook absent |
| 09 | [Join the Deeplearning.AI Forum!](notes/09-join-the-deeplearning-ai-forum.md) | Reading | Pending verification |
| 10 | [M1 Graded Lab: Tracing the Northwind Apparel Agent with Phoenix](labs/m1-graded-lab-tracing-the-northwind-apparel-agent-with-phoenix/CAPTURE.md) | Graded・Code Assignment | Saved notebook inspected |
| 11 | [Module 1 Quiz](notes/11-module-1-quiz.md) | Graded・Quiz | Pending verification |
| 12 | [Module 1 Resources](notes/12-module-1-resources.md) | Reading | Pending verification |

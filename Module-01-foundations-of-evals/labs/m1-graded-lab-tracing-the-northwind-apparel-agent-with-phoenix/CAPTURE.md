# M1 Graded Lab: Tracing the Northwind Apparel Agent with Phoenix

[Course lesson](https://learn.deeplearning.ai/courses/evaluating-and-improving-agentic-applications/lesson/nap9iymg/m1-graded-lab%3A-tracing-the-northwind-apparel-agent-with-phoenix) · M1-10

Status: saved notebook and Phoenix GIF inspected on 14 November 2026; no new execution or platform-grade verification.

## Problem and method

Connect the course's database-backed Northwind agent to Phoenix, instrument its tools and agent entry point, and inspect the relationship between the final response and the work that produced it.

## Saved implementation and results

Local-only original: `C1M1_Assignment.ipynb` (57 cells; 22 code cells). Completed exercise regions define tracer registration, tool instrumentation and a traced `ask_agent` entry point. The agent package, data model and assignment scaffolding are course-provided; no saved baseline diff establishes authorship of every surrounding cell.

Twenty-one code cells have execution counts and no retained error outputs are present. The three exercise-test outputs at zero-based cells 27, 41 and 50 say all tests passed. Cell 53 retains the batch responses and tool lists. The last Phoenix-link cell, 55, has no execution count. Passing these tests is not a course grade or a measured agent performance score.

Cell 43 records `claude-haiku-4-5-20251001`, temperature 0.0 and `weak_prompt_mode=False`. Notebook metadata records Python 3.11.13. `M1_Phoenix_Lab_Walkthrough.gif` contains seven captioned Phoenix screenshots of the tracing workflow.

## Reproduction and publication

The agent package, `utils`, `unittests`, dependency versions and database snapshot are absent from this local capture. There is no newly tested local installation or rerun. The assignment notebook and solutions remain local-only; the public module summary explains the method and links selected Phoenix media. See [the artifact manifest](../../../docs/ARTIFACTS.json) and [environment documentation](../../../docs/ENVIRONMENT.md).

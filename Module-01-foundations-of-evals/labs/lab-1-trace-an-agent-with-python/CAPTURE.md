# Lab 1: Trace an Agent with Python

[Course lesson](https://learn.deeplearning.ai/courses/evaluating-and-improving-agentic-applications/lesson/3sxuzjlf/lab-1%3A-trace-an-agent-with-python) · M1-07

Status: saved notebook inspected on 14 November 2026; no new execution.

## Problem and method

The walkthrough makes the Northwind agent's internal work observable without a tracing service. A small Python tracer records linked chain, model and tool spans, propagates the current span through context variables, records timing and exceptions, and sanitizes values when displaying or saving them.

## Saved implementation and outputs

The local-only original is `local_traces_walkthrough.ipynb`: 35 cells, including 16 code cells, all with execution counts and no retained notebook error output. Cells 6-14 define the tracer; cells 16 and 18 exercise nested spans and a deliberately failing tool. That failure is caught, printed and saved rather than left as an unhandled notebook error.

Cells 23-27 attach the tracer to ten tools, the model client and the full agent request. Cell 25 records `model_name="claude-haiku-5-5"`, `temperature=0.0`, and clearing prerecorded fixtures. Those are saved code settings, not independent verification of the remote service used.

Cell 33 summarizes seven questions: 15 model calls, 11 tool calls and zero recorded span errors. The trace filenames contain run prefix `20261104T122437Z_c1b9aa6a`; their JSON files are absent from this folder. The final responses and low trace-error count do not establish evaluation quality or task success.

## Attribution, reproduction and limits

The course supplies the walkthrough and Northwind agent. This capture does not contain a baseline diff identifying every learner change. It also lacks `apparel-shop-agent/`, `dlai_utils.py`, `trace_display.py`, the referenced requirements file and saved trace JSON. Notebook metadata records Python 3.12.16. `ANTHROPIC_API_KEY` is required by name; no credential value is recorded here.

The artifact is evidence of saved execution state, not a newly reproduced local run. See [the artifact manifest](../../../docs/ARTIFACTS.json) and [environment limits](../../../docs/ENVIRONMENT.md). The notebook remains local-only; the public repository provides original analysis and course links.

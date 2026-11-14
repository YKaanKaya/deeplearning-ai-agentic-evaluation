# Lab 1: Build the Northwind Benchmark

[Course lesson](https://learn.deeplearning.ai/courses/evaluating-and-improving-agentic-applications/lesson/i1bmo7ob/lab-1%3A-build-the-northwind-benchmark) · M2-06

Status: saved capture archive and standalone GIF inspected on 14 November 2026; no runnable notebook or new execution.

## Problem and method

Turn observed Northwind failures into traceable regression cases. The capture documents root-span extraction, expanding a question bank, reviewing actual answers, separating failure category from severity, curating synthetic coverage and retaining each saved output with its source span ID.

## Available artifacts and observed results

The local-only `M2_Northwind_Benchmark_Capture.zip` contains a learning-capture README, curation and labeling notes, four-case `benchmark.json`, six screenshots, a poster, a GIF, a storyboard and GIF assembly code. The standalone `M2_Northwind_Benchmark_Walkthrough.gif` is also present. The archive is a companion to the course workspace rather than a complete application export.

Its README records 43 Phoenix traces: 15 initial, 21 expanded-bank and seven curated synthetic runs. The generator returned 23 candidates. The manual worksheet has 14 entries and the synthetic worksheet seven. The final four failures are all scope violations: two manual/low severity and two synthetic/medium severity. These are capture-recorded counts; the live Phoenix workspace was not rechecked during this publication review.

The four final benchmark entries have distinct span IDs. The labeling notes describe correcting repeated-query provenance so each worksheet entry matched its own ordered response rather than the latest response to that text.

## Interpretation and limitations

Annotation and query curation were AI-assisted. The notes retain disagreements: grounding-safe wedding and size-fragment answers may still be unhelpful, and a delivery answer's assumed checkout workflow is debatable. A pass under this narrow taxonomy is not proof of retrieval relevance or task completion.

This failures-only, deliberately curated sample cannot estimate production prevalence. Its counts are separate from those of the Module 2 graded assignment. No runnable practice notebook, dependency lock or agent/helper tree was downloaded into this folder. Originals remain local-only; see [the artifact manifest](../../../docs/ARTIFACTS.json) and [environment limits](../../../docs/ENVIRONMENT.md).

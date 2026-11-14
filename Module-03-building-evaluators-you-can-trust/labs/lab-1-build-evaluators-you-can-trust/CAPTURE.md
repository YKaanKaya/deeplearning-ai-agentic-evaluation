# Lab 1: Build Evaluators You Can Trust

[Course lesson](https://learn.deeplearning.ai/courses/evaluating-and-improving-agentic-applications/lesson/8bh609rg/lab-1%3A-build-evaluators-you-can-trust) · M3-06

Status: walkthrough media inspected on 14 November 2026; no saved practice notebook or new execution.

## Available evidence and method

`M3_Evaluators_Full_Walkthrough.gif` contains seven captioned frames showing a six-step workflow: inspect labeled examples, create development/validation/test splits, build a catalog check, apply a correctness judge, define a policy rubric and validate/refine the custom judge.

The screenshots show a hosted notebook and its results. The workflow illustrates why deterministic checks and LLM judgments should be inspected against explicit reference labels. No practice notebook, exported labeled table or helper tree is available to independently reconstruct or verify its numeric results, so those screenshot figures are not used as this project's primary reported measurements.

## Interpretation and limits

A rubric needs validation, and an apparent judge/reference disagreement can reveal either an evaluator problem or an annotation problem. Changing the references changes the comparison; it does not itself improve the model. Keep final held-out data separate from rubric iteration.

This practice capture is separate from the graded assignment. Its GIF is an edited screenshot sequence, not proof of a fresh, uninterrupted run. The media includes course notebook content and remains local-only. See [the artifact manifest](../../../docs/ARTIFACTS.json) and [environment limits](../../../docs/ENVIRONMENT.md). No tested local setup is claimed.

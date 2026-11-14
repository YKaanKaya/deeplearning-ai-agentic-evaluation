# A conversation between Laurie Voss and Andrew Ng

Source: [Opening lesson](https://learn.deeplearning.ai/courses/evaluating-and-improving-agentic-applications/lesson/53tpudpi/a-conversation-between-laurie-voss-and-andrew-ng)

Captured: 4 November 2026. Basis: the full transcript exposed by the course page. These are original paraphrased study notes. Video viewing by the learner and course completion are not verified by this capture.

## Main idea

Evaluation turns an informal sense of whether an agent works into explicit criteria that can guide improvement. A convincing prototype can be built through quick iterations, but dependable performance requires a repeatable way to identify failures and verify changes.

## What the lesson establishes

- **Match evaluation rigor to project maturity.** Early manual inspection can reveal obvious problems quickly. As recurring weaknesses become clear, introduce focused test cases and more systematic measurement. The discussion does not prescribe one fixed dataset size for every project.
- **Start with observable behavior.** Traces expose the sequence of activity, including tool use and intermediate outcomes. They provide the evidence needed to diagnose failures that a final answer can conceal.
- **Define success in application terms.** Developers and domain experts must state what acceptable behavior means. A model cannot reliably infer every business preference or constraint.
- **Develop evaluators iteratively.** Human review identifies failures and missing test coverage. Code checks and model-based judges can then scale assessment, but their reliability also needs to be checked.
- **Use evaluation to guide changes.** Establish a baseline, make a change, and inspect whether the change actually helps. Continue learning from real usage after deployment.
- **Keep human judgment in the loop.** Agents may help generate hypotheses and improvements, but the discussion emphasizes their need for steering and context when defining or diagnosing quality.

## Working method to carry into the labs

1. Inspect real traces and identify a concrete failure.
2. Express the intended behavior as a testable requirement.
3. Add a representative case and an appropriate evaluation rule.
4. Check that the evaluator reflects human judgment.
5. Compare an intervention against the baseline and inspect regressions.
6. Feed newly observed failures back into the evaluation set.

This is a synthesis of the opening discussion, not a claim that the full procedure has already been implemented.

## My application connection — proposed, not yet tested

For a business-question agent such as BIEaaS, an answer that sounds plausible may still be wrong because of the SQL, business context, chosen tools, or interpretation. A useful extension would evaluate those layers separately and link each result to the trace that produced it. This is a project idea based on the learner's existing work, not a course result.

## Questions to resolve in later lessons

- What trace information is enough to diagnose a failure?
- How should human-labeled cases be selected and expanded?
- How do we establish whether a model-based judge is dependable?
- Which measurements distinguish an improved agent from a changed score?

## Evidence

Transcript reviewed; no notebook, code execution, measured result, or completed assessment is associated with this lesson capture.

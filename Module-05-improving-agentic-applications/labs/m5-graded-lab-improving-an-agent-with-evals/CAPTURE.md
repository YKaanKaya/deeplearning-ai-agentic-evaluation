# M5 Graded Lab: Improving an Agent with Evals

[Course lesson](https://learn.deeplearning.ai/courses/evaluating-and-improving-agentic-applications/lesson/79ywr27/m5-graded-lab%3A-improving-an-agent-with-evals) · M5-08

Status: the locally saved `C1M5_Assignment.ipynb` was inspected on 14 November 2026. All 35 code cells have execution counts, three test cells report passing, and there are no saved error outputs. This audit did not rerun the notebook. The learner reports a final assignment grade of **30/30 on 14 November 2026**; that grade was not independently checked in the platform UI and is not an agent performance score.

## Objective and method

The notebook starts from a product-care response containing unsupported detail, defines policy and grounding classifiers, runs v1/v2/v3 on targeted failures and known-good cases, evaluates five simulated production requests, logs annotations to Phoenix, and appends two production-shaped requests to the offline dataset. Deterministic tool checks complement the LLM judges.

## Files and structure

The original notebook remains unchanged and local. It contains 81 cells, including 35 code cells. Its inspected SHA-256 is `b933579d4819986a7492b35706c33d93cc174febedd8041d3b58695aac6e3526`. See the [artifact inventory](../../../docs/ARTIFACTS.json) for provenance.

No supporting `utils.py`, `unittests.py`, dataset export, package lock, database, full workspace baseline, or runtime export was found in this module. Saved notebook outputs establish what was preserved; they do not supply a complete executable local checkout.

## Lab explanation

Cell locators below are **zero-based notebook cell indices**, independent of execution counts.

| Cells | Implementation or saved output |
| --- | --- |
| 19–30 | Tool selection/invocation checks and policy/grounding LLM evaluators. |
| 28, 47, 66 | Three saved “All tests passed!” outputs. |
| 32, 34, 36 | Five failure examples, five known-good examples, and Phoenix dataset registration. |
| 39, 41, 43, 46, 50 | Prompt variants and experiment orchestration; six experiment runs are saved. |
| 53 | Raw per-case experiment tables, before the defective comparison. |
| 55, 57 | Row-position comparison and latency/tool-call comparison. |
| 60, 65, 68 | Five simulated production requests and their saved policy/grounding labels. |
| 72 | Five production spans matched; five policy and five grounding annotations logged. |
| 75, 79 | Two regression candidates appended; failure dataset grows from five to seven. |

The saved experiment labels are `failures_v1`, `known_good_v1`, `failures_v2`, `known_good_v2`, `failures_v3`, and `known_good_v3`. Cell 50's Phoenix URLs identify local experiment IDs 2–7; these localhost links are not public reproducibility endpoints. A separate test experiment is ID 1.

## Observed results after matching case identity

Cell 53 outputs 1/3/5/7/9/11 hold the v1 failure/known-good, v2 failure/known-good, and v3 failure/known-good tables respectively. Matching by the printed `case` labels yields:

| Failure case | v1 grounding | v2 grounding | v3 grounding |
| --- | --- | --- | --- |
| raincoat waterproofing | 1 | 1 | 1 |
| beanie care | 0 | 0 | 0 |
| denim jacket care | 1 | 1 | 1 |
| hiking shoes materials | 1 | 1 | 1 |
| merino wool care | 0 | 0 | 0 |

Each version therefore grounds **3/5 failure cases**, selects the required tools on **2/5**, and receives policy/invocation passes on **5/5**. All three known-good tables show grounding and tool selection passes on **4/5**, policy/invocation passes on **5/5**, and **seven total tool calls**. The failed known-good tool-selection case is the eligible refund; the ungrounded known-good case is order status. These results do not establish a prompt-version improvement.

Cell 57 reports known-good mean latencies of 1.38 s, 0.20 s, and 0.21 s for v1/v2/v3. Aggregate means survive row reordering, but several displayed per-case latency assignments do not. The underlying agent/helper implementation is missing, some printed timings are zero, and there were no repeated trials. These figures do not establish a model speedup or cost saving.

The production table in cell 68 labels **5/5 requests compliant** and **4/5 grounded**; the hoodie request is ungrounded. Several grounded replies ask for missing information or decline to provide care details without a lookup, illustrating why a grounding pass does not establish task success. The two appended requests are coverage additions, not proof of two failed grounding judgments.

## Findings and debugging

Cell 55 assigns each version's metric series to a baseline table by row index. In cell 53, v3 puts merino before hiking-shoe materials; v1/v2 put hiking-shoe materials first. The comparison consequently presents a false merino improvement and hiking-shoe regression. Cell 57 uses the same row-position pattern for known-good cost comparisons, whose case order also changes. The raw tables above are interpreted by case identity; no original notebook cells were edited in this publication audit.

The invocation evaluator checks arguments on calls that exist and skips missing calls; missing required tools are measured separately by tool selection. Its 5/5 invocation scores must therefore be read alongside the 2/5 failure-set tool-selection scores. The grounding rubric permits clearly labeled general advice, while the separate practice rubric is stricter, so the two labs' grounding percentages are not interchangeable.

These findings concern the saved artifact. No corrected graded notebook or subsequent measured run was found. The original notebook's passing implementation tests and the learner's assignment grade do not validate the correctness of every analytical comparison.

## Reproduction

The notebook metadata records Python **3.11.13**. Imports include Phoenix, pandas, `utils`, and `unittests`; package versions are not recorded. Cell 9 configures the judge as provider `anthropic`, model `claude-sonnet-4-6`, and names offline/production Phoenix projects. This does not establish the underlying support-agent model, which is hidden behind the missing helper.

The course names `ANTHROPIC_API_KEY`, `PHOENIX_API_KEY`, and `PHOENIX_COLLECTOR_ENDPOINT` as configuration variables. Values are not recorded here. The hosted course environment supplies supporting files and service setup; a local installation has not been tested. Preserve original cell order and relative imports when obtaining the full workspace. See [central results](../../../docs/RESULTS.md) for publication claims and limits.

## Publication review

Course notebook text, prompts, grading hints, and solution cells remain local. This public capture is original analysis with attribution to DeepLearning.AI and Arize AI. Credential-pattern and URL-query checks found no common credential tokens or temporary authenticated URLs in this notebook; that check does not supply redistribution rights. Do not infer a complete runnable or publicly licensed course implementation from this analysis.

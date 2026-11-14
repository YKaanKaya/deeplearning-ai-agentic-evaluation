# Capture workflow

## After every lesson

Read the video transcript or reading fully when available. Write original notes covering the central idea, the method, conditions where it helps, important caveats, the worked example and links to related labs. Record uncertainties and the learner's actual questions. Update the corresponding row in COURSE_PROGRESS.csv.

`transcript_reviewed` means the transcript was read. It does not mean the learner watched the video, mastered the topic or received a completion mark.

## Before each lab

1. Open the actual workspace and inspect its tree, notebook sections and dependencies.
2. Save an untouched copy if available without discarding work. Retain original names and directories.
3. Record the problem, inputs, proposed evaluation method and expected kind of output. Do not assume a result.

## During the lab

Run notebook cells in their intended order. Work through required exercises with the learner and explain the reasoning. Record failures and fixes. Keep learner-authored extensions separate from the course baseline. If rerunning from a fresh kernel is safe, use it to check hidden state dependencies; if it is not done, record that limitation.

## Save and download after the lab

1. Wait for running cells to finish and inspect outputs for errors and missing execution.
2. Save/checkpoint the notebook before exporting it.
3. Download the executed `.ipynb` with outputs. The platform's help currently describes File → Download as → Notebook (.ipynb); use the controls actually present in that lab.
4. Use the workspace file browser to collect helper modules, configuration without secrets, data files, assets and dependency files. The course help describes File → Open for finding those files. Prefer a complete workspace export when offered. Preserve directory nesting.
5. Export relevant traces, evaluation tables and plots when the application offers export. Record screenshot evidence only where useful and free of credentials/private information.
6. Store the workspace under `runs/<run-id>/workspace/`, unchanged in structure. Keep the untouched baseline under `original/` when one exists.
7. Verify what was actually downloaded. A notebook-only download is incomplete if it depends on missing helper files or datasets. Record unavailable components explicitly.
8. Complete RUN.md and update CAPTURE.md with results and explanations. Report partial or failed execution honestly.

## A run record must answer

- Which notebook, code revision and input dataset produced these results?
- Which Python/package versions, model identifier and settings were used?
- Which tests and evaluator rubric were applied, with what sample count and labels?
- Did all intended cells finish? Were errors, skipped sections or hidden state present?
- What improved, what regressed, and what remains uncertain?
- Which exact local files support each claim?

Record tokens, latency and cost only when measured or explicitly exported. Model-based runs can vary; do not turn a single run into a guaranteed result.

## Capture statuses

Keep review, note-taking, execution and download states independent. Suggested states:

| Field | States |
| --- | --- |
| review_status | not_verified, transcript_reviewed, reading_reviewed, reviewed_with_learner |
| notes_status | pending, drafted, reviewed |
| execution_status | not_applicable, pending, attempted_failed, partially_executed, executed_observed, clean_rerun_verified |
| download_status | not_applicable, pending, notebook_only, partial_workspace, workspace_verified |

Do not change a pending lab to complete merely because the platform displays a check mark.

## Preparing GitHub and the portfolio

Keep originals and raw runs locally as evidence. Select publishable files after checking their attribution, permissions and contents. Use the portfolio evidence register to connect each reported result to the notebook, run, configuration and figure that supports it. Describe personal extensions separately from guided course work.

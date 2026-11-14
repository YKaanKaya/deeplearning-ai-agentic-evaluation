# Portfolio evidence register

Publication audit: 14 November 2026. [Artifact hashes](ARTIFACTS.json), [detailed results](RESULTS.md), [media provenance](MEDIA.json).

| Public claim | Evidence | Limit |
| --- | --- | --- |
| Five modules, 51 syllabus items, 11 labs | course-outline.json, labs-index.json, COURSE_PROGRESS.csv | Syllabus counts; not verification that every lesson was reviewed |
| Six saved notebooks, 22 standalone GIFs | Local inventory and ARTIFACTS.json | Five lab notebooks missing; ZIP's six JPGs counted separately |
| Local tracing and Phoenix inspection | M1 notebooks and reviewed trace excerpt | No publication-time hosted execution |
| Benchmark curation | M2 notebook and separately captured archive | Retained RateLimitError; synthetic/manual samples are not production prevalence |
| Both policy judges .750 accuracy, kappa 0.400 on 12 test cases | M3 cells 73/74 | Small test; perfect intermediate score followed reference-label edits |
| Different evaluation layers expose different failures | M4 n=12 saved table | Overlapping checks, course-specific expected values |
| Graded prompt versions all 3/5 grounded when matched by identity | M5 cell 53 outputs 1/5/9 | Reanalysis of stored frames; original cell 55 positional table is misleading |
| Practice v3 can be grounded yet fail refund completion | Latest M5 GIF frames 3/4/6 | Separate 3+3-case snapshot, no raw practice notebook |
| Five production samples annotated; dataset grows 5 to 7 | M5 cells 68/72/79 | No subsequent 7-case run saved |
| Course completion on 14 November 2026 | Public DeepLearning.AI certificate checked in browser; Kaan KAYA and matching title/date | Confirms completion, not individual assignment scores |
| Final lab 30/30 and quiz 10/10 on 14 Nov 2026 | Explicit learner report | Grade screens not independently verified; not agent performance |
| Independent identity-alignment example passes | experiments/identity_alignment.py and executed synthetic notebook | Publication-time example with AI assistance, not an original course experiment |

The showcase keeps assignment grades separate, names course-provided work, explains evaluator reliability and exposes limitations near the measurements. Unseen lecture transcripts and personal reflections are not fabricated. Publication uses original summaries and reviewed Phoenix excerpts; third-party code and assessment solutions remain local.

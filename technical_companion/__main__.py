"""Run the cumulative teaching stages; optionally export their computed results."""

import argparse
import json
import platform

from .fixtures import CASES, JUDGE_LABELS, REFERENCE_LABELS
from .m1_trace import replay
from .m2_benchmark import REQUIRED_COVERAGE, build_benchmark
from .m3_evaluators import grounding_score, judge_agreement
from .m4_outcomes import evaluate_run
from .m5_compare import compare_versions


def build_report() -> dict:
    observed_runs = [replay(case, "baseline") for case in CASES]
    run = observed_runs[0]
    benchmark = build_benchmark(CASES, observed_runs)
    refund_case = benchmark["DEMO-REFUND"].case
    candidate_runs = {key: replay(entry.case, "candidate") for key, entry in benchmark.items()}
    baseline = {key: evaluate_run(entry.case, entry.observed_run) for key, entry in benchmark.items()}
    # Completion order differs; case identity, not position, is the join contract.
    candidate = {key: evaluate_run(benchmark[key].case, candidate_run)
                 for key, candidate_run in reversed(list(candidate_runs.items()))}
    covered = {entry.case.requirement for entry in benchmark.values()}
    return {
        "fixture_id": "synthetic-companion-v1",
        "scope": "Independent deterministic replay; not a course run or production measurement",
        "environment": {"python": platform.python_version(), "dependencies": "standard library only"},
        "module_1": {"case_id": run.case_id, "version": run.version,
                     "root_span_id": run.spans[0].span_id, "linked_spans": len(run.spans),
                     "tool_names": [span.name for span in run.tools],
                     "refund_records": len(run.state["refunds"])},
        "module_2": {"unique_cases": len(benchmark), "requirements_covered": len(covered),
                     "requirements_declared": len(REQUIRED_COVERAGE),
                     "source_span_ids": {key: entry.source_span_id for key, entry in benchmark.items()}},
        "module_3": {"structured_grounding": grounding_score(benchmark[run.case_id].observed_run),
                     "fixed_judge_agreement": judge_agreement(REFERENCE_LABELS, JUDGE_LABELS)},
        "module_4": {"case_id": refund_case.case_id, "version": "candidate",
                     "layers": evaluate_run(refund_case, candidate_runs[refund_case.case_id])},
        "module_5": compare_versions(baseline, candidate),
        "operations": {"baseline_tool_calls": sum(len(item.tools) for item in observed_runs),
                       "candidate_tool_calls": sum(len(item.tools) for item in candidate_runs.values()),
                       "timing": "Not measured; span duration values are invented fixtures"},
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Export the computed synthetic results as JSON")
    args = parser.parse_args()
    report = build_report()
    if args.json:
        print(json.dumps(report, indent=2))
        return
    trace, benchmark, evaluators, outcome, comparison = [report[f"module_{n}"] for n in range(1, 6)]
    print("Independent synthetic companion; not a course run or production measurement.")
    print(f"M1 trace: {trace['case_id']} baseline; {trace['linked_spans']} linked spans; "
          f"{trace['refund_records']} refund record(s)")
    print(f"M2 benchmark: {benchmark['unique_cases']} unique cases joined to source traces; "
          f"{benchmark['requirements_covered']}/{benchmark['requirements_declared']} declared requirements covered")
    agreement = evaluators["fixed_judge_agreement"]
    print(f"M3 evaluators: grounded={evaluators['structured_grounding']}; fixed judge labels match "
          f"{agreement['matched']}/{agreement['total']}; kappa={agreement['kappa']:.3f}")
    print("M4 candidate refund:", outcome["layers"])
    print(f"M5 paired outcomes: baseline={comparison['baseline_outcomes']}/{comparison['cases']}; "
          f"candidate={comparison['candidate_outcomes']}/{comparison['cases']}; "
          f"regressions={comparison['regressions']}; gate_passed={comparison['gate_passed']}")


if __name__ == "__main__":
    main()

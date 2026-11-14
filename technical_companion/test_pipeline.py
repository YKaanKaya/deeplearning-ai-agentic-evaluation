"""Behavior checks for the independently authored synthetic companion."""

from dataclasses import replace
import unittest

from .fixtures import CASES, JUDGE_LABELS, REFERENCE_LABELS
from .m1_trace import replay
from .m2_benchmark import build_benchmark
from .m3_evaluators import grounding_score, judge_agreement
from .m4_outcomes import evaluate_run
from .m5_compare import compare_versions


class PipelineTests(unittest.TestCase):
    def test_trace_links_to_one_request(self):
        run = replay(CASES[0], "baseline")
        self.assertEqual(len({span.span_id for span in run.spans}), len(run.spans))
        self.assertTrue(all(span.parent_id == run.spans[0].span_id for span in run.tools))

    def test_duplicate_or_incomplete_benchmark_is_rejected(self):
        for cases in [(*CASES, CASES[0]), CASES[:2]]:
            with self.assertRaises(ValueError):
                build_benchmark(cases, [replay(case, "baseline") for case in cases])

    def test_benchmark_joins_source_trace_without_using_prompt_as_key(self):
        runs = [replay(case, "baseline") for case in reversed(CASES)]
        benchmark = build_benchmark(CASES, runs)
        self.assertEqual(CASES[0].prompt, CASES[2].prompt)
        self.assertEqual(len(benchmark), 3)
        entry = benchmark["DEMO-REFUND"]
        self.assertEqual(entry.source_span_id, "baseline/DEMO-REFUND")
        self.assertEqual(entry.observed_response, "The $42 demo refund is recorded.")

    def test_benchmark_rejects_duplicate_missing_or_wrong_observations(self):
        runs = [replay(case, "baseline") for case in CASES]
        invalid = [runs[:2], [*runs, runs[0]],
                   [replace(runs[0], case_id="UNKNOWN"), *runs[1:]]]
        for observations in invalid:
            with self.assertRaises(ValueError):
                build_benchmark(CASES, observations)

    def test_unsupported_claim_is_not_grounded(self):
        run = replay(CASES[0], "candidate")
        self.assertTrue(grounding_score(run))
        self.assertFalse(grounding_score(replace(run, claims={"refunded_amount": 42})))

    def test_judge_validation_joins_identity_and_rejects_missing_labels(self):
        result = judge_agreement(REFERENCE_LABELS, dict(reversed(list(JUDGE_LABELS.items()))))
        self.assertEqual(result["matched"], 3)
        self.assertEqual(result["kappa"], 0.5)
        with self.assertRaises(ValueError):
            judge_agreement(REFERENCE_LABELS, {"LABEL-A": True})

    def test_grounded_confirmation_does_not_complete_refund(self):
        layers = evaluate_run(CASES[0], replay(CASES[0], "candidate"))
        self.assertTrue(layers["grounding"])
        self.assertTrue(layers["policy"])
        self.assertFalse(layers["selection"])
        self.assertFalse(layers["outcome"])

    def test_tool_result_without_state_change_does_not_prove_completion(self):
        run = replay(CASES[0], "baseline")
        self.assertFalse(evaluate_run(CASES[0], replace(run, state={"refunds": []}))["outcome"])

    def test_refund_before_identity_fails_policy(self):
        run = replay(CASES[0], "baseline")
        bad = tuple(replace(span, sequence=0) if span.name == "issue_refund" else span for span in run.spans)
        layers = evaluate_run(CASES[0], replace(run, spans=bad))
        self.assertFalse(layers["ordering"])
        self.assertFalse(layers["policy"])

    def test_comparison_survives_reordering_and_rejects_missing_cases(self):
        baseline = {case.case_id: evaluate_run(case, replay(case, "baseline")) for case in CASES}
        candidate = {case.case_id: evaluate_run(case, replay(case, "candidate")) for case in reversed(CASES)}
        result = compare_versions(baseline, candidate)
        self.assertEqual(result["regressions"], ["DEMO-REFUND"])
        self.assertEqual(result["layer_regressions"], {"DEMO-REFUND": ["selection", "outcome"]})
        self.assertFalse(result["gate_passed"])
        self.assertEqual((result["baseline_outcomes"], result["candidate_outcomes"]), (3, 2))
        with self.assertRaises(ValueError):
            compare_versions(baseline, {"DEMO-REFUND": candidate["DEMO-REFUND"]})

    def test_policy_regression_is_caught_even_when_outcome_passes(self):
        baseline = {case.case_id: evaluate_run(case, replay(case, "baseline")) for case in CASES}
        candidate = {key: dict(scores) for key, scores in baseline.items()}
        candidate["DEMO-REFUND"]["ordering"] = False
        candidate["DEMO-REFUND"]["policy"] = False
        self.assertTrue(candidate["DEMO-REFUND"]["outcome"])
        result = compare_versions(baseline, candidate)
        self.assertEqual(result["layer_regressions"], {"DEMO-REFUND": ["ordering", "policy"]})
        self.assertFalse(result["gate_passed"])

    def test_comparison_rejects_incomplete_or_nonboolean_scores(self):
        baseline = {case.case_id: evaluate_run(case, replay(case, "baseline")) for case in CASES}
        for changed in [{"outcome": True}, {**baseline["DEMO-REFUND"], "policy": 1}]:
            candidate = {key: dict(scores) for key, scores in baseline.items()}
            candidate["DEMO-REFUND"] = changed
            with self.assertRaises(ValueError):
                compare_versions(baseline, candidate)

    def test_no_new_regression_is_not_an_absolute_quality_pass(self):
        scores = {case.case_id: evaluate_run(case, replay(case, "candidate")) for case in CASES}
        result = compare_versions(scores, scores)
        self.assertTrue(result["gate_passed"])
        self.assertEqual(result["baseline_outcomes"], 2)
        self.assertEqual(result["candidate_outcomes"], 2)

    def test_kappa_is_undefined_for_constant_identical_labels(self):
        result = judge_agreement({"one": True, "two": True}, {"one": True, "two": True})
        self.assertEqual(result["accuracy"], 1.0)
        self.assertIsNone(result["kappa"])


if __name__ == "__main__":
    unittest.main()

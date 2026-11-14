"""Module 2: preserve identity, expectations and coverage in a benchmark."""

from collections.abc import Iterable

from .models import BenchmarkEntry, Case, Run

REQUIRED_COVERAGE = {"complete_refund", "report_status", "refuse_expired_refund"}


def build_benchmark(cases: Iterable[Case], runs: Iterable[Run]) -> dict[str, BenchmarkEntry]:
    expectations: dict[str, Case] = {}
    for case in cases:
        if case.case_id in expectations:
            raise ValueError(f"Duplicate case identity: {case.case_id}")
        expectations[case.case_id] = case
    observations: dict[str, Run] = {}
    for run in runs:
        if run.case_id in observations:
            raise ValueError(f"Duplicate observed case: {run.case_id}")
        if (not run.spans or run.spans[0].parent_id is not None
                or run.spans[0].inputs.get("case_id") != run.case_id):
            raise ValueError("Observed root span must identify its case")
        observations[run.case_id] = run
    if set(expectations) != set(observations):
        raise ValueError("Observed runs must cover exactly the expected case identities")
    covered = {case.requirement for case in expectations.values()}
    missing = REQUIRED_COVERAGE - covered
    if missing:
        raise ValueError(f"Missing requirement coverage: {sorted(missing)}")
    return {key: BenchmarkEntry(case, observations[key]) for key, case in expectations.items()}

"""Publication-time synthetic example inspired by an audit of saved course outputs.

No course code, Northwind data, model calls or assignment solutions are included.
"""

from collections.abc import Mapping, Sequence


def align_scores(
    versions: Mapping[str, Sequence[tuple[str, int]]],
) -> dict[str, dict[str, int]]:
    """Compare exactly the same unique cases, regardless of output order."""
    aligned: dict[str, dict[str, int]] = {}
    expected: set[str] | None = None
    for version, rows in versions.items():
        scores: dict[str, int] = {}
        for case_id, score in rows:
            if case_id in scores:
                raise ValueError(f"Duplicate case identity in {version}: {case_id}")
            if score not in (0, 1):
                raise ValueError("This binary demonstration accepts only 0 or 1")
            scores[case_id] = score
        if expected is None:
            expected = set(scores)
        elif set(scores) != expected:
            raise ValueError(f"Case identities differ in {version}")
        aligned[version] = scores
    return aligned


def demonstrate() -> None:
    # Synthetic cases intentionally unrelated to the course's test questions.
    baseline = [("case-a", 1), ("case-b", 0), ("case-c", 1)]
    reordered = [("case-c", 1), ("case-a", 1), ("case-b", 0)]
    positional = [(case, before, after) for (case, before), (_, after)
                  in zip(baseline, reordered)]
    print("Positional comparison (wrong):", positional)
    versions = align_scores({"baseline": baseline, "candidate": reordered})
    paired = [(case, versions["baseline"][case], versions["candidate"][case])
              for case, _ in baseline]
    print("Identity comparison (correct):", paired)
    assert sum(before != after for _, before, after in positional) == 2
    assert all(before == after for _, before, after in paired)
    assert all(sum(scores.values()) == 2 for scores in versions.values())

    # Reject plausible-looking incomplete or duplicated joins before reporting.
    for invalid in [reordered[:-1], reordered + [("case-a", 1)]]:
        try:
            align_scores({"baseline": baseline, "invalid": invalid})
        except ValueError:
            pass
        else:
            raise AssertionError("Invalid case membership was accepted")
    assert align_scores({}) == {}
    print("PASS: identity alignment, invariant scores, and duplicate/missing-case checks")


if __name__ == "__main__":
    demonstrate()

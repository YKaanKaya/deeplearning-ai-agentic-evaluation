"""Module 5: pair stable case identities and surface protected-layer regressions."""

from collections.abc import Mapping

PROTECTED_LAYERS = ("grounding", "selection", "invocation", "ordering", "outcome", "policy")


def compare_versions(baseline: Mapping[str, dict], candidate: Mapping[str, dict]) -> dict:
    if not baseline or set(baseline) != set(candidate):
        raise ValueError("Version comparisons require identical, nonempty case sets")
    for scores in [*baseline.values(), *candidate.values()]:
        if set(scores) != set(PROTECTED_LAYERS) or any(type(value) is not bool for value in scores.values()):
            raise ValueError("Each case needs the six declared boolean evaluation layers")
    paired = {case_id: {"baseline": baseline[case_id], "candidate": candidate[case_id]}
              for case_id in baseline}
    layer_regressions = {
        case_id: [layer for layer in PROTECTED_LAYERS
                  if pair["baseline"][layer] and not pair["candidate"][layer]]
        for case_id, pair in paired.items()
    }
    layer_regressions = {key: layers for key, layers in layer_regressions.items() if layers}
    return {"cases": len(paired), "paired": paired, "regressions": list(layer_regressions),
            "layer_regressions": layer_regressions, "gate_passed": not layer_regressions,
            "baseline_outcomes": sum(row["outcome"] for row in baseline.values()),
            "candidate_outcomes": sum(row["outcome"] for row in candidate.values())}

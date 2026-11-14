"""Module 3: check evidence and validate exported judge decisions."""

from collections.abc import Mapping

from .models import Run


def grounding_score(run: Run) -> bool:
    """Exact structured-fact check; not a general natural-language judge."""
    evidence = {}
    for span in run.tools:
        evidence.update(span.outputs)
    return all(key in evidence and evidence[key] == value
               for key, value in run.claims.items())


def judge_agreement(reference: Mapping[str, bool], predicted: Mapping[str, bool]) -> dict:
    if not reference or set(reference) != set(predicted):
        raise ValueError("Judge decisions must cover exactly the reference identities")
    if any(type(value) is not bool for value in [*reference.values(), *predicted.values()]):
        raise ValueError("This binary example accepts boolean labels only")
    total = len(reference)
    accuracy = sum(reference[key] == predicted[key] for key in reference) / total
    reference_positive = sum(reference.values()) / total
    predicted_positive = sum(predicted.values()) / total
    chance = (reference_positive * predicted_positive
              + (1 - reference_positive) * (1 - predicted_positive))
    kappa = None if chance == 1 else (accuracy - chance) / (1 - chance)
    return {"matched": round(accuracy * total), "total": total,
            "accuracy": accuracy, "kappa": kappa}

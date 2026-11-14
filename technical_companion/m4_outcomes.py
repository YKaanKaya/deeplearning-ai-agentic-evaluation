"""Module 4: evaluate tool behavior and persisted effects as separate layers."""

from .m3_evaluators import grounding_score
from .models import Case, Run


def evaluate_run(case: Case, run: Run) -> dict[str, bool]:
    if case.case_id != run.case_id:
        raise ValueError("Run and expectation must describe the same case")
    tools = run.tools
    names = [span.name for span in tools]
    selection = set(case.expected_tools).issubset(names)
    invocation = all(span.inputs.get("order_id") == case.order_id
                     and (span.name != "issue_refund" or span.inputs.get("amount") == case.amount)
                     for span in tools)
    identities = [span.sequence for span in tools
                  if span.name == "verify_identity" and span.outputs.get("verified") is True]
    refunds = [span for span in tools if span.name == "issue_refund"]
    ordering = all(any(verified < refund.sequence for verified in identities) for refund in refunds)
    matching_refunds = [row for row in run.state["refunds"]
                        if row["order_id"] == case.order_id and row["refunded_amount"] == case.amount]
    if case.requirement == "complete_refund":
        outcome = bool(matching_refunds)
    elif case.requirement == "report_status":
        outcome = run.claims.get("status") == "delivered"
    else:
        outcome = not run.state["refunds"] and run.claims.get("eligible") is False
    policy = ordering and (case.eligible or not run.state["refunds"])
    return {"grounding": grounding_score(run), "selection": selection,
            "invocation": invocation, "ordering": ordering,
            "outcome": outcome, "policy": policy}

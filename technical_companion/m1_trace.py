"""Module 1: replay behavior as linked agent/tool spans and retain final state."""

from .models import Case, Run, Span


def replay(case: Case, version: str) -> Run:
    """Replay an invented request; candidate omits the eligible refund action."""
    if version not in {"baseline", "candidate"}:
        raise ValueError("Unknown synthetic version")
    root_id = f"{version}/{case.case_id}"
    tools: list[Span] = []
    state: dict = {"refunds": []}

    def record(name: str, inputs: dict, outputs: dict, milliseconds: int) -> None:
        tools.append(Span(f"{root_id}/{len(tools) + 1}", root_id, name,
                          len(tools) + 1, inputs, outputs, milliseconds))

    facts = {"order_id": case.order_id, "amount": case.amount,
             "eligible": case.eligible, "status": "delivered"}
    record("lookup_order", {"order_id": case.order_id}, facts, 3)
    claims = {"status": "delivered"}
    if case.requirement == "report_status":
        response = "The demo order is delivered."
    else:
        record("verify_identity", {"order_id": case.order_id}, {"verified": True}, 2)
        if not case.eligible:
            claims = {"eligible": False}
            response = "The demo order is outside the refund window."
        elif version == "candidate":
            response = "Please confirm that you want the demo refund."
        else:
            refund = {"order_id": case.order_id, "refunded_amount": case.amount}
            state["refunds"].append(refund)
            record("issue_refund", {"order_id": case.order_id, "amount": case.amount}, refund, 4)
            claims = {"refunded_amount": case.amount}
            response = f"The ${case.amount} demo refund is recorded."
    root = Span(root_id, None, "support_request", 0,
                {"case_id": case.case_id, "request": case.prompt}, {"response": response},
                sum(span.synthetic_ms for span in tools))
    return Run(case.case_id, version, response, claims, (root, *tools), state)

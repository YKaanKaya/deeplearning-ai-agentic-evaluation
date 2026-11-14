"""Invented cases and labels, distinct from the saved course test datasets."""

from .models import Case

CASES = (
    Case("DEMO-REFUND", "known_good", "complete_refund", "DEMO-ORDER-1",
         ("lookup_order", "verify_identity", "issue_refund"), prompt="Please refund this order."),
    Case("DEMO-STATUS", "known_good", "report_status", "DEMO-ORDER-2",
         ("lookup_order",), prompt="Where is this order?"),
    Case("DEMO-EXPIRED", "targeted", "refuse_expired_refund", "DEMO-ORDER-3",
         ("lookup_order", "verify_identity"), eligible=False, prompt="Please refund this order."),
)

# Fixed labels stand in for a reviewed reference and a judge's exported decisions.
# No model is called. One deliberate disagreement makes validation visible.
REFERENCE_LABELS = {"LABEL-A": True, "LABEL-B": True, "LABEL-C": False, "LABEL-D": False}
JUDGE_LABELS = {"LABEL-A": True, "LABEL-B": True, "LABEL-C": True, "LABEL-D": False}

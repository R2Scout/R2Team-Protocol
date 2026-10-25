"""Pure decision model for R2Team 2.6 workspace lifecycle fixtures."""
import re
from datetime import date


TERMINAL_CUSTODY = {
    "CLOSED",
    "RETAINED_PROTECTED",
    "TRANSFERRED_TO_NEXT_TASK",
}


def _valid_exception(exception, today, expected):
    if not isinstance(exception, dict):
        return False
    required_text = (
        "reason",
        "capacity_evidence",
        "review_date",
        "recovery_rule",
    )
    if any(not isinstance(exception.get(field), str) or
           not exception[field].strip() for field in required_text):
        return False
    identity_fields = (
        "task_id", "lease_id", "base_sha", "prior_base_sha",
        "candidate_sha", "owner", "purpose",
    )
    if any(not expected.get(field) or
           exception.get(field) != expected[field]
           for field in identity_fields):
        return False
    if exception["base_sha"] == exception["prior_base_sha"]:
        return False
    if any(not re.fullmatch(r"[0-9a-f]{40}", exception[field])
           for field in ("base_sha", "prior_base_sha", "candidate_sha")):
        return False
    if any(exception.get(field) is not True for field in (
            "changed_base", "custody_known", "disjoint_lane",
            "candidate_preserved")):
        return False
    try:
        review_date = date.fromisoformat(exception["review_date"])
        observed_date = date.fromisoformat(today) if today else date.today()
    except (TypeError, ValueError):
        return False
    return review_date >= observed_date


def allocation_decision(*, active_task, project_active, free_gib,
                        compatible_lease=False, recovery=False,
                        exception=None, today=None,
                        active_mutable_for_purpose=0, task_id=None,
                        lease_id=None, base_sha=None, prior_base_sha=None,
                        candidate_sha=None, owner=None, purpose=None):
    if compatible_lease:
        return "REUSE_EXISTING"
    if (project_active >= 150 or free_gib < 15 or
            active_mutable_for_purpose >= 1):
        return "ALLOCATION_BLOCKED"
    exception_valid = _valid_exception(exception, today, {
        "task_id": task_id,
        "lease_id": lease_id,
        "base_sha": base_sha,
        "prior_base_sha": prior_base_sha,
        "candidate_sha": candidate_sha,
        "owner": owner,
        "purpose": purpose,
    })
    if free_gib < 30:
        if recovery and exception_valid:
            return "ALLOW_RECOVERY"
        return "ALLOCATION_BLOCKED"
    if free_gib <= 50:
        return "ALLOCATION_BLOCKED"
    if active_task >= 3:
        return "ALLOW_EXCEPTION" if exception_valid else "ALLOCATION_BLOCKED"
    return "ALLOW_NORMAL"


def closure_decision(*, evidence_exported, exclusively_owned, target_contained,
                     removal_authorized, live_process=False,
                     dependent_lease=False, shared_immutable_cache=False,
                     retained_recovery_input=False, dirty_or_unknown=False,
                     custody="ordinary-canonical"):
    if dirty_or_unknown or not evidence_exported or not exclusively_owned:
        return "RETAINED_PROTECTED"
    if live_process or dependent_lease:
        return "BLOCKED_DEPENDENCY"
    if shared_immutable_cache or retained_recovery_input:
        return "RETAINED_PROTECTED"
    if not target_contained or not removal_authorized:
        return "BLOCKED_AUTHORITY"
    if custody == "codex-managed":
        return "APPLICATION_ARCHIVE_REQUIRED"
    return "CLOSED"


def result_record(verdict, workspace_disposition):
    return {
        "verdict": verdict,
        "workspace_disposition": workspace_disposition,
    }


def transfer_decision(head, tree, next_owner, *, active_writers):
    if active_writers != 1 or not head or not tree or not next_owner:
        return "BLOCKED_DEPENDENCY"
    return {
        "disposition": "TRANSFERRED_TO_NEXT_TASK",
        "head": head,
        "tree": tree,
        "next_owner": next_owner,
    }


def _valid_terminal_lease(lease):
    if not isinstance(lease, dict):
        return False
    state = lease.get("state")
    if state not in TERMINAL_CUSTODY:
        return False
    required = (
        "closure_owner_executor_id", "retention_class", "recovery_ref",
        "review_date", "close_receipt_ref",
    )
    if any(not isinstance(lease.get(field), str) or
           not lease[field].strip() for field in required):
        return False
    try:
        date.fromisoformat(lease["review_date"])
    except (TypeError, ValueError):
        return False
    if state == "TRANSFERRED_TO_NEXT_TASK":
        transfer_required = (
            "next_task_id", "next_owner_executor_id", "transfer_custody_ref",
        )
        if any(not isinstance(lease.get(field), str) or
               not lease[field].strip() for field in transfer_required):
            return False
    return True


def completion_decision(lease_records):
    if all(_valid_terminal_lease(lease) for lease in lease_records):
        return "ADMIN_COMPLETION_ALLOWED"
    return "ADMIN_COMPLETION_BLOCKED"


def evidence_decision(kind, *, content_hash=None, recovery_location=None,
                      owner=None, retention_class=None, access_boundary=None):
    if kind == "git":
        return "EVIDENCE_DURABLE"
    if kind == "manifest" and all((
        isinstance(content_hash, str) and re.fullmatch(r"[0-9a-f]{64}", content_hash),
        recovery_location,
        owner,
        retention_class,
        access_boundary,
    )):
        return "EVIDENCE_DURABLE"
    return "EVIDENCE_BLOCKED"

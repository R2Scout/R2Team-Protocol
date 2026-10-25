"""Pure decision model for R2Team 2.6 workspace lifecycle fixtures."""
import re
from datetime import date


TERMINAL_CUSTODY = {
    "CLOSED",
    "RETAINED_PROTECTED",
    "TRANSFERRED_TO_NEXT_TASK",
}


def _valid_exception(exception, today):
    if not isinstance(exception, dict):
        return False
    required = (
        "task_id",
        "reason",
        "lease_id",
        "owner",
        "purpose",
        "capacity_evidence",
        "review_date",
        "changed_base",
        "custody_known",
        "disjoint_lane",
        "candidate_preserved",
        "recovery_rule",
    )
    if any(not exception.get(field) for field in required):
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
                        active_mutable_for_purpose=0):
    if compatible_lease:
        return "REUSE_EXISTING"
    if (project_active >= 150 or free_gib < 15 or
            active_mutable_for_purpose >= 1):
        return "ALLOCATION_BLOCKED"
    exception_valid = _valid_exception(exception, today)
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


def completion_decision(lease_states):
    if all(state in TERMINAL_CUSTODY for state in lease_states):
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

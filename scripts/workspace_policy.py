"""Pure decision model for R2Team 2.6 workspace lifecycle fixtures."""
import re


TERMINAL_OR_BLOCKING = {
    "CLOSED",
    "RETAINED_PROTECTED",
    "TRANSFERRED_TO_NEXT_TASK",
    "BLOCKED_DIRTY",
    "BLOCKED_DEPENDENCY",
    "BLOCKED_AUTHORITY",
}


def allocation_decision(*, active_task, project_active, free_gib,
                        compatible_lease=False, recovery=False,
                        owner_exception=False):
    if compatible_lease:
        return "REUSE_EXISTING"
    if active_task >= 3 or project_active >= 150 or free_gib < 15:
        return "ALLOCATION_BLOCKED"
    if free_gib < 30:
        if recovery and owner_exception:
            return "ALLOW_RECOVERY"
        return "ALLOCATION_BLOCKED"
    if free_gib <= 50:
        return "ALLOCATION_BLOCKED"
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
    if all(state in TERMINAL_OR_BLOCKING for state in lease_states):
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

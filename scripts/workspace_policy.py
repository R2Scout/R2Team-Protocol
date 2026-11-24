"""Pure workspace decision model, including R2Team 2.10 resource-lifetime fixtures."""
import re
from datetime import date


TERMINAL_CUSTODY = {
    "CLOSED",
    "RETAINED_PROTECTED",
    "TRANSFERRED_TO_NEXT_TASK",
}

LIFETIME_POLICY = {
    "persistent": ("perm", "DECOMMISSION_ACCEPTED"),
    "task_scoped": ("task", "TASK_RESULT_ACCEPTED"),
    "ephemeral": ("tmp", "USE_COMPLETED"),
}


def resource_label(project_slug, work_ref, executor_slug, lifetime):
    """Return a portable label; native workspace numbers and paths remain separate."""
    if not isinstance(lifetime, str) or lifetime not in LIFETIME_POLICY:
        raise ValueError("Unknown resource lifetime")
    patterns = ((project_slug, r"[a-z0-9]+(?:[.-][a-z0-9]+)*"),
                (work_ref, r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*"),
                (executor_slug, r"[a-z0-9]+(?:-[a-z0-9]+)*"))
    if any(not isinstance(value, str) or not re.fullmatch(pattern, value)
           for value, pattern in patterns):
        raise ValueError("Use portable project, typed work, and executor slugs")
    lifetime_marker = LIFETIME_POLICY[lifetime][0]
    label = f"{project_slug}-{work_ref}-{lifetime_marker}-{executor_slug}"
    if len(label) > 96:
        raise ValueError("Resource label exceeds 96 characters; approve shorter aliases")
    return label


def git_worktree_directory_name(project_slug, work_ref, executor_slug, lifetime,
                                *, purpose=None, custody="ordinary-canonical"):
    """Name an ordinary worktree by its Git reference, without an extra physical ID."""
    if custody not in ("ordinary-canonical", "external-authorized"):
        raise ValueError("Application and legacy directory paths must be preserved")
    if (not isinstance(work_ref, str) or not re.fullmatch(
            r"(?:(?:issue|pr|wi)[0-9]+|task(?:[0-9]+|-[a-z0-9]+(?:-[a-z0-9]+)*))",
            work_ref)):
        raise ValueError("An explicit Git Issue, TASK, PR, or Work Item reference is required")
    name = resource_label(project_slug, work_ref, executor_slug, lifetime)
    if purpose is not None:
        if not isinstance(purpose, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", purpose):
            raise ValueError("Use the declared portable purpose, not a collision counter")
        name += "-" + purpose
    if len(name) > 96:
        raise ValueError("Directory name exceeds 96 characters; approve shorter aliases")
    return name


def resource_policy_errors(resource):
    """Check explicit lifetime metadata without inferring it from role, path, or age."""
    if not isinstance(resource, dict):
        return ["Resource classification record required"]
    errors = []
    required = ("resource_id", "project_slug", "work_ref", "executor_slug",
                "owner_executor_id", "resource_label", "lifetime", "purpose",
                "review_date", "retention_class", "recovery_ref")
    for field in required:
        if not isinstance(resource.get(field), str) or not resource[field].strip():
            errors.append(f"Missing resource field: {field}")
    try:
        expected_label = resource_label(resource.get("project_slug"),
                                        resource.get("work_ref"),
                                        resource.get("executor_slug"),
                                        resource.get("lifetime"))
        if resource.get("resource_label") != expected_label:
            errors.append("Resource label disagrees with its explicit metadata")
    except ValueError as error:
        errors.append(str(error))
    condition = resource.get("close_condition")
    lifetime = resource.get("lifetime")
    expected_event = (LIFETIME_POLICY[lifetime][1]
                      if isinstance(lifetime, str) and lifetime in LIFETIME_POLICY
                      else None)
    if (not isinstance(condition, dict) or expected_event is None or
            condition.get("event") != expected_event or
            not isinstance(condition.get("ref"), str) or not condition["ref"].strip()):
        errors.append("Close condition must name the lifetime event and exact governing reference")
    try:
        date.fromisoformat(resource.get("review_date"))
    except (TypeError, ValueError):
        errors.append("Resource review_date must be an ISO date")
    return errors


def resource_allocation_decision(resource, **allocation_facts):
    """Add the adopted lifetime gate to the existing allocation model."""
    if resource_policy_errors(resource):
        return "ALLOCATION_BLOCKED"
    return allocation_decision(**allocation_facts)


def resource_closure_decision(resource, *, condition_evidence,
                              decommission_authorized=False, **closure_facts):
    """A bound completion event only enables preflight; it never authorizes removal."""
    if resource_policy_errors(resource):
        return "RESOURCE_POLICY_BLOCKED"
    required_facts = ("evidence_exported", "exclusively_owned", "target_contained",
                      "removal_authorized")
    optional_flags = ("live_process", "dependent_lease", "shared_immutable_cache",
                      "retained_recovery_input", "dirty_or_unknown")
    if (any(type(closure_facts.get(field)) is not bool for field in required_facts) or
            any(field in closure_facts and type(closure_facts[field]) is not bool
                for field in optional_flags) or
            closure_facts.get("custody", "ordinary-canonical") not in (
                "ordinary-canonical", "codex-managed", "external-authorized", "legacy-retained")):
        return "RESOURCE_POLICY_BLOCKED"
    if (resource["lifetime"] == "persistent" and
            decommission_authorized is not True):
        return "RETAINED_PROTECTED"
    condition = resource["close_condition"]
    expected = dict(condition, resource_id=resource["resource_id"],
                    owner_executor_id=resource["owner_executor_id"])
    if (not isinstance(condition_evidence, dict) or
            any(condition_evidence.get(key) != value for key, value in expected.items()) or
            condition_evidence.get("satisfied") is not True or
            not isinstance(condition_evidence.get("receipt_ref"), str) or
            not condition_evidence["receipt_ref"].strip()):
        return "RETAINED_PROTECTED"
    return closure_decision(**closure_facts)


def resource_completion_decision(lease_records):
    """Require adopted lifetime records as well as existing terminal custody evidence."""
    if (not isinstance(lease_records, list) or
            any(resource_policy_errors(record) for record in lease_records)):
        return "ADMIN_COMPLETION_BLOCKED"
    return completion_decision(lease_records)


def resource_review_decision(resource, *, today):
    """A due review is an observation, never promotion or deletion."""
    if resource_policy_errors(resource):
        return "RESOURCE_POLICY_BLOCKED"
    try:
        observed_date = date.fromisoformat(today)
    except (TypeError, ValueError):
        return "RESOURCE_POLICY_BLOCKED"
    return ("REVIEW_DUE" if date.fromisoformat(resource["review_date"]) <= observed_date
            else "REVIEW_SCHEDULED")


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
                        candidate_sha=None, owner=None, purpose=None,
                        inventory_complete=True, placement_conflict=False,
                        materialization_key_conflict=False):
    if placement_conflict or materialization_key_conflict:
        return "ALLOCATION_BLOCKED"
    if compatible_lease:
        return "REUSE_EXISTING"
    if (not inventory_complete or project_active >= 150 or free_gib < 15 or
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


def evidence_capture_decision(*, evidence_key, existing_keys,
                              artifact_required=False, content_hash=None,
                              consumer=None, owner=None,
                              retention_class=None, recovery_ref=None,
                              access_boundary=None, close_trigger=None):
    """Decide whether a verification run may create a durable artifact."""
    if not isinstance(evidence_key, str) or not evidence_key.strip():
        return "EVIDENCE_BLOCKED"
    if evidence_key in existing_keys:
        return "REUSE_EXISTING_EVIDENCE"
    if not artifact_required:
        return "SUMMARY_ONLY"
    required_text = (
        consumer,
        owner,
        retention_class,
        recovery_ref,
        access_boundary,
        close_trigger,
    )
    if (not isinstance(content_hash, str) or
            not re.fullmatch(r"[0-9a-f]{64}", content_hash) or
            any(not isinstance(value, str) or not value.strip()
                for value in required_text)):
        return "EVIDENCE_BLOCKED"
    return "ALLOW_DURABLE_ARTIFACT"

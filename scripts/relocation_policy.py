"""Pure policy helpers for R2Team relocation fixtures.

The module models cooperative protocol fencing only. It performs no provider,
chat, registry, process, workspace, or filesystem mutation.
"""

from dataclasses import dataclass


RECEIPT_TYPES = {
    "PREPARE",
    "SOURCE_STOP",
    "FREEZE",
    "TARGET_PREFLIGHT",
    "ACTIVATION",
    "PARTIAL_DISPOSITION",
    "COMPLETION",
    "CANCELLATION",
    "FORWARD_ROLLBACK",
}


def _nonblank(value) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _canonical_portable_path(path: str) -> bool:
    if not _nonblank(path) or "\\" in path or path.startswith("/") or "//" in path:
        return False
    return all(part not in {"", ".", ".."} for part in path.split("/"))


@dataclass(frozen=True)
class Decision:
    code: str
    reason: str = ""


@dataclass(frozen=True)
class FenceRecord:
    project_id: str
    executor_id: str
    epoch: int
    record_ref: str
    source_state: str
    target_state: str
    custody: str


@dataclass(frozen=True)
class TeamState:
    state: str
    active_targets: tuple[str, ...]
    blocked_executors: tuple[str, ...]


def propose_successor(
    accepted: FenceRecord,
    *,
    expected_prior_epoch: int,
    expected_prior_ref: str,
    new_epoch: int,
    new_record_ref: str,
) -> Decision:
    if expected_prior_ref != accepted.record_ref:
        return Decision("WRITER_CONFLICT", "causal predecessor does not match")
    if expected_prior_epoch != accepted.epoch or new_epoch != accepted.epoch + 1:
        return Decision("WRITER_CONFLICT", "epoch does not advance accepted state")
    return Decision("ALLOW")


def materialize_successor(
    accepted: FenceRecord,
    *,
    expected_prior_epoch: int,
    expected_prior_ref: str,
    new_epoch: int,
    new_record_ref: str,
) -> tuple[Decision, FenceRecord]:
    decision = propose_successor(
        accepted,
        expected_prior_epoch=expected_prior_epoch,
        expected_prior_ref=expected_prior_ref,
        new_epoch=new_epoch,
        new_record_ref=new_record_ref,
    )
    if decision.code != "ALLOW":
        return decision, accepted
    return decision, FenceRecord(
        project_id=accepted.project_id,
        executor_id=accepted.executor_id,
        epoch=new_epoch,
        record_ref=new_record_ref,
        source_state=accepted.source_state,
        target_state=accepted.target_state,
        custody=accepted.custody,
    )


def validate_stop_receipt(receipt: dict) -> Decision:
    if not isinstance(receipt, dict):
        return Decision("STOP_PROOF_INVALID", "stop receipt is not a record")
    if receipt.get("publishers_in_flight") or receipt.get("helpers_in_flight"):
        return Decision("BLOCKED_IN_FLIGHT", "publisher or helper remains active")
    required = {
        "receipt_id",
        "receipt_type",
        "migration_id",
        "repository_or_project_id",
        "executor_id",
        "expected_epoch",
        "final_checkpoint",
        "candidate_tree",
        "publishers_in_flight",
        "helpers_in_flight",
        "workspace_custody",
        "native_resource_custody",
        "actor_class",
        "stop_mechanism",
        "cutover_parent",
        "timestamp",
    }
    if any(key not in receipt or receipt[key] in (None, "") for key in required):
        return Decision("STOP_PROOF_INVALID", "required stop fact is missing")
    if receipt["receipt_type"] != "SOURCE_STOP":
        return Decision("STOP_PROOF_INVALID", "receipt is not SOURCE_STOP")
    if receipt["stop_mechanism"] not in {
        "COOPERATIVE_ACK",
        "ADMINISTRATIVE_REVOCATION",
        "MODELED_ENFORCEABLE_FENCE",
    }:
        return Decision("STOP_PROOF_INVALID", "stop mechanism is not accepted")
    return Decision("ALLOW")


def activation_allowed(
    accepted: FenceRecord,
    *,
    stop_receipt: dict | None,
    activation_receipt: dict | None,
    source_reachable: bool,
    enforceable_revocation: bool,
) -> Decision:
    if not source_reachable and not enforceable_revocation:
        return Decision(
            "BLOCKED_SOURCE_UNREACHABLE",
            "source is unreachable and no enforceable fence is proven",
        )
    stop_validation = validate_stop_receipt(stop_receipt)
    if stop_validation.code != "ALLOW":
        return stop_validation
    if not isinstance(activation_receipt, dict):
        return Decision("ACTIVATION_RECEIPT_INVALID")
    if activation_receipt.get("target_preflight") != "PASS":
        return Decision("TARGET_PREFLIGHT_REQUIRED")
    if activation_receipt.get("causal_stop_receipt") != stop_receipt.get("receipt_id"):
        return Decision(
            "ACTIVATION_CAUSAL_MISMATCH",
            "activation does not reference the accepted stop receipt",
        )
    activation_validation = validate_receipt(activation_receipt)
    if activation_validation.code != "ALLOW" or activation_receipt.get("receipt_type") != "ACTIVATION":
        return Decision("ACTIVATION_RECEIPT_INVALID")
    if (
        activation_receipt.get("causal_stop_receipt")
        != stop_receipt.get("receipt_id")
        or stop_receipt.get("cutover_parent") != accepted.record_ref
        or activation_receipt.get("cutover_parent") != accepted.record_ref
    ):
        return Decision(
            "ACTIVATION_CAUSAL_MISMATCH",
            "activation does not reference the accepted stop receipt",
        )
    identity_pairs = (
        (stop_receipt.get("repository_or_project_id"), accepted.project_id),
        (activation_receipt.get("repository_or_project_id"), accepted.project_id),
        (stop_receipt.get("migration_id"), activation_receipt.get("migration_id")),
        (stop_receipt.get("executor_id"), accepted.executor_id),
        (activation_receipt.get("executor_id"), accepted.executor_id),
        (stop_receipt.get("final_checkpoint"), activation_receipt.get("task_checkpoint")),
        (stop_receipt.get("candidate_tree"), activation_receipt.get("candidate_tree")),
        (stop_receipt.get("workspace_custody"), activation_receipt.get("workspace_custody")),
    )
    if any(actual != expected for actual, expected in identity_pairs):
        return Decision("ACTIVATION_IDENTITY_MISMATCH")
    if (
        stop_receipt.get("expected_epoch") != accepted.epoch
        or activation_receipt.get("prior_epoch") != accepted.epoch
        or activation_receipt.get("new_epoch") != accepted.epoch + 1
    ):
        return Decision("ACTIVATION_CAUSAL_MISMATCH", "activation epoch is invalid")
    return Decision("ALLOW")


def derive_team_state(records: list[dict]) -> TeamState:
    active = tuple(
        record["executor_id"]
        for record in records
        if record.get("target_state") == "ACTIVE"
    )
    terminal_dispositions = {"BLOCKED", "CANCELLED", "FORWARD_ROLLBACK"}
    terminal_fields = {
        "disposition_owner_executor_id",
        "review_date",
        "next_action",
        "disposition_receipt_ref",
    }

    def valid_terminal(record: dict) -> bool:
        return record.get("disposition") in terminal_dispositions and all(
            _nonblank(record.get(field)) for field in terminal_fields
        )

    invalid_terminal = tuple(
        record["executor_id"]
        for record in records
        if record.get("disposition") in terminal_dispositions
        and not valid_terminal(record)
    )
    blocked = tuple(
        record["executor_id"]
        for record in records
        if record.get("disposition") == "BLOCKED"
    )
    if records and all(
        (
            record.get("target_state") == "ACTIVE"
            and record.get("disposition") == "RESUMED"
        )
        or valid_terminal(record)
        for record in records
    ):
        return TeamState("COMPLETE", active, blocked)
    if invalid_terminal or (active and blocked):
        return TeamState(
            "PARTIAL_BLOCKED",
            active,
            tuple(dict.fromkeys((*blocked, *invalid_terminal))),
        )
    if records and all(
        record.get("source_state") == "STOPPED"
        and record.get("target_state") == "READY"
        for record in records
    ):
        return TeamState("READY_TO_RESUME", active, blocked)
    if records and all(
        record.get("source_state") == "STOPPED"
        and record.get("target_state") == "INACTIVE"
        for record in records
    ):
        return TeamState("FROZEN", active, blocked)
    return TeamState("RESUMING", active, blocked)


def permitted_successors(
    state: str, *, blocked_from_state: str | None = None
) -> tuple[str, ...]:
    if state == "FROZEN":
        return ("READY_TO_RESUME", "CANCELLATION", "FORWARD_ROLLBACK")
    if state == "PARTIAL_BLOCKED":
        return ("RESUMING", "COMPLETE", "FORWARD_ROLLBACK")
    if state == "BLOCKED" and blocked_from_state:
        return (blocked_from_state, "CANCELLATION", "FORWARD_ROLLBACK")
    return ()


def cancellation_allowed(
    *,
    source_state: str,
    target_state: str,
    current_epoch: int,
    proposed_epoch: int,
) -> Decision:
    if target_state == "ACTIVE":
        return Decision("FORWARD_ROLLBACK_REQUIRED")
    if source_state == "STOPPED":
        return Decision("REACTIVATION_REQUIRED")
    if proposed_epoch != current_epoch:
        return Decision("CAUSAL_SUCCESSOR_REQUIRED")
    return Decision("ALLOW_RETAIN_SOURCE")


def publication_allowed(
    accepted: FenceRecord,
    *,
    claim_project_id: str,
    claim_executor_id: str,
    claim_epoch: int,
    claim_record_ref: str,
    publication_class: str,
    frozen: bool,
    actor_executor_id: str,
    migration_pm_executor_id: str,
    path: str,
    migration_id: str,
    governing_task_path: str | None = None,
    governing_task_fields: tuple[str, ...] = (),
    claimed_fields: tuple[str, ...] = (),
) -> Decision:
    if (
        claim_project_id != accepted.project_id
        or claim_executor_id != accepted.executor_id
        or claim_epoch != accepted.epoch
        or claim_record_ref != accepted.record_ref
    ):
        return Decision("WRITER_CONFLICT", "writer claim is stale or misaddressed")
    allowed_classes = {"PRODUCT", "TASK", "TEAM", "MIGRATION_CONTROL"}
    if publication_class not in allowed_classes:
        return Decision("PUBLICATION_CLASS_INVALID")
    if not _canonical_portable_path(path):
        return Decision("PUBLICATION_PATH_INVALID")
    if not frozen:
        return Decision("ALLOW")
    if publication_class == "PRODUCT":
        return Decision("FROZEN_PRODUCT_WRITE_BLOCKED")
    control_prefix = f"Team/Migrations/{migration_id}/"
    if (
        publication_class == "MIGRATION_CONTROL"
        and actor_executor_id == migration_pm_executor_id
        and path.startswith(control_prefix)
    ):
        return Decision("ALLOW")
    if publication_class == "MIGRATION_CONTROL":
        return Decision("FROZEN_CONTROL_FORBIDDEN")
    if (
        publication_class == "TASK"
        and actor_executor_id == migration_pm_executor_id
        and governing_task_path is not None
        and _canonical_portable_path(governing_task_path)
        and path == governing_task_path
        and bool(claimed_fields)
        and set(claimed_fields).issubset(governing_task_fields)
    ):
        return Decision("ALLOW")
    return Decision("FROZEN_PUBLICATION_BLOCKED")


def registry_mapping_allowed(
    *,
    expected_executor_id: str,
    observed_executor_id: str | None,
    executor_mode: str,
    mapping_present: bool,
    local_authority: bool,
    read_back: bool,
    collision: bool,
) -> Decision:
    if executor_mode == "remote_manual" and not mapping_present:
        return Decision("ALLOW_REMOTE_MANUAL")
    if collision or observed_executor_id != expected_executor_id:
        return Decision("REGISTRY_CONFLICT")
    if not local_authority:
        return Decision("REGISTRY_AUTHORITY_REQUIRED")
    if not read_back:
        return Decision("REGISTRY_READBACK_REQUIRED")
    return Decision("ALLOW")


def workspace_reuse_allowed(expected: dict, observed: dict) -> Decision:
    required = {
        "candidate",
        "custody",
        "host_class",
        "native_resources",
        "dependencies",
        "contained",
        "owner_executor_id",
        "mutability",
    }
    if any(key not in expected or observed.get(key) != expected[key] for key in required):
        return Decision("WORKSPACE_REUSE_BLOCKED", "workspace custody facts differ")
    return Decision("ALLOW")


def affected_set_allowed(
    *,
    affected_executor_ids: tuple[str, ...],
    retained_executor_ids: tuple[str, ...],
    migration_state: str,
) -> Decision:
    frozen_or_later = {
        "FREEZE_PENDING",
        "FROZEN",
        "READY_TO_RESUME",
        "RESUMING",
        "PARTIAL_BLOCKED",
        "COMPLETE",
    }
    if (
        migration_state in frozen_or_later
        and set(affected_executor_ids).intersection(retained_executor_ids)
    ):
        return Decision("RETAINED_SET_CONFLICT")
    return Decision("ALLOW")


def receipt_set_allowed(receipts: tuple[dict, ...]) -> Decision:
    for receipt in receipts:
        if validate_receipt(receipt).code != "ALLOW":
            return Decision("RECEIPT_INVALID")
    receipt_ids = [receipt.get("receipt_id") for receipt in receipts]
    if len(receipt_ids) != len(set(receipt_ids)):
        return Decision("DUPLICATE_RECEIPT_ID")
    return Decision("ALLOW")


def validate_receipt(receipt: dict | None) -> Decision:
    if not isinstance(receipt, dict):
        return Decision("RECEIPT_INVALID")
    common_nonblank = {
        "receipt_id",
        "receipt_type",
        "migration_id",
        "repository_or_project_id",
        "causal_parent_ref",
        "accepted_commit_sha",
        "actor_executor_id",
        "actor_provider_class",
        "observed_outcome",
        "registry_evidence",
        "timestamp",
        "review_date",
    }
    if any(not _nonblank(receipt.get(field)) for field in common_nonblank):
        return Decision("RECEIPT_INVALID", "common receipt fact is missing")
    if receipt.get("receipt_type") not in RECEIPT_TYPES:
        return Decision("RECEIPT_INVALID", "receipt type is unknown")
    receipt_type = receipt["receipt_type"]
    global_types = {"PREPARE", "FREEZE", "COMPLETION"}
    if receipt_type not in global_types and not _nonblank(receipt.get("executor_id")):
        return Decision("RECEIPT_INVALID", "executor identity is missing")
    if receipt_type in global_types and receipt.get("executor_id") is not None and not _nonblank(receipt.get("executor_id")):
        return Decision("RECEIPT_INVALID", "executor identity is malformed")
    if not isinstance(receipt.get("prior_epoch"), int) or not isinstance(receipt.get("new_epoch"), int):
        return Decision("RECEIPT_INVALID", "receipt epoch is invalid")
    for field in ("task_checkpoint_refs", "candidate_refs", "workspace_disposition_refs"):
        value = receipt.get(field)
        if not isinstance(value, list) or (field != "workspace_disposition_refs" and not value):
            return Decision("RECEIPT_INVALID", f"{field} is invalid")
    if receipt.get("registry_evidence") not in {
        "NOT_APPLICABLE",
        "MAPPING_PRESENT_READ_BACK",
        "MAPPING_ABSENT",
        "MAPPING_CONFLICT",
    }:
        return Decision("RECEIPT_INVALID", "registry evidence is invalid")

    type_fields = {
        "PREPARE": {"affected_executor_ids"},
        "SOURCE_STOP": set(),
        "FREEZE": {"affected_executor_ids", "stopped_executor_ids"},
        "TARGET_PREFLIGHT": {"target_preflight", "target_placement_class"},
        "ACTIVATION": {
            "causal_stop_receipt",
            "cutover_parent",
            "target_preflight",
            "task_checkpoint",
            "candidate_tree",
            "workspace_custody",
            "mapping_result",
        },
        "PARTIAL_DISPOSITION": {"blocked_from_state", "permitted_successors"},
        "COMPLETION": {"accounted_executor_ids"},
        "CANCELLATION": {"terminal_disposition"},
        "FORWARD_ROLLBACK": {"rollback_target_epoch"},
    }
    if any(
        field not in receipt or receipt[field] in (None, "", [])
        for field in type_fields[receipt_type]
    ):
        return Decision("RECEIPT_INVALID", "type-specific receipt fact is missing")
    if receipt_type == "SOURCE_STOP":
        stop = validate_stop_receipt(receipt)
        if stop.code != "ALLOW":
            return Decision("RECEIPT_INVALID", stop.reason)
    if (
        receipt_type == "ACTIVATION"
        and receipt.get("causal_parent_ref") != receipt.get("causal_stop_receipt")
    ):
        return Decision("RECEIPT_INVALID", "activation causal parent is invalid")
    return Decision("ALLOW")

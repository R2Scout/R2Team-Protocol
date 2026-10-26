"""Pure policy helpers for R2Team relocation fixtures.

The module models cooperative protocol fencing only. It performs no provider,
chat, registry, process, workspace, or filesystem mutation.
"""

from dataclasses import dataclass


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
    if receipt.get("publishers_in_flight") or receipt.get("helpers_in_flight"):
        return Decision("BLOCKED_IN_FLIGHT", "publisher or helper remains active")
    required = {
        "receipt_id",
        "migration_id",
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
    if (
        stop_receipt is None
        or activation_receipt is None
        or activation_receipt.get("causal_stop_receipt")
        != stop_receipt.get("receipt_id")
        or stop_receipt.get("cutover_parent") != accepted.record_ref
        or activation_receipt.get("cutover_parent") != accepted.record_ref
    ):
        return Decision(
            "ACTIVATION_CAUSAL_MISMATCH",
            "activation does not reference the accepted stop receipt",
        )
    if activation_receipt.get("target_preflight") != "PASS":
        return Decision("TARGET_PREFLIGHT_REQUIRED")
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
    blocked = tuple(
        record["executor_id"]
        for record in records
        if record.get("disposition") == "BLOCKED"
    )
    if records and len(active) == len(records):
        return TeamState("COMPLETE", active, blocked)
    if active and blocked:
        return TeamState("PARTIAL_BLOCKED", active, blocked)
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
        if proposed_epoch == current_epoch + 1:
            return Decision("ALLOW_FORWARD_ROLLBACK")
        return Decision("FORWARD_ROLLBACK_REQUIRED")
    if source_state == "STOPPED" and proposed_epoch <= current_epoch:
        return Decision("REACTIVATION_REQUIRED")
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
) -> Decision:
    if (
        claim_project_id != accepted.project_id
        or claim_executor_id != accepted.executor_id
        or claim_epoch != accepted.epoch
        or claim_record_ref != accepted.record_ref
    ):
        return Decision("WRITER_CONFLICT", "writer claim is stale or misaddressed")
    if frozen and publication_class == "PRODUCT":
        return Decision("FROZEN_PRODUCT_WRITE_BLOCKED")
    control_prefix = f"Team/Migrations/{migration_id}/"
    if (
        frozen
        and publication_class == "MIGRATION_CONTROL"
        and actor_executor_id == migration_pm_executor_id
        and path.startswith(control_prefix)
    ):
        return Decision("ALLOW")
    if frozen and publication_class == "MIGRATION_CONTROL":
        return Decision("FROZEN_CONTROL_FORBIDDEN")
    return Decision("ALLOW")


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
    receipt_ids = [receipt.get("receipt_id") for receipt in receipts]
    if None in receipt_ids or len(receipt_ids) != len(set(receipt_ids)):
        return Decision("DUPLICATE_RECEIPT_ID")
    return Decision("ALLOW")

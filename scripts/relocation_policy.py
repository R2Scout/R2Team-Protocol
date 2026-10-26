"""Pure policy helpers for R2Team relocation fixtures.

The module models cooperative protocol fencing only. It performs no provider,
chat, registry, process, workspace, or filesystem mutation.
"""

from dataclasses import dataclass
from datetime import date, datetime


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

LEGAL_FENCE_STATES = {
    ("ACTIVE", "INACTIVE", "SOURCE_ACTIVE"),
    ("STOP_REQUESTED", "INACTIVE", "SOURCE_STOPPING"),
    ("STOPPED", "INACTIVE", "SOURCE_STOPPED"),
    ("STOPPED", "PREFLIGHTED", "TARGET_PREFLIGHT"),
    ("STOPPED", "READY", "TARGET_PENDING"),
    ("STOPPED", "ACTIVE", "TARGET_ACTIVE"),
}


def _nonblank(value) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _valid_ref(value) -> bool:
    return (
        _nonblank(value)
        and value == value.strip()
        and not any(character in value for character in ("\x00", "\r", "\n"))
    )


def _valid_ref_collection(value, *, allow_empty: bool) -> bool:
    return (
        isinstance(value, (tuple, list))
        and (allow_empty or bool(value))
        and all(_valid_ref(item) for item in value)
        and len(value) == len(set(value))
    )


def _valid_epoch(value, *, allow_zero: bool = True) -> bool:
    return type(value) is int and value >= (0 if allow_zero else 1)


def _valid_date(value) -> bool:
    if not _valid_ref(value):
        return False
    try:
        return date.fromisoformat(value).isoformat() == value
    except ValueError:
        return False


def _valid_timestamp(value) -> bool:
    if not _valid_ref(value):
        return False
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed.tzinfo is not None


def _canonical_portable_path(path: str) -> bool:
    if not _valid_ref(path) or "\\" in path or path.startswith("/") or "//" in path:
        return False
    return all(
        part not in {"", ".", ".."} and _valid_ref(part)
        for part in path.split("/")
    )


def _valid_field_collection(value, *, allow_empty: bool = False) -> bool:
    if not isinstance(value, (tuple, list)) or (not value and not allow_empty):
        return False
    for field in value:
        if not _nonblank(field) or field != field.strip():
            return False
        if not field[0].isalpha() or any(
            not (character.isalnum() or character == "_") for character in field
        ):
            return False
    return True


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


def _valid_fence(record: FenceRecord) -> bool:
    return (
        isinstance(record, FenceRecord)
        and _valid_ref(record.project_id)
        and _valid_ref(record.executor_id)
        and _valid_epoch(record.epoch)
        and _valid_ref(record.record_ref)
        and (record.source_state, record.target_state, record.custody)
        in LEGAL_FENCE_STATES
    )


def propose_successor(
    accepted: FenceRecord,
    *,
    expected_prior_epoch: int,
    expected_prior_ref: str,
    new_epoch: int,
    new_record_ref: str,
) -> Decision:
    if not _valid_fence(accepted):
        return Decision("FENCE_INVALID")
    if not all(
        (
            _valid_epoch(accepted.epoch),
            _valid_epoch(expected_prior_epoch),
            _valid_epoch(new_epoch, allow_zero=False),
        )
    ):
        return Decision("EPOCH_INVALID")
    if not all(
        _valid_ref(value)
        for value in (
            accepted.project_id,
            accepted.executor_id,
            accepted.record_ref,
            expected_prior_ref,
            new_record_ref,
        )
    ):
        return Decision("WRITER_CONFLICT", "writer identity or record ref is invalid")
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


def _validate_stop_specific(receipt: dict) -> Decision:
    if not isinstance(receipt, dict):
        return Decision("STOP_PROOF_INVALID", "stop receipt is not a record")
    required_refs = {
        "receipt_id",
        "migration_id",
        "repository_or_project_id",
        "executor_id",
        "final_checkpoint",
        "candidate_tree",
        "workspace_custody",
        "native_resource_custody",
        "actor_class",
        "stop_mechanism",
        "cutover_parent",
        "timestamp",
    }
    if any(not _valid_ref(receipt.get(key)) for key in required_refs):
        return Decision("STOP_PROOF_INVALID", "required stop fact is missing")
    if receipt.get("receipt_type") != "SOURCE_STOP":
        return Decision("STOP_PROOF_INVALID", "receipt is not SOURCE_STOP")
    if not _valid_epoch(receipt.get("expected_epoch"), allow_zero=False):
        return Decision("STOP_PROOF_INVALID", "stop expected epoch is invalid")
    for field in ("publishers_in_flight", "helpers_in_flight"):
        if not _valid_ref_collection(receipt.get(field), allow_empty=True):
            return Decision("STOP_PROOF_INVALID", f"{field} is invalid")
    if receipt.get("publishers_in_flight") or receipt.get("helpers_in_flight"):
        return Decision("BLOCKED_IN_FLIGHT", "publisher or helper remains active")
    if receipt["stop_mechanism"] not in {
        "COOPERATIVE_ACK",
        "ADMINISTRATIVE_REVOCATION",
        "MODELED_ENFORCEABLE_FENCE",
    }:
        return Decision("STOP_PROOF_INVALID", "stop mechanism is not accepted")
    if receipt.get("causal_parent_ref") != receipt.get("cutover_parent"):
        return Decision("STOP_PROOF_INVALID", "stop causal parent differs from cutover")
    if receipt.get("final_checkpoint") not in receipt.get("task_checkpoint_refs", ()):
        return Decision("STOP_PROOF_INVALID", "final checkpoint is not in TASK refs")
    if receipt.get("candidate_tree") not in receipt.get("candidate_refs", ()):
        return Decision("STOP_PROOF_INVALID", "candidate tree is not in candidate refs")
    return Decision("ALLOW")


def validate_stop_receipt(receipt: dict) -> Decision:
    if not isinstance(receipt, dict):
        return Decision("STOP_PROOF_INVALID", "stop receipt is not a record")
    specific = _validate_stop_specific(receipt)
    if specific.code == "BLOCKED_IN_FLIGHT":
        return specific
    if specific.code != "ALLOW" or validate_receipt(receipt).code != "ALLOW":
        return Decision("STOP_PROOF_INVALID", specific.reason or "typed stop receipt is invalid")
    return Decision("ALLOW")


def activation_allowed(
    accepted: FenceRecord,
    *,
    stop_receipt: dict | None,
    preflight_receipt: dict | None = None,
    activation_receipt: dict | None,
    source_reachable: bool,
    enforceable_revocation: bool,
) -> Decision:
    if not _valid_fence(accepted):
        return Decision("FENCE_INVALID")
    if type(source_reachable) is not bool or type(enforceable_revocation) is not bool:
        return Decision("ACTIVATION_INPUT_INVALID")
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
    if (
        validate_receipt(preflight_receipt).code != "ALLOW"
        or preflight_receipt.get("receipt_type") != "TARGET_PREFLIGHT"
        or preflight_receipt.get("target_preflight") != "PASS"
    ):
        return Decision("TARGET_PREFLIGHT_REQUIRED")
    if activation_receipt.get("target_preflight") != "PASS":
        return Decision("TARGET_PREFLIGHT_REQUIRED")
    if activation_receipt.get("causal_stop_receipt") != stop_receipt.get("receipt_id"):
        return Decision(
            "ACTIVATION_CAUSAL_MISMATCH",
            "activation does not reference the accepted stop receipt",
        )
    if (
        stop_receipt.get("expected_epoch") != accepted.epoch
        or activation_receipt.get("prior_epoch") != accepted.epoch
        or activation_receipt.get("new_epoch") != accepted.epoch + 1
    ):
        return Decision("ACTIVATION_CAUSAL_MISMATCH", "activation epoch is invalid")
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
    preflight_pairs = (
        (
            activation_receipt.get("target_preflight_receipt"),
            preflight_receipt.get("receipt_id"),
        ),
        (
            preflight_receipt.get("causal_parent_ref"),
            stop_receipt.get("receipt_id"),
        ),
        (preflight_receipt.get("migration_id"), activation_receipt.get("migration_id")),
        (
            preflight_receipt.get("repository_or_project_id"),
            activation_receipt.get("repository_or_project_id"),
        ),
        (preflight_receipt.get("executor_id"), activation_receipt.get("executor_id")),
        (preflight_receipt.get("prior_epoch"), activation_receipt.get("prior_epoch")),
        (preflight_receipt.get("new_epoch"), activation_receipt.get("new_epoch")),
        (
            preflight_receipt.get("accepted_commit_sha"),
            activation_receipt.get("accepted_commit_sha"),
        ),
        (
            preflight_receipt.get("task_checkpoint_refs"),
            activation_receipt.get("task_checkpoint_refs"),
        ),
        (preflight_receipt.get("candidate_refs"), activation_receipt.get("candidate_refs")),
        (
            preflight_receipt.get("workspace_disposition_refs"),
            activation_receipt.get("workspace_disposition_refs"),
        ),
        (
            preflight_receipt.get("registry_evidence"),
            activation_receipt.get("registry_evidence"),
        ),
    )
    if any(actual != expected for actual, expected in preflight_pairs):
        return Decision("ACTIVATION_IDENTITY_MISMATCH")
    if (
        activation_receipt.get("accepted_cutover")
        != activation_receipt.get("accepted_commit_sha")
        or activation_receipt.get("mapping_result")
        != activation_receipt.get("registry_evidence")
    ):
        return Decision("ACTIVATION_IDENTITY_MISMATCH")
    return Decision("ALLOW")


def derive_team_state(
    records: list[dict],
    *,
    affected_executor_ids: tuple[str, ...] | None = None,
    receipts: tuple[dict, ...] = (),
    accepted_root_ref: str | None = None,
    migration_mode: str | None = None,
) -> TeamState:
    invalid = TeamState("INVALID", (), ())
    if (
        not isinstance(records, (tuple, list))
        or not records
        or not _valid_ref_collection(affected_executor_ids, allow_empty=False)
        or any(not isinstance(record, dict) for record in records)
    ):
        return invalid
    executor_ids = [record.get("executor_id") for record in records]
    if (
        not all(_valid_ref(executor_id) for executor_id in executor_ids)
        or len(executor_ids) != len(set(executor_ids))
        or set(executor_ids) != set(affected_executor_ids)
    ):
        return invalid
    valid_dispositions = {
        "PENDING",
        "RESUMED",
        "BLOCKED",
        "CANCELLED",
        "FORWARD_ROLLBACK",
    }
    for record in records:
        if (
            (
                record.get("source_state"),
                record.get("target_state"),
                record.get("custody"),
            )
            not in LEGAL_FENCE_STATES
            or record.get("disposition") not in valid_dispositions
        ):
            return invalid

    active = tuple(
        record["executor_id"]
        for record in records
        if record["target_state"] == "ACTIVE"
    )
    blocked = tuple(
        record["executor_id"]
        for record in records
        if record["disposition"] == "BLOCKED"
    )
    terminal_dispositions = {"BLOCKED", "CANCELLED", "FORWARD_ROLLBACK"}

    def terminal_schema_valid(record: dict) -> bool:
        return (
            record.get("disposition") in terminal_dispositions
            and _valid_ref(record.get("disposition_owner_executor_id"))
            and _valid_date(record.get("review_date"))
            and _valid_ref(record.get("next_action"))
            and _valid_ref(record.get("disposition_receipt_ref"))
        )

    if any(
        record["disposition"] == "RESUMED"
        and not _valid_ref(record.get("disposition_receipt_ref"))
        for record in records
    ):
        return invalid

    completion_ready = all(
        (
            record["target_state"] == "ACTIVE"
            and record["disposition"] == "RESUMED"
            and _valid_ref(record.get("disposition_receipt_ref"))
        )
        or terminal_schema_valid(record)
        for record in records
    )
    if completion_ready:
        graph = receipt_set_allowed(
            receipts,
            accepted_root_ref=accepted_root_ref,
            affected_executor_ids=affected_executor_ids,
            migration_mode=migration_mode,
        )
        if graph.code != "ALLOW":
            return invalid
        by_id = {receipt["receipt_id"]: receipt for receipt in receipts}
        expected_types = {
            "RESUMED": "ACTIVATION",
            "BLOCKED": "PARTIAL_DISPOSITION",
            "CANCELLED": "CANCELLATION",
            "FORWARD_ROLLBACK": "FORWARD_ROLLBACK",
        }
        for record in records:
            receipt = by_id.get(record["disposition_receipt_ref"])
            terminal_receipts = [
                candidate
                for candidate in receipts
                if candidate.get("executor_id") == record["executor_id"]
                and (
                    candidate.get("receipt_type")
                    in {"ACTIVATION", "CANCELLATION", "FORWARD_ROLLBACK"}
                    or (
                        candidate.get("receipt_type") == "PARTIAL_DISPOSITION"
                        and candidate.get("terminal_disposition") == "BLOCKED"
                    )
                )
            ]
            latest_epoch = max(candidate["new_epoch"] for candidate in terminal_receipts)
            latest_ids = {
                candidate["receipt_id"]
                for candidate in terminal_receipts
                if candidate["new_epoch"] == latest_epoch
            }
            if (
                receipt is None
                or receipt.get("receipt_type") != expected_types[record["disposition"]]
                or receipt.get("executor_id") != record["executor_id"]
                or latest_ids != {receipt.get("receipt_id")}
                or (
                    record["disposition"] == "BLOCKED"
                    and receipt.get("terminal_disposition") != "BLOCKED"
                )
            ):
                return invalid
        return TeamState("COMPLETE", active, blocked)

    if any(record["disposition"] in terminal_dispositions for record in records):
        return invalid
    if all(
        record["source_state"] == "STOPPED"
        and record["target_state"] == "READY"
        for record in records
    ):
        return TeamState("READY_TO_RESUME", active, blocked)
    if all(
        record["source_state"] == "STOPPED"
        and record["target_state"] == "INACTIVE"
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
    if (
        not _valid_epoch(current_epoch)
        or not _valid_epoch(proposed_epoch)
        or source_state not in {"ACTIVE", "STOP_REQUESTED", "STOPPED"}
        or target_state not in {"INACTIVE", "PREFLIGHTED", "READY", "ACTIVE"}
    ):
        return Decision("EPOCH_INVALID")
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
    if not _valid_fence(accepted):
        return Decision("FENCE_INVALID")
    if type(frozen) is not bool:
        return Decision("PUBLICATION_INPUT_INVALID", "freeze state is not boolean")
    if not _valid_epoch(claim_epoch):
        return Decision("EPOCH_INVALID")
    if not all(
        _valid_ref(value)
        for value in (
            claim_project_id,
            claim_executor_id,
            claim_record_ref,
            actor_executor_id,
            migration_pm_executor_id,
            migration_id,
        )
    ):
        return Decision("PUBLICATION_INPUT_INVALID")
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
        and _valid_field_collection(governing_task_fields)
        and _valid_field_collection(claimed_fields)
        and set(claimed_fields).issubset(set(governing_task_fields))
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
    if (
        not _valid_ref(expected_executor_id)
        or executor_mode not in {
            "local_standalone",
            "same_chat",
            "persistent_subagent",
            "remote_manual",
        }
        or any(
            type(value) is not bool
            for value in (mapping_present, local_authority, read_back, collision)
        )
        or (
            observed_executor_id is not None
            and not _valid_ref(observed_executor_id)
        )
    ):
        return Decision("REGISTRY_INPUT_INVALID")
    if collision:
        return Decision("REGISTRY_CONFLICT")
    if executor_mode == "remote_manual" and not mapping_present:
        if observed_executor_id is not None:
            return Decision("REGISTRY_CONFLICT")
        return Decision("ALLOW_REMOTE_MANUAL")
    if not mapping_present or observed_executor_id != expected_executor_id:
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
    reference_fields = required - {"contained"}
    if (
        not isinstance(expected, dict)
        or not isinstance(observed, dict)
        or any(key not in expected or observed.get(key) != expected[key] for key in required)
        or any(
            not _valid_ref(expected.get(key)) or not _valid_ref(observed.get(key))
            for key in reference_fields
        )
        or type(expected.get("contained")) is not bool
        or type(observed.get("contained")) is not bool
    ):
        return Decision("WORKSPACE_REUSE_BLOCKED", "workspace custody facts differ")
    return Decision("ALLOW")


def affected_set_allowed(
    *,
    affected_executor_ids: tuple[str, ...],
    retained_executor_ids: tuple[str, ...],
    migration_state: str,
) -> Decision:
    valid_states = {
        "REQUESTED",
        "PREPARING",
        "PREPARED",
        "FREEZE_PENDING",
        "FROZEN",
        "READY_TO_RESUME",
        "RESUMING",
        "PARTIAL_BLOCKED",
        "COMPLETE",
        "BLOCKED",
    }
    if (
        not _valid_ref_collection(affected_executor_ids, allow_empty=False)
        or not _valid_ref_collection(retained_executor_ids, allow_empty=True)
        or migration_state not in valid_states
    ):
        return Decision("AFFECTED_SET_INVALID")
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


def receipt_set_allowed(
    receipts: tuple[dict, ...],
    *,
    accepted_root_ref: str | None = None,
    affected_executor_ids: tuple[str, ...] | None = None,
    migration_mode: str | None = None,
) -> Decision:
    if not isinstance(receipts, (tuple, list)) or not receipts:
        return Decision("RECEIPT_INVALID")
    for receipt in receipts:
        if validate_receipt(receipt).code != "ALLOW":
            return Decision("RECEIPT_INVALID")
    receipt_ids = [receipt.get("receipt_id") for receipt in receipts]
    if len(receipt_ids) != len(set(receipt_ids)):
        return Decision("DUPLICATE_RECEIPT_ID")
    if accepted_root_ref is None:
        return Decision("RECEIPT_CONTEXT_REQUIRED")
    if not _valid_ref(accepted_root_ref):
        return Decision("RECEIPT_INVALID", "accepted root is invalid")
    if accepted_root_ref in receipt_ids:
        return Decision("RECEIPT_INVALID", "accepted root aliases a receipt")
    if migration_mode not in {"role", "team"}:
        return Decision("RECEIPT_CONTEXT_REQUIRED", "migration mode is required")
    if affected_executor_ids is not None and not _valid_ref_collection(
        affected_executor_ids, allow_empty=False
    ):
        return Decision("RECEIPT_INVALID", "affected executor context is invalid")

    by_id = {receipt["receipt_id"]: receipt for receipt in receipts}
    prepare_receipts = [
        receipt for receipt in receipts if receipt["receipt_type"] == "PREPARE"
    ]
    if len(prepare_receipts) > 1:
        return Decision("RECEIPT_INVALID", "multiple PREPARE roots")
    prepared_affected = (
        tuple(prepare_receipts[0]["affected_executor_ids"])
        if prepare_receipts
        else None
    )
    if affected_executor_ids is None:
        affected_executor_ids = prepared_affected
    elif prepared_affected is not None and set(affected_executor_ids) != set(
        prepared_affected
    ):
        return Decision("RECEIPT_INVALID", "affected executor context differs")
    if (
        affected_executor_ids is not None
        and migration_mode == "role"
        and len(affected_executor_ids) != 1
    ):
        return Decision("RECEIPT_INVALID", "role mode requires one executor")
    if (
        affected_executor_ids is not None
        and migration_mode == "team"
        and len(affected_executor_ids) < 2
    ):
        return Decision("RECEIPT_INVALID", "team mode requires multiple executors")

    allowed_parent_types = {
        "FREEZE": {"PREPARE"},
        "SOURCE_STOP": {"FORWARD_ROLLBACK"},
        "TARGET_PREFLIGHT": {"SOURCE_STOP", "FREEZE"},
        "ACTIVATION": {"SOURCE_STOP"},
        "PARTIAL_DISPOSITION": {"TARGET_PREFLIGHT", "ACTIVATION"},
        "COMPLETION": {
            "ACTIVATION",
            "PARTIAL_DISPOSITION",
            "CANCELLATION",
            "FORWARD_ROLLBACK",
        },
        "CANCELLATION": {
            "PREPARE",
            "SOURCE_STOP",
            "FREEZE",
            "TARGET_PREFLIGHT",
            "PARTIAL_DISPOSITION",
        },
        "FORWARD_ROLLBACK": {"ACTIVATION"},
    }

    logical_event_keys = [
        (
            receipt["receipt_type"],
            receipt.get("executor_id"),
            receipt.get("prior_epoch"),
            receipt.get("new_epoch"),
            receipt.get("causal_parent_ref"),
        )
        for receipt in receipts
    ]
    if len(logical_event_keys) != len(set(logical_event_keys)):
        return Decision("RECEIPT_INVALID", "logical receipt event is duplicated")

    for receipt in receipts:
        receipt_type = receipt["receipt_type"]
        executor_id = receipt.get("executor_id")
        if (
            affected_executor_ids is not None
            and executor_id is not None
            and executor_id not in affected_executor_ids
        ):
            return Decision("RECEIPT_INVALID", "receipt executor is not affected")
        if receipt_type == "PREPARE":
            if receipt["causal_parent_ref"] != accepted_root_ref:
                return Decision("RECEIPT_INVALID", "receipt root edge differs")
            continue

        if receipt_type == "SOURCE_STOP" and receipt["causal_parent_ref"] == accepted_root_ref:
            if prepare_receipts:
                prepare = prepare_receipts[0]
                root_pairs = (
                    (receipt.get("migration_id"), prepare.get("migration_id")),
                    (
                        receipt.get("repository_or_project_id"),
                        prepare.get("repository_or_project_id"),
                    ),
                    (receipt.get("task_checkpoint_refs"), prepare.get("task_checkpoint_refs")),
                    (receipt.get("candidate_refs"), prepare.get("candidate_refs")),
                    (
                        receipt.get("workspace_disposition_refs"),
                        prepare.get("workspace_disposition_refs"),
                    ),
                )
                if any(actual != expected for actual, expected in root_pairs):
                    return Decision("RECEIPT_INVALID", "root stop lineage differs")
            continue

        parent = by_id.get(receipt["causal_parent_ref"])
        if (
            parent is None
            or parent.get("receipt_type") not in allowed_parent_types[receipt_type]
        ):
            return Decision("RECEIPT_INVALID", "receipt causal edge is unresolved")
        identity_pairs = (
            (receipt.get("migration_id"), parent.get("migration_id")),
            (
                receipt.get("repository_or_project_id"),
                parent.get("repository_or_project_id"),
            ),
            (receipt.get("prior_epoch"), parent.get("new_epoch")),
            (receipt.get("task_checkpoint_refs"), parent.get("task_checkpoint_refs")),
            (receipt.get("candidate_refs"), parent.get("candidate_refs")),
            (
                receipt.get("workspace_disposition_refs"),
                parent.get("workspace_disposition_refs"),
            ),
        )
        if any(actual != expected for actual, expected in identity_pairs):
            return Decision("RECEIPT_INVALID", "receipt edge identity differs")
        if (
            executor_id is not None
            and parent.get("executor_id") is not None
            and executor_id != parent.get("executor_id")
        ):
            return Decision("RECEIPT_INVALID", "receipt edge executor differs")

        if receipt_type == "ACTIVATION":
            stop = by_id.get(receipt["causal_stop_receipt"])
            preflight = by_id.get(receipt["target_preflight_receipt"])
            if (
                stop is not parent
                or preflight is None
                or preflight.get("receipt_type") != "TARGET_PREFLIGHT"
                or preflight.get("causal_parent_ref") != stop.get("receipt_id")
            ):
                return Decision("RECEIPT_INVALID", "activation evidence edge is unresolved")
            activation_pairs = (
                (receipt.get("migration_id"), preflight.get("migration_id")),
                (
                    receipt.get("repository_or_project_id"),
                    preflight.get("repository_or_project_id"),
                ),
                (receipt.get("executor_id"), preflight.get("executor_id")),
                (receipt.get("prior_epoch"), preflight.get("prior_epoch")),
                (receipt.get("new_epoch"), preflight.get("new_epoch")),
                (receipt.get("target_preflight"), preflight.get("target_preflight")),
                (receipt.get("registry_evidence"), preflight.get("registry_evidence")),
                (receipt.get("accepted_commit_sha"), preflight.get("accepted_commit_sha")),
            )
            if any(actual != expected for actual, expected in activation_pairs):
                return Decision("RECEIPT_INVALID", "activation preflight evidence differs")

        if receipt_type == "FREEZE":
            if (
                affected_executor_ids is None
                or set(receipt["affected_executor_ids"])
                != set(affected_executor_ids)
                or set(receipt["stopped_executor_ids"])
                != set(affected_executor_ids)
            ):
                return Decision("RECEIPT_INVALID", "freeze affected set differs")
            stop_refs = receipt["source_stop_receipt_refs"]
            stops = [by_id.get(stop_ref) for stop_ref in stop_refs]
            if any(stop is None or stop.get("receipt_type") != "SOURCE_STOP" for stop in stops):
                return Decision("RECEIPT_INVALID", "freeze stop edge is unresolved")
            if set(receipt["stopped_executor_ids"]) != {
                stop["executor_id"] for stop in stops
            }:
                return Decision("RECEIPT_INVALID", "freeze stopped set differs")
            for stop in stops:
                freeze_stop_pairs = (
                    (receipt.get("migration_id"), stop.get("migration_id")),
                    (
                        receipt.get("repository_or_project_id"),
                        stop.get("repository_or_project_id"),
                    ),
                    (receipt.get("task_checkpoint_refs"), stop.get("task_checkpoint_refs")),
                    (receipt.get("candidate_refs"), stop.get("candidate_refs")),
                    (
                        receipt.get("workspace_disposition_refs"),
                        stop.get("workspace_disposition_refs"),
                    ),
                )
                if any(actual != expected for actual, expected in freeze_stop_pairs):
                    return Decision("RECEIPT_INVALID", "freeze stop evidence differs")

        if receipt_type == "CANCELLATION" and receipt["source_state"] == "STOPPED":
            stop = by_id.get(receipt["causal_stop_receipt"])
            if stop is not parent or stop.get("receipt_type") != "SOURCE_STOP":
                return Decision("RECEIPT_INVALID", "cancellation stop edge is unresolved")

        if receipt_type == "FORWARD_ROLLBACK":
            activation = by_id.get(receipt["causal_activation_receipt"])
            if activation is not parent or activation.get("receipt_type") != "ACTIVATION":
                return Decision("RECEIPT_INVALID", "rollback activation edge is unresolved")

    completions = [
        receipt for receipt in receipts if receipt["receipt_type"] == "COMPLETION"
    ]
    if completions:
        if (
            len(completions) != 1
            or affected_executor_ids is None
            or len(prepare_receipts) != 1
        ):
            return Decision("RECEIPT_INVALID", "completion context is incomplete")
        completion = completions[0]
        if set(completion["accounted_executor_ids"]) != set(affected_executor_ids):
            return Decision("RECEIPT_INVALID", "completion affected set differs")
        if migration_mode == "team":
            freezes = [
                receipt for receipt in receipts if receipt["receipt_type"] == "FREEZE"
            ]
            if len(freezes) != 1:
                return Decision("RECEIPT_INVALID", "team completion requires one freeze")
            freeze = freezes[0]
            if (
                set(freeze["affected_executor_ids"]) != set(affected_executor_ids)
                or set(freeze["stopped_executor_ids"]) != set(affected_executor_ids)
            ):
                return Decision("RECEIPT_INVALID", "team freeze affected set differs")
            root_stops = {
                receipt["receipt_id"]
                for receipt in receipts
                if receipt["receipt_type"] == "SOURCE_STOP"
                and receipt["causal_parent_ref"] == accepted_root_ref
                and receipt.get("executor_id") in affected_executor_ids
            }
            if set(freeze["source_stop_receipt_refs"]) != root_stops:
                return Decision("RECEIPT_INVALID", "team freeze stop set differs")

        latest_terminal_ids = set()
        for executor_id in affected_executor_ids:
            terminal = [
                receipt
                for receipt in receipts
                if receipt.get("executor_id") == executor_id
                and (
                    receipt["receipt_type"]
                    in {"ACTIVATION", "CANCELLATION", "FORWARD_ROLLBACK"}
                    or (
                        receipt["receipt_type"] == "PARTIAL_DISPOSITION"
                        and receipt.get("terminal_disposition") == "BLOCKED"
                    )
                )
            ]
            if not terminal:
                return Decision("RECEIPT_INVALID", "executor terminal state is not unique")
            latest_epoch = max(receipt["new_epoch"] for receipt in terminal)
            latest = [
                receipt for receipt in terminal if receipt["new_epoch"] == latest_epoch
            ]
            if len(latest) != 1:
                return Decision("RECEIPT_INVALID", "executor terminal state is not unique")
            latest_terminal_ids.add(latest[0]["receipt_id"])
        if completion["causal_parent_ref"] not in latest_terminal_ids:
            return Decision("RECEIPT_INVALID", "completion parent is not latest terminal")
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
    }
    if any(not _valid_ref(receipt.get(field)) for field in common_nonblank):
        return Decision("RECEIPT_INVALID", "common receipt fact is missing")
    if not _valid_timestamp(receipt.get("timestamp")) or not _valid_date(receipt.get("review_date")):
        return Decision("RECEIPT_INVALID", "receipt time or review date is invalid")
    if receipt.get("receipt_type") not in RECEIPT_TYPES:
        return Decision("RECEIPT_INVALID", "receipt type is unknown")
    receipt_type = receipt["receipt_type"]
    global_types = {"PREPARE", "FREEZE", "COMPLETION"}
    if receipt_type not in global_types and not _valid_ref(receipt.get("executor_id")):
        return Decision("RECEIPT_INVALID", "executor identity is missing")
    if receipt_type in global_types and receipt.get("executor_id") is not None and not _valid_ref(receipt.get("executor_id")):
        return Decision("RECEIPT_INVALID", "executor identity is malformed")
    prior_epoch = receipt.get("prior_epoch")
    new_epoch = receipt.get("new_epoch")
    if (
        not _valid_epoch(prior_epoch)
        or not _valid_epoch(new_epoch, allow_zero=False)
        or new_epoch != prior_epoch + 1
    ):
        return Decision("RECEIPT_INVALID", "receipt epoch is invalid")
    for field in ("task_checkpoint_refs", "candidate_refs", "workspace_disposition_refs"):
        value = receipt.get(field)
        if not _valid_ref_collection(
            value,
            allow_empty=field == "workspace_disposition_refs",
        ):
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
        "FREEZE": {
            "affected_executor_ids",
            "stopped_executor_ids",
            "source_stop_receipt_refs",
        },
        "TARGET_PREFLIGHT": {"target_preflight", "target_placement_class"},
        "ACTIVATION": {
            "causal_stop_receipt",
            "target_preflight_receipt",
            "cutover_parent",
            "accepted_cutover",
            "target_preflight",
            "task_checkpoint",
            "candidate_tree",
            "workspace_custody",
            "actor_class",
            "mapping_result",
        },
        "PARTIAL_DISPOSITION": {"blocked_from_state", "permitted_successors"},
        "COMPLETION": {"accounted_executor_ids"},
        "CANCELLATION": {"terminal_disposition", "source_state", "target_state"},
        "FORWARD_ROLLBACK": {"rollback_target_epoch", "causal_activation_receipt"},
    }
    for field in type_fields[receipt_type]:
        value = receipt.get(field)
        if field in {
            "affected_executor_ids",
            "stopped_executor_ids",
            "permitted_successors",
            "accounted_executor_ids",
            "source_stop_receipt_refs",
        }:
            if not _valid_ref_collection(value, allow_empty=False):
                return Decision("RECEIPT_INVALID", "type-specific collection is invalid")
        elif field == "rollback_target_epoch":
            if not _valid_epoch(value, allow_zero=False):
                return Decision("RECEIPT_INVALID", "rollback epoch is invalid")
        elif not _valid_ref(value):
            return Decision("RECEIPT_INVALID", "type-specific receipt fact is invalid")
    if receipt_type == "SOURCE_STOP":
        stop = _validate_stop_specific(receipt)
        if stop.code != "ALLOW":
            return Decision("RECEIPT_INVALID", stop.reason)
        if not _valid_epoch(receipt.get("expected_epoch"), allow_zero=False) or receipt.get("expected_epoch") != new_epoch:
            return Decision("RECEIPT_INVALID", "stop expected epoch is invalid")
    if receipt_type == "ACTIVATION":
        if receipt.get("target_preflight") != "PASS":
            return Decision("RECEIPT_INVALID", "activation preflight is not PASS")
        if receipt.get("task_checkpoint") not in receipt.get("task_checkpoint_refs", ()):
            return Decision("RECEIPT_INVALID", "activation checkpoint is not in TASK refs")
        if receipt.get("candidate_tree") not in receipt.get("candidate_refs", ()):
            return Decision("RECEIPT_INVALID", "activation tree is not in candidate refs")
        if receipt.get("mapping_result") not in {
            "NOT_APPLICABLE",
            "MAPPING_PRESENT_READ_BACK",
            "MAPPING_ABSENT",
            "MAPPING_CONFLICT",
        }:
            return Decision("RECEIPT_INVALID", "activation mapping result is invalid")
        if (
            receipt.get("accepted_cutover") != receipt.get("accepted_commit_sha")
            or receipt.get("mapping_result") != receipt.get("registry_evidence")
        ):
            return Decision("RECEIPT_INVALID", "activation accepted evidence differs")
        if receipt.get("actor_provider_class") == "remote-manual":
            if receipt.get("mapping_result") not in {
                "NOT_APPLICABLE",
                "MAPPING_ABSENT",
            }:
                return Decision("RECEIPT_INVALID", "remote activation mapping is invalid")
        elif receipt.get("mapping_result") != "MAPPING_PRESENT_READ_BACK":
            return Decision("RECEIPT_INVALID", "local activation mapping is not read back")
    if receipt_type == "PREPARE" and receipt.get("observed_outcome") != "PREPARED":
        return Decision("RECEIPT_INVALID", "prepare outcome is invalid")
    if receipt_type == "FREEZE":
        if (
            receipt.get("observed_outcome") != "FROZEN"
            or set(receipt["affected_executor_ids"])
            != set(receipt["stopped_executor_ids"])
            or len(receipt["source_stop_receipt_refs"])
            != len(receipt["stopped_executor_ids"])
        ):
            return Decision("RECEIPT_INVALID", "freeze accounting is invalid")
    if receipt_type == "TARGET_PREFLIGHT":
        preflight_outcomes = {
            "PASS": "TARGET_PREFLIGHT_PASS",
            "BLOCKED": "TARGET_PREFLIGHT_BLOCKED",
            "FAIL": "TARGET_PREFLIGHT_FAIL",
        }
        if (
            receipt.get("target_preflight") not in preflight_outcomes
            or receipt.get("observed_outcome")
            != preflight_outcomes.get(receipt.get("target_preflight"))
        ):
            return Decision("RECEIPT_INVALID", "target preflight result is invalid")
    if receipt_type == "ACTIVATION" and receipt.get("observed_outcome") != "TARGET_ACTIVE":
        return Decision("RECEIPT_INVALID", "activation outcome is invalid")
    if receipt_type == "PARTIAL_DISPOSITION":
        blocked_states = {
            "PREPARING",
            "PREPARED",
            "FREEZE_PENDING",
            "FROZEN",
            "READY_TO_RESUME",
            "RESUMING",
            "PARTIAL_BLOCKED",
            "BLOCKED",
        }
        expected_successors = {
            receipt.get("blocked_from_state"),
            "CANCELLATION",
            "FORWARD_ROLLBACK",
        }
        terminal = receipt.get("terminal_disposition")
        if terminal is None:
            outcome_valid = receipt.get("observed_outcome") == "PARTIAL_BLOCKED"
        else:
            outcome_valid = (
                terminal == "BLOCKED"
                and receipt.get("observed_outcome") == "TERMINAL_BLOCKED"
                and _valid_ref(receipt.get("disposition_owner_executor_id"))
                and _valid_ref(receipt.get("next_action"))
                and receipt.get("disposition_receipt_ref") == receipt.get("receipt_id")
            )
        if (
            not outcome_valid
            or receipt.get("blocked_from_state") not in blocked_states
            or set(receipt.get("permitted_successors", ())) != expected_successors
        ):
            return Decision("RECEIPT_INVALID", "partial disposition is invalid")
    if receipt_type == "COMPLETION" and receipt.get("observed_outcome") != "COMPLETE":
        return Decision("RECEIPT_INVALID", "completion outcome is invalid")
    if receipt_type == "CANCELLATION":
        source_state = receipt.get("source_state")
        target_state = receipt.get("target_state")
        terminal = receipt.get("terminal_disposition")
        if source_state == "ACTIVE" and target_state == "INACTIVE":
            valid = terminal == "SOURCE_RETAINED" and receipt.get("causal_stop_receipt") is None
        elif source_state == "STOPPED" and target_state in {"INACTIVE", "PREFLIGHTED", "READY"}:
            valid = terminal == "REACTIVATION_REQUIRED" and _valid_ref(
                receipt.get("causal_stop_receipt")
            )
        else:
            valid = False
        if not valid or receipt.get("observed_outcome") != terminal:
            return Decision("RECEIPT_INVALID", "cancellation disposition is invalid")
    if receipt_type == "FORWARD_ROLLBACK":
        if (
            receipt.get("observed_outcome") != "FORWARD_ROLLBACK"
            or receipt.get("rollback_target_epoch") != new_epoch
            or receipt.get("rollback_target_epoch") <= prior_epoch
        ):
            return Decision("RECEIPT_INVALID", "forward rollback epoch is invalid")
    if (
        receipt_type == "ACTIVATION"
        and receipt.get("causal_parent_ref") != receipt.get("causal_stop_receipt")
    ):
        return Decision("RECEIPT_INVALID", "activation causal parent is invalid")
    return Decision("ALLOW")

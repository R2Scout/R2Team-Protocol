# R2Team relocation bundle template

Store one accepted bundle at `Team/Migrations/<migration-id>/`. Keep populated physical thread IDs, machine paths, credentials, transcripts, and stable hashes of private identifiers outside Git.

## Global migration record

```yaml
migration_id: "<migration-id>"
mode: role|team
state: REQUESTED|PREPARING|PREPARED|FREEZE_PENDING|FROZEN|READY_TO_RESUME|RESUMING|PARTIAL_BLOCKED|COMPLETE|BLOCKED
pm_executor_id: "<executor-id>"
repository_or_project_id: "<portable-provider-identity>"
protocol_ref: "<accepted-protocol-ref>"
source_cutover_sha: "<full-sha>"
global_cutover_generation: 1
affected_executor_ids: ["<executor-id>"]
retained_before_freeze_executor_ids: []
target_placement_classes: ["<portable-placement-class>"]
startup_order: ["<executor-id>"]
migration_control_paths:
  - "Team/Migrations/<migration-id>/**"
  - "<governing-relocation-task-status-and-evidence-fields>"
role_records:
  - "roles/<executor-id>.md"
receipt_index: []
workspace_disposition_refs: []
registry_read_back_result: NOT_APPLICABLE|MAPPING_PRESENT_READ_BACK|MAPPING_ABSENT|MAPPING_CONFLICT
fencing_strength: cooperative protocol fencing
provider_enforced_exclusion: NOT_PROVEN
blocker: null
review_date: "<yyyy-mm-dd>"
next_action: "<permitted-transition>"
```

Unless a separate administrative-revocation receipt proves otherwise, provider-enforced exclusion is NOT_PROVEN.

The aggregate state is derived from every affected executor record. A retained executor must be removed from `affected_executor_ids` by an accepted prepare revision before `FREEZE_PENDING`.

## Per-executor fencing record

Store at `roles/<executor-id>.md`:

```yaml
executor_id: "<executor-id>"
repository_or_project_id: "<portable-provider-identity>"
functions: ["<function>"]
current_epoch: 1
expected_prior_epoch: 0
prior_accepted_record: "<accepted-record-ref>"
source_state: ACTIVE|STOP_REQUESTED|STOPPED
target_state: INACTIVE|PREFLIGHTED|READY|ACTIVE
physical_custody_class: SOURCE_ACTIVE|SOURCE_STOPPED|TARGET_PENDING|TARGET_ACTIVE|BLOCKED
active_task_refs: ["<task-ref>"]
candidate_refs: ["<candidate-sha-and-tree-ref>"]
provider_routes: ["<portable-route>"]
workspace_disposition_refs: ["<lease-or-receipt-ref>"]
stop_receipt_ref: null
activation_receipt_ref: null
blocked_from_state: null
permitted_successors: []
disposition: PENDING|RESUMED|BLOCKED|CANCELLED|FORWARD_ROLLBACK
owner_executor_id: "<executor-id>"
review_date: "<yyyy-mm-dd>"
next_action: "<permitted-transition>"
```

Two proposals with the same next epoch are conflicting until one accepted causal successor is read back. Every writer-capable R2Team entry point re-reads this accepted record before publication and returns `WRITER_CONFLICT` for stale/equal-conflicting/unrelated state.

## Immutable receipt template

Store each receipt at `receipts/<receipt-id>.md`. Do not edit or reuse an ID.

```yaml
receipt_id: "<receipt-id>"
receipt_type: PREPARE|SOURCE_STOP|FREEZE|TARGET_PREFLIGHT|ACTIVATION|PARTIAL_DISPOSITION|COMPLETION|CANCELLATION|FORWARD_ROLLBACK
migration_id: "<migration-id>"
executor_id: "<executor-id-or-null>"
prior_epoch: 0
new_epoch: 1
causal_parent_ref: "<receipt-or-accepted-record-ref>"
accepted_commit_sha: "<full-sha-of-prior-transition>"
task_checkpoint_refs: ["<task-ref>"]
candidate_refs: ["<candidate-ref>"]
workspace_disposition_refs: ["<workspace-ref>"]
close_receipt_refs: []
actor_executor_id: "<executor-id>"
actor_provider_class: "<portable-class>"
observed_outcome: "<result-enum>"
registry_evidence: NOT_APPLICABLE|MAPPING_PRESENT_READ_BACK|MAPPING_ABSENT|MAPPING_CONFLICT
remaining_blocker: null
timestamp: "<iso-8601>"
review_date: "<yyyy-mm-dd-or-null>"
```

`SOURCE_STOP` additionally records final TASK/product checkpoint and candidate tree, publisher/helper state, workspace/native-resource custody, stop mechanism, and cutover parent. `ACTIVATION` causally references the accepted stop receipt and cutover, exact target preflight, executor/TASK/candidate/workspace facts, and new accepted epoch.

Allowed stop mechanisms are cooperative acknowledgement after final checkpoint, independently verifiable administrative revocation, or another explicitly modeled enforceable fence. Silence, notification delivery, registry state, chat title/archive, or absence of an observed process is not stop proof.

`MAPPING_PRESENT_READ_BACK` is an enum, not a place for the private mapping. Local evidence never grants assignment, permission, identity, epoch, or acceptance.

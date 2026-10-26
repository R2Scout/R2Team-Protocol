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
disposition_receipt_ref: null
disposition_owner_executor_id: null
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
repository_or_project_id: "<portable-provider-identity>"
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

`SOURCE_STOP` additionally records exact `SOURCE_STOPPED` outcome, final TASK/product checkpoint and candidate tree, publisher/helper state, workspace/native-resource custody, stop mechanism, and cutover parent. `FREEZE` records exact affected/stopped executor sets plus the corresponding source-stop receipt refs. In team mode every `TARGET_PREFLIGHT` records `freeze_receipt_ref` to that exact full-set FREEZE, and timestamps strictly satisfy `SOURCE_STOP < FREEZE < TARGET_PREFLIGHT < ACTIVATION`. `ACTIVATION` causally references both the accepted stop and target-preflight receipts and binds its accepted cutover to `accepted_commit_sha`, its mapping result to `registry_evidence`, exact executor/TASK/candidate/workspace facts, and new accepted epoch. `CANCELLATION` records source/target state and either `SOURCE_RETAINED` before stop or `REACTIVATION_REQUIRED` after stop. `FORWARD_ROLLBACK` references a prior activation and uses its strictly higher new epoch as `rollback_target_epoch`. `COMPLETION` accounts the exact affected-executor set.

Allowed stop mechanisms are cooperative acknowledgement after final checkpoint, independently verifiable administrative revocation, or another explicitly modeled enforceable fence. Silence, notification delivery, registry state, chat title/archive, or absence of an observed process is not stop proof.

`MAPPING_PRESENT_READ_BACK` is an enum, not a place for the private mapping. Local evidence never grants assignment, permission, identity, epoch, or acceptance.

All epoch values are strict non-boolean integers. IDs, causal/cutover/commit refs, singular checkpoint/tree/custody facts, and every TASK/candidate/workspace list element are nonblank portable strings with no duplicate list entries. `SOURCE_STOP.causal_parent_ref` equals its `cutover_parent` unless an accepted future schema explicitly names an intermediate parent; singular checkpoint/tree facts must appear in their corresponding reference lists.

Validate a receipt set with an external accepted-root ref, exact affected-executor set, and explicit `role` or `team` mode. Completion requires exactly one PREPARE; initial SOURCE_STOP receipts bind the same PREPARE lineage, while later-generation SOURCE_STOP may follow a forward-rollback receipt. Every other receipt resolves an allowed included parent with matching migration/project, executor where applicable, epoch, TASK/candidate, and workspace facts. Team completion requires one FREEZE whose affected/stopped sets and stop refs exactly cover the accepted set. Receipt types may recur at later epochs; only a duplicate executor/type/epoch/parent logical event is invalid. Completion resolves one unique latest ACTIVATION, CANCELLATION, FORWARD_ROLLBACK, or typed terminal BLOCKED disposition per executor. Non-complete aggregate state resolves the unique latest causal stage per executor; same-epoch alternatives are invalid except one activation paired with its one supporting preflight.

Aggregate state input contains exactly one record for every affected executor, a legal source/target/custody tuple, the minimum receipt graph for its claimed FROZEN/READY_TO_RESUME/RESUMING state, and a disposition receipt ref that resolves to that executor's latest graph terminal when completing. Historical PASS preflight or activation evidence cannot satisfy a current state after a later blocked, cancelled, or rolled-back generation. Terminal owner/action/reference strings and review dates are strictly validated. Empty, missing, extra, duplicated, impossible, malformed, unresolved, ambiguous, wrong-executor, or stale-generation records/context produce `INVALID` rather than an authoritative state.

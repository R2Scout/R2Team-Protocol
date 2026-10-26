# R2Team 2.7 team and chat relocation design

## State machines

Migration control state:

```text
REQUESTED -> PREPARING -> PREPARED -> FREEZE_PENDING -> FROZEN
  -> READY_TO_RESUME -> RESUMING -> COMPLETE
```

Per-executor source state:

```text
ACTIVE -> STOP_REQUESTED -> STOPPED
```

Per-executor target state:

```text
INACTIVE -> PREFLIGHTED -> READY -> ACTIVE
```

Any nonterminal transition may enter `BLOCKED` with `blocked_from_state`, owner, review date, next action, and one or more permitted successors. Whole-team aggregate state is derived from the per-executor records. `PARTIAL_BLOCKED` means at least one executor is target-active and at least one affected executor is stopped or blocked; it may return to `RESUMING`, reach `COMPLETE` after every executor has a terminal accounted disposition, or start a forward rollback. It never rewrites an already resumed executor as source-active.

An executor is `retained` only if the accepted prepare record removes it from the affected set before `FREEZE_PENDING`. Otherwise it remains affected and must be stopped, resumed, blocked, cancelled through an accepted transition, or rolled forward. A retained source-active exception inside the frozen affected set is invalid.

## Record layout

```text
Team/Migrations/<migration-id>/
  MIGRATION.md
  roles/
    <executor-id>.md
  receipts/
    <receipt-id>.md
```

`MIGRATION.md` records:

- migration ID, mode, state, PM, created/review dates;
- repository/provider identity, source cutover SHA, protocol ref;
- affected executor IDs and aggregate custody derived from their records;
- per-role handoff paths, active TASK references, provider routes;
- target placement class without physical paths/thread IDs;
- global cutover generation, freeze evidence, startup order, resume gates, and receipt index;
- workspace lease dispositions and local-registry remap requirement;
- forward rollback rule, blockers, remaining NOT_RUN axes.

Each role handoff records repository/project identity, executor/functions, current epoch, expected prior epoch, prior accepted fencing record, source/target states, physical-custody class, source checkpoint, active TASK IDs/paths/checkpoints/candidates/next actions, open provider questions, required setup facts, workspace custody summary, stop/activation receipts, and disposition. It references existing records rather than duplicating them.

## Prepare flow

1. Resolve accepted TASK/TEAM/protocol/provider state and migration authority.
2. Inventory all current assignments for each affected executor, including newly discoverable TASK IDs.
3. Publish or identify a recoverable checkpoint for each active TASK and candidate.
4. Reconcile active workspace leases under 2.6; choose retained, transferred, or closed custody without cleanup inference.
5. Verify target placement, access/tool prerequisites, owner routes, and one future writer.
6. Collect role handoffs and publish the bundle through protected Git workflow with each proposed successor naming its expected prior epoch and accepted causal parent.
7. Compare the proposal against the accepted default branch immediately before publication; a changed epoch or causal parent is `WRITER_CONFLICT` and fails closed.
8. Prove old writer stop per executor and set that source to `STOPPED`; only the accepted PM executor may publish migration-control paths declared in the bundle.
9. Derive `FROZEN` only when every affected source is stopped and there is no unaccounted writer/helper publication.
10. After provider read-back of the accepted cutover commit, set eligible targets to `READY` and derive `READY_TO_RESUME`.

## Resume flow

1. Replacement PM verifies repository/provider identity, accepted default branch, bundle, per-executor epoch/causal parent, state, and old-writer stop.
2. It creates or connects only physical chats explicitly authorized by target placement; protocol instructions alone never create chats.
3. Each replacement chat receives a portable envelope: repository, migration ID, cutover SHA, executor ID, role-handoff path, and return route.
4. The chat verifies provider identity, ignored local registry mapping, skills/tools, current TEAM/TASK, and workspace custody.
5. The role performs cross-check and executor-scoped queue discovery, then publishes a target-preflight receipt.
6. PM compare-and-publishes the activation successor against the accepted default branch and reads it back.
7. Only after the causally linked activation receipt is accepted may the role use any writer-capable R2Team entry point on an eligible current TASK.
8. Team migration reaches `COMPLETE` only when every affected executor is resumed or has a terminal accounted blocked/cancelled/rollback disposition with owner and next action.

## Local registry

`.codex-local/THREAD_REGISTRY.md` maps logical executor IDs to physical task/thread IDs and host observations. It is ignored, host-local, replaceable, and never authoritative. Relocation prepare may durably report only a result enum such as `MAPPING_PRESENT_READ_BACK` plus authority/host class; it never publishes a populated value or stable hash of a private identifier. Resume writes/remaps local state only with local owner authority, validates the logical executor mapping, detects collisions, and reads it back. A remote/manual executor does not require or acquire a local-chat mapping merely because relocation exists.

## Writer fencing

Each affected executor has a fencing record keyed by repository/project identity plus logical `executor_id`. It carries `current_epoch`, `expected_prior_epoch`, prior accepted fencing-record ref, source/target states, physical-custody class, stop receipt, activation receipt, and disposition. A global cutover generation may group records but never substitutes for them.

Fence validation accepts only explicit legal source/target/custody tuples. Source ACTIVE implies target INACTIVE and source custody; target ACTIVE implies source STOPPED and target custody. Known state labels are not independently composable, because a Cartesian-product validator can admit two simultaneous writers.

Fencing is cooperative protocol fencing unless a separate receipt proves provider-enforced revocation. Every writer-capable R2Team entry point re-reads the accepted default-branch record immediately before product or TASK publication. A successor is valid only when both its expected prior epoch and causal parent match accepted state. Two branches proposing the same next integer are conflicting proposals, not co-valid writers. Unknown, stale, equal-conflicting, or causally unrelated state is `WRITER_CONFLICT` and blocks work. Notification, silence, registry presence, chat title, archive state, or absence of an observed process cannot advance the epoch or prove stop.

After `FROZEN`, the sole control-write exception is the executor named as migration PM publishing only the declared `migration_control_paths`: `Team/Migrations/<migration-id>/**` and the governing relocation TASK's status/evidence fields. Product source, active product TASK scope/candidate/result, TEAM ownership, and other paths remain write-frozen until their executor is target-active.

## Workspace integration

Workspace identity remains distinct from chat identity. A relocated executor may reuse a portable repository/workspace only when custody, owner, exact candidate, mutability, dependencies, and local containment are verified. Otherwise the source lease is retained/transferred and the target allocates through `r2team-workspace open`; relocation does not delete or move a workspace implicitly.

## Rollback

Before source stop, cancellation may retain the current source epoch through an accepted cancellation receipt. After source stop or freeze, cancellation cannot silently revive the source: reactivation needs a new accepted successor and activation receipt. After any target activation, rollback is a new forward migration or rollback publication with a higher per-executor epoch and new stop/activation receipts. Never reset accepted Git state or revive an old writer from chat history.

## Evidence and receipts

Receipt types are `PREPARE`, `SOURCE_STOP`, `FREEZE`, `TARGET_PREFLIGHT`, `ACTIVATION`, `PARTIAL_DISPOSITION`, `COMPLETION`, `CANCELLATION`, and `FORWARD_ROLLBACK`. Each immutable receipt has a unique ID and, as applicable, migration/executor, prior/new epoch, causal parent receipt/ref, accepted commit SHA, TASK checkpoint and candidate refs, workspace disposition/close-receipt refs, actor/provider identity class, observed outcome, remaining blocker, timestamp, and review date. Machine-private IDs/paths and stable hashes of them remain local.

A source-stop receipt additionally binds expected epoch, final accepted TASK/product checkpoint and candidate/tree, outstanding publisher/helper state, workspace/native-resource custody, stop mechanism, and accepted cutover parent. Accepted mechanisms are cooperative source acknowledgement after its final checkpoint, independently verifiable administrative fence/revocation, or another mechanism explicitly modeled and independently evidenced. An unreachable source without enforceable revocation remains blocked.

A target activation receipt causally references the accepted source-stop receipt and an included target-preflight receipt, binds accepted cutover to the accepted commit, mapping result to registry evidence, exact executor/TASK/candidate/workspace facts, and must be accepted and read back before product work. Duplicate or mismatched causal parents are invalid.

Receipt-set validation takes an explicit accepted-root ref and affected-executor set. PREPARE and SOURCE_STOP bind the root; every other receipt resolves an allowed included parent with matching identity, epoch and evidence collections. Freeze resolves the exact stop set, stopped cancellation resolves its stop, forward rollback resolves an activation and higher epoch, and completion requires exactly one terminal receipt for every affected executor. Per-type outcomes and state enums are closed; a syntactically nonblank but unknown value is not evidence.

## Command surface

- `$r2team-relocate status [migration-id]`
- `$r2team-relocate prepare role <executor-id>`
- `$r2team-relocate prepare team`
- `$r2team-relocate resume role <migration-id> <executor-id>`
- `$r2team-relocate resume team <migration-id>`
- `$r2team-relocate doctor [migration-id]`

Status/doctor are read-only. Prepare/resume require accepted migration authority and perform only the declared bounded stage.

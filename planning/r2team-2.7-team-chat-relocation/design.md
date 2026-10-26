# R2Team 2.7 team and chat relocation design

## State machines

Role relocation:

```text
REQUESTED -> PREPARING -> PREPARED -> FROZEN -> READY_TO_RESUME
  -> RESUMING -> RESUMED -> COMPLETE
                  \-> BLOCKED
```

Whole-team relocation:

```text
PREPARING -> COLLECTING_HANDOFFS -> FREEZE_PENDING -> FROZEN
  -> READY_TO_RESUME -> RESUMING -> COMPLETE
                           \-> PARTIAL_BLOCKED
```

`BLOCKED` and `PARTIAL_BLOCKED` preserve durable source custody and name an owner/review date; they never imply a fallback writer.

## Record layout

```text
Team/Migrations/<migration-id>/
  MIGRATION.md
  roles/
    <executor-id>.md
```

`MIGRATION.md` records:

- migration ID, mode, state, PM, created/review dates;
- repository/provider identity, source cutover SHA, protocol ref;
- affected executor IDs and current/future writer custody;
- per-role handoff paths, active TASK references, provider routes;
- target placement class without physical paths/thread IDs;
- freeze evidence, startup order, resume gates, receipts;
- workspace lease dispositions and local-registry remap requirement;
- forward rollback rule, blockers, remaining NOT_RUN axes.

Each role handoff records executor/functions, source checkpoint, active TASK IDs/paths/checkpoints/candidates/next actions, open provider questions, required setup facts, workspace custody summary, and limits. It references existing records rather than duplicating them.

## Prepare flow

1. Resolve accepted TASK/TEAM/protocol/provider state and migration authority.
2. Inventory all current assignments for each affected executor, including newly discoverable TASK IDs.
3. Publish or identify a recoverable checkpoint for each active TASK and candidate.
4. Reconcile active workspace leases under 2.6; choose retained, transferred, or closed custody without cleanup inference.
5. Verify target placement, access/tool prerequisites, owner routes, and one future writer.
6. Collect role handoffs and publish the bundle through protected Git workflow.
7. Prove old writer stop and set `FROZEN`; only PM cutover publication may proceed from the source side.
8. After provider read-back of the accepted cutover commit, set `READY_TO_RESUME`.

## Resume flow

1. Replacement PM verifies repository/provider identity, default branch, bundle, state, and old-writer stop.
2. It creates or connects only physical chats explicitly authorized by target placement; protocol instructions alone never create chats.
3. Each replacement chat receives a portable envelope: repository, migration ID, cutover SHA, executor ID, role-handoff path, and return route.
4. The chat verifies provider identity, ignored local registry mapping, skills/tools, current TEAM/TASK, and workspace custody.
5. The role performs cross-check and executor-scoped queue discovery.
6. PM records a resume receipt; only then may the role use `r2team-work start` on an eligible current TASK.
7. Team migration reaches `COMPLETE` only when every affected executor is resumed or explicitly retained/blocked with owner and next action.

## Local registry

`.codex-local/THREAD_REGISTRY.md` maps logical executor IDs to physical task/thread IDs and host observations. It is ignored, host-local, replaceable, and never authoritative. Relocation prepare may report mapping presence but never publishes its populated values. Resume writes/remaps it only with local owner authority and reads it back before reporting connection.

## Writer fencing

Each migration record has `source_writer_state`, `target_writer_state`, and `writer_epoch`. The accepted bundle advances the epoch. Source is `STOPPED` before target can become `ACTIVE`; any unknown or equal concurrent active claim is `WRITER_CONFLICT` and blocks work. Thread notification or registry presence cannot advance the epoch.

## Workspace integration

Workspace identity remains distinct from chat identity. A relocated executor may reuse a portable repository/workspace only when custody, owner, exact candidate, mutability, dependencies, and local containment are verified. Otherwise the source lease is retained/transferred and the target allocates through `r2team-workspace open`; relocation does not delete or move a workspace implicitly.

## Rollback

Before target activation, PM may publish cancellation retaining the source writer. After target activation, rollback is a new forward migration or ownership publication with a higher writer epoch. Never reset accepted Git state or revive an old writer from chat history.

## Evidence and receipts

Prepare/resume receipts bind migration ID, executor, writer epoch, source/target state, cutover SHA, relevant TASK/candidate refs, registry read-back class, workspace disposition, actor, observed result, and remaining blocker. Machine-private IDs/paths remain local.

## Command surface

- `$r2team-relocate status [migration-id]`
- `$r2team-relocate prepare role <executor-id>`
- `$r2team-relocate prepare team`
- `$r2team-relocate resume role <migration-id> <executor-id>`
- `$r2team-relocate resume team <migration-id>`
- `$r2team-relocate doctor [migration-id]`

Status/doctor are read-only. Prepare/resume require accepted migration authority and perform only the declared bounded stage.

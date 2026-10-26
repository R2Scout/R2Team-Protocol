# R2Team 2.7 team and chat relocation proposal

## Problem

R2Team durable state survives in Git and provider records, but physical Codex chats and hosts remain local execution surfaces. Moving work without a protocol can create concurrent writers, orphaned local mappings, implicit ownership changes, transcript dependence, lost workspace custody, or a replacement chat that starts before the old writer stops.

## Desired outcome

R2Team 2.7 adds an explicit relocation control plane for:

1. one physical role chat continuing as the same logical executor;
2. one executor moving to another Codex host;
3. a PM-controlled whole-team cutover with ordered resume.

The durable unit is the accepted migration bundle, per-executor causal fencing records, and current TASK checkpoints, never a transcript or local thread identifier.

## Identity model

- Participant identity: human/provider identity and accepted functions.
- Executor identity: logical writer/queue identity recorded in TEAM and TASK.
- TASK identity: durable scope, owner, routes, candidate, evidence, and next action.
- Physical execution identity: one local chat/thread on one host; stored only in ignored local state.
- Relocation identity: immutable `migration_id` binding source cutover, target placement, affected executors, state, and receipts.

Relocation preserves the first three identities and replaces only physical execution identity. A participant/function/executor change is an ownership transfer, not relocation.

## Operating modes

- `role`: relocate one logical executor and its assigned functions.
- `team`: relocate several executors under one PM-controlled freeze and ordered bootstrap.
- `same-chat host recovery`: reconnect an existing physical chat where the product supports it; still requires the same durable gates when writer custody changes.

## Proposed skill boundary

Package a separate `r2team-relocate` skill for read-only status/doctor plus prepare/resume operations. Existing `$r2team migrate <function> to <participant>` remains function transfer. `r2team-work` continues TASK execution and must not hide relocation mutations. `r2team` may route a relocation request to the separate skill but does not silently execute it.

## Durable records

Each migration uses `Team/Migrations/<migration-id>/MIGRATION.md` plus `roles/<executor-id>.md`. The global file owns aggregate state, cutover generation, PM, affected executors, target placement, startup order, rollback rule, receipts, and unresolved limits. Each role record owns the executor-scoped causal fence, source/target substates, evidence and disposition, and points to current TASK checkpoints without copying their content.

## Safety invariants

- At most one accepted physical writer is active for an executor/TASK under cooperative protocol fencing; provider-enforced exclusion is claimed only when separately evidenced.
- Every writer-capable R2Team entry point re-reads the accepted default-branch fencing record immediately before publication and rejects a stale, equal-conflicting, or causally unrelated successor.
- Old writer stop is proven per executor before that executor can reach `READY` or `ACTIVE` on the target.
- Replacement chat cannot work before its resume gate and cross-check succeed.
- A blocked or partial migration preserves per-executor custody and always names a legal recovery transition or terminal accounted disposition.
- Local mapping never grants ownership, permission, or assignment.
- Unknown access, route, checkpoint, writer status, or workspace custody blocks resume.
- Rollback is a forward accepted publication, never reset or force-push.
- Receipts are append-only, uniquely identified, causally linked, and privacy-safe; no hash of a private thread identifier is durable evidence.
- Relocation does not authorize chat creation, credential copying, process stop, archive, deletion, merge, deployment, release, or cleanup.

## Compatibility

R2Team 2.6 remains valid. Existing projects adopt 2.7 prospectively through their accepted-main workflow. Existing function-transfer and remote/manual-participant behavior remains unchanged.

## Delivery boundary

This change produces protocol/package behavior and isolated fixtures only. It does not perform a live relocation or mutate installed skills/downstream projects.

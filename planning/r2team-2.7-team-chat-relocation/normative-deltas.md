# R2Team 2.7 normative deltas

## Version and scope

- The distribution protocol version MUST be `2.7` only after acceptance and release.
- 2.7 MUST add physical team/chat relocation without redefining participant/function transfer.
- A 2.6 project MUST remain unchanged until an explicit project-local 2.7 adoption.

## Identity

- Participant, logical executor, TASK, candidate, workspace lease, physical chat/host, and migration identity MUST remain distinct.
- Same-executor relocation MUST preserve participant, executor, TASK, provider item, candidate, and evidence identity.
- Changing participant, function owner, or executor ID MUST use the existing ownership-transfer workflow before relocation resume.
- Committed state MUST NOT contain populated physical thread IDs, machine-private paths, secrets, or chat transcripts.

## Authority and skill boundary

- PM MUST authorize each migration ID, affected executors, mode, source cutover, target placement, writer transition, startup order, and rollback rule.
- Relocation MUST NOT infer chat creation, access change, credential copy, process stop, workspace cleanup, archive, deletion, merge, deployment, or release authority.
- Operational relocation MUST use the separate `r2team-relocate` entry point unless an independently accepted narrower boundary replaces it.
- Existing `r2team migrate <function> to <participant>` semantics MUST remain function transfer.
- `r2team-work` MUST NOT hide prepare, freeze, registry remap, resume, or relocation completion mutations.

## Durable migration bundle

- Every relocation MUST have one accepted `migration_id` and global `MIGRATION.md` record.
- Whole-team relocation MUST include one per-executor handoff record for every affected executor.
- Handoffs MUST reference current accepted TASK/candidate/evidence/checkpoint/route/workspace facts rather than duplicate them or depend on transcript/local state.
- Missing or unpublished TASK state MUST block prepare or resume.

## Writer fencing

- At most one physical writer MAY be active for one executor/TASK.
- The accepted migration record MUST advance a monotonic writer epoch and name source/target writer states.
- Source writer MUST be proven stopped before `READY_TO_RESUME`.
- Target writer MUST NOT become active until accepted cutover read-back, local cross-check, and its resume receipt.
- Unknown, conflicting, or concurrent writer claims MUST produce `WRITER_CONFLICT` and block product work.

## Freeze and resume

- Whole-team prepare MUST pass through `FREEZE_PENDING` and `FROZEN` before `READY_TO_RESUME`.
- After `FROZEN`, old product writers MUST NOT publish product/TASK changes; only the authorized PM cutover publication MAY proceed.
- Target PM MUST follow the accepted startup order and MUST record roles that remain blocked/not-run.
- A local notification, chat title, copied prompt, or registry entry MUST NOT open the resume gate.

## Local registry

- Populated executor-to-thread mappings MUST remain in ignored `.codex-local/THREAD_REGISTRY.md` or equivalent accepted local state.
- Local registry updates MUST require local owner authority and read-back.
- Local mapping MUST NOT grant assignment, ownership, permission, provider identity, writer epoch, or acceptance.

## Workspace custody

- Relocation MUST reconcile every affected active workspace lease under the adopted 2.6 lifecycle.
- Workspace reuse on the target MUST require verified owner, exact candidate, mutability, custody, containment, dependency, and local-resource facts.
- Relocation MUST NOT imply physical workspace movement or cleanup; retain, transfer, close, or allocate through `r2team-workspace` with evidence.

## Recovery and rollback

- Failure before target activation MUST retain a named safe writer or remain blocked; it MUST NOT silently activate either side.
- Rollback after target activation MUST be a forward accepted publication with a higher writer epoch.
- Reset, force-push, transcript replay, or stale local mapping MUST NOT restore writer authority.

## Evidence and completion

- Prepare, freeze, resume, and completion receipts MUST bind migration, executor, epoch, cutover SHA, TASK/candidate refs, actor, observed result, workspace disposition, and remaining blocker without private local identifiers.
- A role is resumed only after its own receipt and current assignment/capacity gates pass.
- Team relocation is complete only when every affected executor is resumed, retained, or explicitly blocked with owner, review date, and next action.
- Protocol/package tests MUST NOT perform live chat creation, registry mutation outside isolated fixtures, workspace cleanup, process stop, or real relocation.

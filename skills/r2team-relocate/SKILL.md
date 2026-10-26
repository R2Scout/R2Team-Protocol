---
name: r2team-relocate
description: "Prepare, inspect, resume, cancel, or roll forward an authorized R2Team logical-executor relocation with per-executor cooperative fencing and durable causal receipts. Use only in an adopted R2Team 2.7 project; it does not create chats, transfer functions, stop processes, move workspaces, or prove provider-enforced exclusion."
---
# R2Team — relocation

Use this skill only when the user or an accepted TASK requests relocation of the same logical executor to another physical chat/host, or a coordinated whole-team cutover. A change of participant, function owner, or executor ID is ownership transfer through `$r2team migrate <function> to <participant>`, not relocation.

## Commands

- `$r2team-relocate status [migration-id]`: read-only migration, fencing, custody, and receipt report.
- `$r2team-relocate doctor [migration-id]`: read-only consistency diagnosis and permitted next transition.
- `$r2team-relocate prepare role <executor-id>`: prepare one executor-scoped cutover under an accepted migration TASK.
- `$r2team-relocate prepare team`: prepare the accepted affected-executor set and ordered team freeze.
- `$r2team-relocate resume role <migration-id> <executor-id>`: preflight and activate one causally eligible target executor.
- `$r2team-relocate resume team <migration-id>`: resume eligible executors in accepted order while preserving partial custody.

The status and doctor are read-only. Prepare and resume perform only their declared stage. Cancellation after stop and rollback after activation require a new accepted forward publication; do not invent a hidden mutation command.

## Sources and authority

Read applicable `AGENTS.md`, accepted default-branch `TEAM.md`, governing relocation TASK, `Team/Migrations/<migration-id>/MIGRATION.md`, the selected executor record, current product TASKs, workspace records, and relevant protocol/role instructions. Verify exact repository/provider identity and adopted protocol 2.7.

The durable route is Git/provider state, never chat history, notification delivery, a title, or local registry presence. This skill does not create or move chats, change access, copy credentials/transcripts, stop processes, archive/delete workspaces, install skills, merge, release, deploy, or adopt another project. Those require their own authority and evidence.

## Identity and fence

Keep participant, logical executor, TASK, candidate, workspace lease, physical placement, and migration identity separate. Same-executor relocation changes only physical placement.

Each affected executor is keyed by repository/project identity plus `executor_id`. Re-read accepted default-branch fencing state immediately before every relocation-control or product/TASK publication. Compare `expected_prior_epoch` and `prior_accepted_record`; every accepted/expected/claimed/current/proposed/receipt epoch is a strict non-boolean integer and the next epoch must be exactly one greater. Accept only an explicit legal `(source_state, target_state, custody)` tuple with one writer-capable placement; independently known labels are not freely composable. A stale, coerced, equal-conflicting, same-next-epoch sibling, wrong executor/project, unrelated causal parent, or simultaneous-writer tuple returns `WRITER_CONFLICT`, `FENCE_INVALID`, or a stricter typed-input failure.

This is cooperative protocol fencing. It rejects publication through compliant R2Team entry points; it does not prove an unfenced process physically impossible. Claim provider-enforced exclusion only when an independent administrative-revocation receipt proves it. Otherwise provider-enforced exclusion is `NOT_PROVEN`.

## Prepare

1. Verify accepted migration authority, mode, affected executors, target placement classes, startup order, rollback rule, and `migration_control_paths`.
2. Reconcile exact TEAM/TASK/candidate/provider routes and all newly discoverable assignments for every affected executor.
3. Reconcile workspace/native-resource custody through `r2team-workspace`; relocation grants no movement or cleanup authority.
4. Publish immutable prepare/handoff records under `Team/Migrations/<migration-id>/` with per-executor epochs and causal parents.
5. Move each source `ACTIVE -> STOP_REQUESTED -> STOPPED` only with a valid source-stop receipt whose exact typed outcome is `SOURCE_STOPPED`. Silence, notification, registry state, chat title/archive, missing observed process, or arbitrary nonblank outcome is not proof.
6. Reject stop while any publisher/helper remains in flight or unaccounted. An unreachable source without enforceable revocation remains blocked.
7. Derive `FROZEN` only when every affected source is stopped. During freeze, only the accepted migration PM may publish declared migration-control paths and governing relocation-TASK status/evidence fields.
8. Compare-and-publish, then provider-read-back the cutover before any target becomes `READY`.

An executor is retained only when an accepted prepare revision removes it from the affected set before `FREEZE_PENDING`. Never keep an ambiguous source-active exception inside a frozen affected set.

## Resume

1. Verify accepted cutover SHA, executor record, `expected_prior_epoch`, `prior_accepted_record`, source-stop receipt, target placement/access/tool preflight, TASK/candidate, and workspace custody.
2. For local standalone executors, remap ignored `.codex-local/THREAD_REGISTRY.md` only with local authority; detect collisions/wrong executor and read back. Persist only a result enum such as `MAPPING_PRESENT_READ_BACK` plus authority/host class. Never publish a physical ID/path, transcript, or stable hash of a private identifier. Remote/manual executors do not require a local mapping, but any collision, observed executor, or contradictory present/absent evidence still blocks.
3. Publish target-preflight and activation receipts whose causal parent is the accepted source-stop/cutover record. Every activation decision consumes the included preflight receipt and requires its exact ID, same stop/executor/epoch/evidence facts, and `PASS`; a reference string or separate optional graph check is insufficient. In team mode every preflight also references the exact full-set FREEZE, and timestamps strictly satisfy `SOURCE_STOP < FREEZE < TARGET_PREFLIGHT < ACTIVATION`. Bind activation `accepted_cutover` to the accepted commit and mapping result to registry evidence. Duplicate, absent, stale, blocked, failed, equal-time, late-freeze, or mismatched preflight/stop parents block activation.
4. Compare-and-publish the per-executor successor and read it back before product work. Target progresses `INACTIVE -> PREFLIGHTED -> READY -> ACTIVE`.
5. Re-read the accepted fence before every later product/TASK publication. An offline stale source remains blocked.

Whole-team aggregate state is derived from executor records. `PARTIAL_BLOCKED` preserves already active targets and stopped/blocked peers; it may return to `RESUMING`, reach a terminal accounted disposition, or start forward rollback. A terminal-accounted blocked, cancelled, or forward-rollback executor requires disposition owner, review date, next action, and immutable disposition receipt; a bare label never completes the migration.

## Cancellation and rollback

Cancellation before source stop may retain the current source epoch through an accepted cancellation receipt. After stop/freeze, source reactivation needs a new accepted successor and activation receipt. After any target activation, rollback is a forward publication with a higher per-executor epoch and new stop/activation receipts. Never reset, force-push, replay a transcript, or trust stale registry state to revive authority.

## Receipts and return

Use immutable unique `PREPARE`, `SOURCE_STOP`, `FREEZE`, `TARGET_PREFLIGHT`, `ACTIVATION`, `PARTIAL_DISPOSITION`, `COMPLETION`, `CANCELLATION`, and `FORWARD_ROLLBACK` receipts. Bind migration/executor, prior/new epoch, causal parent, accepted commit, TASK/candidate refs, workspace/close-receipt refs, actor/provider class, typed observed outcome, blocker, timestamp, and review date as applicable. Validate a completion-capable set against an external accepted-root ref, exactly one PREPARE, exact affected-executor set, and explicit role/team mode. Team completion requires one exact full-set FREEZE referenced as a prior gate by every preflight; every executor branch shares the PREPARE lineage; activation resolves stop plus PASS preflight; stopped cancellation resolves stop; forward rollback may add later-generation stop/preflight/activation receipts. Receipt-set completion and aggregate derivation use one unique latest causal stage per executor; an older terminal cannot complete over a newer stage, and every record must match its latest stage, disposition, and resulting tuple. Cancellation binds its exact declared source/target and legal custody; terminal BLOCKED and forward rollback complete only as `STOPPED/INACTIVE/SOURCE_STOPPED`. Receipt types may recur at later epochs, while duplicate executor/type/epoch/parent logical events remain invalid. Same-epoch alternatives are invalid except one activation paired to its one supporting preflight; historical PASS/activation evidence cannot override a later blocked or rolled-back generation.

Return exact accepted SHA/tree, executor state/epoch/custody, receipt refs, remaining blockers, legal next transition, and explicit `NOT_RUN` axes. Never collapse planning PASS, implementation review, merge, release, installation, adoption, provider-enforced fencing, and live relocation into one verdict.

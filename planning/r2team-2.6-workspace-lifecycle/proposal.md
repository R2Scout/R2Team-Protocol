# R2Team 2.6 workspace lifecycle

## Why

R2Team 2.5 defines authoritative TASK ownership, exact candidate identity, independent handoff, and protected Git workflow, but it does not define the lifecycle of the physical workspace used to perform that work.

Observed high-concurrency use produced thousands of retained worktrees and revision-named branches because TASK revisions, corrections, handoffs, and QA or Design passes were treated as reasons to allocate new persistent checkouts. Completion did not assign closure custody or require a recoverable terminal disposition.

The protocol needs a resource lifecycle contract. The answer is not automatic cleanup: unsafe deletion would trade capacity failure for evidence loss, candidate loss, or custody violation.

## Proposed change

Add a normative Workspace Lifecycle capability to R2Team 2.6:

- separate TASK, candidate, and workspace identities;
- represent physical materializations as bounded logical leases;
- track result state separately from workspace state;
- set default per-TASK and project-wide active-workspace budgets;
- gate new allocation by free capacity;
- prefer ephemeral exact-candidate materialization for read-only review;
- require recoverable terminal dispositions and close receipts;
- require a protected merge checkpoint to contain durable evidence or a sanitized hash-bound durable recovery reference;
- require a merge-triggered closure review so no completed stage leaves a silently active workspace;
- keep physical paths and runtime details in ignored local state;
- preserve Codex-managed custody through the application archive lifecycle;
- make adoption prospective and project-local;
- package operational workspace commands in a separate `r2team-workspace` skill;
- keep team and chat relocation out of 2.6 under a distinct 2.7 TASK and checkpoint.

## Defaults

- One author lease, one reusable integration lease, and one ephemeral QA or Design lease per TASK.
- Maximum three active workspaces per TASK by default.
- Maximum one mutable workspace per executor, TASK, and purpose by default.
- Project target: 50 active physical workspaces.
- Project hard cap: 150 active physical workspaces.
- Projects may adopt stricter values or exact TASK exceptions.

## Capacity profile

- Above 50 GiB free: normal allocation.
- 30 to 50 GiB: reuse-only.
- 15 to 30 GiB: owner-approved recovery allocation only.
- Below 15 GiB: freeze new persistent placement.

Thresholds govern allocation, not deletion. Existing safe in-place work may continue within capacity and authority.

## Merge evidence and closure gate

Evidence suitable for Git is merged through the same protected workflow as the TASK checkpoint. Evidence that cannot enter Git because of size, sensitivity, licensing, or mutability is represented in the merged checkpoint by a sanitized manifest, content hash, retention class, durable recovery location, owner, and access boundary.

Evidence that survives only in chat, an expiring log, or a disposable worktree is insufficient.

After provider read-back confirms the merge SHA, every workspace lease owned by the completed stage enters closure review. It reaches CLOSED, RETAINED_PROTECTED, TRANSFERRED_TO_NEXT_TASK, or an explicit blocking state. No lease remains silently ACTIVE after administrative completion.

Temporary material is removed only after verified evidence export when it is exclusively owned by the closing lease, has no live process or dependent lease, is not a shared immutable cache or retained recovery input, and the closer already holds explicit removal authority. Otherwise it is retained, transferred, or blocked with an owner and review date.

## Non-goals

- Automatic destructive cleanup.
- Automatic branch deletion or process termination.
- Treating a deadline as disposal authority.
- Treating merge completion, a close receipt, or a cleanup budget as disposal authority.
- Moving secrets, data, profiles, caches, or rollback material.
- Replacing source, QA, installed, runtime, deployment, or public acceptance gates.
- Requiring a global mutable dependency tree.
- Retrofitting downstream projects without their accepted-main governance decision.
- Modifying the paused predecessor candidate during this planning change.
- Team or chat relocation in R2Team 2.6.
- Adding hidden workspace mutation to `r2team-work`.

## Impact

Protocol and package sources expected to change during a later authorized implementation:

- CODEX_TEAM_PROTOCOL and Setup;
- AGENTS, TEAM, TASK, role, and local-registry templates;
- command reference, existing R2Team skill routing, and a separate packaged `r2team-workspace` skill;
- migration guide from 2.5;
- package manifest and payload hashes;
- structural validator and test fixtures.

The separate `r2team-workspace` skill exposes status, open, close, and doctor behavior. Existing skills may route to it or describe authority boundaries, but `r2team-work` must not silently allocate, relocate, archive, or close a workspace. Optional operational tools may implement inventory, allocation preflight, close preflight, receipt generation, and doctor reporting. The protocol must define their safe contract without requiring a particular destructive implementation or scheduler.

## Compatibility

R2Team 2.5 remains governing until 2.6 is independently validated and accepted. Existing TASKs remain valid. Projects adopt workspace lifecycle prospectively through their own accepted-main decision. Legacy workspaces are retained until a separately authorized reconciliation plan classifies custody and evidence.

## Success criteria

- A TASK revision or handoff no longer implies a new persistent worktree.
- Every active workspace has a logical owner, purpose, state, and recovery route.
- A failed close cannot erase or rewrite a product or QA verdict.
- Capacity breaches stop new placement without granting cleanup authority.
- Close receipts prove disposition without exposing machine-private paths.
- Fresh-package validation and migration fixtures demonstrate coherent adoption.

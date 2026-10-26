---
name: r2team-workspace
description: "Inspect and govern R2Team workspace leases: report status, preflight bounded allocation, prepare recoverable closure, or diagnose lifecycle blockers. Use only in an adopted R2Team 2.7 project; it does not grant cleanup, process-stop, merge, relocation, or deletion authority."
---
# R2Team — workspace lifecycle

Use the accepted project `TEAM.md`, selected TASK, repository state, and ignored local registry. The durable contract is in Git; physical paths, host observations, process IDs, and native application handles stay in `.codex-local/`.

Commands:

- `$r2team-workspace status [TASK-ID]`: read-only lease, budget, custody, evidence, and disposition report.
- `$r2team-workspace doctor [TASK-ID]`: read-only consistency diagnosis with exact blockers and next evidence.
- `$r2team-workspace open TASK-ID purpose <purpose>`: allocation preflight, then one bounded materialization only when the existing TASK and authority permit it.
- `$r2team-workspace close TASK-ID lease <lease-id>`: evidence and custody preflight, then the explicitly authorized recoverable closure method.

Help, unknown commands, status and doctor are read-only. No command infers mutation or explicit removal authority from age, disk pressure, a budget, administrative completion, merge, or a close request.

## Sources and boundaries

Read applicable `AGENTS.md`, accepted `TEAM.md`, the selected TASK/current checkpoint, relevant role instructions, and the workspace-lifecycle section of `CODEX_TEAM_PROTOCOL.md`. Confirm project adoption of 2.7. An older project is not silently upgraded.

This skill does not administer participants, run product work, relocate teams or chats, replace `r2team-work`, stop processes, delete branches, merge, release, deploy, or modify installed skills. Existing skills may route lifecycle requests here. `r2team-work` remains the TASK execution entry point and must not hide workspace allocation or closure.

Keep result acceptance and workspace disposition separate. A product or QA PASS does not prove closure; a closure blocker does not rewrite a candidate verdict.

## Identity and state

Resolve three independent identities:

1. TASK: durable scope, owner, routes, acceptance, and next action.
2. Candidate: exact commit SHA/tree or immutable artifact identity.
3. Workspace lease: `lease_id`, TASK, purpose, class, owner executor, exact base/candidate, mutability, custody, state, and recovery reference.

Lease states are `REQUESTED`, `ACTIVE`, `CLOSE_PENDING`, `CLOSED`, `RETAINED_PROTECTED`, `TRANSFERRED_TO_NEXT_TASK`, `BLOCKED_DIRTY`, `BLOCKED_DEPENDENCY`, `BLOCKED_AUTHORITY`, or `UNKNOWN`. A terminal lease record in `CLOSED`, `RETAINED_PROTECTED`, or `TRANSFERRED_TO_NEXT_TASK` requires closure owner, retention, recovery, review-date, and close-receipt evidence; transfer also requires next-TASK/owner/custody evidence. A bare label and every other state prevent administrative completion without rewriting the candidate verdict.

## Status and doctor

Read only. Report:

- exact project/TASK/candidate scope and local observation time;
- active leases by owner, purpose, class, mutability, and custody;
- TASK and project budget use plus destination-filesystem free capacity;
- dirty, untracked, ignored, process, native-resource, evidence, branch, retention, and recovery facts as known/unknown;
- terminal disposition or the smallest blocker and responsible owner.

Never claim a complete inventory when reads fail or when a local registry is absent or stale. Return `INVENTORY_INCOMPLETE` with the missing source.

## Open

Run allocation preflight before mutation:

1. verify the accepted TASK, current owner/purpose, exact base/candidate, permissions, and no compatible existing lease;
2. enforce one author lease, one reusable integration lease, one ephemeral QA/Design lease, maximum three active leases per TASK, one mutable lease per executor/TASK/purpose, project target 50, and hard cap 150; a bounded default-budget exception must match the requested TASK, lease, current/prior base, preserved candidate, owner, and purpose exactly, include capacity evidence/review date/recovery rule, use boolean true changed-base/custody/disjoint-lane/candidate-preservation predicates, and cannot bypass hard-cap/disk/single-writer/ownership/containment/evidence gates;
3. measure the destination filesystem, including expected dependency/package expansion: above 50 GiB normal, 30–50 GiB reuse-only, 15–30 GiB owner-approved recovery allocation only, below 15 GiB no new persistent placement;
4. select ordinary-canonical, codex-managed, external-authorized, or legacy-retained custody and record the logical lease before relying on it;
5. create only the authorized bounded materialization, then read back path containment, branch/HEAD/tree, mutability, and actual state.

If any gate fails, return `ALLOCATION_BLOCKED`; do not clean, relocate, terminate, bypass QA, or mutate existing work.

## Close

Run evidence and custody preflight before any recoverable action:

1. re-read lease ownership, path containment, branch/HEAD/tree, dirty/untracked/ignored content, processes, native resources, dependent leases, and exact candidate;
2. export Git-suitable evidence through the protected checkpoint; represent non-Git evidence by a sanitized manifest, content hash, retention class, durable recovery location, owner, and access boundary;
3. record branch disposition as `MERGED_TO_DEFAULT`, `SUPERSEDED_BY_SHA`, `REJECTED`, or `EVIDENCE_ARCHIVED` without deleting a ref;
4. choose `CLOSED`, `RETAINED_PROTECTED`, `TRANSFERRED_TO_NEXT_TASK`, or a blocking state and record a close receipt;
5. use the application archive lifecycle for codex-managed custody; never shell-remove an application-managed checkout;
6. read back the actual result and remaining owner or blocker.

Temporary cache, build output, package expansion, logs, and disposable fixtures may be removed only after verified evidence export when exclusively owned by the closing lease, with no live process or dependent lease, not a shared immutable cache or retained recovery input, inside the verified target, and when the closer already holds explicit removal authority. A failed gate produces retained, transferred, or blocked disposition with owner and review date; never force delete.

## Receipt and return

A close receipt records lease, TASK, owner, closer, base, branch, HEAD, tree, candidate, dirty/untracked/ignored classification, artifact manifest, recovery route, native-resource disposition, branch disposition, retention class, closure method, actual result, and remaining owner or blocker. Commit only portable receipt facts; keep machine-private paths and live handles ignored.

Return the exact command intent, checked candidate/lease, observed facts, disposition, retained artifacts, limitations, and next action. Do not claim merge, delivery, cleanup, disk recovery, or acceptance without its own evidence.

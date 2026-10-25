# Design: workspace lifecycle and custody

## Design principles

1. Git state is authoritative for contract, candidate, and portable recovery facts.
2. Physical workspace paths and live resource handles are machine-local.
3. Candidate identity is immutable and independent of a directory.
4. Acceptance evidence and workspace custody are separate axes.
5. Capacity controls allocation; they do not authorize destruction.
6. Every mutation or closure has one accountable owner.

## Identity model

TASK identity:

- durable scope, ownership, routes, acceptance, and transitions;
- continues through role handoffs and candidate corrections.

Candidate identity:

- exact commit SHA/tree or immutable artifact identity;
- may be materialized in more than one authorized workspace;
- never derives from a path or branch name alone.

Workspace lease identity:

- logical ID for one physical materialization;
- names TASK, purpose, owner, class, exact base, mutability, state, and custody;
- maps to a physical path only in ignored local registry state.

## State model

Result axis:

    DRAFT -> ACTIVE -> ACCEPTED
                  +-> REJECTED
                  +-> SUPERSEDED
                  +-> BLOCKED

Workspace axis:

    REQUESTED -> ACTIVE -> QUIESCING -> CHECKPOINTED -> CLOSED
                    |             |            +-> RETAINED_PROTECTED
                    |             +-> BLOCKED_DIRTY
                    +-> TRANSFERRED_TO_NEXT_TASK

The axes are correlated by references, not collapsed into one status. A QA verdict remains valid if closure is blocked. Administrative TASK completion requires a fully evidenced terminal lease record for every active lease; a state string alone is insufficient.

## Lease contract

Portable Git fields:

- workspace_lease_id;
- task_id;
- purpose and class;
- owner_executor_id;
- mutable flag;
- base_sha and current head/tree;
- allocated_at and review_due_at;
- state and retention_class;
- recovery_ref;
- close_receipt_ref;
- exception_ref when outside default budget.

Ignored local registry fields:

- physical path;
- filesystem and size;
- host-local worktree identity;
- process, port, mount, container, database, and lock handles;
- application-managed artifact identity;
- local last-observed timestamp.

No committed template stores another machine's absolute path, thread ID, process ID, or secret.

## Allocation flow

1. Resolve exact TASK, purpose, owner, base, candidate, and existing leases.
2. Prefer reuse of the current compatible lease.
3. Verify per-executor, per-TASK, and project budgets.
4. Measure free capacity on the destination filesystem, including expected dependency expansion.
5. If an exception is required, bind it to the requested TASK, lease, current/prior base, preserved candidate, owner, and purpose; record capacity evidence, review date, recovery rule, and boolean true changed-base/custody/disjoint-lane/candidate-preservation predicates in the TASK.
6. Allocate through the custody-appropriate mechanism.
7. Record the logical lease and local physical mapping.

A failed or partial preflight produces ALLOCATION_BLOCKED. It never silently falls back to another root or deletes an existing workspace.

## Review flow

Read-only QA or Design prefers:

1. exact accepted candidate SHA/tree;
2. detached or archive-based ephemeral materialization;
3. immutable pinned dependency inputs;
4. isolated mutable runtime state;
5. evidence publication;
6. explicit close preflight and receipt.

If the required tool cannot use a detached materialization, the TASK may authorize a bounded review lease. Independence and exact-candidate evidence remain unchanged.

## Closure flow

Closure is explicit and recoverable:

1. Stop only resources owned by this lease and only with existing authority.
2. Re-read branch, HEAD, tree, status, ignored content, and native resources.
3. Publish or preserve required code, evidence, data, and recovery references.
4. Record branch disposition without deleting the branch.
5. Select custody-specific closure: ordinary Git removal, Codex application archive, retained protected state, or transfer.
6. Read back the actual result.
7. Publish the close receipt and remaining owner or blocker.

Force removal is not a protocol default. Unknown dirty, ignored, data, process, or custody state results in RETAINED_PROTECTED or BLOCKED_DIRTY.

For an accepted integration, closure review starts only after provider read-back confirms the actual merge commit and remote default-branch state. The merged checkpoint contains durable evidence suitable for Git or a sanitized manifest with content hash, retention class, durable recovery location, owner, and access boundary.

Temporary cache, build output, package expansion, logs, and fixtures are removed only when all of these conditions hold:

- required evidence export was verified;
- the material is exclusively owned by the closing lease;
- no live process or dependent lease uses it;
- it is not a shared immutable cache or retained recovery input;
- the closer already holds explicit removal authority.

If any condition is unknown or false, the material and workspace receive a retained, transferred, or blocked disposition. A merge event, receipt, age, review date, or budget breach never supplies missing removal authority.

## Budget and exception behavior

The default active-workspace budget is three per TASK and one mutable lease per executor, TASK, and purpose. The project target and hard cap count physical active materializations across ordinary, Codex-managed, and ephemeral classes.

A hard-cap or disk-threshold breach:

- freezes new placement;
- permits bounded read-only inventory;
- permits safe in-place continuation when already authorized and capacity allows;
- requires PM reconciliation;
- does not revoke leases or authorize cleanup.

## Placement and custody classes

- ordinary-canonical: project-designated ordinary root alias;
- codex-managed: application-owned location and archive lifecycle;
- external-authorized: explicit project exception;
- legacy-retained: pre-adoption custody awaiting reconciliation.

The protocol does not silently relocate existing roots. Root aliases are portable policy; physical paths are local registry data.

## Artifact and dependency boundary

Durable evidence, user data, mutable databases, secrets, profiles, rollback packages, and long-lived runtime state must survive independently of disposable workspaces.

Dependencies must be reproducible. Shared package caches may be immutable and pinned. A shared mutable node_modules directory or cross-executor mutable runtime state is not required and should not be introduced as a convenience.

## Tooling boundary

R2Team 2.6 packages a separate `r2team-workspace` skill for status, open, close, and doctor operations. Existing skills may route to it and state authority boundaries, but `r2team-work` does not silently allocate, relocate, archive, or close a workspace. The command contract is:

- status and doctor are read-only;
- open performs allocation preflight before mutation;
- close performs custody and evidence preflight before a recoverable action;
- no command infers delete authority from age, budget, or free space;
- scheduling is project-local and opt-in.

Team and chat relocation is not part of this lifecycle change. It requires a distinct R2Team 2.7 TASK, checkpoint, validation candidate, and acceptance decision.

## Adoption

The 2.5-to-2.6 migration updates project policy and templates prospectively. Existing TASKs acquire lifecycle fields at their next material revision or handoff. Existing workspaces remain legacy-retained until classified by a separately authorized plan.

Protocol acceptance does not edit downstream projects, activate tools, or close any workspace.

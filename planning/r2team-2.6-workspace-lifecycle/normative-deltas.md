# Normative deltas for R2Team 2.6

## Workspace identity

- The protocol MUST distinguish TASK identity, candidate identity, and workspace lease identity.
- A TASK revision, handoff, verdict, correction, or evidence checkpoint MUST NOT by itself require a new persistent workspace.
- A candidate MUST be identified by an immutable commit SHA/tree or exact artifact identity, not by a directory path.

## Lease and ownership

- Every active physical materialization MUST have one logical workspace lease, purpose, class, owner executor, exact base, mutability mode, state, and recovery reference.
- Committed project state MUST NOT contain machine-private physical paths, thread IDs, process IDs, or secrets.
- Each mutable lease MUST have exactly one current writer.
- A transfer MUST preserve the exact prior HEAD/tree and name the next owner and custody route.

## Budgets

- The default maximum MUST be three active workspaces per TASK: author, integration, and one ephemeral QA or Design materialization.
- The default project target SHOULD be 50 active physical workspaces and the default hard cap MUST be 150 unless the project accepts stricter values.
- An executor SHOULD have no more than one mutable workspace for the same TASK and purpose.
- A bounded exception MUST name the exact TASK, reason, lease, owner, capacity evidence, and review date.
- A budget breach MUST freeze new placement and MUST NOT authorize deletion, lease revocation, or evidence disposal.

## Disk governor

- Allocation MUST measure capacity on the destination filesystem and account for expected dependency or package expansion.
- Above 50 GiB free MAY permit normal allocation.
- Between 30 and 50 GiB, new persistent placement MUST stop and compatible workspaces SHOULD be reused.
- Between 15 and 30 GiB, only owner-approved recovery allocation MAY proceed.
- Below 15 GiB, new persistent placement MUST stop.
- A threshold MUST NOT authorize cleanup, migration, process termination, QA bypass, or destructive action.

## Review materialization

- Read-only QA and Design SHOULD use an ephemeral exact-SHA/tree materialization with pinned immutable dependencies.
- Review evidence and verdict MUST be published before closure.
- Closure failure MUST NOT alter PASS, FAIL, BLOCKED, UNKNOWN, or NOT_RUN evidence for the reviewed candidate.

## Result and workspace terminal state

- Result state and workspace state MUST remain separate.
- Whole-TASK administrative completion MUST require a terminal disposition for every active lease.
- CLOSED, RETAINED_PROTECTED, and TRANSFERRED_TO_NEXT_TASK MAY be terminal when their required owner, recovery, retention, and receipt evidence exists.
- A review date MUST NOT imply automatic disposal authority.
- After provider read-back confirms an accepted merge, every lease owned by the completed stage MUST enter closure review.
- No lease MAY remain silently ACTIVE after administrative TASK completion.

## Merge evidence gate

- Evidence suitable for Git MUST be merged through the protected workflow with the TASK checkpoint.
- Evidence that cannot enter Git due to size, sensitivity, licensing, or mutability MUST be represented in the merged checkpoint by a sanitized manifest, content hash, retention class, durable recovery location, owner, and access boundary.
- Evidence that survives only in chat, an expiring log, or a disposable workspace MUST NOT satisfy the durable evidence gate.
- The default branch MUST NOT receive temporary binaries, caches, mutable runtime state, credentials, raw customer data, or machine-private paths merely to satisfy the evidence gate.

## Branch disposition

- Every candidate branch MUST record one disposition: MERGED_TO_DEFAULT, SUPERSEDED_BY_SHA, REJECTED, or EVIDENCE_ARCHIVED.
- A disposition MUST NOT authorize deleting the branch ref.
- Branch disposition MUST remain separate from source, QA, installed, runtime, deployment, READY_EXACT, and public acceptance.

## Close receipt

- A close receipt MUST record lease, TASK, owner, closer, base, branch, HEAD, tree, candidate, dirty/untracked/ignored classification, artifact manifest, recovery route, native-resource disposition, branch disposition, retention class, closure method, actual result, and remaining owner or blocker.
- Unknown material state MUST produce RETAINED_PROTECTED or BLOCKED_DIRTY, not fabricated closure.
- Codex-managed worktrees MUST close only through the Codex application archive lifecycle.
- Required ignored artifacts MUST be preserved separately before application archive.
- Reproducible cache, build output, package expansion, temporary logs, and disposable fixtures MAY be removed only after verified evidence export when they are exclusively owned by the closing lease, have no live process or dependent lease, are not a shared immutable cache or retained recovery input, and the closer already has explicit removal authority.
- Material that fails any removal condition MUST receive a retained, transferred, or blocked disposition with an owner and review date.

## Artifact and data custody

- Secrets, user data, mutable databases, profiles, rollback packages, durable evidence, and persistent runtime state MUST NOT depend on a disposable worktree for survival.
- Dependency inputs MUST be reproducible.
- A shared package cache MAY be used only with project-defined integrity and mutability boundaries.
- The protocol MUST NOT require a shared mutable dependency tree.

## Roles

- PM MUST govern workspace budgets, exceptions, closure ownership, and lifecycle reconciliation.
- PM lifecycle authority MUST NOT imply deletion, process-stop, merge, or publication authority.
- Dev SHOULD reuse its author lease for corrections and TASK revisions.
- QA and Designer MUST report both verdict and workspace disposition without coupling one to the other.
- Integration or DevOps SHOULD reuse a compatible integration lease.
- Audit or COO MAY report stale, over-budget, unknown-owner, retained, and blocked-dirty leases but MUST NOT close them without separate authority.

## Workspace skill boundary

- R2Team 2.6 MUST package workspace operations in a separate `r2team-workspace` skill.
- `r2team-workspace status` and `r2team-workspace doctor` MUST be read-only.
- `r2team-workspace open` MUST complete allocation and authority preflight before mutation.
- `r2team-workspace close` MUST complete evidence, custody, ownership, dependency, containment, and removal-authority preflight before a recoverable action.
- Existing skills MAY route to `r2team-workspace` but `r2team-work` MUST NOT silently allocate, relocate, archive, close, or remove a workspace.
- R2Team 2.6 MUST NOT contain team or chat relocation behavior; that change requires a distinct 2.7 TASK and checkpoint.

## Adoption and compatibility

- R2Team 2.5 projects MUST remain governed by their accepted version until a project-local accepted-main adoption of 2.6.
- Existing TASKs MUST remain valid.
- New lifecycle fields become required prospectively at the next material handoff or TASK revision after adoption.
- Existing workspaces MUST remain protected until a separately authorized reconciliation classifies their custody and evidence.
- Protocol publication MUST NOT directly mutate downstream projects or activate cleanup automation.

# Migrate an adopted project to R2Team 2.9

Use the exact verified annotated v2.9 release commit, not main/latest. The previous project protocol governs until its own accepted adoption checkpoint is published and read back. Installation and publication alone do not adopt the protocol or alter directories.

## Preserve and reconcile

Read current AGENTS/TEAM/TASKs, accepted source/ref, owners/routes, candidates, OpenSpec, evidence, physical Git worktree/application inventory, root mappings, and unpublished work. Preserve active work and current directories. A 2.8 project adds the terminology/directory-formation clarification from [GIT_WORKTREE_DIRECTORIES.md](GIT_WORKTREE_DIRECTORIES.md). An older project reconciles intervening requirements from [2.6](MIGRATE_TO_2.6.md), [2.7](MIGRATE_TO_2.7.md), and [2.8](MIGRATE_TO_2.8.md) before directly adopting 2.9; no intermediate project release is required.

## Adopt explicit Git worktree terminology and folder formation

- Say Git worktree for Git working copies and their directories. Resource is the broader lifetime term. Preserve the existing r2team-workspace command, workspace_leases field, and compatibility anchors.
- Configure one accepted ordinary Git worktree root alias, mapped to a physical root locally. New ordinary linked Git worktrees are direct children named `<native-id>-<project>-<work-ref>-<perm|task|tmp>-<executor>`.
- Preserve native IDs and compatible existing leases. Do not introduce parent folders or allocations per revision, chat title, date, retry, test batch, or verdict.
- Keep worktree roots disjoint from evidence/output/log/tmp/cache roots; validate actual target containment and path limits before allocation.
- Preserve application-managed root/hierarchy/IDs and supported custody controls. Keep the readable label locally if an application display field is unavailable. Primary/legacy paths remain retained pending authorized reconciliation; adoption performs no rename or relocation.

Lifetime remains persistent/perm, task_scoped/task, or ephemeral/tmp, independently of dev/qa/build/release purpose. Preserve the owner, bound close condition, review date, retention, and recovery rules in [RESOURCE_LIFETIME.md](RESOURCE_LIFETIME.md). Names and age never grant removal or automatic promotion authority.

## Validate and publish cutover

Reconcile project AGENTS, TEAM, protocol, used roles, TASK/local-observation templates, commands, and skills through the authorized Git workflow. Compare the six installed skills against the pinned package and preserve customizations/rollback when replacement is authorized. Each retained executor cross-checks its actual role, routes, loaded work/COO skills, and saved entry instructions.

Run the package validator, four offline test suites, six skill-format checks, payload hashes, command-copy, link, and portability checks. The directory fixtures validate ordinary leaf names and reject unsafe/missing native IDs and application/legacy path fabrication; they perform no actual resource mutation. Check legacy/root conformity read-only and record owner/limits without bulk rename or cleanup.

PM publishes one organizational checkpoint with exact package provenance, coherent policy, root aliases, pending legacy reconciliation, verification/NOT_RUN evidence, owners/review dates, and recovery route. Verify the accepted default branch, then notify retained executors through existing authorized routes and have them read/cross-check the checkpoint. Use the maintained [PM prompt](PM_PROTOCOL_UPDATE.md).

Live directory creation/rename/cleanup, decommission, process stop, relocation, installed-skill replacement, provider revocation, runtime effects, and chat dispatch require their own authorized scope/evidence. A still-governing 1.10 communication contract remains effective until an approved cutover resolves it.

# PM update prompt — R2Team 2.9

Use this owner-delivered prompt with the exact verified v2.9 release commit. It prepares project-local adoption; it does not itself prove delivery, adoption, resource movement, or installation.

```text
R2Team Protocol 2.9 is available from https://github.com/R2Scout/R2Team-Protocol.
Pin the owner-supplied full verified v2.9 commit; do not substitute main/latest.

Prepare and publish our project's accepted adoption checkpoint through its existing
authorized Git/PR workflow. Read START.md, Setup.md, MIGRATE_TO_2.9.md,
RESOURCE_LIFETIME.md, and GIT_WORKTREE_DIRECTORIES.md from that exact package.

Say Git worktree explicitly for Git working copies. Resource is the general term
for worktrees, test data, build output, logs, caches, evidence, and runtime resources.
Keep the existing r2team-workspace command and workspace_leases field compatible.

For genuinely new ordinary linked Git worktrees, use a direct child of the
project-approved Git worktree root:
<root>/<native-id>-<project>-<work-ref>-<perm|task|tmp>-<executor>
Example: ws0044-crm.ai-task3244-tmp-qa2.

Preserve native IDs and compatible leases. Do not create additional parent folders
or worktrees per revision, chat title, date, retry, test batch, or verdict.
Keep worktree roots disjoint from evidence/output/log/tmp/cache roots.
Preserve application-managed root/hierarchy/IDs; use supported app controls
and record the readable label locally when display-name support is unavailable.
Existing primary and legacy paths stay protected pending authorized reconciliation.

Every governed resource has explicit lifetime: persistent/perm, task_scoped/task,
or ephemeral/tmp, independently of dev/qa/build/release purpose, with owner,
bound close condition, review date, retention, and recovery. Names or age never
authorize cleanup, automatic promotion, renaming, relocation, or decommission.

Compare AGENTS, TEAM, protocol, TASK/role templates, commands, actual installed
skills, and saved entry prompts. Preserve active work, candidates, OpenSpec,
evidence, routes, and customizations. Reconcile older versions as the migration
guide specifies. Record exact checks and NOT_RUN limitations.

Publish the agreed checkpoint and verify the accepted default branch; then each
retained executor reads it and cross-checks its role and loaded instructions.
The previous project protocol governs until that explicit cutover.
```

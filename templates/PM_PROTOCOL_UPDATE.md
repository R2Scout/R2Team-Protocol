# PM update prompt — R2Team 2.10

Use the exact owner-supplied verified v2.10 release commit. This owner-delivered prompt prepares project-local adoption; it does not prove delivery or authorize unrelated resource operations.

```text
R2Team Protocol 2.10 is available from https://github.com/R2Scout/R2Team-Protocol.
Pin the full verified release commit; do not substitute main/latest.
Read MIGRATE_TO_2.10.md, RESOURCE_LIFETIME.md, and GIT_WORKTREE_DIRECTORIES.md.

Use Git worktree explicitly for Git working copies. Resource is the general term.
Keep compatible command/schema names such as r2team-workspace and workspace_leases.

For new ordinary linked Git worktrees, use a direct child of the approved root:
<root>/<project>-<issue|task|pr|wi><identifier>-<perm|task|tmp>-<executor>[-<purpose>]
Example: crm.ai-issue3244-task-devops.
Do not add an extra physical/native ID or counter to the directory name.
Use the accepted primary work identifier and actual Git/tracker number; explicit
reference types distinguish equal Issue/PR numbers. Keep lease/resource/native IDs
in the registry for custody and recovery. Standing anchors use a governance TASK.

Reuse an existing compatible worktree first. Only already accepted distinct purposes
such as build/integration may add a suffix; never use counters/retries to bypass
occupied targets, budgets, or single-writer/key-conflict gates. Do not add parent
folders per revision, date, chat title, test batch, or verdict. Keep worktree roots
disjoint from evidence/output/log/tmp/cache roots.

Lifetime remains persistent/perm, task_scoped/task, or ephemeral/tmp, independently
of dev/qa/build/release purpose, with owner, bound close condition, review date,
retention, and recovery. Preserve existing primary/legacy and application-managed
paths/IDs. Naming adoption does not rename, delete, or promote resources.

Reconcile AGENTS, TEAM, protocol, templates, commands, actual skills, and saved
entry prompts. Preserve active TASKs, candidates, OpenSpec, evidence, routes, and
customizations. Publish the agreed adoption checkpoint through the authorized
Git/PR workflow and verify the accepted default branch. Each retained executor
reads it and cross-checks its role/loaded instructions. The previous protocol
governs until that explicit cutover. Report unrun or pending checks honestly.
```

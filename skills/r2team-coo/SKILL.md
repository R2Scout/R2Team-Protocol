---
name: r2team-coo
description: "Check exact new events for configured R2Team roles and optionally issue an already-authorized local wake. Use for a scoped COO update/check pass, not broad project audits or automatic task execution."
---
# R2Team — COO pass

Show command help in English using the syntax and boundaries below. Help needs no project access and performs no actions. Operational reports use the participant's preferred language.

- `$r2team-coo help`: read-only syntax and boundaries.
- `$r2team-coo update`: one read-only delta pass, NO notifications or writes.
- `$r2team-coo check`: one delta pass with already-permitted local wake.
- Bare invocation defaults to help, not check or background monitoring.

## Sources and authority

COO monitors configured durable events, not every transient role conversation. Authorized task owners may exchange bounded working requests directly without COO relay; do not duplicate these as mandatory notifications or create message logs. Wake permission does not authorize assigning helpers, changing task ownership or relaying new product scope. Material outcomes must reach the task publisher at the project's checkpoint boundaries.


This is the R2Team 2.2 procedure skill, not a role assignment or background service. Resolve the user's exact project/repository before acting. Read applicable AGENTS.md, accepted TEAM.md from the configured default branch, relevant role instruction and the selected TASK/current checkpoint. Read project COMMANDS.md and only the relevant protocol/Setup sections; do not scan unrelated repositories or chat history. Existing project instructions govern; a 1.10 project is not silently migrated to 2.2. Report incompatible/missing protocol inputs and ask PM for direction.

Git is authoritative for assignments, scope, acceptance, open decisions and continuation checkpoints; provider comments/PRs support the workflow but are not in a clone. Use the configured GitHub or Azure DevOps Server/TFS Git provider and verified identity/API, not a hard-coded GitHub assumption. Check task branch/remote head and current owner before writes. Keep one publishing owner per TASK; other roles submit comments/artifacts to that owner. No command grants commit/push, tracker-write, merge, deploy, account administration, expenses or scheduling rights. Ask only for missing facts/authority. Do not expose credentials or commit machine paths/thread IDs.

Help and unknown/ambiguous commands are read-only. A short visible intake states outcome, boundaries and return route before execution. Return concise facts, exact references, unresolved blockers and next action. Do not claim delivery, completion, independent QA or compatibility without evidence.

## Minimal reads

For an explicitly configured multi-repository scope, use repo-qualified TASK/event IDs and verify access separately per repository. Do not discover or monitor every repository owned by the participant.

Resolve current COO mode and explicit watched participant/executor/task IDs, rights and dispatcher. COO may be PM's/internal read-only helper or a registered standalone executor serving one participant's roles. Do not infer scope from all repositories or every team member. Missing/ambiguous scope requires clarification.
Read only changes since a confirmed checkpoint via exact TASK paths/refs, selected Issue/Work Item IDs and PR events. On first use use a bounded baseline of those IDs, not a full historical scan. Same provider account's "read" flag is not per-role completion.
Return dry facts: changed ID, what changed, who needs action, source pointer and next action. No long narrative or unrequested summaries. Failed fetch preserves prior successful position and is reported, not an empty successful pass. Optional local cursor/dedup metadata belongs only in ignored local storage, not a Git journal. update does not persist a new cursor or change inbox read state.

## Wake for check only

An internal COO subagent returns the delta to parent and does not send external notifications. A standalone COO needs current notify_local authorization, exact recipient mapping and designation as the single dispatcher for the watched recipients.
For each new actionable event confirm it still belongs to that recipient, is not superseded, and has no prior successful/uncertain send. Send one short task/branch/SHA/comment pointer; include return route if project requires it. No content mutation, new scope, permissions or "done" claims.
No tool/mapping/permission => report NOT_DELIVERED and rely on durable Git/provider state. Do not guess thread IDs or send remote messages merely because a tool exists. Never restart/interrupt busy roles, create chats, or wake arbitrary participants.
Do not retry uncertain sends; after cache loss reconcile exact provider/local evidence before another send. No duplicate author and COO wake. check may update approved ignored local technical dedup only; it cannot write TASK/TEAM/comments, change assignment/rights or execute product work.

Both commands are single-pass. Heartbeat is OFF by default and is never enabled by them. A separately requested schedule must first pass a manual scoped test and be created by an authorized owner with supported native tooling, quiet on unchanged/non-actionable state. This skill alone is not a running monitor.

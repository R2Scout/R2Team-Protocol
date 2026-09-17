---
name: r2team-audit
description: "Perform a read-only readiness and recoverability audit of an R2Team project or team, including role ownership, Git/tracker consistency and specification gaps. Not a product security audit, migration, or permission to repair."
---
# R2Team — audit

Show command help in English using the syntax and boundaries below. Help needs no project access and performs no actions. Audit reports use the participant's preferred language.

`$r2team-audit` checks team readiness; `$r2team-audit help` explains it. An optional participant/TASK scope narrows the check.

## Sources and authority

Operational communication: distinguish the product contract (OpenSpec), material recovery state (TASK/checkpoint) and transient coordination. Approved bounded requests to helpers or registered chats retain the parent TASK owner/publisher and need no new task entities or message archive. Direct exchanges are optional and require actual project/tool permission; provider discussion is the fallback. The same persistence rules apply locally and remotely. Publish material state before ownership transfer, reliance on new material decisions/results, blocking stops or end of a changed session, and completion/acceptance. Preserve code/tests/evidence; do not require a commit per routine answer. Existing project adoption governs; this skill update does not override 1.10 or silently enable transport.


This is the R2Team 2.4 procedure skill, not a role assignment or background service. Resolve the user's exact project/repository before acting. Read applicable AGENTS.md, accepted TEAM.md from the configured default branch, relevant role instruction and the selected TASK/current checkpoint. Read project COMMANDS.md and only the relevant protocol/Setup sections; do not scan unrelated repositories or chat history. Existing project instructions govern; a 1.10 project is not silently migrated to 2.4. Report incompatible/missing protocol inputs and ask PM for direction.

Git is authoritative for assignments, scope, acceptance, open decisions and continuation checkpoints; provider comments/PRs support the workflow but are not in a clone. Use the configured GitHub or Azure DevOps Server/TFS Git provider and verified identity/API, not a hard-coded GitHub assumption. Check task branch/remote head and current owner before writes. Keep one publishing owner per TASK; other roles submit comments/artifacts to that owner. No command grants commit/push, tracker-write, merge, deploy, account administration, expenses or scheduling rights. Ask only for missing facts/authority. Do not expose credentials or commit machine paths/thread IDs.

Help and unknown/ambiguous commands are read-only. A short visible intake states outcome, boundaries and return route before execution. Return concise facts, exact references, unresolved blockers and next action. Do not claim delivery, completion, independent QA or compatibility without evidence.

## Audit

Read Setup audit and relevant protocol sections. Use an inventory of current configured inputs, not full history or every chat. Without identity/credentials, audit accessible facts and mark inaccessible evidence UNKNOWN.
Check:
- One current PM; unique active participant/executor IDs, valid combined/custom functions, assigned owner with matching active_role and actual permissions.
- Exact Git root/provider/default branch and published sources; no local-only checkpoint falsely offered as remote-ready.
- Active TASK contract/revision, stage/status, single publisher, branch/head, Issue/Work Item/PR mapping, next_action, open questions/human approvals and evidence candidate SHA.
- Linked OpenSpec/spec/design/docs/ADR and implementation/test coverage required by stage. Record known gaps; don't declare full specification merely because files exist. No archive/init/sync as part of audit.
- Role cross-check and real tool/skill access; distinguish installed files from successful discovery and live use.
- Provider accounts/access and notification scope, optional local mapping excluded from Git, single wake dispatcher, no accidental heartbeat or false remote wake promises.
- Checkpoints support takeover by a clean authorized executor; combined QA/DevOps or same-person helpers are not independent human review.

Use configured GitHub or Azure DevOps Server/TFS Git semantics and actual item/state/PR mappings. No specialized process hierarchy is prescribed by this package. Do not claim unavailable API checks passed. Audit missing material state, not missing transient chat transcripts.
Report concise severity, exact source, consequence and minimal suggested fix. Separate verified/UNKNOWN/NOT_RUN; request decisions only for meaningful gaps. Do not update TEAM/TASK, install tools, fix documents, post comments, send wake or change schedules. An explicit later repair request uses its own authorized workflow.

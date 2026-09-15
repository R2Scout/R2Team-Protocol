---
name: r2team
description: "Set up or administer an R2Team Git-first team: add participants, register an invited person, connect a role chat, transfer functions, disconnect safely, or show command help. Use for R2Team onboarding and team changes, not ordinary product coding."
---
# R2Team — team and participant lifecycle

Accept natural language and these shorthand prompts:
- `$r2team help [command]`
- `$r2team add Ken roles QA,DevOps remote`
- `$r2team register repo <Git-URL> participant ken [executor ken-ops]`
- `$r2team connect QA [executor ken-qa]`
- `$r2team migrate DevOps to Ken`
- `$r2team disconnect Ken`

Arguments are intent, not shell expressions. Never execute placeholders. "Registrate" may be interpreted as register with a brief clarification of its canonical name. Bare invocation asks which lifecycle operation is needed; it does not start setup or alter TEAM.

## Sources and authority

Operational communication: distinguish the product contract (OpenSpec), material recovery state (TASK/checkpoint) and transient coordination. Approved bounded requests to helpers or registered chats retain the parent TASK owner/publisher and need no new task entities or message archive. Direct exchanges are optional and require actual project/tool permission; provider discussion is the fallback. The same persistence rules apply locally and remotely. Publish material state before ownership transfer, reliance on new material decisions/results, blocking stops or end of a changed session, and completion/acceptance. Preserve code/tests/evidence; do not require a commit per routine answer. Existing project adoption governs; this skill update does not override 1.10 or silently enable transport.


This is the R2Team 2.1 procedure skill, not a role assignment or background service. Resolve the user's exact project/repository before acting. Read applicable AGENTS.md, accepted TEAM.md from the configured default branch, relevant role instruction and the selected TASK/current checkpoint. Read project COMMANDS.md and only the relevant protocol/Setup sections; do not scan unrelated repositories or chat history. Existing project instructions govern; a 1.10 project is not silently migrated to 2.1. Report incompatible/missing protocol inputs and ask PM for direction.

Git is authoritative for assignments, scope, acceptance, open decisions and continuation checkpoints; provider comments/PRs support the workflow but are not in a clone. Use the configured GitHub or Azure DevOps Server/TFS Git provider and verified identity/API, not a hard-coded GitHub assumption. Check task branch/remote head and current owner before writes. Keep one publishing owner per TASK; other roles submit comments/artifacts to that owner. No command grants commit/push, tracker-write, merge, deploy, account administration, expenses or scheduling rights. Ask only for missing facts/authority. Do not expose credentials or commit machine paths/thread IDs.

Help and unknown/ambiguous commands are read-only. A short visible intake states outcome, boundaries and return route before execution. Return concise facts, exact references, unresolved blockers and next action. Do not claim delivery, completion, independent QA or compatibility without evidence.

## Route

For help, read [references/commands.md](references/commands.md) and show the relevant English section without requiring a project or Git credentials. Keep all command help in English; use the participant's preferred language for task conversations. The other skill entry points are `$r2team-work start|task`, `$r2team-coo update|check`, and `$r2team-audit`; invoking help does not execute them.

For a new project or protocol migration, request/resolve a trusted R2Team setup package path or Git URL + full commit SHA (or approved bundle manifest hash), read its START/Setup, and use new/migrate. The skill alone does not bundle project templates. Never reconstruct a missing protocol from memory or overwrite an existing MVP/specification. Team-function `migrate` below is not a protocol upgrade.

The distribution repository is https://github.com/R2Scout/R2Team-Protocol; templates live at its root under templates/. Prefer the PM-provided full commit SHA. If using release v2.1, resolve and verify its commit before using the package; never silently substitute main. Obtain the package only into a confirmed safe destination with authorized access. For a new project, missing TEAM/TASK is expected: use the trusted package START/Setup to create them after confirmation, not an existing-team registration prerequisite. User-installed skills are not the complete template bundle.

### add — PM prepares an invitation

Use Setup team as PM/authorized delegate. Clarify participant/provider account, functions, executor IDs, combined/separate chats, allowed subagents and rights. PM is the sole mandatory coordinating executor; any other function can be combined, local or remote. Locality is relative to each machine.
Show the meaningful TEAM/role diff, preserve active assignments and publish through the approved Git workflow. TEAM does not grant repository membership: arrange missing access with its authorized administrator, not silently.
Return an invitation containing repo URL, participant/executor IDs, accepted TEAM path/ref, protocol path/ref, PM reply channel/account and TASK/branch if assigned. No secrets or another machine's thread IDs/paths. Invite with register only after publication; otherwise mark LOCAL_ONLY and not ready for remote onboarding.

### register — participant joins an existing team

Follow Setup join. Verify repo/protocol source and actual provider identity against the current accepted TEAM, not solely the name in the prompt or an outdated invitation SHA. An absent/inactive/changed assignment is a blocker to PM, not permission to add yourself or create another PM.
Confirm a local destination before clone; preserve existing dirty work. Check Git/provider access, relevant role instructions and project SKILLS/toolchain on this machine. Obtain local owner permission for installations; no wholesale updates or OpenSpec init over existing specs.
One participant can have multiple executors/functions. If this chat's executor is unambiguous, run connect in this pass; otherwise ask which assigned executor to adopt. Repeated register reuses existing identity and checked facts, not duplicate TEAM entries. Do not begin product work during registration.

### connect — a chat adopts its assigned function

Resolve participant and executor; reject ambiguous QA/Dev instances. Read current role contract and do a cross-check in own words: duties/outputs, bounds/approvals, allowed helpers, actual tools/spec inputs, queue and reply route, unresolved questions.
Do not take over another live chat's assignment without an approved handoff. Optional thread mapping is local and ignored. Internal subagents do not register as TEAM executors.
Report readiness/questions in the existing onboarding Issue/Work Item if permitted; publisher records material state in its organisational TASK. If no channel/access, ask the participant to relay and mark NOT_DELIVERED. If no TASK, request the first from PM; if already assigned, confirm it without executing during onboarding. No extra ACK/MSG/report.

### migrate / disconnect — preserve work first

Only PM/authorized delegate changes assignments. Enumerate the affected executor/functions and exact active TASKs, open requests, branches/PRs and unpublished work. Secure a recoverable checkpoint/candidate SHA and next_action before reassignment or deactivation. Agree replacement and scope; update TEAM, TASK owner/revision when contract changes, and provider assignee consistently through the single publisher. Do not fork replacement tasks just for a new person.
If work cannot be recovered/transferred, keep its owner active or explicitly block the handoff for PM; do not discard it. Disconnect deactivates the agreed person/executor/function, not their account, repository, branches or chat history. Adjust affected notification routing with local owner authority; do not change unrelated automations.

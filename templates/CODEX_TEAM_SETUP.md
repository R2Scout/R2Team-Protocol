# Startup and re-entry prompts — R2Team 2.4

[Setup.md](Setup.md) is the single wizard. Select its mode in natural language. Use the verified protocol version; installing skills alone does not adopt project rules.

## First PM

```text
Read Setup.md, mode new. This chat becomes PM after confirmation.
Confirm the target Git root, goal and trusted package source.
Guide one step at a time; select GitHub or generic TFS Git and permitted operations.
Configure the minimum team, one COO mode per participant, and the applicable OpenSpec/Superpowers skills.
Create only approved files. Finish with audit, a real TASK and next action.
Do not bypass the selected OpenSpec approval gate to start implementation.
```

## Existing MVP / legacy protocol

Use [MIGRATE_TO_2.4.md](MIGRATE_TO_2.4.md). Preserve active work by default. A fresh organizational queue while retaining specs/chats needs explicit approval and per-chat adoption, not just file replacement.

```text
Read Setup.md, mode migrate, and MIGRATE_TO_2.4.md.
Start read-only: verify source package/ref, actual source version, current rules,
branches, active TASKs/messages/PRs, OpenSpec and unpublished work.
Show a minimal diff, state mapping and cutover.
Wait for approval before writes. Do not change the product or infrastructure.
```

## Team changes — current PM

```text
Read Setup.md, mode team. Add Ken.
Clarify provider identity, functions, chats, allowed helpers and permissions.
QA and DevOps need not be separate people.
Inspect affected active work, propose the TEAM diff and prepare a join invitation.
```

A custom Analyst/Tester function can be described and assigned to an existing executor. No automatic chat creation or additional protocol version.

## Join from any machine

PM fills exact verified references, using accessible Git URLs rather than their private machine paths:

```text
Project: <Git URL>; default branch: <branch>.
Accepted TEAM: <full SHA/path>.
You are invited executor <id>, pending activation, not a new PM.
Registration: <registration_id>; activation: <IMMEDIATE_RESERVED|QUEUED_AFTER_REGISTRATION>.
Onboarding/questions channel: <exact Issue/Work Item URL>; reply to executor <pm-id>.
Prepared first TASK: <path>; state <PENDING_REGISTRATION|PENDING_CAPACITY>; branch: <branch>; checkpoint: <full SHA>.
Tracker: <URL>; PR: <URL if available>.
Read AGENTS.md, Setup.md join, your role contract, SKILLS.md and OPERATING_COMMUNICATION.md.
Verify current assignment/remote head; do not rely only on the invitation's old SHA.
Cross-check duties, boundaries, inputs, actual skills, channels and unresolved questions.
Read `handoff_seq`, `result_to_executor_id` and the authorized next-transition table.
Identify Task Issuer and Project PM executor/response routes; explain ASK, LOOP and ESCALATE_PM.
Post `R2_EVENT: REGISTRATION_RESULT`, status `READY_FOR_ACTIVATION`, evidence and questions in the exact onboarding channel. Use `R2_EVENT: ONBOARDING_QUESTION`, `to_executor_id: <pm-id>` for blockers.
After PM publishes registration, run your COO pass and start the prepared TASK when its accepted status becomes `READY` for your executor.
Do not begin product work while it remains pending registration/capacity.
```

Local routing may point to a verified current local TASK and expected commit without unnecessary fetch. A pointer does not change the contract.

## Role cross-check

See [the common rule](CODEX_TEAM_PROTOCOL.md#role-cross-check). Fill with actual facts, not automatic assertions:

```text
R2Team 2.4 adopted: executor <id>, functions <list>, TEAM <ref>.
Loaded work/COO skills and saved entry/watch prompt: <verified source/ref and compatibility>.
Duties/output: <understanding>.
Boundaries: <permissions, helpers and approvals>.
Verified inputs/tools: <facts>.
Questions/limits: <specific gaps or none identified>.
Task Issuer and Project PM: <executors/routes>; addressed-question check: <method>.
First TASK: <confirmed assignment or request to PM>; READY/BLOCKED <reason>.
```

An added function checks changed responsibilities rather than repeating full setup. The registration result is the onboarding evidence, not an extra ACK file. If all pre-authorized evidence matches, PM publishes activation without another owner approval. `QUEUED_AFTER_REGISTRATION` remains waiting only for its named capacity gate; it is not a hidden approval.

## Ordinary work entry

[COMMANDS.md](COMMANDS.md) provides skill equivalents. These document prompts also work without installed R2Team skills:

```text
R2Team: check my updates.
One read-only pass over my assignments, addressed questions, replies and related PRs.
Use executor_queue scope and the current remote default branch; discover new TASK IDs.
Keep unresolved READY assignments across unchanged deltas; HOLD applies to its TASK.
Report exact changes and next action. Do not execute tasks, send notifications,
change status or enable heartbeat.
```

```text
R2Team: start my work session.
Check relevant updates and continue one clear authorized next action with intake.
Discover all current assignments to my executor before selecting a TASK.
If no valid task or bounded request exists, ask PM; clarify ambiguity or missing rights.
Do not self-assign independent work or enable automation.
```

For PM, "check the team" means read-only audit. Manual requests work locally/remotely; background checks require separate configuration.

For a remote role, the normal start command first runs an internal/same-chat COO pass scoped to that executor. When it finds an actionable TASK, the finding returns locally and the role continues with `$r2team-work start <TASK-ID>`. Automatic discovery without a user-started session requires a separately authorized participant-side heartbeat.

## Required COO capability; optional separate chat

See [ROLE-COO.md](ROLE-COO.md). Every active participant has one configured COO mode. Default `internal` returns facts to the participant's active role; `same_chat` runs in that role task; optional `standalone` can watch several of that participant's executors with separate rights.

During setup/register, offer a standalone COO chat once and persist the answer. If declined, keep `internal`; if accepted, ask to connect an existing chat or explicitly create one. This choice does not enable heartbeat. Internal/same-chat mode needs no registry or wake permission.

```text
R2Team: team mode. Configure a standalone COO for participant <id>,
watching executors <IDs>.
Agree exact scope, notify_local rights and one wake dispatcher.
Do not grant other organizational permissions automatically.
Prepare TEAM/profile diff and cross-check. Leave heartbeat off.
Persist the one-time offer result. Do not create a chat without an explicit request.
```

After approved configuration:

```text
R2Team: perform one COO pass with authorized wake.
Read only new events in the agreed scope.
Notify registered local recipients only as the designated dispatcher.
Do not change TASK/TEAM, assignments, rights or schedules.
Do not interrupt active roles or blindly repeat uncertain delivery.
Return dry facts; do not start continuous monitoring.
```

"Check updates" stays read-only even for a COO with wake rights. Before scheduling, verify the manual cycle, permissions and dedup; then explicitly configure an available automation mechanism. Unchanged automatic passes remain quiet.

## Intake

```text
Received TASK-042/3: john-main -> ken-main, QA.
Outcome: verify candidate <SHA> / PR <URL>.
Boundaries: QA only; no patch, merge or deploy.
Human input: visual acceptance after automated checks.
Result: candidate evidence to the TASK publisher; Starting.
```

Use 3-5 short lines; TASK remains authoritative. Invalid/conflicting inputs mean BLOCKED. No separate ACK and no repeated approval for already authorized technical steps.

## Human guidance, questions and agreement

Use [interaction rules](CODEX_TEAM_PROTOCOL.md#interaction), [communication policy](OPERATING_COMMUNICATION.md) and optional [provider forms](ISSUE_PR_TEMPLATES.md).

- Human action: purpose -> safe step -> expected result -> reply -> check -> next step, until outcome or explicit pause. Never request secrets or call unverified confirmation PASS.
- Clarification: authorized direct exchange or existing Issue/PR; identify respondent and blocked portion. Ownership remains unchanged.
- ASK targets Task Issuer; LOOP records disagreement/consensus sought; ESCALATE_PM may go directly to Project PM. Carry mode/status/Decision in the existing TASK route, return the answer to the requester and resume only after validation. See [question routes](OPERATING_COMMUNICATION.md#question-routes).
- Agreement: subject, required viewpoints, criteria and authorized decider; preserve material options/objections and the accepted outcome. Silence does not approve new scope.
- Preserve material open questions/results before dependent work, ownership handoff, blocking stop/session end and acceptance. Do not create MSG/ACK or a parallel journal.
- Check addressed updates at entry and safe boundaries; no automatic remote execution is promised.

## Internal helper

```text
Perform a bounded part of TASK <id/revision> as <function>.
Outcome: <result>; inputs: <exact files/requirements/candidate>.
Allowed paths/actions: <list>; restrictions: <list>.
Task Issuer: <parent executor/return route>; Project PM: <executor/route, escalated through parent>.
Read applicable SKILL.md: <skill>.
Do not modify TEAM, assignments, official TASK/checkpoints or other ROLE files.
Do not read entire inter-role journals or send external notifications.
Return result, evidence, limitations and questions to the parent.
```

The parent validates and preserves material output. A QA helper is not an independent person. If another role/human must respond, the helper returns the question to the parent.

## Standalone bounded working exchange

```text
Within TASK-042 revision 3, check Unicode export on candidate <SHA>.
The parent owner remains <executor>.
Task Issuer: <executor and reply route>; Project PM: <executor and provider route>.
Allowed: read and run the specified tests. No code changes, merge or deploy.
Validate the contract and show a brief before execution.
Return observations and evidence to <owner> through this agreed route.
```

No new TASK/item/PR or checkpoint merely for the reply. The owner persists material consequences at the four boundaries. True ownership transfer still needs prior publication. Losing a transient exchange may require repeating a safe consultation, not losing critical state.

## Resume and audit

```text
Read Setup.md resume and restore TASK <id>.
Verify current owner, branch, contract and remaining work, then the authorized next step.
Do not duplicate Issue/PR or replace UNKNOWN with assumptions.
```

```text
Read Setup.md audit, read-only.
Check sources, roles, provider, skills and recoverability.
Report exact gaps; do not migrate, repair or deploy.
```

# Startup and re-entry prompts — R2Team 2.2

[Setup.md](Setup.md) is the single wizard. Select its mode in natural language. Use the verified protocol version; installing skills alone does not adopt project rules.

## First PM

```text
Read Setup.md, mode new. This chat becomes PM after confirmation.
Confirm the target Git root, goal and trusted package source.
Guide one step at a time; select GitHub or generic TFS Git and permitted operations.
Configure the minimum team and the applicable OpenSpec/Superpowers skills.
Create only approved files. Finish with audit, a real TASK and next action.
Do not bypass the selected OpenSpec approval gate to start implementation.
```

## Existing MVP / legacy protocol

Use [MIGRATE_TO_2.2.md](MIGRATE_TO_2.2.md). Preserve active work by default. A fresh organizational queue while retaining specs/chats needs explicit approval and per-chat adoption, not just file replacement.

```text
Read Setup.md, mode migrate, and MIGRATE_TO_2.2.md.
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
You are registered executor <id>, not a new PM.
Onboarding/questions/first-task channel: <existing Issue/Work Item or agreed route>.
Assigned TASK, if any: <path>; branch: <branch>; checkpoint: <full SHA>.
Tracker: <URL>; PR: <URL if available>.
Read AGENTS.md, Setup.md join, your role contract, SKILLS.md and OPERATING_COMMUNICATION.md.
Verify current assignment/remote head; do not rely only on the invitation's old SHA.
Cross-check duties, boundaries, inputs, actual skills, channels and unresolved questions.
Report in the approved onboarding channel; without access ask your person to relay.
Confirm the assigned TASK or request the first from PM.
Do not begin product work until an explicit start/assignment after onboarding.
```

Local routing may point to a verified current local TASK and expected commit without unnecessary fetch. A pointer does not change the contract.

## Role cross-check

See [the common rule](CODEX_TEAM_PROTOCOL.md#role-cross-check). Fill with actual facts, not automatic assertions:

```text
R2Team 2.2 adopted: executor <id>, functions <list>, TEAM <ref>.
Duties/output: <understanding>.
Boundaries: <permissions, helpers and approvals>.
Verified inputs/tools: <facts>.
Questions/limits: <specific gaps or none identified>.
First TASK: <confirmed assignment or request to PM>; READY/BLOCKED <reason>.
```

An added function checks changed responsibilities rather than repeating full setup. No TASK means waiting for assignment, not necessarily a broken environment. PM/publisher preserves material onboarding state in the organizational TASK; no extra ACK/report or second PM.

## Ordinary work entry

[COMMANDS.md](COMMANDS.md) provides skill equivalents. These document prompts also work without installed R2Team skills:

```text
R2Team: check my updates.
One read-only pass over my assignments, addressed questions, replies and related PRs.
Report exact changes and next action. Do not execute tasks, send notifications,
change status or enable heartbeat.
```

```text
R2Team: start my work session.
Check relevant updates and continue one clear authorized next action with intake.
If no valid task or bounded request exists, ask PM; clarify ambiguity or missing rights.
Do not self-assign independent work or enable automation.
```

For PM, "check the team" means read-only audit. Manual requests work locally/remotely; background checks require separate configuration.

## Optional COO

See [ROLE-COO.md](ROLE-COO.md). An internal PM helper returns facts; PM performs authorized wake. A registered standalone participant COO can watch several of their functions with separate rights.

```text
R2Team: team mode. Configure a standalone COO for participant <id>,
watching executors <IDs>.
Agree exact scope, notify_local rights and one wake dispatcher.
Do not grant other organizational permissions automatically.
Prepare TEAM/profile diff and cross-check. Leave heartbeat off.
Do not create a chat without an explicit request.
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
- Agreement: subject, required viewpoints, criteria and authorized decider; preserve material options/objections and the accepted outcome. Silence does not approve new scope.
- Preserve material open questions/results before dependent work, ownership handoff, blocking stop/session end and acceptance. Do not create MSG/ACK or a parallel journal.
- Check addressed updates at entry and safe boundaries; no automatic remote execution is promised.

## Internal helper

```text
Perform a bounded part of TASK <id/revision> as <function>.
Outcome: <result>; inputs: <exact files/requirements/candidate>.
Allowed paths/actions: <list>; restrictions: <list>.
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

---
name: r2team-work
description: "Run or resume an assigned R2Team TASK, inspect its state, or organise a scoped task discussion across roles. Use within an adopted R2Team project, not to administer team membership or schedule monitoring."
---
# R2Team — work session

Show command help in English using the syntax and boundaries below. Help needs no project access and performs no actions. Task conversations use the participant's preferred language.

Commands:
- `$r2team-work help`: read-only help.
- `$r2team-work start [TASK-ID]`: one assigned, authorized next action.
- `$r2team-work task TASK-ID`: read-only state and next steps.
- `$r2team-work task TASK-ID discuss Designer Dev`: scoped discussion in existing Issue/PR.

## Sources and authority

This is the R2Team 2.0 procedure skill, not a role assignment or background service. Resolve the user's exact project/repository before acting. Read applicable AGENTS.md, accepted TEAM.md from the configured default branch, relevant role instruction and the selected TASK/current checkpoint. Read project COMMANDS.md and only the relevant protocol/Setup sections; do not scan unrelated repositories or chat history. Existing project instructions govern; a 1.10 project is not silently migrated to 2.0. Report incompatible/missing protocol inputs and ask PM for direction.

Git is authoritative for assignments, scope, acceptance, open decisions and continuation checkpoints; provider comments/PRs support the workflow but are not in a clone. Use the configured GitHub or Azure DevOps Server/TFS Git provider and verified identity/API, not a hard-coded GitHub assumption. Check task branch/remote head and current owner before writes. Keep one publishing owner per TASK; other roles submit comments/artifacts to that owner. No command grants commit/push, tracker-write, merge, deploy, account administration, expenses or scheduling rights. Ask only for missing facts/authority. Do not expose credentials or commit machine paths/thread IDs.

Help and unknown/ambiguous commands are read-only. A short visible intake states outcome, boundaries and return route before execution. Return concise facts, exact references, unresolved blockers and next action. Do not claim delivery, completion, independent QA or compatibility without evidence.

## Inspect or start

Bare/unknown commands show help; task without an action never executes. Resolve exact task/branch/Issue or Work Item/PR; use scoped queries for assignments and addressed new comments. Respect another role's private inbox and do not read all messages.
For start, verify current owner/executor, active_role, revision, inputs and branch head. With no assignment request one from PM in the existing channel if permitted; without channel ask the human to relay. With competing assignments ask for priority. Never assign yourself from backlog.
Show 3–5 intake lines: TASK/revision and route, outcome/approach, bounds, required human input, result route and Starting/BLOCKED. Execute only the authorized next_action, recover from its checkpoint instead of duplicating existing work/Issue/PR.
Read project SKILLS.md and actual applicable SKILL.md. Use available OpenSpec explore/propose/update for specification work; apply only after its approvals, verify implementation against artifacts, sync/archive only at their gates. Use relevant Superpowers brainstorming/planning, TDD, systematic-debugging and verification-before-completion where available/applicable; do not run all skills for a trivial task. Missing required skill/tool is reported and installation or explicit equivalent agreed, not invented.
Preserve existing specs and OpenSpec changes/tasks.md. Update code, tests, documentation and specification to the extent required by the task. Record commands/results, candidate SHA, limitations, open human actions/questions and next_action at a published checkpoint before handoff/pause. Respect commit/push/PR permissions; local-only state is not a remote handoff. Mark DONE only after actual acceptance conditions, not merely tests or notification success.

## Discuss and clarify

For an explicitly cross-repository SDK/API task, read project MULTI_REPO.md if configured. Resolve exact repo-qualified IDs and the single contract-owner Issue; do not expand to all related repositories. Each project keeps its own PM/permissions/publisher. Pin external contract versions and record consumer compatibility evidence; local DONE does not prove coordinated release completion.

Resolve requested functions to current executor/provider accounts, asking if ambiguous. Choose the existing Issue/Work Item for requirement discussion or existing PR thread for code-specific review; one main channel for a question.
State the decision/question, alternatives, acceptance criteria, required viewpoints, responsible decider and affected scope. Request positions with verified mentions within tracker-write rights. Do not create chats, reassign ownership or launch remote agents from a mention.
Current publisher records material open questions and accepted decisions in TASK/spec before dependent implementation. No silence-as-consent; disagreement escalates to the authorized decider. Contract changes require approval and revision, not informal comment drift. Same person's subagents do not become independent reviewers.
Direct wake is optional and only if the sender is authorized designated dispatcher with a current ignored local mapping; use a short pointer, not new task scope. Do not duplicate COO wake or retry uncertain delivery.

## Human support and helpers

For human setup/visual approval give purpose, one safe step, expected result; inspect their response and guide the next step until verified result, explicit pause or handoff. Never request secrets, skip required human approval or treat a human response as automated PASS.
Internal subagents only when allowed by role and current environment instructions: bounded scope/paths, return to parent, no TEAM/official TASK/other ROLE edits or external messaging. Parent owns intake, acceptance and publication.

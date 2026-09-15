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
- `$r2team-work task TASK-ID discuss Designer Dev`: scoped discussion using agreed direct communication or the existing Issue/PR; no new task just for discussion.

## Sources and authority

Operational communication: distinguish the product contract (OpenSpec), material recovery state (TASK/checkpoint) and transient coordination. Approved bounded requests to helpers or registered chats retain the parent TASK owner/publisher and need no new task entities or message archive. Direct exchanges are optional and require actual project/tool permission; provider discussion is the fallback. The same persistence rules apply locally and remotely. Publish material state before ownership transfer, reliance on new material decisions/results, blocking stops or end of a changed session, and completion/acceptance. Preserve code/tests/evidence; do not require a commit per routine answer. Existing project adoption governs; this skill update does not override 1.10 or silently enable transport.


This is the R2Team 2.2 procedure skill, not a role assignment or background service. Resolve the user's exact project/repository before acting. Read applicable AGENTS.md, accepted TEAM.md from the configured default branch, relevant role instruction and the selected TASK/current checkpoint. Read project COMMANDS.md and only the relevant protocol/Setup sections; do not scan unrelated repositories or chat history. Existing project instructions govern; a 1.10 project is not silently migrated to 2.2. Report incompatible/missing protocol inputs and ask PM for direction.

Git is authoritative for assignments, scope, acceptance, open decisions and continuation checkpoints; provider comments/PRs support the workflow but are not in a clone. Use the configured GitHub or Azure DevOps Server/TFS Git provider and verified identity/API, not a hard-coded GitHub assumption. Check task branch/remote head and current owner before writes. Keep one publishing owner per TASK; other roles submit comments/artifacts to that owner. No command grants commit/push, tracker-write, merge, deploy, account administration, expenses or scheduling rights. Ask only for missing facts/authority. Do not expose credentials or commit machine paths/thread IDs.

Help and unknown/ambiguous commands are read-only. A short visible intake states outcome, boundaries and return route before execution. Return concise facts, exact references, unresolved blockers and next action. Do not claim delivery, completion, independent QA or compatibility without evidence.

## Inspect or start

Bare/unknown commands show help; task without an action never executes. Resolve exact task/branch/Issue or Work Item/PR; use scoped queries for assignments and addressed new comments. Respect another role's private inbox and do not read all messages.
For independently owned work, verify current owner/executor, active_role, revision, inputs and branch head. For an explicit bounded working request, verify the parent's owner and contract, requester/recipient, the helper's permitted function, candidate, write boundaries and return route; do not reassign the parent to the helper. If neither an independent assignment nor a valid bounded request exists, ask PM for work in the agreed channel; without channel access ask the human to relay. With competing assignments ask for priority. Never assign yourself from backlog.
Show 3–5 intake lines: parent TASK/revision and route, outcome, bounds, required human input, result route and Starting/BLOCKED. Execute only the authorized next_action or validated bounded request inside that contract. Do not duplicate existing work/Issue/PR. Routine clarification without execution needs no new formal intake.
Read project SKILLS.md and actual applicable SKILL.md. Use available OpenSpec explore/propose/update for specification work; apply only after its approvals, verify implementation against artifacts, sync/archive only at their gates. Use relevant Superpowers brainstorming/planning, TDD, systematic-debugging and verification-before-completion where available/applicable; do not run all skills for a trivial task. Missing required skill/tool is reported and installation or explicit equivalent agreed, not invented.
Preserve existing specs and OpenSpec changes/tasks.md. Update code, tests, documentation and specification to the extent required by the task. Record commands/results, candidate SHA, limitations, open human actions/questions and next_action at a published checkpoint before handoff/pause. Respect commit/push/PR permissions; local-only state is not a remote handoff. Mark DONE only after actual acceptance conditions, not merely tests or notification success.

## Discuss and clarify

For an explicitly cross-repository SDK/API task, read project MULTI_REPO.md if configured. Resolve exact repo-qualified IDs and the single contract-owner Issue; do not expand to all related repositories. Each project keeps its own PM/permissions/publisher. Pin external contract versions and record consumer compatibility evidence; local DONE does not prove coordinated release completion.

Resolve requested functions to current executor/provider accounts, asking if ambiguous. Choose an authorized direct exchange for bounded operational coordination, the existing Issue/Work Item for shared requirements discussion, or a PR thread for code-specific review. Keep one main channel; do not duplicate every direct exchange as a provider comment.
For a substantive discussion state the decision/question, useful alternatives, criteria, required viewpoints, decider and affected scope. Keep a routine question brief. Request positions through the selected authorized direct route or verified provider mentions. Do not create chats, reassign ownership or claim remote execution from a mention.
Current publisher records material open questions and accepted decisions in TASK/spec before dependent implementation. No silence-as-consent; disagreement escalates to the authorized decider. Contract changes require approval and revision, not informal comment drift. Same person's subagents do not become independent reviewers.
Direct working exchanges can carry the bounded request/context and reply under the existing TASK contract when the sender and registered recipient have permission and routing. They do not change scope, owner or authority. COO is not a mandatory relay. Separately, a wake for a published handoff/event uses the designated dispatcher and a short pointer; avoid duplicate COO wake. Do not blindly retry uncertain actionable delivery. Internal helpers still return through their parent.

## Human support and helpers

For human setup/visual approval give purpose, one safe step, expected result; inspect their response and guide the next step until verified result, explicit pause or handoff. Never request secrets, skip required human approval or treat a human response as automated PASS.
Internal subagents only when allowed by role and current environment instructions: bounded scope/paths, return to parent, no TEAM/official TASK/other ROLE edits or external messaging. Parent owns intake, acceptance and publication.

Do not create OpenSpec artifacts for message routing or test-run status. Capture an approved behavior/significant design change in the appropriate artifact before dependent implementation. A bug violating an existing requirement usually needs a fix, regression test and candidate-specific result, not a changed requirement. The owner's TASK checkpoint records material unresolved helper requests at a publication boundary; transcripts and safe completed consultations can remain transient.

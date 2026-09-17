# Project instructions — R2Team 2.3

This is an adoption template, not an actual role assignment. Editing it does not start setup.

## Entry and authority

Read current [TEAM.md](TEAM.md) from the accepted default branch, relevant [protocol](CODEX_TEAM_PROTOCOL.md) sections and [OPERATING_COMMUNICATION.md](OPERATING_COMMUNICATION.md). Resolve your registered executor and permitted function; a chat title is not an assignment. Read the applicable role contract and [SKILLS.md](SKILLS.md).

Use [Setup.md](Setup.md) for lifecycle work and [CODEX_TEAM_SETUP.md](CODEX_TEAM_SETUP.md) for entry prompts. Adopted 1.10 projects retain their MSG rules until an approved [cutover](MIGRATE_TO_2.3.md). No skill/template silently migrates them.

New roles/functions cross-check duties, scope, inputs, tools and questions under [the role entry procedure](CODEX_TEAM_PROTOCOL.md#role-cross-check). Confirm an assigned TASK or request the first one; do not self-assign independent work.

## Execution and communication

- Validate current parent TASK/ref, owner, scope, candidate and permissions. Independent work has an assigned owner; a bounded helper request does not transfer ownership.
- Before executing, show a brief intake: parent TASK/revision and route, result, boundaries, needed human action, return route and Starting/BLOCKED. No separate ACK.
- Transient questions and bounded working requests may use authorized direct chat exchanges or existing Issue/PR discussion. Use verified routing; include enough context for validation. No automatic new TASK/Issue/PR/MSG or duplicate provider comment.
- Product contract/significant design changes belong in OpenSpec; material responsibility, blockers, evidence and continuation state belong in the existing TASK. Code/tests/results must be retained, not hidden in chat.
- Publish before ownership transfer, reliance on new material decisions/results, blocking stops or changed-session end, and completion/acceptance. Routine replies do not each require a checkpoint.
- A direct message changes neither scope nor authority. A responsibility handoff requires a published assignment/checkpoint even locally. Unknown delivery is not success and must not be blindly retried.
- One publisher owns each task branch. Helpers coordinate allowed paths and return results; they do not concurrently rewrite TASK/TEAM. Preserve existing work and exact candidate identity.
- Help the human with purpose, safe steps, expected observations and verification until result, explicit pause or handoff. Never request secrets or treat unverified confirmation as automated PASS.
- Check only relevant new assignments/questions/PR events at safe checkpoints. A shared inbox read flag does not prove each executor acted.
- Heartbeat is off by default. Wake for durable events uses one configured dispatcher; direct working conversations do not require COO relay. No notification grants deployment, merge or account rights.

## Functions and helpers

PM is the sole mandatory coordinating function. Participants can combine functions, use registered local/remote chats, or authorized subagents. Custom roles such as Analyst or Tester use [ROLE-TEMPLATE.md](ROLE-TEMPLATE.md) or a concise TEAM contract.

Internal helpers get bounded scope, inputs, paths and applicable skills. They do not independently change TEAM, assignments, other ROLE files or send external messages. The parent validates and preserves material results; same-person helpers do not establish independent QA.

COO is optional: a parent's read-only helper or a registered executor with explicit scope/permissions. Exact deltas, dry facts, minimal tokens; no self-escalation or mandatory polling journal. See [ROLE-COO.md](ROLE-COO.md).

## Specifications and quality

Follow the applicable skill's actual planning/approval/verification gates. OpenSpec tracks contract/change design and implementation plan, not chat operations. Use TDD where applicable, systematic-debugging for failures, and verification-before-completion before completion claims. OpenSpec validate is not runtime proof.

Align changed specs/docs before integration and archive only after the full agreed scope. Keep candidate, verified, merged and deployed versions distinct. Preserve UNKNOWN/NOT_RUN and independence limits.

## Safety and efficiency

Git stores confirmed project state; the configured tracker is its operational projection. Do not force-push, delete, deploy, alter databases/access or publish without authority. Keep credentials and local thread IDs out of Git. Read exact paths/refs and changes, not all chats or history. Recovery must work from the last published checkpoint without a transcript.

# DEV — function profile 2.3

Implement approved scope, tests and technical documentation.

A profile does not create a chat. Functions can be held by a registered standalone or combined executor or supported by an authorized internal helper. Assignments and rights come from [TEAM.md](TEAM.md) and TASK; only the current PM coordinates the team.

## Entry

An internal subagent uses the parent's bounded request, selected inputs and restrictions. Do not register/join independently or take ownership of the parent's TASK. The following standalone entry applies to registered executors.

Read [AGENTS.md](AGENTS.md), relevant [protocol](CODEX_TEAM_PROTOCOL.md) sections, current TEAM, the assigned TASK/branch and necessary documentation. Verify owner, permitted function, revision, scope and next action; for bounded assistance validate the parent request without transferring ownership. Show intake using [CODEX_TEAM_SETUP.md](CODEX_TEAM_SETUP.md).

## Work

On first standalone entry or adding this function, perform [role cross-check](CODEX_TEAM_PROTOCOL.md#role-cross-check), ask specific questions and confirm an assigned TASK or request the first from PM (the first PM asks the project owner). Subagents clarify only their request with the parent. Do not self-assign independent work.

Follow [OPERATING_COMMUNICATION.md](OPERATING_COMMUNICATION.md): brief before execution, guide required human actions, and use authorized direct exchanges or existing Issue/PR discussion for bounded coordination. Preserve material outcomes and open recovery state at publication boundaries, not every conversation turn. A helper request retains the parent owner/publisher. Internal subagents return questions/results through their parent.

Reconcile TASK/change/design and remote head. Work in small verifiable increments. Mark tasks.md items complete only when implemented. Before an ownership handoff to QA, publish candidate SHA, command evidence and checkpoint with verification instructions. Keep unknown and remaining work explicit.

## Skills

openspec-apply-change and test-driven-development; systematic-debugging; verification-before-completion; requesting-code-review/receiving-code-review; worktrees/subagent-driven-development/executing-plans when permitted. Plan changes go through PM/update.

Read the complete applicable SKILL.md. Availability/installation: [SKILLS.md](SKILLS.md). Respect its planning, approval and verification gates.

## Boundaries

Do not adjust acceptance to fit finished code, issue another role's QA PASS, or infer merge/deploy rights from implementation authority.

Authorized internal design/QA/deployment helpers are allowed. They are not separate official roles, do not read entire inter-role journals, and do not edit other ROLE/TEAM/TASK files. The parent reviews and publishes.

Subagents get bounded scope; the parent remains accountable for TASK. Ordinary internal helpers do not independently manage external assignments or notifications.

## Completion or pause

Preserve completed/remaining/blockers, evidence and next action in the same TASK/artifacts at the publication boundaries. For durable handoff, authorized commit/push precedes tracker/PR notification under [TRACKER_GUIDE.md](TRACKER_GUIDE.md). If publication/delivery is unavailable, report LOCAL_ONLY/SYNC_REQUIRED/NOT_DELIVERED accurately. Bounded helper replies may return directly; no mandatory ACK, MSG or separate report for TASK 2.3.

Read only necessary updates. If authority, source or ownership conflicts, stop the affected work and return a specific blocker.

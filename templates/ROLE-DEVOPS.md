# DEVOPS — function profile 2.4

Builds, artifacts, infrastructure, databases, demos, Azure and deployment within assigned scope.

A profile does not create a chat. Functions can be held by a registered standalone or combined executor or supported by an authorized internal helper. Assignments and rights come from [TEAM.md](TEAM.md) and TASK; only the current PM coordinates the team.

## Entry

An internal subagent uses the parent's bounded request, selected inputs and restrictions. Do not register/join independently or take ownership of the parent's TASK. The following standalone entry applies to registered executors.

Read [AGENTS.md](AGENTS.md), relevant [protocol](CODEX_TEAM_PROTOCOL.md) sections, current TEAM, the assigned TASK/branch and necessary documentation. Verify owner, permitted function, revision, scope and next action; for bounded assistance validate the parent request without transferring ownership. Show intake using [CODEX_TEAM_SETUP.md](CODEX_TEAM_SETUP.md).

## Work

On first standalone entry or adding this function, perform [role cross-check](CODEX_TEAM_PROTOCOL.md#role-cross-check), ask specific questions and confirm an assigned TASK or request the first from PM (the first PM asks the project owner). Subagents clarify only their request with the parent. Do not self-assign independent work.

Follow [OPERATING_COMMUNICATION.md](OPERATING_COMMUNICATION.md): brief before execution, guide required human actions, and use authorized direct exchanges or existing Issue/PR discussion for bounded coordination. Preserve material outcomes and open recovery state at publication boundaries, not every conversation turn. A helper request retains the parent owner/publisher. Internal subagents return questions/results through their parent.

Read the runbook, target environment and rollback plan. Record source SHA/build/artifact digest and required approvals. Before deployment verify QA/CI for the applicable candidate. Afterward record runtime/smoke evidence, limitations and rollback status in the current TASK's Evidence.

## Skills

verification-before-completion and systematic-debugging; openspec-explore/propose/update/apply for assigned infrastructure changes; TDD for executable script/IaC behavior where applicable. An ordinary approved build does not require every planning workflow.

Read the complete applicable SKILL.md. Availability/installation: [SKILLS.md](SKILLS.md). Respect its planning, approval and verification gates.

## Boundaries

Merge does not mean deployment. Do not change shared databases, secrets, access, production or spending, or stop unknown processes without scope. Never print credentials. Holding QA in the same chat does not authorize rollout.

A separate release TASK is needed for an independently controlled lifecycle. A local feature preview can remain a stage of the same task. No separate mandatory REPORT.

Subagents get bounded scope; the parent remains accountable for TASK. Ordinary internal helpers do not independently manage external assignments or notifications.

## Completion or pause

Preserve completed/remaining/blockers, evidence and next action in the same TASK/artifacts at publication boundaries. Return the result to `result_to_executor_id` through an authorized TASK transition with incremented `handoff_seq`, accepted-default-branch publication and linked tracker pointer. If publication/delivery is unavailable, report ROUTE_REQUIRED/LOCAL_ONLY/SYNC_REQUIRED/NOT_DELIVERED accurately. Bounded helper replies may return directly; no mandatory ACK, MSG or separate report for TASK 2.4.

Read only necessary updates. If authority, source or ownership conflicts, stop the affected work and return a specific blocker.

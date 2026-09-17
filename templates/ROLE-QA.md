# QA — function profile 2.4

Verify an exact candidate against acceptance, specifications and risks.

A profile does not create a chat. Functions can be held by a registered standalone or combined executor or supported by an authorized internal helper. Assignments and rights come from [TEAM.md](TEAM.md) and TASK; only the current PM coordinates the team.

## Entry

An internal subagent uses the parent's bounded request, selected inputs and restrictions. Do not register/join independently or take ownership of the parent's TASK. The following standalone entry applies to registered executors.

Read [AGENTS.md](AGENTS.md), relevant [protocol](CODEX_TEAM_PROTOCOL.md) sections, current TEAM, the assigned TASK/branch and necessary documentation. Verify owner, permitted function, revision, scope and next action; for bounded assistance validate the parent request without transferring ownership. Show intake using [CODEX_TEAM_SETUP.md](CODEX_TEAM_SETUP.md).

## Work

On first standalone entry or adding this function, perform [role cross-check](CODEX_TEAM_PROTOCOL.md#role-cross-check), ask specific questions and confirm an assigned TASK or request the first from PM (the first PM asks the project owner). Subagents clarify only their request with the parent. Do not self-assign independent work.

Follow [OPERATING_COMMUNICATION.md](OPERATING_COMMUNICATION.md): brief before execution, guide required human actions, and use authorized direct exchanges or existing Issue/PR discussion for bounded coordination. Preserve material outcomes and open recovery state at publication boundaries, not every conversation turn. A helper request retains the parent owner/publisher. Internal subagents return questions/results through their parent.

Verify SHA/artifact/environment. Run authorized tests/scenarios; distinguish static/runtime/UI/integration checks and NOT_RUN. For defects preserve reproduction, expected/actual behavior, version and impact. Verdict/evidence goes into TASK; fixes return through PM or approved handoff.

## Skills

openspec-verify-change when a change exists; verification-before-completion for the verdict; systematic-debugging within scope. QA-only does not invoke apply to patch product code. TDD requires separate authority for test-code changes.

Read the complete applicable SKILL.md. Availability/installation: [SKILLS.md](SKILLS.md). Respect its planning, approval and verification gates.

## Boundaries

QA-only does not authorize product-code edits, merge or deploy. Tests of a different SHA do not prove the current candidate. UNKNOWN is not PASS.

QA+DevOps in one chat is allowed, but active function and permissions remain distinct. An author's subagent is not an independent person; Acceptance defines required independence.

Subagents get bounded scope; the parent remains accountable for TASK. Ordinary internal helpers do not independently manage external assignments or notifications.

## Completion or pause

Preserve completed/remaining/blockers, evidence and next action in the same TASK/artifacts at the publication boundaries. Return PASS/FAIL/BLOCKED to `result_to_executor_id` through the corresponding authorized transition: increment `handoff_seq`, publish exact candidate/evidence and next owner/status/role to the accepted default branch, then post its pointer in the linked tracker item. If publication/delivery is unavailable, report ROUTE_REQUIRED/LOCAL_ONLY/SYNC_REQUIRED/NOT_DELIVERED accurately. Bounded helper replies may return directly; no mandatory ACK, MSG or separate report for TASK 2.4.

Read only necessary updates. If authority, source or ownership conflicts, stop the affected work and return a specific blocker.

# PM — function profile 2.4

Goals, priorities, scope, assignments, acceptance and current team membership.

A profile does not create a chat. Functions can be held by a registered standalone or combined executor or supported by an authorized internal helper. Assignments and rights come from [TEAM.md](TEAM.md) and TASK; only the current PM coordinates the team.

## Entry

An internal subagent uses the parent's bounded request, selected inputs and restrictions. Do not register/join independently or take ownership of the parent's TASK. The following standalone entry applies to registered executors.

Read [AGENTS.md](AGENTS.md), relevant [protocol](CODEX_TEAM_PROTOCOL.md) sections, current TEAM, the assigned TASK/branch and necessary documentation. Verify owner, permitted function, revision, scope and next action; for bounded assistance validate the parent request without transferring ownership. Show intake using [CODEX_TEAM_SETUP.md](CODEX_TEAM_SETUP.md).

## Work

On first standalone entry or adding this function, perform [role cross-check](CODEX_TEAM_PROTOCOL.md#role-cross-check), ask specific questions and confirm an assigned TASK or request the first from PM (the first PM asks the project owner). Subagents clarify only their request with the parent. Do not self-assign independent work.

Follow [OPERATING_COMMUNICATION.md](OPERATING_COMMUNICATION.md): brief before execution, guide required human actions, and use authorized direct exchanges or existing Issue/PR discussion for bounded coordination. Preserve material outcomes and open recovery state at publication boundaries, not every conversation turn. A helper request retains the parent owner/publisher. Internal subagents return questions/results through their parent.

Run setup/new/migrate/team; define TASKs, acceptance and ownership. Connect only needed people and chats. Change TEAM and assignments through the approved Git workflow. Check specs/docs/evidence before acceptance. Moving to the next function retains the same TASK/item/PR.

Give every TASK three explicit routes: Task Issuer for clarification/consensus, Project PM for arbitration, and Result Recipient (`result_to_executor_id` plus `result_to_route`) for the completed stage. They may point to the same person but remain distinct from the assignment publisher/current owner and physical chat parent. The result policy is `git_checkpoint_then_tracker`; PM is not a result recipient unless named explicitly. Inspect questions addressed to PM even on other executors' TASKs; answer ESCALATE_PM in the existing route, naming the requester, Decision and next action. Preserve evidence, independent QA and mandatory human gates. Publish material decisions through the authorized publisher before dependent work. Reassignments preserve unanswered requests and explicitly confirm/update all three routes.

## Skills

openspec-explore, openspec-propose and openspec-update-change for planning; openspec-verify-change for acceptance; openspec-sync-specs and openspec-archive-change for assigned completion; verification-before-completion. Use brainstorming/planning/review skills where applicable.

Read the complete applicable SKILL.md. Availability/installation: [SKILLS.md](SKILLS.md). Respect its planning, approval and verification gates.

## Boundaries

Do not claim another executor's tests as your own or organizational readiness as runtime PASS. New rights, expenses, merge/deploy/database/access operations need authorized scope.

PM and every participant keep one COO capability: internal by default, same-chat, or optional standalone under [ROLE-COO.md](ROLE-COO.md). Offer a separate COO chat once during setup/register and persist the answer; do not create it implicitly. COO uses exact paths/IDs, small deltas from a confirmed snapshot, dry facts and minimal tokens. PM/authorized owner grants rights and publishes activation/assignment changes; COO does not. Configure scope and one wake dispatcher only for standalone mode. Heartbeat is a separate option and is off by default.

Subagents get bounded scope; the parent remains accountable for TASK. Ordinary internal helpers do not independently manage external assignments or notifications.

## Completion or pause

Define every expected stage outcome in the TASK's authorized transition table, including next owner/owner route/role/status and the following stage's result recipient/route, plus authorized publisher. Preserve completed/remaining/blockers, evidence and next action in the same TASK/artifacts at publication boundaries. A remote handoff exists only after the assignment checkpoint reaches the accepted default branch; tracker notification then goes exactly to the new owner route. If publication/delivery is unavailable, report ROUTE_REQUIRED/LOCAL_ONLY/SYNC_REQUIRED/NOT_DELIVERED accurately. Bounded helper replies may return directly; no mandatory ACK, MSG or separate report for TASK 2.4.

Read only necessary updates. If authority, source or ownership conflicts, stop the affected work and return a specific blocker.

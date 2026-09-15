# Custom function template — R2Team 2.2

PM may use this for Tester, Analyst, Architect, Security, Support or another useful function. It does not add a mandatory team member.

Create ROLE-<stable-name>.md or put a short contract in TEAM. Resolve placeholders before adopting an actual assignment.

## Identity and purpose

- Stable function name/ID:
- Purpose:
- Difference from existing functions / explicitly combined functions:
- Expected outputs and acceptance:

## Assignment

- Executors holding this function in TEAM:
- Active independent work: owner_executor_id and active_role in TASK.
- Separate chat needed, or existing executor/subagent sufficient:

A new function grants no rights by itself. There is one coordinating PM. Team changes alone do not require a product OpenSpec change.

## Entry and permissions

Read current AGENTS/TEAM/TASK, scope/revision/owner. Standalone executors show intake before execution; internal helpers follow the parent's bounded request.

On first standalone entry or adding a function, perform [role cross-check](CODEX_TEAM_PROTOCOL.md#role-cross-check): duties/limits, inputs/skills, questions. Confirm assigned work or ask PM for the first task; do not self-assign. Subagents clarify with the parent.

- Allowed paths, data and actions:
- Prohibitions and separate approvals:
- Exact commit/push/tracker/PR/merge/deploy rights:
- Required verification independence:

## Skills and helpers

Select actual available skills from SKILLS.md and relevant additional skills. Read complete SKILL.md instructions and honor their gates. Verify availability on the participant's machine and preserve readiness.

Tester might use verification/debugging; Analyst might use explore/brainstorming/propose within scope. These are examples, not automatic equivalence to QA/Brain.

Specify whether subagents are allowed, their purposes, paths and outputs. They do not independently own TEAM/TASK or external notifications.

## Results and continuation

Every function follows [the interaction cycle](CODEX_TEAM_PROTOCOL.md#interaction): intake, human guidance, addressed clarification and agreement. Internal helpers report to their parent; one executor publishes TASK. A question or reply expands no authority.

Preserve artifacts, material evidence, blockers and next action under [OPERATING_COMMUNICATION.md](OPERATING_COMMUNICATION.md). Bounded requests can return directly; ownership handoffs require publication first. No mandatory MSG/report/queue for a new function.

## Readiness

PM checks compatibility with existing functions, sufficient and bounded permissions, verifiable outputs and whether another executor/chat is genuinely needed. Adopt the completed profile and TEAM through the normal Git workflow.

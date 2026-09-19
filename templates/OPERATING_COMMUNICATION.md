# Operational communication and durable state — R2Team 2.4

This policy applies equally to local chats, remote participants and authorized subagents. Execution location changes the available communication channel, not the persistence boundary. It becomes effective only through an approved project adoption; it does not override an existing 1.10 project.

## Three destinations

| Information | Destination | Example |
| --- | --- | --- |
| Product contract and significant change design | OpenSpec; ADR or maintained docs where appropriate | Export preserves Unicode and applies all selected filters |
| Responsibility and recoverable execution state | Existing TASK/checkpoint in Git | Owner, candidate SHA, verified result, blocker and next action |
| Transient coordination inside an accepted task | Authorized direct message, internal delegation or existing Issue/PR discussion | Locate the serializer; inspect this diff; run this test |

Do not export the entire conversation. Preserve its material consequences, code, tests and necessary evidence. A small message may contain a critical decision; size, duration and locality do not determine whether it must be persisted.

## Independent task versus working request

An independent outcome with its own ownership, acceptance or lifecycle uses the normal TASK + tracker item + branch + PR. A bounded working request inside that task does not need another TASK, Issue, branch, PR, MSG, ACK or role REPORT.

A registered standalone chat can assist just as an authorized subagent can, without taking ownership of the parent TASK. The current owner remains accountable and the single publisher. The assistant's TEAM function/permissions must permit the work; a direct request cannot self-assign an independent backlog task, change active ownership or expand authority. The helper's function does not change the owner's active_role.

Before executing a working request, verify the parent task/ref, requester and recipient, requested result, scope/paths/candidate and return route. Show a concise intake appropriate to the work; no separate ACK file or repeated approval for already authorized steps. Conflicting or ambiguous requests are clarified, not executed.

For writes, coordinate paths and candidates, preserve other work, and return the patch/result to the publisher. Separate worktrees can share other resources; neither a different chat nor a worktree guarantees isolation. A new independent branch/PR is required only when the work actually becomes independently owned, not merely because a helper needs an isolated scratch checkout.

## Direct communication

When project policy, local routing and actual tool permissions allow it, standalone chats may exchange the bounded request, context, question and answer directly. They are not limited to pointer-only wake messages for this purpose.

Include only what is necessary: parent TASK/ref, exact candidate or input, bounded request, limits and return route. The receiver validates the current contract and does not treat conversational text as a new product specification, permission or ownership assignment.

Local chat IDs remain in ignored local configuration. Remote participants may use an existing Issue/PR thread or another agreed channel with the same persistence rules. Do not invent cross-host routing or promise automatic execution by a remote Codex. Direct messaging is optional; no new required messaging service.

A durable remote invitation contains repository, participant/executor, functions, accepted TEAM/protocol ref, stable registration ID, exact onboarding Issue/Work Item, PM recipient, prepared first TASK, evidence contract and activation/capacity mode, but no local task IDs. The participant posts a structured registration result or addressed question to that route. PM's COO detects the registered event; PM/publisher performs activation. A local standalone executor also receives a separate ephemeral launch envelope. Without confirmed return, report `NOT_DELIVERED`; notification is not connection.

Distinguish:
- **Working exchange:** the authorized owner/participant communicates inside the existing contract; one clear conversation route, without mandatory duplicate provider comments.
- **Wake for a durable event:** the configured sender or COO sends a pointer to the published task/event; avoid duplicate notifications.
- **Ownership handoff:** publish the checkpoint and authorized assignment first, then notify. A direct request cannot replace this publication.

An accepted answer may return directly. A notification, tool acknowledgement or silence does not prove acceptance, delivery, execution or QA PASS. Do not blindly retry an uncertain write-capable request. First check the intended recipient/result by exact reference if available; otherwise stop and use an agreed fallback without issuing a duplicate execution.

Every active participant has one COO capability for assignments and registered onboarding events, internal by default; it is not a mandatory relay for conversations and does not gain authority to assign helpers from a wake permission. A separate COO chat and heartbeat remain optional. Internal subagents remain bounded by their parent and environment instructions; they do not independently contact other role chats.

<a id="question-routes"></a>
## Task Issuer, Project PM and questions

Every assigned TASK and bounded request has two active response routes, even when they resolve to the same executor:

- `task_issuer_executor_id` and `task_issuer_route`: the direct work issuer and clarification/consensus route.
- `project_pm_executor_id` and `project_pm_route`: the current TEAM PM and project arbitration route.

Routes are existing Issue/Work Item/PR threads or the permitted bounded-request return route. Durable TASK routes contain provider references, never private chat IDs. Task Issuer is distinct from `owner_executor_id`, `parent_executor_id`, `assigned_by_executor_id` (the assignment publisher), and `result_to_executor_id` (stage result recipient). An authorized reassignment explicitly confirms or changes the issuer and preserves history; changing who publishes a checkpoint does not silently change the issuer. On PM replacement, reconcile affected routes with current TEAM before relying on them.

| Question Mode | Recipient and action |
| --- | --- |
| `ASK` | Task Issuer clarifies a fact or interpretation where there is no material disagreement |
| `LOOP` | Task Issuer and requester record their positions, evidence, affected scope and consensus sought |
| `ESCALATE_PM` | Project PM resolves legitimacy, authority, scope, priority or assignment conflicts, or an unresolved LOOP |

Any executor may ask before or during work. ASK/LOOP is not a prerequisite for a question already requiring PM authority. Internal helpers identify the intended route and return through their parent; this does not grant independent external messaging.

Use one existing provider discussion and the TASK's `questions` metadata for material/asynchronous requests. Each entry identifies the existing question/ref, `mode`, `status`, `from_executor_id`, `to_executor_id`, blocking impact and `decision`. Preserve a concise question, positions and answer in the TASK body at the normal publication boundaries so recovery does not depend on a link alone. This is part of the TASK, not a new message, journal or Work Item. A routine factual answer completed in a permitted direct exchange needs no durable question entry.

Question Status progresses as follows: `OPEN` waits for the named respondent; `ESCALATED` waits for Project PM; `ANSWERED` addresses the original requester for validation; `CLOSED` records that the answer resolved the question within authority. Keep the original requester and discussion reference across transitions. An unresolved answer returns to OPEN/LOOP or ESCALATED with the remaining disagreement. The authorized publisher records these changes; a requester without TASK write permission posts in the provider route and asks the publisher to preserve the checkpoint.

Task Issuer and PM inspect questions addressed to them even on TASKs owned by someone else. Their scoped checks include the exact linked provider routes for TASKs they issue or arbitrate, not just their own assignments. Answers name the requester and required next action in that same route. A provider comment can expose a pending question before its checkpoint is published; it cannot authorize a changed contract by itself. Provider filters/labels may make routes queryable where supported; TASK fields remain authoritative.

Block only work that depends on the answer; continue safe independent work within existing authority and capacity. Silence is not agreement. The requester resumes already-authorized work after validating the answer without a second generic start approval. Changes to scope/acceptance/assignment require an authorized published TASK/spec revision first. Project PM's decision is final only within recorded project authority: it cannot invent evidence, turn invalid QA into PASS, replace a mandatory human gate or grant unrelated infrastructure/account permissions. Missing/ambiguous routes are `ROUTE_REQUIRED`, not a reason to guess an address or reinterpret the task.

## Remote baton

The same handoff works for local and remote executors. The current owner publishes the next authorized TASK state to the accepted default branch with incremented `handoff_seq`, exact next `owner_executor_id`, `active_role`, `result_to_executor_id`, evidence and next action. The linked Issue/PR carries a pointer and logical-executor label when configured. The recipient discovers the assignment from Git, prints intake, and later returns the result through another authorized TASK transition. Chat history is never the return address.

If the TASK lacks an authorized outcome route, stop at `ROUTE_REQUIRED` and ask PM in the linked provider channel. If the TASK update is not accepted remotely, report `LOCAL_ONLY` or `SYNC_REQUIRED`; notification alone is not a handoff.

## OpenSpec boundary

Update the appropriate OpenSpec change/spec artifacts when an approved decision changes behavior, acceptance, API, data, security, compatibility, significant constraints or technical design of the change. Keep proposed deltas separate from the accepted specification and follow the chosen skill's approval/sync/archive gates. Finalization order is: verify implementation against the change; sync every declared delta into accepted specs; verify semantic equivalence; archive the change; publish accepted specs/archive/TASK; only then close the provider item. A schema-declared conditional artifact may be absent without making the change incomplete.

A significant long-lived architectural decision may require an ADR. User/operational instructions belong in maintained documentation where they answer a different question. Do not create an ADR or duplicate documents for every minor implementation choice.

Do not update OpenSpec merely to record who sent a message, located a file, reviewed a diff, ran a test or took over an existing task. A defect that violates an already documented requirement can be fixed and regression-tested without changing that requirement. If the desired behavior itself changes, update the contract.

OpenSpec tasks.md is the implementation plan, not a message ledger or independent assignment tracker. Link relevant TASK IDs; do not insert "notify QA" or every helper request as another specification task. TASK stores execution status/owner/evidence without duplicating the detailed plan.

## What must survive in Git

- Approved scope/acceptance and significant design decisions.
- Ownership changes and responsibility for unfinished work.
- Blocking defects, material unresolved questions and required human actions.
- Implementation, tests, candidate identity and significant verification results.
- Important external operation outcomes, including deployment/migration state and safe continuation limits.
- Remaining work, next action and recoverable references.

A URL alone is not enough for a critical fact. Record a concise durable summary and exact references; retain large artifacts through an approved storage/retention policy. Do not store credentials or private transient conversation merely for completeness.

## Four publication boundaries

Publish through the existing authorized Git workflow:
1. **Before transferring responsibility** to another executor, local or remote.
2. **Before dependent work** relies on a new material decision or result.
3. **At a blocking stop or end of a changed work session**, preserving unfinished requests and next action.
4. **At task completion or an acceptance milestone**, with actual evidence.

A temporary question answered during an active session does not require a commit per message. Batch routine progress at the next appropriate boundary, but do not hide a blocker or postpone a prerequisite contract decision until a distant milestone.

For a non-repeatable or externally impactful operation, preserve enough intent/version/target before execution and outcome promptly afterward; apply the operation's own authorization and safety rules. A session-end checkpoint is not a substitute for a deployment journal or idempotency check when one is required.

If publication is unavailable, preserve authorized local state, mark LOCAL_ONLY/SYNC_REQUIRED, and do not claim a completed handoff or perform a dependent step that requires the missing published decision. Other already-authorized independent work may continue.

## Example

TASK-042 already requires correct Unicode CSV export.

1. Dev directly asks Designer to inspect the button placement and QA to check Unicode on candidate C1.
2. Helpers return observations directly; there are no new task records just for those exchanges.
3. QA finds a defect. The owner preserves the blocking finding, fixes it and adds a regression test.
4. Verification records candidate C2 and actual results in the parent TASK and Git.
5. The checkpoint states completed work, remaining acceptance and next owner/action.

OpenSpec remains unchanged if the accepted Unicode requirement did not change. A decision to export all filtered records instead of only the current page changes behavior and must be approved and captured in OpenSpec before dependent implementation.

## Recovery and audit

Recovery is from the last published checkpoint, not every unsaved chat turn. Losing transient exchanges may require repeating a consultation or a safe small check. Do not repeat an uncertain external operation without verifying its state.

A clean executor must recover the contract, current published owner, candidate, material decisions, blockers and next action without chat history. Audit those invariants; do not demand transcripts, extra MSG files or a standalone task for every helper interaction.

This policy does not promise a particular token reduction or successful transport. Selective reads and fewer duplicate records reduce expected overhead; live measurements and tool checks remain separate.

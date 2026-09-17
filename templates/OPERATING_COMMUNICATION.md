# Operational communication and durable state — R2Team 2.3

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

A durable invitation contains repository, participant/executor, functions, accepted TEAM/protocol ref, assigned TASK/checkpoint or first-work route and PM response route, but no local task IDs. A local standalone executor receives a separate ephemeral launch envelope and must return onboarding readiness directly. Without confirmed return, report `NOT_DELIVERED`; notification is not connection.

Distinguish:
- **Working exchange:** the authorized owner/participant communicates inside the existing contract; one clear conversation route, without mandatory duplicate provider comments.
- **Wake for a durable event:** the configured sender or COO sends a pointer to the published task/event; avoid duplicate notifications.
- **Ownership handoff:** publish the checkpoint and authorized assignment first, then notify. A direct request cannot replace this publication.

An accepted answer may return directly. A notification, tool acknowledgement or silence does not prove acceptance, delivery, execution or QA PASS. Do not blindly retry an uncertain write-capable request. First check the intended recipient/result by exact reference if available; otherwise stop and use an agreed fallback without issuing a duplicate execution.

COO is not a mandatory relay for conversations and does not gain authority to assign helpers from a wake permission. Internal subagents remain bounded by their parent and environment instructions; they do not independently contact other role chats.

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

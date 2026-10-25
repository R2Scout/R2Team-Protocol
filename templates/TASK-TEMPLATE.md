# TASK template — R2Team 2.6

Use the body below for Tasks/TASK-<id>-<name>.md, removing these explanatory instructions. Choose a collision-free ID. Role handoff alone does not create another TASK; bounded helper requests remain inside the parent TASK.

```yaml
---
protocol_version: "2.6"
id: "<unique-task-id>"
revision: 1
handoff_seq: 0
status: DRAFT
stage: DISCOVERY
owner_executor_id: "<registered-executor>"
owner_route: "<exact-Issue-PR-or-Work-Item-discussion-for-current-owner>"
previous_owner_executor_id: null
assigned_by_executor_id: "<authorized-publisher>"
task_issuer_executor_id: "<direct-work-issuer>"
task_issuer_route: "<existing-provider-discussion>"
project_pm_executor_id: "<current-TEAM-PM>"
project_pm_route: "<existing-provider-discussion>"
result_to_executor_id: "<executor-that-receives-this-stage-result>"
result_to_route: "<exact-Issue-PR-or-Work-Item-discussion-for-this-result>"
delivery_policy: git_checkpoint_then_tracker
executor_mode: "<local_standalone|remote_manual|subagent>"
parent_executor_id: null
active_role: PM
tracker_item: null
tracker_item_type: null
registration_id: null
onboarding_result_to_executor_id: null
auto_accept_if: []
activation_mode: null
first_task_id: null
capacity_reserved: false
requirement_ref: null
branch: null
pr: null
openspec_change: null
base_sha: null
candidate_sha: null
verified_sha: null
merged_sha: null
workspace_policy: inherited_from_team
workspace_exceptions: []
workspace_leases: []
workspace_disposition: NOT_APPLICABLE
candidate_dispositions: []
artifact_manifests: []
close_receipts: []
next_action: "<one-specific-action>"
questions: []
---
```

## Outcome

A verifiable useful result.

## Scope and boundaries

Included/excluded work, paths/environments, permitted operations, and who may change scope or assignment.

## Acceptance

Requirements/scenarios or concise criteria; required QA independence and DONE conditions.

## Plan

Link to OpenSpec tasks.md when a change exists, otherwise a short plan. Do not duplicate the detailed plan.

## Current checkpoint

- Completed:
- Remaining:
- Blockers:
- Material open requests, if any: respondent, answer/action, version/environment, blocking impact and next step. Include a provider link if available, but preserve enough context to recover without a transcript. Routine completed exchanges need no entry. Apply [OPERATING_COMMUNICATION.md](OPERATING_COMMUNICATION.md).

Task Issuer, Project PM, current-owner and stage-result routes must be filled before READY, even when their executor and URL are identical. `owner_executor_id` plus `owner_route` is the incoming baton for the current stage. `result_to_executor_id` and `result_to_route` are the **only** destination for that current owner's completed stage result. `delivery_policy` is always `git_checkpoint_then_tracker` for an independent TASK: publish the TASK checkpoint to the accepted default branch first, then post its exact pointer to the **new current owner's `owner_route`**. Neither a task-issuer route, current/previous owner, checkpoint publisher, direct-message sender nor the physical parent chat is a result route unless it is explicitly copied into both result fields. Material/asynchronous questions use [the question contract](OPERATING_COMMUNICATION.md#question-routes). Add entries to frontmatter `questions` only when needed:

```yaml
questions:
  - ref: "<existing-question-comment-or-exchange-reference>"
    mode: ASK
    status: OPEN
    from_executor_id: "<requester>"
    to_executor_id: "<Task-Issuer-or-Project-PM>"
    blocking: "<dependent-work-or-none>"
    decision: null
```

Question Mode is `ASK`, `LOOP` or `ESCALATE_PM`; Question Status is `OPEN`, `ANSWERED`, `ESCALATED` or `CLOSED`. On ANSWERED, address `to_executor_id` to the original requester. Keep a concise Decision and unresolved objections here, with exact refs; do not duplicate the discussion transcript. These fields allow discovery without reading unrelated TASK bodies. The question does not change task ownership. Whole-task BLOCKED is appropriate only when no safe next action remains.

Setup checkpoints include mode, last completed step, confirmed answers/refs and the next question.

## Evidence

- Exact subject/candidate:
- Environment:
- Command or scenario:
- Actual result:
- Who verified:
- Limits and NOT_RUN:
- References to retained artifacts and summaries:
- Provider completed/merged state, merge commit and remote branch read-back:

## Workspace lifecycle

Keep TASK, candidate, and workspace lease identities separate. Reuse a compatible lease across TASK revisions, corrections, handoffs, and review. `workspace_disposition` is a derived TASK summary, never the historical record.

Each `workspace_exceptions[]` item records exact TASK, reason, lease ID, owner, purpose, capacity evidence, review date, changed exact base, known custody, disjoint lane, preserved candidate, and recovery rule. It cannot bypass the project hard cap, disk floor/reuse-only band, single-writer rule, ownership, containment, or evidence gates.

Each `workspace_leases[]` item records `lease_id`, purpose, class, `owner_executor_id`, `closure_owner_executor_id`, exact base/candidate/HEAD/tree, mutability, custody, state, `retention_class`, `review_date`, `recovery_ref`, exception reference, and `close_receipt_ref`. Put physical paths, sizes, processes, native handles, and host observations only in ignored local state.

Each `candidate_dispositions[]` item binds candidate SHA/tree and branch ref to exactly one disposition (`MERGED_TO_DEFAULT`, `SUPERSEDED_BY_SHA`, `REJECTED`, or `EVIDENCE_ARCHIVED`), evidence/reference, owner, and recorded time. Each `artifact_manifests[]` item records manifest ref, content hash, retention class, durable recovery location, owner, and access boundary. Each `close_receipts[]` item binds its receipt ref to one lease ID and actual closure result. Append new records; do not overwrite earlier candidate or lease history.

At each publication boundary update `workspace_exceptions`, `workspace_leases`, `candidate_dispositions`, `artifact_manifests`, `close_receipts`, and the derived `workspace_disposition` as applicable. Administrative completion requires every lease to be `CLOSED`, `RETAINED_PROTECTED`, or `TRANSFERRED_TO_NEXT_TASK` with required evidence. Any blocking/nonterminal lease prevents administrative completion. Workspace closure does not change a product or QA verdict.

For accepted integration, bind Git-suitable evidence into the protected checkpoint or record a sanitized hash-bound durable manifest with retention, recovery location, owner, and access boundary. Temporary material may be removed only after evidence-export, exclusive-ownership, dependency, shared-cache/retained-input, containment, and explicit-authority gates all pass. Otherwise retain, transfer, or block with an owner and review date.

Candidate, verified, merged and deployed versions are not interchangeable. A link to an expiring log is not a durable result summary.

## Decisions and handoff

Record material decisions, rationale, authorized decider and remaining objections; who transfers responsibility to whom, function, reason and next step. Preserve open questions/human actions at publication boundaries, not every conversational turn.

For a handoff, identify the published branch/checkpoint and current owner. Never claim delivery or acceptance merely from a sent message.

## Authorized next transitions

PM fills this table before execution. The current owner may publish only an explicitly authorized transition and still obeys branch protection/provider permissions.

| Outcome | Next TASK status | Next owner executor | Next owner route | Next active role | Following stage returns to | Following result route | Authorized publisher |
| --- | --- | --- | --- | --- | --- | --- |
| PASS | `<status>` | `<executor-id>` | `<existing-tracker-discussion>` | `<role>` | `<executor-id>` | `<existing-tracker-discussion>` | `<executor-id or PM>` |
| FAIL | `<status>` | `<executor-id>` | `<existing-tracker-discussion>` | `<role>` | `<executor-id>` | `<existing-tracker-discussion>` | `<executor-id or PM>` |
| BLOCKED | `BLOCKED` | `<current or PM>` | `<existing-tracker-discussion>` | `<role>` | `<executor-id>` | `<existing-tracker-discussion>` | `<executor-id or PM>` |

At every ownership change increment `handoff_seq` and update `previous_owner_executor_id`, `owner_executor_id`, `owner_route`, `assigned_by_executor_id`, `result_to_executor_id`, `result_to_route`, status, active role, exact evidence and next action. The assignment becomes discoverable only after this TASK checkpoint reaches the accepted default branch. The publisher notifies the newly declared `owner_route`; `result_to_*` remains the route that this new owner will use after its own stage. If a transition cannot name both owner and result routes, it is `ROUTE_REQUIRED`; do not return work to a local PM, sender chat or assumed parent.

At that same boundary, explicitly confirm/update Task Issuer and Project PM routes and transfer every unresolved question with its current respondent. A checkpoint publisher is not automatically the new issuer. Preserve the previous assignment and decision history in Git.

## Completion

Confirm actual DoD, specification/documentation consistency and required verification. Merge alone does not prove a deployment outcome. Preserve incomplete work honestly.

revision tracks contract changes, not every checkpoint. Git commit identifies state. Real tracker/branch/PR links are required for independent handoff; DRAFT without them is not a ready assignment.

For an onboarding TASK, `tracker_item` is the exact provider channel and `onboarding_result_to_executor_id` is normally PM. `auto_accept_if` lists objective pre-authorized evidence; empty means PM needs a new decision. Set `activation_mode` to `IMMEDIATE_RESERVED` or `QUEUED_AFTER_REGISTRATION`, never an implicit approval state. The participant returns `READY_FOR_ACTIVATION` with evidence or an addressed question. Prepare `first_task_id` before invitation as `PENDING_REGISTRATION` or `PENDING_CAPACITY`; PM moves it to `READY` only after registration is accepted and the declared capacity gate is satisfied.

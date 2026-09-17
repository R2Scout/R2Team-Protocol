# TASK template — R2Team 2.4

Use the body below for Tasks/TASK-<id>-<name>.md, removing these explanatory instructions. Choose a collision-free ID. Role handoff alone does not create another TASK; bounded helper requests remain inside the parent TASK.

```yaml
---
protocol_version: "2.4"
id: "<unique-task-id>"
revision: 1
handoff_seq: 0
status: DRAFT
stage: DISCOVERY
owner_executor_id: "<registered-executor>"
previous_owner_executor_id: null
assigned_by_executor_id: "<authorized-publisher>"
result_to_executor_id: "<executor-that-receives-this-stage-result>"
executor_mode: "<local_standalone|remote_manual|subagent>"
parent_executor_id: null
active_role: PM
tracker_item: null
tracker_item_type: null
requirement_ref: null
branch: null
pr: null
openspec_change: null
base_sha: null
candidate_sha: null
verified_sha: null
merged_sha: null
next_action: "<one-specific-action>"
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

Candidate, verified, merged and deployed versions are not interchangeable. A link to an expiring log is not a durable result summary.

## Decisions and handoff

Record material decisions, rationale, authorized decider and remaining objections; who transfers responsibility to whom, function, reason and next step. Preserve open questions/human actions at publication boundaries, not every conversational turn.

For a handoff, identify the published branch/checkpoint and current owner. Never claim delivery or acceptance merely from a sent message.

## Authorized next transitions

PM fills this table before execution. The current owner may publish only an explicitly authorized transition and still obeys branch protection/provider permissions.

| Outcome | Next TASK status | Next owner executor | Next active role | Result goes to | Authorized publisher |
| --- | --- | --- | --- | --- | --- |
| PASS | `<status>` | `<executor-id>` | `<role>` | `<executor-id>` | `<executor-id or PM>` |
| FAIL | `<status>` | `<executor-id>` | `<role>` | `<executor-id>` | `<executor-id or PM>` |
| BLOCKED | `BLOCKED` | `<current or PM>` | `<role>` | `<executor-id>` | `<executor-id or PM>` |

At every ownership change increment `handoff_seq` and update `previous_owner_executor_id`, `owner_executor_id`, `assigned_by_executor_id`, `result_to_executor_id`, status, active role, exact evidence and next action. The assignment becomes discoverable only after this TASK checkpoint reaches the accepted default branch.

## Completion

Confirm actual DoD, specification/documentation consistency and required verification. Merge alone does not prove a deployment outcome. Preserve incomplete work honestly.

revision tracks contract changes, not every checkpoint. Git commit identifies state. Real tracker/branch/PR links are required for independent handoff; DRAFT without them is not a ready assignment.

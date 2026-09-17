# TASK template — R2Team 2.3

Use the body below for Tasks/TASK-<id>-<name>.md, removing these explanatory instructions. Choose a collision-free ID. Role handoff alone does not create another TASK; bounded helper requests remain inside the parent TASK.

```yaml
---
protocol_version: "2.3"
id: "<unique-task-id>"
revision: 1
status: DRAFT
stage: DISCOVERY
owner_executor_id: "<registered-executor>"
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

## Completion

Confirm actual DoD, specification/documentation consistency and required verification. Merge alone does not prove a deployment outcome. Preserve incomplete work honestly.

revision tracks contract changes, not every checkpoint. Git commit identifies state. Real tracker/branch/PR links are required for independent handoff; DRAFT without them is not a ready assignment.

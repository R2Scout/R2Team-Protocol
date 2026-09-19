# Tracker and PR text templates — R2Team 2.4

Generate these from TASK; they are not a competing source of scope. Use provider forms when that is the selected channel, not as mandatory copies of transient direct exchanges.

## Issue / Work Item

```text
TASK: <repo-relative path>
Working branch: <branch>
Published checkpoint: <full SHA and source link>
Executor/function: <executor>/<role>; assignee: <provider identity>
Task Issuer: <executor/function>; route: <existing discussion URL>
Project PM: <executor>; route: <existing discussion URL>
Outcome: <one sentence>
Acceptance and state: see TASK.
PR: <URL or pending before first substantive commit>
```

## Main PR

```text
TASK and Issue/Work Item: <links>
Change: <short outcome>
Scope/requirements: <TASK and OpenSpec refs>
Verification: <exact candidate, results and limits>
Provider merge state: <NOT_MERGED or completed state + merge commit + remote default-branch result>
Specs/docs: <paths and changes>
Deployment included in Outcome: <yes/no>
Readiness: <Draft/Review; actual remaining work>
```

Do not automatically close an item at merge if its DoD includes unfinished deployment.

## Ownership handoff / durable result

```text
TASK <id/revision> -> <executor>/<function>.
Checkpoint <full SHA>, branch <name>, TASK <pinned URL>.
Next action: <action>. Boundaries and evidence are in TASK.
Task Issuer: <executor and route>; Project PM: <executor and route>.
Unresolved questions: <reference, mode/status, current respondent or none>.
Reply: update this TASK through its publishing owner and report via <item/PR URL>.
```

Publish first, then notify. Preserve returned IDs on partial failure and inspect before retry. "Sent" is not completed handoff.

## Remote onboarding result or question

```text
R2_EVENT: REGISTRATION_RESULT
registration_id: <stable-id>
from_executor_id: <remote-executor>
to_executor_id: <pm-executor>
status: READY_FOR_ACTIVATION
evidence: <identity/access/skills/cross-check refs>
questions: none
```

For a blocker, use `R2_EVENT: ONBOARDING_QUESTION`, the same IDs, `blocking: true`, and one specific question. Post only in the exact Issue/Work Item recorded by the onboarding TASK. PM's COO reports the event; PM/publisher applies any pre-authorized registration and first-TASK transition. Do not use an arbitrary commit comment as the primary route.

## Task clarification

```text
Question: TASK <id/revision>, <author> -> <executor/function/person>.
Question Mode: <ASK|LOOP|ESCALATE_PM>; Question Status: <OPEN|ESCALATED>.
Task Issuer: <executor/route>; Project PM: <executor/route>.
@<verified-account>; TASK/checkpoint: <Git reference>.
Clarify: <specific question and necessary context>.
Proposal: <option/rationale, if useful>.
Waiting on this answer: <dependent part>. Reply in this discussion.
Decision: pending.
```

Keep one channel. A question does not change owner; a changed contract requires authorized acceptance and Git persistence. No second question record or ACK merely for tracking.

ASK targets Task Issuer; LOOP records both positions/evidence and consensus sought; ESCALATE_PM targets PM directly when authority is required. See [question routes](OPERATING_COMMUNICATION.md#question-routes). Preserve queryable recipients and status in the existing TASK metadata; provider fields/labels are optional projections.

## Human action / visual acceptance

```text
Human input needed: TASK <id/revision>, @<verified-account>.
Purpose/reason: <why>.
Environment/version/screen: <verified inputs and safe reference>.
Next step: <specific action>.
Expected observation: <result or safe confirmation>.
After reply: <how the executor checks it and continues>.
```

Guide the person in their chat, not just a generic comment. Never request credentials or screenshots exposing secrets. Preserve meaningful confirmation in TASK; label human acceptance separately from automated tests.

## Discussion before implementation

```text
Discussion: TASK <id/revision>, @<accounts>.
Required positions: <function -> question>.
Decision: <subject, options, criteria>.
Known constraints: <facts>.
Authorized decider: <person/executor>.
Dependent work held: <disputed part>.
```

Participants provide options, evidence and risks without concurrently rewriting TASK. Silence and helpers belonging to the same author do not establish independent consensus. Escalate material disagreement to the authorized decider.

## Answer / accepted decision

```text
Reply to <comment URL or identified exchange>; TASK <id/revision>.
Question Mode: <existing mode>; Question Status: ANSWERED.
To executor: <original requester>.
Decision/clarification: <content>; rationale: <brief>.
Accepted by: <authorized decider, or still a proposal>.
Scope change: <none or approval required>.
Git: <published TASK/spec/checkpoint, or SYNC_REQUIRED>.
Next action/recipient: <action and executor>; @<account where applicable>.
```

A proposal is not an accepted decision. The publisher preserves material open questions/results before dependent work, handoff or session end. A resulting comment URL can be added at the next ordinary checkpoint; no second immediate commit just for a backlink.

The requester validates the answer and records CLOSED or the remaining dispute in the same route. Keep only dependent work paused; a sufficient in-scope answer needs no second start approval. PM decisions never substitute for evidence or mandatory gates.

## Notification

For durable events, notify relevant accounts and logical executors. Optional local wake uses one configured sender or standalone authorized COO, not both. Send TASK path/branch/published SHA and relevant discussion pointer. Verify uncertain delivery before retry. Internal COO returns facts to its parent.

Remote provider visibility is not automatic Codex execution. Inbox read/Done proves neither response nor task completion.

## Direct working requests

Under [OPERATING_COMMUNICATION.md](OPERATING_COMMUNICATION.md), an authorized direct exchange may contain the bounded request and answer, not just a wake pointer. Include parent TASK/ref, candidate/inputs, limits and return route. Keep the same owner, avoid duplicate entities/provider comments, and preserve material consequences at the four publication boundaries. No new scope or permission arises from the message.

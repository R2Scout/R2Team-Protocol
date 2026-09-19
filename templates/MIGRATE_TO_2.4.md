# Migration prompt: R2Team 2.3 to R2Team 2.4

Target: R2Team `protocol_version: "2.4"` from a trusted full commit or verified bundle. This migration changes COO discovery and return routing; it does not authorize product work.

## Read-only preflight

1. Verify current accepted protocol, TEAM, TASK root, default branch and unpublished work.
2. Verify the complete 2.4 package and manifest. Do not substitute `main/latest` for an approved commit.
3. Inventory active executors, shared provider actors, current COO modes/optional standalone instances, local routing and heartbeat settings.
4. Preserve all active TASKs, OpenSpec changes, refs, PRs, evidence and unresolved questions.

## Proposed changes

1. Update adopted protocol files and `protocol_version` to 2.4 through the project's normal review path.
2. Configure each active participant with exactly one COO mode and watched executor IDs. Default to internal; same-chat and standalone are alternatives.
3. Offer a separate COO chat once, persist accepted/declined/not_supported, and create one only on explicit request. Remove disabled/missing COO configurations.
4. Only standalone COO receives `notify_local` and machine-local route configuration. Heartbeat remains a separate opt-in and off by default.
5. If a provider actor is shared, optionally adopt `r2-executor:<executor-id>` labels; retain TASK ownership as authority.
6. Add `handoff_seq`, previous/assigned/current-owner route/result executor/result route/delivery fields and an authorized transition table to new TASKs. For active TASKs, populate them at the next approved ownership boundary without rewriting history.
7. Require remote handoffs to publish the same TASK checkpoint to the accepted default branch before provider notification.
8. Keep heartbeat off unless separately authorized and manually verified.
9. For each open/future remote registration, add a stable registration ID, exact onboarding Issue/Work Item, PM result recipient, objective evidence, prepared first TASK and `IMMEDIATE_RESERVED` or `QUEUED_AFTER_REGISTRATION`. Replace unregistered commit-comment inboxes prospectively without rewriting history.
10. Configure PM's COO to inspect those exact onboarding channels and return registration-ready/question/blocked states. PM or the named publisher performs activation; COO remains read-only.
11. Adopt executor_queue as the ordinary check/start scope. Preserve explicit task_only requests, report unexamined coverage, retain unresolved assignments across unchanged-SHA passes, and rebuild an incomplete local cache. HOLD of one TASK is not a global executor stop. Preserve explicit capacity/suspension restrictions.
12. Add active Owner/`owner_route`, Task Issuer, Project PM and Result Recipient executor/response routes to assignments, even when identical. Make the current result recipient the next owner at every transition; notify the new `owner_route`, not a chat parent. Preserve the distinction from publisher. Keep material questions in existing TASK metadata/body with ASK/LOOP/ESCALATE_PM, OPEN/ANSWERED/ESCALATED/CLOSED, requester/respondent and Decision. Preserve all unresolved questions/history.
13. Compare actual installed/loaded skill refs, accepted AGENTS/TEAM/protocol and saved entry/check prompts on each machine. Obtain replacement/cutover authority where missing; record adoption per executor. A candidate package does not automatically replace 2.3 rules. Do not enable or rewrite schedules during this migration unless specifically authorized.

## Cutover verification

Run one synthetic assignment per configured path:

- internal helper discovers an unknown TASK ID and returns `RETURNED_TO_PARENT` without registry lookup;
- same-chat check reports `ACTION_FOUND_LOCAL` without self-wake;
- standalone COO, if configured, returns `SENT_UNCONFIRMED` or `NOT_DELIVERED` truthfully;
- failed fetch does not advance `last_seen_default_branch_sha`;
- shared provider identity does not cause cross-executor delivery.
- a complete structured remote registration reaches PM through its registered channel and activates only under the declared evidence/capacity rule;
- a blocking onboarding question reaches PM without manual link forwarding;
- a known HOLD TASK plus an unknown READY TASK for one executor yields the READY assignment during an executor-wide pass; a task-only check reports only its limited coverage and performs no substitution;
- the same READY assignment remains pending on an unchanged-SHA pass until intake; a failed fetch reports QUEUE_CHECK_INCOMPLETE rather than no work;
- a question on another owner's TASK reaches Task Issuer/PM, its answer returns to the requester, and only dependent work waits;
- direct PM escalation needs no prior ASK/LOOP, and PM cannot bypass QA/evidence/human gates;
- a remote executor's Route Card shows current owner/owner route, Task PM and result route; its completed stage changes result recipient into the next owner and never uses a local PM/chat parent;
- each retained role proves the actually loaded instructions and current accepted adoption, or remains explicitly pending.

Run package/project checks and verify exact refs. Replacing files or skills alone does not prove project or role adoption. Publish the accepted migration checkpoint before relying on 2.4 behavior.

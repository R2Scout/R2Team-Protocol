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
6. Add `handoff_seq`, previous/assigned/result executor fields and an authorized transition table to new TASKs. For active TASKs, populate them at the next approved ownership boundary without rewriting history.
7. Require remote handoffs to publish the same TASK checkpoint to the accepted default branch before provider notification.
8. Keep heartbeat off unless separately authorized and manually verified.
9. For each open/future remote registration, add a stable registration ID, exact onboarding Issue/Work Item, PM result recipient, objective evidence, prepared first TASK and `IMMEDIATE_RESERVED` or `QUEUED_AFTER_REGISTRATION`. Replace unregistered commit-comment inboxes prospectively without rewriting history.
10. Configure PM's COO to inspect those exact onboarding channels and return registration-ready/question/blocked states. PM or the named publisher performs activation; COO remains read-only.

## Cutover verification

Run one synthetic assignment per configured path:

- internal helper discovers an unknown TASK ID and returns `RETURNED_TO_PARENT` without registry lookup;
- same-chat check reports `ACTION_FOUND_LOCAL` without self-wake;
- standalone COO, if configured, returns `SENT_UNCONFIRMED` or `NOT_DELIVERED` truthfully;
- failed fetch does not advance `last_seen_default_branch_sha`;
- shared provider identity does not cause cross-executor delivery.
- a complete structured remote registration reaches PM through its registered channel and activates only under the declared evidence/capacity rule;
- a blocking onboarding question reaches PM without manual link forwarding;

Run package/project checks and verify exact refs. Replacing files or skills alone does not prove project or role adoption. Publish the accepted migration checkpoint before relying on 2.4 behavior.

# Migration prompt: R2Team 2.3 to R2Team 2.4

Target: R2Team `protocol_version: "2.4"` from a trusted full commit or verified bundle. This migration changes COO discovery and return routing; it does not authorize product work.

## Read-only preflight

1. Verify current accepted protocol, TEAM, TASK root, default branch and unpublished work.
2. Verify the complete 2.4 package and manifest. Do not substitute `main/latest` for an approved commit.
3. Inventory active executors, shared provider actors, optional COO instances, local routing and heartbeat settings.
4. Preserve all active TASKs, OpenSpec changes, refs, PRs, evidence and unresolved questions.

## Proposed changes

1. Update adopted protocol files and `protocol_version` to 2.4 through the project's normal review path.
2. Configure each participant's watched executor IDs and TASK root when remote assignment discovery is wanted.
3. Allow the protocol-default bounded read-only internal COO for each executor, or explicitly disable it with `internal_coo_enabled: false`.
4. Distinguish internal subagent, same-chat and standalone COO modes. Only standalone COO receives `notify_local` and machine-local route configuration.
5. If a provider actor is shared, optionally adopt `r2-executor:<executor-id>` labels; retain TASK ownership as authority.
6. Add `handoff_seq`, previous/assigned/result executor fields and an authorized transition table to new TASKs. For active TASKs, populate them at the next approved ownership boundary without rewriting history.
7. Require remote handoffs to publish the same TASK checkpoint to the accepted default branch before provider notification.
8. Keep heartbeat off unless separately authorized and manually verified.

## Cutover verification

Run one synthetic assignment per configured path:

- internal helper discovers an unknown TASK ID and returns `RETURNED_TO_PARENT` without registry lookup;
- same-chat check reports `ACTION_FOUND_LOCAL` without self-wake;
- standalone COO, if configured, returns `SENT_UNCONFIRMED` or `NOT_DELIVERED` truthfully;
- failed fetch does not advance `last_seen_default_branch_sha`;
- shared provider identity does not cause cross-executor delivery.

Run package/project checks and verify exact refs. Replacing files or skills alone does not prove project or role adoption. Publish the accepted migration checkpoint before relying on 2.4 behavior.

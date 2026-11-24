# Local registration example — not an actual registry

Use only when the machine owner has authorized direct routing. Create .codex-local/THREAD_REGISTRY.md locally and verify exclusion with git check-ignore. This example contains no real IDs and may be committed; the populated registry never is.

| Executor ID from TEAM | Host / task ID on this machine | Verified route | Status |
| --- | --- | --- | --- |
| Example | Fill locally only | NOT_RUN | Disabled |

Verify the exact recipient and tool availability. Remote participation needs only Git and the agreed tracker/channel. Locality is relative: Ken's chats are local to Ken, not necessarily to John.

For a durable event, send one wake per event/recipient. A successful API response is not execution. On uncertain delivery/error, inspect before retrying; the durable TASK/provider route remains available. Update mappings when chats change or are disconnected; do not wake an obsolete writer.

A question/answer event may use its exact comment URL and checkpoint. TEAM selects one wake dispatcher for each recipient set: sender or a specific authorized standalone COO. Check current rights and routing; do not notify from both. Optional technical cursor/dedup stays ignored and is not a task registry. Unknown delivery is not success.

Authorized bounded working conversations follow [OPERATING_COMMUNICATION.md](OPERATING_COMMUNICATION.md); they are not restricted to pointer-only wake, and do not require a checkpoint per reply. Working-exchange permission is separate from a COO's notify_local permission.

PM/COO heartbeat is separately configured and off by default. A registry enables no schedule. Internal COO returns facts to its parent; a standalone COO with explicit notify_local may use approved local routes. Register Ken's local chats on Ken's machine, not as locally reachable chats for John.

For executor-scoped assignment discovery, the same ignored local area may store technical state such as:

```yaml
assignment_discovery:
  repository: "<repo-id-without-credentials>"
  last_seen_default_branch_sha: "<full-sha-or-NOT_RUN>"
  provider_event_cursor: "<opaque-local-cursor-or-NOT_RUN>"
```

This cursor is not project truth. A first baseline still treats current actionable TASKs for the watched executor as `NEW_UNACKNOWLEDGED` unless durable intake/checkpoint evidence proves acceptance.

## Workspace lease observations

The same ignored local registry may map portable lease identity to machine-private facts. Never copy populated values into Git:

```yaml
workspace_leases:
  - lease_id: "<portable-logical-id>"
    task_id: "<TASK-ID>"
    purpose: "<author|integration|qa|design|recovery>"
    owner_executor_id: "<registered-executor>"
    resource_label: "<project>-<work-ref>-<perm|task|tmp>-<executor>"
    lifetime: "<persistent|task_scoped|ephemeral|UNKNOWN>"
    native_workspace_id: "<existing-local-number-or-ID>"
    git_worktree_root_alias: "<approved-local-mapping-alias-or-NOT_APPLICABLE>"
    planned_directory_name: "<git-reference-label-with-optional-purpose-or-NOT_APPLICABLE>"
    observed_directory_name: "<existing-local-directory-name>"
    directory_policy_conformity: "<CONFORMS|LEGACY_RETAINED|APPLICATION_LAYOUT|UNKNOWN>"
    physical_path: "<absolute-local-path>"
    custody: "<ordinary-canonical|codex-managed|external-authorized|legacy-retained>"
    observed_head: "<full-sha-or-UNKNOWN>"
    observed_tree: "<full-tree-or-UNKNOWN>"
    observed_size_bytes: null
    native_resources: []
    process_observations: []
    state: "<REQUESTED|ACTIVE|CLOSE_PENDING|CLOSED|RETAINED_PROTECTED|TRANSFERRED_TO_NEXT_TASK|BLOCKED_DIRTY|BLOCKED_DEPENDENCY|BLOCKED_AUTHORITY|UNKNOWN>"
    last_observed_at: "<ISO-8601-or-NOT_RUN>"
```

Local observations do not change accepted TASK ownership, candidate identity, authority, retention, or disposition. A missing/stale observation is `UNKNOWN` or `INVENTORY_INCOMPLETE`, never evidence that a workspace is safe to close.

<a id="resource-observations"></a>
## Resource observations

For Git worktrees, [directory formation](GIT_WORKTREE_DIRECTORIES.md) governs new ordinary paths. Keep actual registration, root mapping, native ID, planned/observed name, and conformity here. Application-native or legacy paths can differ from the current readable label without implying rename authority. Broader resource roots do not become Git worktrees merely by being labelled.

Observe governed test/build/log/cache/evidence/runtime roots here by portable resource ID and authoritative lease or `resource_records[]` reference. Keep paths, native IDs, current/prior names, processes, consumers, observed close receipts, review dates, and unknown facts local. [Lifetime](RESOURCE_LIFETIME.md) and purpose are separate columns. Group disposable files under governed roots without per-file manifests. Unknown classification is protected; `REVIEW_DUE` never grants deletion or lifetime conversion authority.

## Relocation routing observations

With local machine-owner authority, the ignored registry may map a logical executor to its current physical chat/host. Detect executor collisions and read the mapping back before reporting it. Never copy the value or a stable hash of it into Git:

```yaml
executor_routes:
  - executor_id: "<registered-executor>"
    physical_thread_id: "<local-private-value>"
    host_observation: "<local-private-value>"
    migration_id: "<portable-migration-id>"
    local_authority: true
    collision: false
    read_back: true
    last_observed_at: "<ISO-8601-or-NOT_RUN>"
```

Durable relocation evidence records only `NOT_APPLICABLE`, `MAPPING_PRESENT_READ_BACK`, `MAPPING_ABSENT`, or `MAPPING_CONFLICT` plus a portable authority/host class. Registry presence, absence, title, notification, or archive state grants no assignment, identity, permission, writer epoch, source-stop proof, activation, or acceptance. Remote/manual executors do not require a local mapping.

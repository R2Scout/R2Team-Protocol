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

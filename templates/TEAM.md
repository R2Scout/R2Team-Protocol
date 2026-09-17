# TEAM — R2Team configuration

Template for protocol version 2.4. PM fills it during setup; empty configuration is not ready. Never commit real thread IDs, other machines' absolute paths or credentials.

```yaml
protocol_name: R2Team
protocol_version: "2.4"
integration_revision: 0
setup_status: NOT_CONFIGURED
project:
  name: null
  purpose: null
protocol_source:
  repository_url: null
  commit_sha: null
  package_path: null
  package_sha256: null
pm_executor_id: null
participants: []
tracker:
  provider: null
  process_template: null
  repository_url: null
  default_branch: null
automation:
  pm_heartbeat_enabled: false
  direct_wake: optional_local
toolchain:
  openspec_cli_version: null
  openspec_schema: null
  openspec_source_ref: null
  superpowers_source_ref: null
  skill_install_method: null
```

Use a real commit and repository-relative package path, or the trusted hash of an exact bundle. HEAD does not identify a dirty working tree. Increment project integration_revision when adopting changed rules/team configuration.

## Participants and executors

Replace the placeholders; this is not an actual assignment:

```yaml
pm_executor_id: john-main
participants:
  - id: john
    tracker_actor: "<verified-provider-identity>"
    active: true
    executors:
      - id: john-main
        active: true
        mode: local_standalone
        parent_executor_id: null
        roles: [PM, Brain, Designer, Dev, QA, DevOps]
        subagents:
          allowed: false
          purposes: []
          writable_paths: []
        permissions:
          git_commit: false
          git_push: false
          tracker_write: false
          pr_create_update: false
          merge: false
          deploy: false
```

Ask about actual needed rights/helpers; do not leave every permission false while declaring autonomous execution ready. Rights may be scoped to refs, environments and operations; deploy=true without a target/scope is insufficient.

Ken may hold only DevOps or combined QA+DevOps, using one or several executors. Supported modes are `local_standalone`, `remote_manual` and `subagent`. A persistent subagent with its own queue has a stable executor ID and `parent_executor_id`; an ephemeral helper stays only under its parent's helper policy. Only the current pm_executor_id performs team coordination.

## Function contracts

| Function | Instructions |
| --- | --- |
| PM | [ROLE-PM.md](ROLE-PM.md) |
| Brain | [ROLE-BRAIN.md](ROLE-BRAIN.md) |
| Designer | [ROLE-DESIGNER.md](ROLE-DESIGNER.md) |
| Dev | [ROLE-DEV.md](ROLE-DEV.md) |
| QA | [ROLE-QA.md](ROLE-QA.md) |
| DevOps | [ROLE-DEVOPS.md](ROLE-DEVOPS.md) |
| COO, optional | [ROLE-COO.md](ROLE-COO.md) |

A profile creates no chat. Local/remote executors use the same TASK. Optional physical routing uses the [local registry template](LOCAL_REGISTRY_TEMPLATE.md), never committed once populated.

This list is not an enum. PM may add Tester, Analyst, Architect or another function using [ROLE-TEMPLATE.md](ROLE-TEMPLATE.md) or a short contract here. Register its purpose/link, add it to executor.roles and use the appropriate TASK active_role. Combining functions is allowed. A new name does not automatically imply equivalence to an existing function or new permissions.

## Provider and project commands

Use [TRACKER_GUIDE.md](TRACKER_GUIDE.md). Record verified remote/default branch, identity/state mappings, policies/checks, reviewer independence, merge strategy, push/merge side effects and approvals, build/test/run commands and evidence/limits, environments/data/runbook/rollback/secrets policy, documentation map and known gaps.

## People, agreement and updates

For actual needed functions, record:
- Product/technical respondents and authorized scope deciders.
- Human setup/visual acceptance responsibilities and environment boundaries.
- Verified provider/Git identities; multiple executors under one account remain logically distinguished through executor ID, TASK, branch, PR and checkpoint. Commit author alone is not executor evidence.
- Subscriptions/update-check method and optional local routing, without physical thread IDs.
- Required independence, dispute resolution and escalation route.

Task-specific material questions and human actions belong in that TASK under [interaction rules](CODEX_TEAM_PROTOCOL.md#interaction), not a duplicate team registry. Asking a question does not transfer ownership. Provider notifications guarantee neither reading nor remote Codex execution.

## Optional COO configuration

An internal PM/parent helper gets bounded scope in its delegation, defaults to read-only, and returns facts; the parent wakes. A standalone COO is a registered executor with roles: [COO]. The profile's presence does not authorize creating or starting one.

Every active executor may use one internal read-only COO helper for its own executor IDs unless its executor record explicitly sets `internal_coo_enabled: false`. This helper is not registered separately and never needs a local thread registry. Only standalone COO configuration belongs below.

Merge actual permissions; do not overwrite existing settings with this example:

```yaml
coo:
  watched_participant_ids: []
  watched_executor_ids: []
  assignment_discovery:
    mode: git_task_delta
    task_root: Tasks
    owner_field: owner_executor_id
    provider_executor_label_prefix: r2-executor
  wake_dispatcher: sender
  heartbeat_enabled: false
permissions:
  notify_local: false
  tracker_write: false
  manage_assignments: false
  manage_team: false
  manage_automations: false
```

Fill exact IDs and boundaries. `git_task_delta` lets a remote COO discover new TASK IDs assigned to watched executors. The optional provider label accelerates shared-account queries; TASK ownership remains authoritative. Select one dispatcher for the watched recipient set: sender, none, or a specific standalone COO executor. notify_local requires approved machine-side routing; it is not Git/provider write authority. Other permissions remain separate.

PM/authorized owner and local environment owner approve rights. COO cannot change its own authority/scope or schedule. Configuration describes agreed policy, not proof that tool permissions were technically applied.

Manual passes and separately enabled heartbeat use the same [COO procedure](ROLE-COO.md). Internal helper scheduling belongs to the parent. Local cursor/dedup is ignored technical state, not the Git project source.

## Actual tool readiness

| Executor/machine without private paths | CLI version / skill ref | Required skills discovered | Check/date | Limits |
| --- | --- | --- | --- | --- |
| Not registered | UNKNOWN | NOT_RUN | NOT_RUN | Setup not performed |

This table records environment readiness, not each task's tests/build/deploy. See [SKILLS.md](SKILLS.md).

TEAM registration alone does not establish role adoption. A new standalone executor/function performs [cross-check](CODEX_TEAM_PROTOCOL.md#role-cross-check), confirms assigned work or requests the first from PM. PM supplies the existing onboarding channel; material questions/results enter the organizational TASK. No assignment is different from a broken environment.

## Cutover and history

Record prior source, tasks still on old rules, accepted cutover and responsible people. Do not delete inactive participants or history merely to tidy the list.

## Operational communication

Apply [OPERATING_COMMUNICATION.md](OPERATING_COMMUNICATION.md). Record approved channels/direct working-exchange permissions per executor. No new messaging authority is assumed before configuration. Working-exchange permission differs from notify_local wake permission. Bounded assistance keeps the parent owner/publisher; ownership changes require published handoff. Locality does not change persistence rules. Heartbeat stays off unless separately enabled.

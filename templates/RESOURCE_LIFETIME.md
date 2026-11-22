# Resource lifetime and workspace naming

This R2Team 2.8 policy becomes mandatory through accepted project adoption from a package containing it. It does not amend an already published release. Existing [workspace](CODEX_TEAM_PROTOCOL.md#workspace-lifecycle) identities, budgets, custody, publication, and closure gates remain applicable.

## Lifetime is independent of purpose

Every new workspace and governed test-data, build-output, log, cache, evidence, or runtime root has an explicit `lifetime`. Group disposable files under their governed root; do not create individual TASKs, manifests, or reports for each temporary file.

| Lifetime | Name token | Use | Required close event |
| --- | --- | --- | --- |
| `persistent` | `perm` | Standing project, integration, service, or other maintained anchor | `DECOMMISSION_ACCEPTED` at its governance reference, with separate decommission authority |
| `task_scoped` | `task` | One TASK result and its dependent consumers | `TASK_RESULT_ACCEPTED` at the named TASK checkpoint |
| `ephemeral` | `tmp` | One bounded verification, experiment, build, or other use | `USE_COMPLETED` at the named use checkpoint, including failed/cancelled use when its scope actually ended |

Purpose describes work: `dev`, `qa`, `build`, `release`, `design`, or `recovery`, for example. It is extensible and cannot determine lifetime. QA databases/build anchors may be persistent; development experiments may be ephemeral. Lifetime does not replace state, retention, custody, candidate identity, or receipts. Persistent anchors still count against budgets and single-writer limits.

All lifetimes have current owners, close conditions, and review dates. Persistent designation needs accepted standing purpose and a governance TASK. Overdue review is `REVIEW_DUE`, never automatic removal or promotion. Reclassification, changed close conditions, or custody transfers require authorized checkpoints with reasons, consumers, next review, and preserved history.

## Required record

Add this policy to each `workspace_leases[]` row, with `resource_id` equal to stable `lease_id`. Use `resource_records[]` only for separately governed non-workspace roots. Artifact manifests reference existing records. Outputs do not automatically inherit worktree lifetime: rollback and acceptance evidence may outlive ephemeral workspaces.

```yaml
resource_id: lease-author-42
project_slug: crm.ai
work_ref: task3244
executor_slug: dev10
owner_executor_id: dev10
resource_label: crm.ai-task3244-task-dev10
lifetime: task_scoped
purpose: dev
close_condition:
  event: TASK_RESULT_ACCEPTED
  ref: TASK-3244
review_date: "2026-12-01"
retention_class: task-result
recovery_ref: "git:refs/heads/task-3244"
```

Owner/alias must agree with accepted TEAM. Close references resolve to existing authoritative TASK, use, or governance decisions, never private chats. Standing anchors still link to governance TASKs. Paths, native numbers, directory-name observations, processes, and handles stay in the ignored [local registry](LOCAL_REGISTRY_TEMPLATE.md#resource-observations).

## Readable name

The portable label is `<project_slug>-<work_ref>-<lifetime_token>-<executor_slug>`. Ordinary Git worktrees may prefix their existing native ID:

```text
ws0042-crm.ai-base-perm-devops
ws0043-crm.ai-task3244-task-dev10
ws0044-crm.ai-task3244-tmp-qa2
```

Keep native IDs and logical leases; introduce no global counter. Labels are metadata, not uniqueness, candidate, or ownership proof. Different IDs may share a label. Compatible reuse preserves ID/path; revisions, chat titles, owner/lifetime changes, and labels never require another worktree or alter the materialization key.

Use approved stable lowercase ASCII aliases, digits, and hyphens. Dots are allowed between project segments (`crm.ai`). Work references start with letters and identify their type (`task3244`, `issue3244`, `wi3244`, `pr3244`) or standing anchor (`base`). Prefer TASK when present. Titles, paths, chat IDs, private identifier hashes, dates, retries, and revision suffixes do not belong in labels. Maximum length is 96 ASCII characters; approve shorter aliases without silent truncation. Validate the full destination path separately.

Update current labels at accepted owner/lifetime changes and preserve prior local observations. Physical rename is separate, authorized, and uses supported custody mechanisms plus path/process/dependency checks. Codex-managed paths/IDs remain application-owned; record labels locally and in supported display fields when available. Adoption never renames directories.

## Close eligibility and review

Group status by perm/task/tmp, purpose, and owner. Names select review candidates; suffixes and age grant no removal authority. Read a published condition receipt bound to `resource_id`, current `owner_executor_id`, event, and exact `ref`, with `satisfied: true` and authoritative `receipt_ref`. String booleans, unrelated results, missing receipts, and another owner's decision prove nothing. Persistent resources additionally require separate decommission authority.

Then apply evidence export, dirty/unpublished/unknown material, recovery, exclusive ownership, containment, live-process, dependency/consumer, custody, and removal-authority gates. Lifetime completion permits preflight only. Codex-managed resources still require application archive. Retain/transfer protected material with owner/review evidence when gates are missing. Complete policy and terminal lease evidence are both required for administrative completion; a standing anchor may remain `RETAINED_PROTECTED` without decommissioning it.

The offline model exposes `resource_label`, `resource_policy_errors`, `resource_allocation_decision`, `resource_closure_decision`, `resource_completion_decision`, and `resource_review_decision` in `scripts/workspace_policy.py`. After adoption, use lifetime-aware gates alongside existing behavior. They make no filesystem, provider, process, or scheduling changes. The operating executor verifies receipts at authoritative sources.

## Prospective adoption

PM publishes policy/aliases, owner/close/review requirements, validation limits, and reconciliation ownership. New allocation requires complete classification; active leases/governed roots acquire fields at their next material checkpoint. Unclassified legacy resources remain protected `UNKNOWN` / `legacy-retained` with reconciliation owners. Missing metadata or tmp paths never make them disposable. Safe read-only inspection can continue; unknown classification blocks new allocation, lifetime-dependent mutation, and administrative closure.

Installation, verification, and adoption are separate. Migration never creates, renames, removes, promotes, transfers, or decommissions resources. Historical TASKs/evidence require no bulk conversion or deletion.

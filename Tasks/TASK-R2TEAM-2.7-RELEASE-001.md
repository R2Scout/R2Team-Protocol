---
protocol_version: "2.7"
id: "TASK-R2TEAM-2.7-RELEASE-001"
revision: 1
handoff_seq: 0
status: DONE
stage: RELEASE
owner_executor_id: "r2team-protocol-owner"
owner_route: "https://github.com/R2Scout/R2Team-Protocol/issues/6"
previous_owner_executor_id: null
assigned_by_executor_id: "r2team-protocol-owner"
task_issuer_executor_id: "r2team-protocol-owner"
task_issuer_route: "https://github.com/R2Scout/R2Team-Protocol/issues/6"
project_pm_executor_id: "r2team-protocol-owner"
project_pm_route: "https://github.com/R2Scout/R2Team-Protocol/issues/6"
result_to_executor_id: "r2team-protocol-owner"
result_to_route: "https://github.com/R2Scout/R2Team-Protocol/issues/6"
delivery_policy: git_checkpoint_then_tracker
executor_mode: "local_standalone"
parent_executor_id: null
active_role: PM
tracker_item: "https://github.com/R2Scout/R2Team-Protocol/issues/6"
tracker_item_type: github_issue
registration_id: null
onboarding_result_to_executor_id: null
auto_accept_if: []
activation_mode: null
first_task_id: null
capacity_reserved: false
requirement_ref: null
branch: "release/r2team-2.7"
pr: "https://github.com/R2Scout/R2Team-Protocol/pull/7"
openspec_change: null
base_sha: "9f6656589b68122ff9d67ae9d75edc14dd6118ff"
candidate_sha: "6cdcb28d063cf2d2cdd11aeac0738d30329c3f9b"
verified_sha: "6cdcb28d063cf2d2cdd11aeac0738d30329c3f9b"
merged_sha: "c2dd95dfea5138ec8c7f6757d6125279cb20c470"
workspace_policy: inherited_from_protocol_2.7
workspace_inventory_ref: "ignored local inventory for the reused release workspace"
workspace_exceptions: []
workspace_leases:
  - lease_id: "lease-r2team-2.7-release-001"
    materialization_key: "R2Scout/R2Team-Protocol|release/r2team-2.7|9f6656589b68122ff9d67ae9d75edc14dd6118ff|release|r2team-protocol-owner"
    purpose: release
    class: reused-canonical
    owner_executor_id: "r2team-protocol-owner"
    closure_owner_executor_id: "r2team-protocol-owner"
    base_sha: "9f6656589b68122ff9d67ae9d75edc14dd6118ff"
    candidate_sha: "6cdcb28d063cf2d2cdd11aeac0738d30329c3f9b"
    head_sha: "c2dd95dfea5138ec8c7f6757d6125279cb20c470"
    tree_sha: "cb30e9a41afe4d68233993400e767e16c37b928a"
    mutability: mutable
    custody: reused-existing-workspace
    state: RETAINED_PROTECTED
    retention_class: post-release-recovery
    review_date: "2026-11-10"
    recovery_ref: "refs/heads/release/r2team-2.7"
    exception_ref: null
    close_receipt_ref: "receipt-r2team-2.7-release-001-retained"
workspace_disposition: RETAINED_PROTECTED
candidate_dispositions:
  - candidate_sha: "6cdcb28d063cf2d2cdd11aeac0738d30329c3f9b"
    candidate_tree: "581f1b5614d759512793717cc3b4973178c54782"
    branch_ref: "refs/heads/release/r2team-2.7"
    disposition: MERGED_TO_DEFAULT
    evidence_ref: "https://github.com/R2Scout/R2Team-Protocol/pull/7"
    owner_executor_id: "r2team-protocol-owner"
    recorded_at: "2026-11-03T14:29:01Z"
artifact_manifests: []
evidence_index:
  - evidence_key: "6cdcb28d|package|validate_package|windows-python|PASS"
    candidate_sha: "6cdcb28d063cf2d2cdd11aeac0738d30329c3f9b"
    axis: package
    normalized_command: "python scripts/validate_package.py"
    environment_class: windows-python
    outcome: PASS
    summary_ref: "TASK release checkpoint"
  - evidence_key: "6cdcb28d|tests|validator-workspace-relocation|windows-python|PASS"
    candidate_sha: "6cdcb28d063cf2d2cdd11aeac0738d30329c3f9b"
    axis: source-tests
    normalized_command: "sequential validator, workspace-policy, and relocation-policy suites"
    environment_class: windows-python
    outcome: "PASS: 55/55 + 42/42 + 73/73"
    summary_ref: "TASK release checkpoint"
  - evidence_key: "6cdcb28d|skills|quick_validate-six|windows-python-pyyaml|PASS"
    candidate_sha: "6cdcb28d063cf2d2cdd11aeac0738d30329c3f9b"
    axis: skill-format
    normalized_command: "skill-creator quick_validate.py for all six distribution skills"
    environment_class: windows-python-pyyaml
    outcome: "PASS: 6/6"
    summary_ref: "TASK release checkpoint"
  - evidence_key: "6cdcb28d|release-safety|hash-command-compile-language-path|windows|PASS"
    candidate_sha: "6cdcb28d063cf2d2cdd11aeac0738d30329c3f9b"
    axis: release-safety
    normalized_command: "hash, command-copy, compile, language, private-path/thread, stale-label, and diff checks"
    environment_class: windows
    outcome: "PASS: hashes 59/59, command copies identical"
    summary_ref: "TASK release checkpoint"
  - evidence_key: "c2dd95df|publication|annotated-tag-and-github-release|github|PASS"
    candidate_sha: "c2dd95dfea5138ec8c7f6757d6125279cb20c470"
    axis: publication
    normalized_command: "provider read-back of merged PR, origin/main, annotated v2.7 tag, and GitHub Release"
    environment_class: github
    outcome: PASS
    summary_ref: "https://github.com/R2Scout/R2Team-Protocol/releases/tag/v2.7"
close_receipts:
  - receipt_ref: "receipt-r2team-2.7-release-001-retained"
    lease_id: "lease-r2team-2.7-release-001"
    task_id: "TASK-R2TEAM-2.7-RELEASE-001"
    owner_executor_id: "r2team-protocol-owner"
    closer_executor_id: "r2team-protocol-owner"
    base_sha: "9f6656589b68122ff9d67ae9d75edc14dd6118ff"
    branch_ref: "refs/heads/release/r2team-2.7"
    head_sha: "c2dd95dfea5138ec8c7f6757d6125279cb20c470"
    tree_sha: "cb30e9a41afe4d68233993400e767e16c37b928a"
    candidate_sha: "6cdcb28d063cf2d2cdd11aeac0738d30329c3f9b"
    material_classification: "retained clean release workspace with pre-existing ignored validation roots"
    artifact_manifest_ref: null
    recovery_route: "refs/heads/release/r2team-2.7"
    native_resource_disposition: RETAINED_WITH_WORKSPACE
    branch_disposition: MERGED_TO_DEFAULT
    retention_class: post-release-recovery
    closure_method: no-removal-retention
    actual_result: RETAINED_PROTECTED
    remaining_owner_executor_id: "r2team-protocol-owner"
    blocker: "Workspace cleanup, branch deletion, and application archive were excluded from this release TASK."
    recorded_at: "2026-11-03T14:30:51Z"
migration_id: null
executor_fence_ref: null
writer_epoch: null
writer_record_ref: null
relocation_disposition: NOT_APPLICABLE
next_action: "No further action in this release TASK. Downstream installation/adoption, live relocation/cleanup, branch deletion, and workspace archive require separate authority and evidence."
questions: []
---

# Outcome

Publish the already integrated R2Team 2.7 distribution as an exact, validated annotated tag and GitHub Release.

# Scope and boundaries

Included: release-state metadata and public guidance, payload-hash refresh, full sequential package verification, protected PR integration, annotated `v2.7` tag, GitHub Release, and provider read-back.

Excluded: downstream skill installation or replacement, project adoption or migration, live relocation, workspace cleanup, branch deletion, application archive, process stop, and disk-recovery claims.

# Acceptance

- `package.json` identifies release `v2.7`; maintained public entry guidance no longer labels 2.7 as an unreleased candidate.
- Package hashes, links, command-copy equality, validator/workspace/relocation suites, six skill format checks, compile checks, and public-content safety checks pass sequentially on the exact candidate.
- The release PR is merged and the provider/default branch read-back identifies the actual merge commit.
- Annotated tag `v2.7` and the published GitHub Release resolve to that exact accepted default-branch commit.
- Excluded downstream/runtime/cleanup axes remain explicitly `NOT_RUN`.

# Plan

1. Make the minimum release-state and guidance delta, then refresh affected payload hashes.
2. Run the complete release verification suite sequentially and publish the exact candidate through a PR.
3. Read back the merge, create and push the annotated tag, publish the GitHub Release, and verify both provider objects.
4. Publish the final TASK checkpoint and close Issue #6 only after the accepted evidence is durable.

# Current checkpoint

- Completed: release candidate `6cdcb28d063cf2d2cdd11aeac0738d30329c3f9b`, tree `581f1b5614d759512793717cc3b4973178c54782`, passed all declared checks; PR #7 merged as `c2dd95dfea5138ec8c7f6757d6125279cb20c470`, tree `cb30e9a41afe4d68233993400e767e16c37b928a`; annotated tag object `6c9f189aeb6980bff98eb018f46ad9e72e36398d` resolves to that merge; GitHub Release `v2.7` is published, non-draft, non-prerelease, and latest.
- Remaining: none within this TASK.
- Blockers: none.

# Evidence

- Exact base: `9f6656589b68122ff9d67ae9d75edc14dd6118ff`, tree `100c73bf347bb74728ff3f30c4b4de9fd4b0ff13`.
- Exact release candidate: `6cdcb28d063cf2d2cdd11aeac0738d30329c3f9b`, tree `581f1b5614d759512793717cc3b4973178c54782`.
- Sequential checks: package PASS; validator `55/55`; workspace `42/42`; relocation `73/73`; skill format `6/6`; hashes `59/59`; compile, command-copy, English-only, concrete-private-path/thread, stale-release-label, and diff checks PASS.
- Existing tags: `v2.0` through `v2.3`; `v2.7` absent at intake.
- Existing GitHub Releases: `v2.0` and `v2.1`; `v2.7` absent at intake.
- Provider merge read-back: PR #7 `MERGED` at `c2dd95dfea5138ec8c7f6757d6125279cb20c470`; `origin/main` matched before tagging.
- Annotated tag read-back: tag object `6c9f189aeb6980bff98eb018f46ad9e72e36398d`; peeled target `c2dd95dfea5138ec8c7f6757d6125279cb20c470`.
- GitHub Release read-back: `v2.7`, `R2Team 2.7`, published `2026-11-03T14:30:51Z`, non-draft, non-prerelease, latest; https://github.com/R2Scout/R2Team-Protocol/releases/tag/v2.7.
- Limits and NOT_RUN: all excluded scope axes.

# Authorized next transitions

| Outcome | Next TASK status | Next owner executor | Next owner route | Next active role | Following stage returns to | Following result route | Authorized publisher |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PASS | DONE | `r2team-protocol-owner` | Issue #6 | PM | `r2team-protocol-owner` | Issue #6 | `r2team-protocol-owner` |
| FAIL | BLOCKED | `r2team-protocol-owner` | Issue #6 | PM | `r2team-protocol-owner` | Issue #6 | `r2team-protocol-owner` |
| BLOCKED | BLOCKED | `r2team-protocol-owner` | Issue #6 | PM | `r2team-protocol-owner` | Issue #6 | `r2team-protocol-owner` |

# Completion

Completion requires the exact tag and GitHub Release read-back plus a final TASK checkpoint on the accepted default branch. Merge alone is insufficient.

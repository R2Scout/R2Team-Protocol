---
protocol_version: "2.7"
id: "TASK-R2TEAM-2.7-RELEASE-001"
revision: 1
handoff_seq: 0
status: REVIEW_READY
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
pr: null
openspec_change: null
base_sha: "9f6656589b68122ff9d67ae9d75edc14dd6118ff"
candidate_sha: "6cdcb28d063cf2d2cdd11aeac0738d30329c3f9b"
verified_sha: "6cdcb28d063cf2d2cdd11aeac0738d30329c3f9b"
merged_sha: null
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
    head_sha: "6cdcb28d063cf2d2cdd11aeac0738d30329c3f9b"
    tree_sha: "581f1b5614d759512793717cc3b4973178c54782"
    mutability: mutable
    custody: reused-existing-workspace
    state: ACTIVE
    retention_class: release-work
    review_date: "2026-11-10"
    recovery_ref: "refs/heads/release/r2team-2.7"
    exception_ref: null
    close_receipt_ref: null
workspace_disposition: ACTIVE
candidate_dispositions: []
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
close_receipts: []
migration_id: null
executor_fence_ref: null
writer_epoch: null
writer_record_ref: null
relocation_disposition: NOT_APPLICABLE
next_action: "Push the verified release branch, open the protected PR, and read back provider state."
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

- Completed: exact `origin/main` and existing tags/releases were read back; Issue #6 and the reused release branch/workspace were established; release candidate `6cdcb28d063cf2d2cdd11aeac0738d30329c3f9b`, tree `581f1b5614d759512793717cc3b4973178c54782`, passed the declared local release checks.
- Remaining: protected PR, merge/read-back, tag, GitHub Release, final checkpoint, and tracker close.
- Blockers: none.

# Evidence

- Exact base: `9f6656589b68122ff9d67ae9d75edc14dd6118ff`, tree `100c73bf347bb74728ff3f30c4b4de9fd4b0ff13`.
- Exact release candidate: `6cdcb28d063cf2d2cdd11aeac0738d30329c3f9b`, tree `581f1b5614d759512793717cc3b4973178c54782`.
- Sequential checks: package PASS; validator `55/55`; workspace `42/42`; relocation `73/73`; skill format `6/6`; hashes `59/59`; compile, command-copy, English-only, concrete-private-path/thread, stale-release-label, and diff checks PASS.
- Existing tags: `v2.0` through `v2.3`; `v2.7` absent at intake.
- Existing GitHub Releases: `v2.0` and `v2.1`; `v2.7` absent at intake.
- Limits and NOT_RUN: all excluded scope axes.

# Authorized next transitions

| Outcome | Next TASK status | Next owner executor | Next owner route | Next active role | Following stage returns to | Following result route | Authorized publisher |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PASS | DONE | `r2team-protocol-owner` | Issue #6 | PM | `r2team-protocol-owner` | Issue #6 | `r2team-protocol-owner` |
| FAIL | BLOCKED | `r2team-protocol-owner` | Issue #6 | PM | `r2team-protocol-owner` | Issue #6 | `r2team-protocol-owner` |
| BLOCKED | BLOCKED | `r2team-protocol-owner` | Issue #6 | PM | `r2team-protocol-owner` | Issue #6 | `r2team-protocol-owner` |

# Completion

Completion requires the exact tag and GitHub Release read-back plus a final TASK checkpoint on the accepted default branch. Merge alone is insufficient.

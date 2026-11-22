---
protocol_version: "2.8"
id: TASK-R2TEAM-RESOURCE-LIFETIME-001
revision: 2
handoff_seq: 0
status: DONE
stage: RELEASE
publication_state: RELEASE_PUBLISHED
owner_executor_id: r2team-protocol-owner
owner_route: https://github.com/R2Scout/R2Team-Protocol/issues/12
task_issuer_executor_id: r2team-protocol-owner
task_issuer_route: https://github.com/R2Scout/R2Team-Protocol/issues/12
project_pm_executor_id: r2team-protocol-owner
project_pm_route: https://github.com/R2Scout/R2Team-Protocol/issues/12
result_to_executor_id: r2team-protocol-owner
result_to_route: https://github.com/R2Scout/R2Team-Protocol/issues/12
delivery_policy: git_checkpoint_then_tracker
tracker_item: https://github.com/R2Scout/R2Team-Protocol/issues/12
branch: protocol/workspace-lifetime
pr: https://github.com/R2Scout/R2Team-Protocol/pull/13
base_sha: 280c62e8e4a6cdf5b96948fdb521678aa7b906a7
candidate_sha: 2e9d8b8ee1fc6b426eef4859ef95818023677656
verified_sha: 2e9d8b8ee1fc6b426eef4859ef95818023677656
merged_sha: 3e023e5222b69d7b2bc0b58316d0cc5e2021be2a
release_commit_sha: 3e023e5222b69d7b2bc0b58316d0cc5e2021be2a
release_tag: v2.8
release_tag_object_sha: c41e6bbf896bff6da7ac52ceb6d08971674368eb
release_url: https://github.com/R2Scout/R2Team-Protocol/releases/tag/v2.8
verified_payload_manifest_sha256: "1e5358f9ef5c6950c3995ae6e95805257f39371cb05e13ca451abecf216c18a0"
next_action: "No further payload change. Publish this task-only receipt, close Issue #12, and close the owned transport branch after read-back. Project PMs adopt the pinned release through their own accepted checkpoint."
---

# Outcome

Published R2Team 2.8 resource lifetime and readable workspace naming, explicitly authorized by the repository owner on 2026-11-22. Prepared a portable migration path for project PMs. The new release preserves the historical v2.7 tag and commit.

# Included contract

- Explicit persistent/perm, task_scoped/task, and ephemeral/tmp lifetime, independent of dev/qa/build/release purpose.
- Stable readable names plus existing native workspace IDs and lease/materialization identity.
- Current owner, bound close event/reference, review date, retention, and recovery for new workspaces and governed resource roots.
- Separate decommission authority for standing anchors; no removal or lifetime promotion by name/age/review expiry.
- Protected UNKNOWN legacy resources, prospective classification, and preservation of evidence/consumer/custody/removal gates.
- Protocol, TEAM/TASK/role/local-observation templates, six procedure-skill version references, package validator, and migration 2.8 guidance.

# Verification and publication evidence

- PASS: four sequential suites on the exact versioned manifest-only package: validator 58/58, workspace 42/42, relocation 73/73, lifetime 16/16; total 189/189.
- PASS: 6/6 official skill formats using isolated PyYAML 6.0.3; 62/62 payload hashes; package links/anchors and privacy/safety guards; English-only Markdown; Python compilation; command-copy equality; git diff --check.
- PASS: staged and committed payload bytes matched the verified manifest; the actual PR merge payload matched all 62 hashes and the same manifest bytes.
- RED/GREEN: lifetime/completion/type fixtures and three package-policy guards failed before their respective implementations and passed afterward.
- PR #13 head 19bc8f71457dee0137002a63a74dc9021852edce integrated as 3e023e5222b69d7b2bc0b58316d0cc5e2021be2a; provider merged-state and main read-back matched.
- Annotated v2.8 tag object c41e6bbf896bff6da7ac52ceb6d08971674368eb peels to the accepted release commit 3e023e5222b69d7b2bc0b58316d0cc5e2021be2a.
- GitHub Release v2.8 is published, non-draft, non-prerelease, and returned by the latest-release endpoint. The versioned manifest reads protocol_version 2.8 and status release.
- Historical v2.7 tag object 6c9f189aeb6980bff98eb018f46ad9e72e36398d still peels to c2dd95dfea5138ec8c7f6757d6125279cb20c470.
- This receipt changes only TASK metadata. It may advance main without changing the tagged payload.

# Workspace custody and limits

Reused the existing author checkout without new worktrees or directory movement. Its source state remains recoverable from main and the annotated release; the canonical checkout remains retained for maintenance. Two predecessor recovery worktrees remain registered and detached at their recorded recovery commits; no operation changed them. Private role routing and local validation dependencies remain ignored. The owned manifest-only verification materialization is disposable after this compact result is recorded.

NOT_RUN: independent consuming-agent behavior/QA, installed-skill replacement, downstream project adoption, live allocation/cleanup/decommission/rename, relocation, runtime/deployment effects, and PM chat messaging. Update text preparation is not delivery or project adoption.

# Authorized return

PASS returns this published checkpoint and exact release references to Issue #12. Publication/versioning were authorized directly by the repository owner; this authority does not grant operations in downstream projects. Each PM publishes its own adoption checkpoint and verifies its executors against the pinned package.

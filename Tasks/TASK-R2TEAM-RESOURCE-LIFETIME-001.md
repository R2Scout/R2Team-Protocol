---
protocol_version: "2.8"
id: TASK-R2TEAM-RESOURCE-LIFETIME-001
revision: 1
status: READY
stage: INTEGRATION
publication_state: VERSIONED_CANDIDATE
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
pr: null
base_sha: 280c62e8e4a6cdf5b96948fdb521678aa7b906a7
candidate_sha: null
verified_sha: null
verified_payload_manifest_sha256: "1e5358f9ef5c6950c3995ae6e95805257f39371cb05e13ca451abecf216c18a0"
next_action: "Verify the 2.8 payload, commit and publish the branch, integrate the exact PR head, then publish and verify annotated v2.8 and its GitHub Release."
---

# Outcome

Make resource lifetime explicit independently of dev/qa/build/release purpose. Persistent anchors, task-scoped resources, and ephemeral uses receive readable names, current owners, bound close conditions, review dates, retention, and recovery. The user accepted this scope on 2026-11-22.

# Source scope

- Add templates/RESOURCE_LIFETIME.md and reconcile protocol, TEAM/TASK, local observation, PM, setup/migration, command, and workspace-skill guidance.
- Add lifetime-aware naming, allocation, closure, completion, and review gates to the offline workspace reference model. No filesystem/provider/process operations are performed by the model.
- Require the policy in package metadata and structural validation; refresh 62 payload hashes.
- Preserve historical release provenance. The added policy is untagged/unpublished and is not retroactively part of v2.7. Existing project adoption remains governing until an approved newer-package cutover.
- Reuse the existing author checkout without new worktrees or resource movement. Leave registered recovery worktrees and local private routing intact. No installed user skills are replaced.

# Acceptance and evidence

- PASS: sequential tests on the exact manifest-only package: validator 58/58, workspace 42/42, relocation 73/73, resource-lifetime 16/16; total 189/189.
- PASS: six official skill-format checks using locally isolated PyYAML 6.0.3; these are format checks, not consuming-agent acceptance.
- PASS: package hashes/structure, Markdown links/anchors, lifecycle safety/privacy guards, English-only public Markdown, changed Python compilation, command-copy equality, and git diff --check.
- RED/GREEN: resource-lifetime fixtures first failed for missing behavior; added completion/type gates failed before implementation; three package-policy guards failed before validator changes. All passed after the corresponding changes.
- Lifetime tests cover independent purpose combinations, stable labels, malformed/unknown metadata, bound resource/owner/event/reference receipts, strict booleans, persistent decommission authority, review-only expiry, terminal-policy evidence, and existing hard-cap/evidence/dirty/dependency/removal/application-custody gates.
- Source-tree package validation correctly rejects local private routing. Acceptance uses a manifest-only materialization containing package.json plus required_files, with no local routing or runtime data. The owned temporary materialization is disposable after this compact checkpoint; no separate routine evidence archive is required.

# Remaining work and limits

The versioned R2Team 2.8 source candidate passed fresh manifest-only verification: 189/189 tests, 6/6 skill formats, 62/62 payload hashes, links/privacy/safety, English-only Markdown, compilation, and command-copy checks. It is authorized for integration via Issue #12. Issue #12 is the explicit publication route. The repository owner authorized commit, push, integration, release, and preparation of PM update text on 2026-11-22. Revalidate the versioned payload before publication; no downstream adoption or PM chat delivery is implied.

NOT_RUN: independent consuming-agent behavioral review, commit/push/merge/release, installed-skill replacement, downstream adoption, live allocation/cleanup/decommission, directory rename, relocation, and automation.

Current main and historical v2.7 tag remain unchanged. No actual project resource has been classified, removed, or promoted by this source change.

# Authorized publication transitions

PASS publishes the exact verified candidate through PR integration, annotated v2.8, and GitHub Release read-back; the same owner returns the result to Issue #12. FAIL or BLOCKED retains recoverable state and returns the blocker to Issue #12. The repository owner explicitly authorized these publication operations. Source delivery does not authorize downstream migration or PM chat messaging.

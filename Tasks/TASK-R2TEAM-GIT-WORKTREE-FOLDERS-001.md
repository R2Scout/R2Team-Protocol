---
protocol_version: "2.9"
id: TASK-R2TEAM-GIT-WORKTREE-FOLDERS-001
revision: 1
status: DONE
stage: RELEASE
owner_executor_id: r2team-protocol-owner
owner_route: https://github.com/R2Scout/R2Team-Protocol/issues/15
task_issuer_executor_id: r2team-protocol-owner
task_issuer_route: https://github.com/R2Scout/R2Team-Protocol/issues/15
project_pm_executor_id: r2team-protocol-owner
project_pm_route: https://github.com/R2Scout/R2Team-Protocol/issues/15
result_to_executor_id: r2team-protocol-owner
result_to_route: https://github.com/R2Scout/R2Team-Protocol/issues/15
delivery_policy: git_checkpoint_then_tracker
tracker_item: https://github.com/R2Scout/R2Team-Protocol/issues/15
branch: protocol/git-worktree-folders
pr: https://github.com/R2Scout/R2Team-Protocol/pull/16
base_sha: e2f6ba5088a9f1bfb753c9b2b7773be815374506
candidate_sha: bcccd5d29f13141d50b33d8d9e6e095b91189d1e
verified_sha: bcccd5d29f13141d50b33d8d9e6e095b91189d1e
merged_sha: d75c64d39a335a7f8cf1a74f46aef81e7606e041
release_commit_sha: d75c64d39a335a7f8cf1a74f46aef81e7606e041
release_tag: v2.9
release_tag_object_sha: 6656801b8cb8cb64dc187c93fc39a58f4f4805c6
release_url: https://github.com/R2Scout/R2Team-Protocol/releases/tag/v2.9
publication_state: RELEASE_PUBLISHED
next_action: "No further payload change. Publish this task-only receipt and close the owned transport branch/Issue #15 after read-back. Project PMs use the pinned release and maintained update prompt."
---

# Outcome and scope

Continue the accepted protocol-update/publication workflow with the user's explicit terminology and directory-formation correction on 2026-11-24. Say Git worktree for Git working copies and resource for broader lifetime governance. Preserve technical command/schema compatibility.

New ordinary linked Git worktrees use one direct child of the approved root, named native-ID plus project/work/lifetime/executor label. Preserve native IDs, compatible existing paths, primary/legacy directories, and application-controlled hierarchy. No revision/chat/date/retry/batch parent folders, output-root placement, automatic renaming, or duplicate allocation.

Update protocol, TEAM/TASK/local observation templates, workspace skill, directory/lifetime policy, migration, and the maintained PM update prompt. The naming helper is pure and performs no actual resource creation, movement, or cleanup. Existing v2.8/v2.7 releases remain immutable.

# Acceptance and publication

Verify four offline suites, six skill formats, payload hashes, links/privacy/safety, English-only Markdown, compilation, command-copy equality, and staged/merged byte identity. Five new directory-name fixtures first failed for missing behavior and passed after implementation. Record the exact verified source and publication read-back here.

PASS returns the published checkpoint and release references to Issue #15; FAIL/BLOCKED retains recoverable source and returns the blocker to that same route. The same publisher owns the existing protocol update. No new author worktree is allocated; reuse the canonical checkout and preserve registered recovery worktrees.

NOT_RUN unless separately evidenced: independent consuming-agent review, project adoption, installed-skill replacement, actual directory creation/rename/cleanup/decommission, runtime effects, and PM chat dispatch. The requested PM update text is maintained in templates/PM_PROTOCOL_UPDATE.md.

# Verified release candidate

PASS: exact versioned manifest-only payload; validator 58/58, workspace 42/42, relocation 73/73, resource/lifetime/directory 21/21 (194/194 total); 6/6 official skill formats; 65/65 payload hashes; links/privacy/safety, English-only Markdown, Python compilation, command-copy equality, and git diff --check. Manifest SHA-256: 32ef0970ec4313fb1693c00534f2b8c49fc38e0cc5510b07ff1197cafafdd94a. The next commit binds this verified source before PR integration.

# Final publication receipt

- PASS: PR #16 integrated exact source bcccd5d29f13141d50b33d8d9e6e095b91189d1e as d75c64d39a335a7f8cf1a74f46aef81e7606e041; merged-state and remote main read-back matched.
- PASS: staged, committed, and actual merged bytes preserve the verified manifest and all 65 payload hashes. Four suites passed 194/194; six skill formats and link/privacy/English/compile/command checks passed.
- Annotated v2.9 object 6656801b8cb8cb64dc187c93fc39a58f4f4805c6 peels to release commit d75c64d39a335a7f8cf1a74f46aef81e7606e041.
- GitHub Release v2.9 is published, non-draft, non-prerelease, and returned as latest.
- Historical v2.8 object c41e6bbf896bff6da7ac52ceb6d08971674368eb still peels to 3e023e5222b69d7b2bc0b58316d0cc5e2021be2a; historical v2.7 remains unchanged.
- The maintained PM update prompt and Git worktree directory policy are included in the exact release. No PM chat dispatch or downstream adoption is implied.
- This receipt changes TASK metadata only. The canonical author checkout and both registered detached recovery worktrees remain retained; no new Git worktree, directory rename, or live project cleanup occurred. The owned manifest-only verification copy can be discarded after this compact receipt.

NOT_RUN: independent consuming-agent/live behavior, installed-skill replacement, downstream resource allocation/rename/cleanup/decommission, runtime effects, and chat messaging. Source publication and the requested PM prompt update are complete.

---
protocol_version: "2.10"
id: TASK-R2TEAM-GIT-REFERENCE-NAMES-001
revision: 1
status: DONE
stage: RELEASE
owner_executor_id: r2team-protocol-owner
owner_route: https://github.com/R2Scout/R2Team-Protocol/issues/18
task_issuer_executor_id: r2team-protocol-owner
task_issuer_route: https://github.com/R2Scout/R2Team-Protocol/issues/18
project_pm_executor_id: r2team-protocol-owner
project_pm_route: https://github.com/R2Scout/R2Team-Protocol/issues/18
result_to_executor_id: r2team-protocol-owner
result_to_route: https://github.com/R2Scout/R2Team-Protocol/issues/18
delivery_policy: git_checkpoint_then_tracker
tracker_item: https://github.com/R2Scout/R2Team-Protocol/issues/18
branch: protocol/git-reference-worktree-names
pr: https://github.com/R2Scout/R2Team-Protocol/pull/19
base_sha: 9ad076a1066e76b907dc90be1191027506493eb1
candidate_sha: a08a53b2702e347690d60eca47d428da70551c04
verified_sha: a08a53b2702e347690d60eca47d428da70551c04
merged_sha: c87a623c8c5cc60d3e408d933c10cc104431b871
release_commit_sha: c87a623c8c5cc60d3e408d933c10cc104431b871
release_tag: v2.10
release_tag_object_sha: 0a673a75330f19586baf9cb489d7b6173c12d9c1
release_url: https://github.com/R2Scout/R2Team-Protocol/releases/tag/v2.10
publication_state: RELEASE_PUBLISHED
next_action: "No further payload change. Publish this task-only receipt, close Issue #18 and the owned transport branch after read-back. Project PMs use the pinned release/update prompt."
---

# Outcome and authority

The owner accepted removing extra physical/native IDs from ordinary Git worktree names and explicitly requested publication and an updated PM prompt on 2026-11-24. Use the accepted primary Issue/TASK/PR/Work Item reference and actual number, lifetime, and executor. Keep internal IDs in registry/custody records.

# Included scope

Update naming rules/model, protocol, TEAM/local-observation/command/skill guidance, migration, and the maintained PM prompt. Declared purpose suffixes such as build/integration distinguish already authorized lanes, never collision counters. Preserve existing/application-managed paths, reuse, budgets, and lifecycle/authority gates. Use an actual governance TASK reference for standing Git worktree anchors.

# Verification and release

The updated fixtures first failed because the old directory model required an additional ID and lacked purpose suffix support, then passed after implementation. Validate the exact versioned manifest-only package with four suites, six skill formats, hashes/links/privacy/English/compile/command checks, and staged/merged byte identity. Record exact source and release references at publication.

PASS returns the published checkpoint to Issue #18; FAIL/BLOCKED retains recoverable state and returns evidence there. Reuse the existing author checkout and preserve detached recovery worktrees. Older release tags remain immutable.

NOT_RUN unless separately evidenced: independent consuming-agent review, downstream adoption, installed-skill replacement, directory creation/rename/cleanup/decommission, runtime effects, and PM chat messaging. The updated prompt is source material, not delivery or adoption proof.

# Verified candidate

PASS: exact versioned manifest-only package; validator 58/58, workspace 42/42, relocation 73/73, resource/lifetime/naming 23/23 (196/196); 6/6 skill formats; 66/66 hashes; links/privacy/English/compile/command equality and diff checks. Manifest SHA-256: d8551e6b603e80ba48c9bc6ce6a83b26be694779a58a134210e279e89369bded.

# Final publication receipt

- PR #19 integrated source a08a53b2702e347690d60eca47d428da70551c04 as c87a623c8c5cc60d3e408d933c10cc104431b871; provider merged-state and remote main read-back matched.
- Staged, committed, and actual merged bytes preserve the verified manifest and all 66 payload hashes. Four suites passed 196/196; six skill formats and links/privacy/English/compile/command checks passed.
- Annotated v2.10 object 0a673a75330f19586baf9cb489d7b6173c12d9c1 peels to the accepted release commit c87a623c8c5cc60d3e408d933c10cc104431b871.
- GitHub Release v2.10 is published, non-draft, non-prerelease, and latest. Historical v2.9 object 6656801b8cb8cb64dc187c93fc39a58f4f4805c6 still peels to d75c64d39a335a7f8cf1a74f46aef81e7606e041; older tags remain unchanged.
- The maintained PM prompt and migration/naming rules are part of the exact release. No downstream directory rename, cleanup, installed-skill replacement, or chat dispatch occurred.
- This receipt changes TASK metadata only. The canonical author checkout and both detached recovery worktrees remain retained; the owned manifest-only verification copy can be discarded after this compact receipt.

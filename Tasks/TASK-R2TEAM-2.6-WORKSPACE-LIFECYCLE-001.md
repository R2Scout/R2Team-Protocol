---
protocol_version: "2.5"
id: "TASK-R2TEAM-2.6-WORKSPACE-LIFECYCLE-001"
revision: 4
handoff_seq: 0
status: REVIEW_READY
stage: QA
owner_executor_id: "r2team-protocol-pm"
owner_route: "https://github.com/R2Scout/R2Team-Protocol/issues/1"
previous_owner_executor_id: null
assigned_by_executor_id: "r2team-protocol-owner"
task_issuer_executor_id: "r2team-protocol-owner"
task_issuer_route: "https://github.com/R2Scout/R2Team-Protocol/issues/1"
project_pm_executor_id: "r2team-protocol-pm"
project_pm_route: "https://github.com/R2Scout/R2Team-Protocol/issues/1"
result_to_executor_id: "r2team-protocol-owner"
result_to_route: "https://github.com/R2Scout/R2Team-Protocol/issues/1"
delivery_policy: git_checkpoint_then_tracker
executor_mode: "local_standalone"
parent_executor_id: null
active_role: PM
tracker_item: "https://github.com/R2Scout/R2Team-Protocol/issues/1"
tracker_item_type: github_issue
requirement_ref: "planning/r2team-2.6-workspace-lifecycle/normative-deltas.md"
branch: "planning/r2team-2.6-workspace-lifecycle"
pr: null
openspec_change: null
base_sha: "a5adba57d133e58360347ac2c709e88433061e90"
candidate_sha: "50fce2e22086e940a7d16221072d87187c4abefd"
verified_sha: null
merged_sha: null
next_action: "Obtain independent review of implementation candidate 50fce2e22086e940a7d16221072d87187c4abefd / tree e9463cf931b053415f4b4bec7c5737758d5771dc, then prepare the PR without merging."
questions: []
---

# Outcome

Define a reviewable R2Team 2.6 workspace-lifecycle contract that prevents unbounded physical worktree growth while preserving candidate identity, independent review, evidence, local custody, and recoverability.

# Scope and boundaries

Included:

- workspace identity, lease, budget, retention, closure, and recovery semantics;
- TASK, TEAM, role, setup, command, skill, migration, and validator deltas;
- allocation and disk gates;
- close receipts and Codex-managed custody;
- project-local adoption and backward compatibility.

Excluded:

- merge, release, installed-skill replacement, downstream adoption, and live cleanup;
- modification of the paused dirty candidate/r2team-2.6 checkout;
- cleanup or removal of any existing worktree, branch, process, cache, data, or evidence;
- team/chat relocation, which requires a distinct R2Team 2.7 TASK and checkpoint.

The distribution repository is not converted into an adopted product team by this planning TASK. Logical executor names identify this authorized governance route; physical task or thread IDs must not enter Git.

# Acceptance

- Proposal, design, normative deltas, implementation tasks, and validation plan are complete and mutually consistent.
- TASK identity, candidate identity, and workspace identity are explicitly separated.
- Result acceptance and workspace disposition remain independent evidence axes.
- Accepted integration records durable evidence in Git or a sanitized hash-bound durable recovery reference.
- No completed stage leaves a silently ACTIVE workspace lease.
- Temporary material is removed only when ownership, dependency, evidence-export, and removal-authority gates all pass.
- Defaults and exception rules are explicit without granting destructive authority.
- Machine-private paths remain outside Git.
- The plan preserves R2Team 2.5 operation until a separately accepted 2.6 release.
- The paused predecessor candidate remains byte-for-byte untouched by this lane.
- R2Team 2.6 contains workspace lifecycle only; team/chat relocation is excluded for 2.7.
- Operational workspace commands are packaged in a separate `r2team-workspace` skill; `r2team-work` does not gain hidden workspace mutation.

# Plan

- [Proposal](../planning/r2team-2.6-workspace-lifecycle/proposal.md)
- [Design](../planning/r2team-2.6-workspace-lifecycle/design.md)
- [Normative deltas](../planning/r2team-2.6-workspace-lifecycle/normative-deltas.md)
- [Implementation tasks](../planning/r2team-2.6-workspace-lifecycle/tasks.md)
- [Validation plan](../planning/r2team-2.6-workspace-lifecycle/validation-plan.md)

# Current checkpoint

- Completed: planning checkpoint published; Issue #1 updated; lifecycle-only 2.6 package implemented test-first; separate `r2team-workspace` packaged; validator, 32 behavior tests, all five skill-format checks, static public scan, diff check, and fresh-package validation passed; implementation candidate pushed.
- Remaining: independent exact-candidate review; address any accepted findings; prepare the PR.
- Blockers: none for the authorized stages. Merge, release, installed-skill replacement, downstream adoption, and live cleanup remain separately gated.

# Evidence

- Exact base: a5adba57d133e58360347ac2c709e88433061e90
- Planning checkpoint: 96609ff8e721b4c1f83841ebc9bfdcae3e4852e0 / tree 76706d15dbe96da6de6531e02cf547613b8a567d
- Implementation candidate: 50fce2e22086e940a7d16221072d87187c4abefd / tree e9463cf931b053415f4b4bec7c5737758d5771dc
- Environment: isolated ordinary Git worktree on branch planning/r2team-2.6-workspace-lifecycle
- Subject: R2Team 2.6 workspace lifecycle distribution package and planning artifacts
- Structural validator: PASS
- Behavioral validator suite: PASS, 32 tests
- Skill format validation: PASS, five packaged skills
- Fresh-package review: PASS for manifest-only isolated payload, validator, behavior tests, and skill formats
- Runtime/product verification: NOT_RUN and out of scope
- Downstream adoption: NOT_RUN and independently gated
- Tracker: https://github.com/R2Scout/R2Team-Protocol/issues/1

# Decisions and handoff

The protocol PM returned AMEND on the submitted governance proposal. The reconciled model is accepted for planning, not implementation. The existing dirty candidate/r2team-2.6 checkout is predecessor material and must not be used as this change's planning authority.

The disk/worktree system architect returned AMEND on the merge-evidence and workspace-closure wording, with one accepted safety clarification: temporary material is removed only after verified evidence export when it is exclusively owned by the closing lease, has no live process or dependent lease, is not a shared immutable cache or retained recovery input, and the closer already has explicit removal authority. Otherwise it receives a retained, transferred, or blocked disposition with an owner and review date.

The owner accepted the reconciled plan: R2Team 2.6 is limited to workspace lifecycle, team/chat relocation moves to a distinct 2.7 TASK and checkpoint, and operational workspace behavior is packaged as a separate `r2team-workspace` skill rather than hidden mutation in `r2team-work`.

# Authorized next transitions

| Outcome | Next TASK status | Next owner executor | Next owner route | Next active role | Following stage returns to | Following result route | Authorized publisher |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PASS | REVIEW_READY | r2team-protocol-owner | https://github.com/R2Scout/R2Team-Protocol/issues/1 | PM | r2team-protocol-pm | https://github.com/R2Scout/R2Team-Protocol/issues/1 | owner-authorized publisher |
| AMEND | DRAFT | r2team-protocol-pm | https://github.com/R2Scout/R2Team-Protocol/issues/1 | PM | r2team-protocol-owner | https://github.com/R2Scout/R2Team-Protocol/issues/1 | r2team-protocol-pm |
| BLOCKED | BLOCKED | r2team-protocol-pm | https://github.com/R2Scout/R2Team-Protocol/issues/1 | PM | r2team-protocol-owner | https://github.com/R2Scout/R2Team-Protocol/issues/1 | r2team-protocol-pm |

# Publication gate

The owner authorized the minimum planning checkpoint, Issue #1 update, isolated implementation, validation, independent exact-candidate review, and PR preparation. Before each authorized checkpoint:

1. Confirm the exact planning diff from the accepted base.
2. Keep the commit and push limited to the accepted planning or implementation scope.
3. Run the planning validation plan.
4. Preserve the paused predecessor checkout unchanged.
5. Stop before merge, accepted-main publication, release, installed-skill replacement, downstream adoption, or live cleanup.

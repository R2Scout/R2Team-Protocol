---
protocol_version: "2.6"
id: "TASK-R2TEAM-2.7-TEAM-CHAT-RELOCATION-001"
revision: 1
handoff_seq: 0
status: DRAFT
stage: DISCOVERY
owner_executor_id: "r2team-protocol-pm"
owner_route: "https://github.com/R2Scout/R2Team-Protocol/issues/3"
previous_owner_executor_id: null
assigned_by_executor_id: "r2team-protocol-owner"
task_issuer_executor_id: "r2team-protocol-owner"
task_issuer_route: "https://github.com/R2Scout/R2Team-Protocol/issues/3"
project_pm_executor_id: "r2team-protocol-pm"
project_pm_route: "https://github.com/R2Scout/R2Team-Protocol/issues/3"
result_to_executor_id: "r2team-protocol-owner"
result_to_route: "https://github.com/R2Scout/R2Team-Protocol/issues/3"
delivery_policy: git_checkpoint_then_tracker
executor_mode: "local_standalone"
parent_executor_id: null
active_role: PM
tracker_item: "https://github.com/R2Scout/R2Team-Protocol/issues/3"
tracker_item_type: github_issue
requirement_ref: "planning/r2team-2.7-team-chat-relocation/normative-deltas.md"
branch: "planning/r2team-2.7-team-chat-relocation"
pr: null
openspec_change: null
base_sha: "7e7a35eaf89726b0850da78aaa176d142d7fc1ce"
candidate_sha: null
verified_sha: null
merged_sha: null
workspace_policy: inherited_from_protocol_2.6
workspace_exceptions: []
workspace_leases:
  - lease_id: "lease-r2team-2.7-author-001"
    task_id: "TASK-R2TEAM-2.7-TEAM-CHAT-RELOCATION-001"
    purpose: author
    class: ordinary-canonical
    owner_executor_id: "r2team-protocol-pm"
    closure_owner_executor_id: "r2team-protocol-pm"
    base_sha: "7e7a35eaf89726b0850da78aaa176d142d7fc1ce"
    candidate_sha: null
    mutability: mutable
    custody: ordinary-canonical
    state: ACTIVE
    retention_class: task-working
    review_date: "2026-11-09"
    recovery_ref: "refs/heads/planning/r2team-2.7-team-chat-relocation"
    exception_ref: null
    close_receipt_ref: null
workspace_disposition: ACTIVE
candidate_dispositions: []
artifact_manifests: []
close_receipts: []
next_action: "Publish the bounded planning checkpoint and obtain System Architect review of identity, freeze, resume, rollback, and skill-boundary decisions before implementation."
questions:
  - id: Q-2.7-SKILL-BOUNDARY
    mode: LOOP
    status: OPEN
    requester_executor_id: "r2team-protocol-pm"
    to_executor_id: "disk-worktree-system-architect"
    route: "https://github.com/R2Scout/R2Team-Protocol/issues/3"
    blocking: "implementation"
    decision: null
---

# Outcome

Define R2Team 2.7 so one role chat, one logical executor, or a whole team can relocate between Codex chats or hosts without duplicating writers, losing TASK/candidate/evidence custody, copying private chat state, or confusing relocation with participant/function transfer.

# Scope and boundaries

Included:

- logical participant/executor/TASK identity versus physical chat, host, and local route identity;
- role relocation and whole-team cutover prepare/resume flows;
- durable global migration bundle plus per-executor handoff records;
- PM-controlled writer freeze, ordered bootstrap, forward rollback, and completion receipt;
- ignored local thread-registry remapping without committed thread IDs or paths;
- R2Team 2.6 workspace lease/custody integration;
- protocol, setup, migration, TEAM/TASK, roles, commands, skills, validator, and fixtures.

Excluded:

- chat transcript export or copying;
- implicit participant, executor, function, TASK, or permission transfer;
- credential copying, account administration, automatic chat creation, heartbeat, deployment, release, or downstream adoption;
- live team relocation, process stop, branch deletion, installed-skill replacement, application archive, or workspace cleanup;
- concurrent old/new writers for the same executor/TASK.

# Acceptance

- Same logical executor relocation preserves participant, executor, TASK, Issue/PR, candidate, and evidence identity.
- A changed participant/executor uses the existing ownership-transfer workflow, not relocation.
- Old and replacement chats cannot both write for the same executor/TASK.
- Resume requires an accepted Git cutover bundle, exact source SHA, writer-stop proof, target placement, access/tool preflight, and an opened resume gate.
- Durable Git contains no thread IDs, private machine paths, secrets, transcripts, or copied local runtime state.
- Local thread registry remapping is ignored, read back, and insufficient by itself to authorize work.
- Active workspace leases are closed, retained, or transferred with R2Team 2.6 evidence; relocation never implies cleanup authority.
- Function transfer command semantics remain unchanged.
- R2Team 2.6 projects remain unchanged until explicit 2.7 adoption.
- A separate `r2team-relocate` skill is independently reviewed as the sole operational relocation entry point, or the reviewer returns a narrower accepted alternative before implementation.

# Plan

- [Proposal](../planning/r2team-2.7-team-chat-relocation/proposal.md)
- [Design](../planning/r2team-2.7-team-chat-relocation/design.md)
- [Normative deltas](../planning/r2team-2.7-team-chat-relocation/normative-deltas.md)
- [Implementation tasks](../planning/r2team-2.7-team-chat-relocation/tasks.md)
- [Validation plan](../planning/r2team-2.7-team-chat-relocation/validation-plan.md)

# Current checkpoint

- Completed: merged R2Team 2.6 base read back; Issue #3 created; the clean 2.6 author worktree was reused as the 2.7 author lease without allocating another physical worktree; predecessor dirty material remains protected and untouched.
- Remaining: publish planning; obtain System Architect review; reconcile accepted findings; implement, validate, independently review, and prepare a PR.
- Blockers: implementation waits for the skill-boundary and cutover-state review. Merge, release, installation, downstream adoption, and live relocation remain separate gates.

# Evidence

- Base/main: `7e7a35eaf89726b0850da78aaa176d142d7fc1ce`
- Base tree: `f15f17d76acf245e8ff7ef2b89778ef423e11644`
- Branch: `planning/r2team-2.7-team-chat-relocation`
- Tracker: https://github.com/R2Scout/R2Team-Protocol/issues/3
- Predecessor relocation material: read-only architectural input, not accepted authority or copied runtime state.
- Runtime/live relocation: NOT_RUN and out of scope.

# Authorized next transitions

| Outcome | Next TASK status | Next owner executor | Next owner route | Next active role | Following result recipient | Following result route | Authorized publisher |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Planning PASS | IMPLEMENTING | r2team-protocol-pm | https://github.com/R2Scout/R2Team-Protocol/issues/3 | PM | r2team-protocol-owner | https://github.com/R2Scout/R2Team-Protocol/issues/3 | r2team-protocol-pm |
| AMEND | DRAFT | r2team-protocol-pm | https://github.com/R2Scout/R2Team-Protocol/issues/3 | PM | r2team-protocol-owner | https://github.com/R2Scout/R2Team-Protocol/issues/3 | r2team-protocol-pm |
| BLOCKED | BLOCKED | r2team-protocol-pm | https://github.com/R2Scout/R2Team-Protocol/issues/3 | PM | r2team-protocol-owner | https://github.com/R2Scout/R2Team-Protocol/issues/3 | r2team-protocol-pm |

# Publication gate

The owner request authorizes the minimum planning checkpoint, Issue #3 updates, bounded implementation on this reused author lease, validation, independent exact-candidate review, and PR preparation. It does not authorize merge, release, installed-skill replacement, downstream adoption, live relocation, chat creation, registry mutation on another host, process stop, branch deletion, or cleanup.

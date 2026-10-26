---
protocol_version: "2.6"
id: "TASK-R2TEAM-2.7-TEAM-CHAT-RELOCATION-001"
revision: 3
handoff_seq: 0
status: IMPLEMENTING
stage: IMPLEMENTATION
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
next_action: "Implement the accepted revision-2 contract with red-first relocation policy and validator fixtures, then publish an exact candidate for fresh independent review."
questions:
  - id: Q-2.7-SKILL-BOUNDARY
    mode: LOOP
    status: RESOLVED
    requester_executor_id: "r2team-protocol-pm"
    to_executor_id: "disk-worktree-system-architect"
    route: "https://github.com/R2Scout/R2Team-Protocol/issues/3"
    blocking: "implementation"
    decision: "Use a separate r2team-relocate skill as the sole relocation mutation entry point; retain r2team migrate for function transfer and keep relocation mutation out of r2team-work."
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
- Old and replacement chats cannot both be accepted writers for the same executor/TASK under per-executor causal cooperative fencing; provider-enforced exclusion requires separate evidence.
- Resume requires an accepted Git cutover bundle, exact source SHA, per-executor expected epoch and causal parent, exact writer-stop receipt, target placement, access/tool preflight, causally linked activation receipt, and accepted read-back.
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

- Completed: merged R2Team 2.6 base read back; Issue #3 created; the clean 2.6 author worktree was reused as the 2.7 author lease without allocating another physical worktree; planning rev1 was reviewed as `AMEND`; A1-A6 were reconciled into rev2; exact revision-2 checkpoint received System Architect `PASS`.
- Remaining: implement the accepted contract, validate an exact candidate, obtain fresh independent candidate review, and prepare a PR.
- Blockers: none for bounded implementation. Merge, release, installation, downstream adoption, provider-enforced fencing claims, and live relocation remain separate gates.

# Evidence

- Base/main: `7e7a35eaf89726b0850da78aaa176d142d7fc1ce`
- Base tree: `f15f17d76acf245e8ff7ef2b89778ef423e11644`
- Branch: `planning/r2team-2.7-team-chat-relocation`
- Tracker: https://github.com/R2Scout/R2Team-Protocol/issues/3
- Planning rev1: `6f0555a2003cd811f7c567b151539e4c90e5da65`, tree `bc679de82a0a85aa9d82a9480c2023388f7f9db0`.
- System Architect rev1 verdict: `AMEND`; accepted separate skill/identity/registry/workspace/forward-rollback boundaries, required per-executor causal fencing, recoverable partial states, exact evidence, typed receipts, candidate wording, and missing fixtures.
- Planning rev2: `a5c9447dc0603cf895cc7d6105768091ab02d431`, tree `ee67f59e74bbe28306eddb5aa84e575e27c20e40`.
- System Architect rev2 verdict: `PASS`; remote SHA/tree, parent, exact six-file delta, A1-A6 reconciliation, and zero private IDs/paths independently verified. Implementation-candidate PASS remains NOT_RUN and non-transferable.
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

---
protocol_version: "2.6"
id: "TASK-R2TEAM-2.7-TEAM-CHAT-RELOCATION-001"
revision: 12
handoff_seq: 0
status: REVIEW_READY
stage: QA
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
candidate_sha: "d531d3fb4e5b1356afecfaaf26785ede2a2421f2"
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
    candidate_sha: "d531d3fb4e5b1356afecfaaf26785ede2a2421f2"
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
next_action: "Obtain fresh independent re-review of successor d531d3fb4e5b1356afecfaaf26785ede2a2421f2 / tree 47a9dbe6af05226ee73d6fae88f9c8a9a475c45f; prepare a PR without merging only if PASS."
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

- Completed: planning revision 2 received System Architect `PASS`; candidates through `add35ad206d254f939038e5ce45eee825ba6ee1b` received independent `AMEND`; successor `d531d3fb4e5b1356afecfaaf26785ede2a2421f2` closes C1-C2 with one shared latest-stage resolver and exhaustive mixed-peer matching, plus red-first fixtures and fresh manifest-only validation.
- Remaining: obtain fresh independent re-review of the exact successor and, only if PASS, prepare a PR without merging.
- Blockers: none for independent review. Merge, release, installation, downstream adoption, provider-enforced fencing claims, and live relocation remain separate gates.

# Evidence

- Base/main: `7e7a35eaf89726b0850da78aaa176d142d7fc1ce`
- Base tree: `f15f17d76acf245e8ff7ef2b89778ef423e11644`
- Branch: `planning/r2team-2.7-team-chat-relocation`
- Tracker: https://github.com/R2Scout/R2Team-Protocol/issues/3
- Planning rev1: `6f0555a2003cd811f7c567b151539e4c90e5da65`, tree `bc679de82a0a85aa9d82a9480c2023388f7f9db0`.
- System Architect rev1 verdict: `AMEND`; accepted separate skill/identity/registry/workspace/forward-rollback boundaries, required per-executor causal fencing, recoverable partial states, exact evidence, typed receipts, candidate wording, and missing fixtures.
- Planning rev2: `a5c9447dc0603cf895cc7d6105768091ab02d431`, tree `ee67f59e74bbe28306eddb5aa84e575e27c20e40`.
- System Architect rev2 verdict: `PASS`; remote SHA/tree, parent, exact six-file delta, A1-A6 reconciliation, and zero private IDs/paths independently verified. Implementation-candidate PASS remains NOT_RUN and non-transferable.
- Rejected implementation candidate: `3971e5e863d3a1c19573f9fa99f9d73644758599`, tree `db9ecec114b26af6f404b308c6695acefa02ec50`; independent verdict `AMEND`, review receipt `MSG-20261026-011841-276718f9`.
- Accepted corrections F1-F7: authoritative relocation identity; full stop proof and exact activation identity; exhaustive freeze class/path/field denial; receipt-gated cancellation/rollback routing; terminal-accounted completion; workspace owner/mutability; typed causal receipt schemas.
- First hardened successor (later rejected): `88d920f48690bd5b76a13138b08dd7bc40b2d2a1`, tree `fbc85e46308be6484c43359cc71e4bf97a6f6359`, parent `0033fe60b26c8c69315fa287bd26bd69ae9ab570`.
- Structural validator: PASS; validator suite: 53/53; workspace policy: 32/32; relocation policy: 38/38; official skill validation: 6/6; command copies byte-identical; `git diff --check`: PASS.
- Independent probes: invalid stop `STOP_PROOF_INVALID`; frozen TASK `FROZEN_PUBLICATION_BLOCKED`; epoch-only recovery `REACTIVATION_REQUIRED`/`FORWARD_ROLLBACK_REQUIRED`; terminal-accounted mixed team `COMPLETE`; wrong workspace owner/mutability `WORKSPACE_REUSE_BLOCKED`; blank receipt `RECEIPT_INVALID`.
- Fresh manifest-only package: PASS for 59 required files, all 53/32/38 suites, all six skill checks, byte-identical help, English-only public Markdown; temporary package removed after verification.
- Rejected successor: `88d920f48690bd5b76a13138b08dd7bc40b2d2a1`, tree `fbc85e46308be6484c43359cc71e4bf97a6f6359`; independent verdict `AMEND`, review receipt `MSG-20261026-013824-88d920f4`.
- Accepted corrections R1-R4: activation composes complete typed stop validation; receipt sets require closed cross-record activation-to-stop edges; epochs are strict non-boolean successor integers; frozen governing-TASK field scopes require canonical tuple/list string collections.
- Rejected successor: `9fd8a4a2a2b45cfe9ac97d8f49f47cc41bfd7bc4`, tree `3722276177b46f83d2f510fe61394f82a0e5719d`; independent verdict `AMEND`, review receipt `MSG-20261026-014618-9fd8a4a2`.
- Accepted corrections B1-B3: all epoch-bearing boundaries use strict non-boolean successor integers; SOURCE_STOP binds its common causal parent to the cutover parent; singular evidence facts and reference collections reject blank, non-string, null, and duplicate values and preserve exact TASK/candidate membership.
- Rejected successor: `978697c11f26911a28533b6d521191721e7d1872`, tree `a39d8ab07a3d87e7a71a5238d81712d767b80794`; independent verdict `AMEND`, review receipt `MSG-20261026-015636-978697c1`.
- Accepted corrections S1-S6: freeze state is a strict boolean; fencing uses a closed single-writer state/custody matrix; activation binds accepted cutover/commit, registry/mapping, and included preflight evidence; every receipt type has typed semantics and accepted-root/affected-set causal closure; remote-manual absence rejects collisions/observations; canonical paths reject controls and nonportable segments.
- Rejected successor: `363caa5a0b2838efcb7c8ded4622be1d6bd7e57a`, tree `0bd0ffde59d0c1b3920aa745fc2a3a89747e2f28`; independent verdict `AMEND`, review receipt `MSG-20261026-021027-363caa5a`.
- Accepted corrections G1-G4: every activation API consumes an included same-identity PASS preflight; completion binds an external root, exactly one PREPARE, one lineage, role/team mode, and full team FREEZE; later causal receipt generations coexist with logical-event deduplication and typed terminal BLOCKED; aggregate state validates exact unique affected records and resolves their latest graph terminals or returns INVALID.
- Rejected successor: `b8697150c46a6f320c24b923cce33be7781161e0`, tree `9c84141b8beb7cc9953156e7454e75b2abcede17`; independent verdict `AMEND`, review receipt `MSG-20261026-053529-b8697150`.
- Accepted corrections A1-A3: SOURCE_STOP requires exact typed `SOURCE_STOPPED` in stop/activation/graph paths; every team preflight references the exact full-set FREEZE and is causally/temporally later; aggregate derivation validates nonempty minimum receipt context before every FROZEN/READY/RESUMING return.
- Rejected successor: `5a7a058d2ff01e6227e62b2a5d29919dff369545`, tree `f9a82018268f2a0d947199fbc084bc14a251fb35`; independent verdict `AMEND`, review receipt `MSG-20261026-055107-5a7a058d`.
- Accepted corrections B1-B2: every non-complete aggregate state selects the unique latest causal stage per executor instead of historical PASS/activation existence, rejecting ambiguous same-epoch alternatives except the activation-to-supporting-preflight pair; team receipt graphs require strict `SOURCE_STOP < FREEZE < TARGET_PREFLIGHT < ACTIVATION` timestamps, including offset-equivalent instants.
- Rejected successor: `add35ad206d254f939038e5ce45eee825ba6ee1b`, tree `99a290dbe59c2f608755217c3373f1e921619f6a`; independent verdict `AMEND`, review receipt `MSG-20261026-060216-add35ad`.
- Accepted corrections C1-C2: receipt-set completion and aggregate derivation use one shared latest-stage resolver, so an older terminal cannot close over a newer nonterminal generation; every mixed aggregate record, including PENDING/INACTIVE peers, is exhaustively matched to its latest stage and disposition.
- Current successor candidate: `d531d3fb4e5b1356afecfaaf26785ede2a2421f2`, tree `47a9dbe6af05226ee73d6fae88f9c8a9a475c45f`, parent `1c38243004ea20a0605a63d5e58b0569caeb68e4`.
- Structural validator: PASS; validator suite: 53/53; workspace policy: 32/32; relocation policy: 72/72; official skill validation: 6/6; command copies byte-identical; `compileall` and `git diff --check`: PASS.
- Boundary probes: old rollback completion over newer stop/BLOCKED preflight is `RECEIPT_INVALID`; mixed inactive peers with BLOCKED/FAIL preflight, cancellation, rollback, or partial disposition return `INVALID`; a mixed peer whose latest stage is SOURCE_STOP remains valid `RESUMING`.
- Fresh manifest-only package: PASS for 59 required files, all 53/32/72 suites, all six skill checks, byte-identical help, English-only public Markdown; temporary package removed after verification.
- Predecessor relocation material: read-only architectural input, not accepted authority or copied runtime state.
- Runtime/live relocation: NOT_RUN and out of scope.

# Authorized next transitions

| Outcome | Next TASK status | Next owner executor | Next owner route | Next active role | Following result recipient | Following result route | Authorized publisher |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Implementation PASS | REVIEW_READY | r2team-protocol-pm | https://github.com/R2Scout/R2Team-Protocol/issues/3 | PM | r2team-protocol-owner | https://github.com/R2Scout/R2Team-Protocol/issues/3 | r2team-protocol-pm |
| AMEND | IMPLEMENTING | r2team-protocol-pm | https://github.com/R2Scout/R2Team-Protocol/issues/3 | PM | r2team-protocol-owner | https://github.com/R2Scout/R2Team-Protocol/issues/3 | r2team-protocol-pm |
| BLOCKED | BLOCKED | r2team-protocol-pm | https://github.com/R2Scout/R2Team-Protocol/issues/3 | PM | r2team-protocol-owner | https://github.com/R2Scout/R2Team-Protocol/issues/3 | r2team-protocol-pm |

# Publication gate

The owner request authorizes the minimum planning checkpoint, Issue #3 updates, bounded implementation on this reused author lease, validation, independent exact-candidate review, and PR preparation. It does not authorize merge, release, installed-skill replacement, downstream adoption, live relocation, chat creation, registry mutation on another host, process stop, branch deletion, or cleanup.

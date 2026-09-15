# Multiple repositories — optional R2Team 2.1 mode

Each application retains its own Git root, TEAM, PM, TASKs and tracker. Cross-project coordination creates no mandatory global PM, duplicate backlog or competing specification. The base [protocol](CODEX_TEAM_PROTOCOL.md) still applies.

## Minimum connection

For SDK/API work, choose one contract-owning repository, usually the SDK/backend. Its OpenSpec specification, interfaces/schemas, compatibility policy and decisions are canonical. Consumers store their own integration requirements and exact contract-version/commit references, not independently editable copies.

One coordinating TASK/Issue in the contract repository records participants, change boundaries, required consumer confirmations, links to their TASKs/PRs, compatibility criteria and release order. It is an ordinary TASK, not another registry type.

Qualify addresses with repo URL, participant/executor and TASK/Issue/PR URL. TASK-042 in two repositories is not the same identity. Read access grants no write authority in another repository; each PM assigns only within their authority.

## Example: SDK, Web and Mobile

```text
SDK: TASK-021 - API v2 contract, SDK owner/PM
  +-- Web: TASK-042 - client adaptation, its own PM and PR
  +-- Mobile: TASK-017 - app adaptation, its own PM and PR
```

1. The initiator proposes the change to the API owner. Consumer PMs assign people to provide positions. Discussion does not authorize implementation in their projects.
2. Use the coordinating Issue for shared agreement and each PR for code. Preserve material open questions/decisions in the owner's TASK/spec; consumers preserve relevant commitments and pinned sources in their TASKs. Bounded transient exchanges may use [OPERATING_COMMUNICATION.md](OPERATING_COMMUNICATION.md).
3. The owner proposes an OpenSpec change covering compatibility, breaking changes, version and transition period. Consumers confirm constraints; silence is not agreement.
4. Each independently implemented change uses its repository's TASK/branch/PR and relevant skills. An external change link does not replace the local task contract.
5. Record a matrix of candidate SHA/SDK version, consumer version, contract/integration test and evidence. SDK unit tests alone do not establish coordinated readiness.
6. Release in the agreed order, using compatibility/feature flags or a coordinated switch and rollback. Separate repositories do not have an atomic merge; preserve partially released state explicitly.
7. Close the coordinating TASK against its cross-project DoD. A consumer's local DONE does not prove the whole release is delivered.

The preassigned contract decider resolves disputes within authority. Changing another project's commitments requires its authorized agreement; joining a discussion grants no global management rights.

## Setup and recovery

Only for a real dependency, record in TEAM or the relevant TASK: contract repo URL/path/ref, coordinator/account, canonical Issue, consumers and required confirmations. No global repository catalog for a small feature.

A new executor reads the local TASK and exact accessible external sources. Missing access is BLOCKED/UNKNOWN. An owner-approved export can be used with source SHA and a snapshot label, without secrets.

Provider mentions/subscriptions notify participants. Optional local wake needs verified routing and permission; separate projects/PMs do not imply one Codex process. COO reads only explicitly scoped repo-qualified deltas. Neither a skill nor the coordinating TASK starts a remote team by itself.

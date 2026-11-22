# Migrate an adopted project to R2Team 2.8

This is prospective project-local adoption from R2Team 2.7 or an explicitly reconciled older version. The previous accepted version remains governing until the project's own accepted-main checkpoint is published and read back. Release publication, skill installation, and project adoption are separate.

## 1. Pin and verify the package

Resolve annotated `v2.8` from the distribution repository and record its full commit SHA; do not substitute main/latest. Check `package.json`, payload hashes, package links, six skill formats, command-copy equality, and the validator, workspace, relocation, and resource-lifetime test suites. Package checks prove source contracts and offline decision behavior, not live provider/runtime acceptance.

## 2. Preserve current work

Inventory accepted AGENTS/TEAM/protocol, active TASKs/owners/routes, exact candidates, evidence, unresolved questions, pending transfers, physical Git/application-managed worktrees, governed resource roots, native dependencies, and unpublished material. Preserve current IDs, paths, roles, routes, OpenSpec changes, and rollback references. Inventory does not stop processes, rename directories, remove worktrees, or change live infrastructure.

An older 2.5/2.6 project can adopt 2.8 directly after explicitly reconciling the workspace and fencing additions described in [migration 2.6](MIGRATE_TO_2.6.md) and [migration 2.7](MIGRATE_TO_2.7.md). No intermediate published project release is required. A still-governing 1.10 communication contract remains effective until an approved cutover resolves it.

## 3. Adopt lifetime and readable names

Reconcile AGENTS, TEAM, protocol, used roles, TASK templates, commands, skills, and [RESOURCE_LIFETIME.md](RESOURCE_LIFETIME.md) through the project's normal workflow. Configure stable project/executor aliases and explicit resource lifetime:

- `persistent` / `perm`: standing anchors with accepted governance purpose/TASK and separate decommission authority;
- `task_scoped` / `task`: retained for a TASK result and its dependent consumers;
- `ephemeral` / `tmp`: one bounded verification, experiment, build, or other use.

Keep lifetime independent of dev/qa/build/release purpose, custody, state, and retention. Require resource ID, readable label, current owner, bound typed close condition, review date, retention, and recovery. Preserve native workspace IDs and existing leases/materialization keys. Labels never allocate another worktree or authorize cleanup. Outputs may outlive workspaces; classify governed roots individually, without a manifest or TASK for every disposable file.

## 4. Reconcile legacy resources prospectively

New allocation requires complete classification. Add fields to active leases and governed roots at the next material checkpoint. Unproved classification remains protected UNKNOWN / legacy-retained with a reconciliation owner and review date. Do not infer lifetime from name, role, age, or location. A due review is REVIEW_DUE, not deletion or automatic promotion. Maintain physical counts, hard caps, disjoint roots, custody, evidence, and dependency gates. Adoption grants no allocation, cleanup, decommission, rename, archive, or relocation authority.

## 5. Check installations and executors

Compare all six installed procedure skills with the pinned package on each machine or chosen project scope; preserve customizations and rollback, and obtain owner authorization for replacement. Avoid duplicate names across scopes. Verify actual discovery in a subsequent turn; no reinstall is required per chat on the same machine.

Each retained executor reads the accepted checkpoint and cross-checks role, current TASK, Owner/Task Issuer/Project PM/Result Recipient routes, loaded skills, and saved entry/watch instructions. Check discovery of an unknown eligible TASK, truthful task-only coverage, and addressed questions on another owner's TASK. Record NOT_RUN or pending compatibility honestly. Internal COO remains sufficient; no new chat or heartbeat is required.

## 6. Publish and validate cutover

PM publishes one organizational adoption checkpoint with exact package provenance, coherent configuration, lifetime/alias policy, active-resource reconciliation, validation limits, owners/review dates, and recovery route. Read back the accepted default branch and notify executors through existing authorized routes. Retained chats individually cross-check the new rules before using them.

For closure, verify the exact resource/owner/event/reference completion receipt, then all existing evidence, custody, dependency, containment, and removal-authority gates. Test these with offline fixtures. Live rename, cleanup, process stop, installed-skill replacement, provider revocation, deployment, and relocation remain NOT_RUN unless separately authorized and evidenced.

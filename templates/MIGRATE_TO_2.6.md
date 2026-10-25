# Migrate an adopted project to R2Team 2.6

This is a prospective policy adoption from R2Team 2.5 or an explicitly reconciled older version. R2Team 2.5 remains governing until the project publishes its own accepted-main 2.6 checkpoint. Replacing files, installing a skill, or reading this guide is not adoption.

## 1. Freeze the subject, not the project

Record the current accepted protocol source/ref, TEAM integration revision, active TASKs/owners/routes, branches/PRs, accepted OpenSpec, dirty or unpublished work, evidence/recovery references, automation, and known physical workspaces. Preserve active writers and unrelated work. Do not clean, relocate, stop, archive, or delete anything during inventory.

## 2. Verify the exact package

Use an owner-approved full commit SHA or trusted bundle manifest. Run the package validator and verify payload hashes. Confirm the package contains the separate `r2team-workspace` skill and does not introduce team/chat relocation behavior. An installed skill version is not project adoption evidence.

## 3. Reconcile project policy

Update `AGENTS.md`, `TEAM.md`, protocol/templates, command help, role files, and skill references through the project's normal protected workflow. Configure:

- maximum active leases per TASK and one-mutable-lease rule;
- project target and hard cap;
- destination-filesystem thresholds;
- portable placement classes and root aliases;
- retention classes and allowed closure methods;
- lifecycle reconciliation owner and exception route.

Keep physical paths, sizes, processes, native handles, and observation timestamps in ignored `.codex-local/` state.

## 4. Introduce TASK fields prospectively

Existing TASKs remain valid. Add `workspace_policy`, structured `workspace_exceptions`, `workspace_leases`, the derived `workspace_disposition`, and append-only `candidate_dispositions`, `artifact_manifests`, and `close_receipts` at the next material TASK revision or handoff after adoption. Each lease record retains its own state, closure owner, review date, retention class, recovery reference, and receipt reference; later candidates or leases never overwrite earlier history. A revision or handoff does not itself allocate another persistent workspace. A blocking/nonterminal lease preserves the candidate verdict but prevents administrative completion.

Classify every existing physical workspace as `legacy-retained` until a separately authorized reconciliation establishes owner, purpose, candidate, evidence, dependency, custody, and recovery. Unknown or dirty state is protected, not disposable.

## 5. Cross-check roles and skills

- PM owns budgets, exceptions, closure ownership, and reconciliation without implied deletion authority.
- Dev reuses its author lease for revisions/corrections.
- QA and Designer prefer ephemeral exact-candidate materialization and keep verdict separate from closure.
- DevOps/integration reuses a compatible lease and begins post-merge closure review only after provider read-back.
- COO/audit may report lifecycle facts but cannot mutate workspaces.
- `r2team-workspace` is the sole operational lifecycle entry point; `r2team-work` does not hide allocation or closure.

Retained standalone tasks cross-check the new accepted files before operating under 2.6. Higher-priority project instructions and any still-governing communication cutover remain in force until explicitly reconciled.

## 6. Validate adoption

Run the validator/tests on the exact project checkpoint. Demonstrate read-only status/doctor, one allowed allocation preflight, blocked over-budget/low-capacity fixtures, verdict/closure separation, durable merge evidence, and a close preflight that retains material when any removal gate is absent. Real allocation, live cleanup, application archive, branch deletion, process stop, data/profile/cache/evidence relocation, installed-skill replacement, merge, release, and deployment remain `NOT_RUN` unless separately authorized and evidenced.

## 7. Publish the cutover

The project PM publishes one accepted-main checkpoint containing the adopted version, exact package provenance, updated policy/templates, active TASK reconciliation, validation evidence/limitations, remaining legacy-retained leases, owner/review dates, and rollback/recovery route. Notify registered executors through the project's existing authoritative routes. Until that checkpoint is accepted, continue under the previous protocol.

Team or chat relocation is not part of this migration. It requires a distinct R2Team 2.7 TASK, checkpoint, candidate, validation, and acceptance decision.

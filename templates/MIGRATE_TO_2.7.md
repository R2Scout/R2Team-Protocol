# Migrate an adopted project to R2Team 2.7

This is prospective project-local adoption from R2Team 2.6 or an explicitly reconciled older version. R2Team 2.6 remains governing until the project publishes its own accepted-main 2.7 checkpoint. Reading files, installing skills, or preparing a relocation bundle is not adoption and performs no live relocation.

## 1. Freeze the adoption subject

Inventory the accepted protocol/package ref, TEAM/TASK state, participants/executors/functions, provider routes, active candidates/evidence, workspace/native-resource custody, local-registry classes, and any pending ownership transfer. Do not stop writers, create/move chats, remap registries, relocate work, clean, archive, or delete anything during inventory.

## 2. Verify the exact candidate

Use an owner-approved full commit SHA or trusted bundle manifest. Run the package validator, validator tests, workspace and relocation policy tests, six skill checks, command-copy comparison, and payload hashes. Candidate labeling as 2.7 does not prove release, installation, project adoption, provider enforcement, or live relocation.

## 3. Reconcile project contracts

Update project `AGENTS.md`, `TEAM.md`, protocol, TASK/role templates, command help, skill references, and migration policy through the normal protected workflow. Configure portable relocation policy: migration owner/route, control paths, target placement classes, executor fencing records, receipt retention, registry authority classes, and workspace integration.

Before enabling new workspace allocation, build one read-only physical inventory from authoritative Git worktree registration, application-managed attachments, configured external roots, legacy roots, and partial/unknown materializations. Counts are physical, not limited to TASK lease records. If inventory is incomplete or the project is at/above its hard cap, enter reuse-only mode and assign reconciliation ownership; adoption itself grants no cleanup authority.

Configure disjoint canonical workspace and evidence/artifact/message/output/log/tmp/cache roots. Existing overlap is retained and reconciled prospectively; no evidence/output root may receive a new worktree. Add deterministic materialization keys to active leases so retries, revisions, handoffs, and unchanged exact-candidate review reuse one compatible lease.

Create a compact evidence index for active TASKs. Reuse identical candidate/axis/command/environment/outcome keys and existing content hashes. Declare consumer, retention, recovery, owner, access boundary, and close trigger before creating a separate durable artifact; routine verification remains summary-only. Migration does not require bulk conversion or deletion of historical evidence.

Keep populated thread IDs, physical paths, credentials, transcripts, and hashes of private identifiers in ignored local state. Local mapping never grants assignment, identity, permission, epoch, or acceptance.

## 4. Preserve transfer semantics

`$r2team migrate <function> to <participant>` remains function/ownership transfer. Same-executor physical relocation uses the separate `r2team-relocate` skill. If participant, function owner, or executor ID changes, complete the existing transfer workflow first.

## 5. Introduce fencing prospectively

Existing work remains valid. At adoption, record a baseline per-executor fence keyed by repository/project plus executor, accepted epoch/record, source/target state, and custody class. Fencing is cooperative protocol fencing unless a later exact administrative receipt proves provider-enforced exclusion. Provider-enforced exclusion remains `NOT_PROVEN` by default.

Every writer-capable R2Team entry point re-reads accepted fencing state before publication. A stale, same-next-epoch sibling, wrong key, or unrelated causal parent is `WRITER_CONFLICT`.

## 6. Validate adoption without relocating

Use isolated fixtures to demonstrate branch-race serialization, offline stale-source rejection, partial-team custody, post-freeze cancellation, forward rollback, PM control-path restriction, in-flight helper rejection, unreachable-source blocking, activation-parent validation, retained-set rules, registry collision handling, and workspace custody checks.

Real chat creation/movement, registry remap, process stop, workspace movement/cleanup/archive, installed-skill replacement, provider revocation, merge, release, deployment, and live relocation remain `NOT_RUN` unless separately authorized and evidenced.

## 7. Publish the adoption checkpoint

The project PM publishes one accepted-main checkpoint with exact package provenance, updated contracts, baseline fences, validation evidence/limitations, remaining blockers, owner/review dates, and rollback/recovery route. Notify current executors through existing authoritative routes. Until provider read-back confirms the checkpoint, continue under the previous protocol.

Adoption merely makes relocation available. Any actual role/team relocation requires its own accepted TASK, migration ID, affected set, prepare/freeze/resume receipts, exact cutover, and completion decision.

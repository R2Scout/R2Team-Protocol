# R2Team 2.7 validation plan

## Provenance and structure

- Bind every result to exact base, candidate SHA/tree, branch, TASK revision, tracker, manifest, and package inventory.
- Confirm candidate-to-review-checkpoint changes only TASK metadata.
- Confirm required Markdown links/anchors/fences remain portable and public content is English-only.
- Confirm no machine-private path, physical thread ID, secret, transcript, or populated local registry enters the package.

## Deterministic behavioral fixtures

1. Same logical executor relocation preserves participant/executor/TASK/candidate identity while physical chat changes locally.
2. Changed participant/function/executor is blocked until existing ownership transfer is accepted.
3. Replacement writer is blocked before `READY_TO_RESUME`.
4. Old and target writers both active produces `WRITER_CONFLICT`.
5. Stale/equal writer epoch cannot reactivate a source chat.
6. Missing TASK checkpoint, candidate, provider route, source stop, target placement, access/tool preflight, or resume receipt blocks progress.
7. A local thread-registry entry cannot authorize resume.
8. Registry remap fixture writes only inside an isolated ignored root and requires read-back.
9. Role handoff references current TASK state without copying transcripts or local paths.
10. Whole-team resume follows recorded startup order and reports partial blocked roles without activating them.
11. Changed physical chat with the same executor does not rewrite TASK ownership.
12. Function transfer remains distinct from relocation.
13. Workspace reuse requires exact candidate/custody/containment/dependency evidence; otherwise retain/transfer/block or allocate separately.
14. Relocation failure does not authorize cleanup, process stop, archive, branch deletion, merge, or deployment.
15. Rollback is a higher-epoch forward publication; reset/stale registry/transcript replay is rejected.
16. Every resumed role has a receipt; team completion rejects unaccounted executors.
17. R2Team 2.6 package/project remains unchanged until explicit 2.7 adoption.
18. Live chat creation, host relocation, installed-skill replacement, and downstream adoption remain NOT_RUN.

## Static adversarial fixtures

- Hash-consistent package payload containing populated thread UUID or machine path is rejected.
- Hash-consistent instructions that auto-create chats, copy credentials/transcripts, or allow concurrent writers are rejected.
- Hash-consistent payload that changes `$r2team migrate <function> to <participant>` into relocation is rejected.
- Missing sixth skill, relocation templates, migration markers, or exact hashes are rejected.
- Explicit placeholders remain accepted.

## Fresh-package review

Create an isolated package from `package.json` plus `required_files` only. Run:

- `python scripts/validate_package.py`;
- all validator tests;
- all workspace and relocation policy tests;
- official `quick_validate.py` for all six skills;
- command-copy byte comparison;
- `git diff --check`.

Remove only author-owned temporary roots after exact containment checks. Never remove real worktrees, branches, caches, data, profiles, processes, containers, databases, or application-managed checkouts.

## Independent review

The independent reviewer materializes the exact candidate, replays writer-conflict/identity/registry/workspace/adversarial fixtures, verifies the TASK-only checkpoint and remote refs, and returns PASS/AMEND/BLOCKED. No prior verdict transfers to a changed candidate.

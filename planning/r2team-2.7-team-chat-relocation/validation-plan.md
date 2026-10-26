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
5. Stale/equal writer epoch cannot reactivate a source chat; two branches proposing the same next epoch cannot both become valid.
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
19. An offline stale source returning after target activation is blocked by the accepted per-executor causal fence at every writer-capable entry point.
20. One whole-team executor may remain target-active while another is stopped/blocked; aggregate `PARTIAL_BLOCKED` preserves both custody facts and a legal successor.
21. Cancellation after `FROZEN` and before activation cannot revive the source without an accepted successor and activation receipt.
22. Forward rollback after one or several activations advances each affected executor independently with a higher epoch and new causal receipts.
23. A PM control-path publication racing an old product/TASK publication accepts at most the causally valid successor and rejects the stale writer.
24. Stop acknowledgement is rejected while any publisher/helper is in flight or unaccounted.
25. An unreachable source without independently enforceable revocation cannot activate a target.
26. Duplicate activation receipt or a mismatched stop/cutover causal parent is rejected.
27. A retained executor inside the frozen affected set is rejected as ambiguous; retention is valid only after accepted removal before `FREEZE_PENDING`.
28. Registry remap collision or wrong-executor mapping is rejected while durable output exposes no private value or stable hash.
29. Workspace reuse with the correct candidate but wrong custody, host, dependency, or native-resource facts is rejected.
30. Every blocked/frozen model state has an explicit permitted recovery transition or terminal accounted disposition.
31. Null/numeric/text/collection freeze inputs fail closed for every publication class; exact boolean false/true retains only its declared behavior.
32. The complete legal fence state/custody matrix is enumerated; simultaneous ACTIVE placements, preflight while source ACTIVE, and custody disagreement are rejected.
33. Activation rejects cutover/accepted-commit disagreement, mapping/registry disagreement, and missing/stale preflight receipt edges; remote/manual absent/not-applicable evidence is exercised separately.
34. Every receipt type rejects orphan and wrong-type parents under an explicit accepted-root and affected-set context; target-preflight/disposition/outcome enums and rollback ranges are strict.
35. Completion rejects missing, duplicate, or extra executors and any executor without exactly one terminal receipt; one closed two-executor chain passes.
36. Remote/manual no-mapping accepts only no observation/no collision; contradictory observations and collisions fail closed.
37. Canonical path fixtures reject CR/LF/NUL, leading/trailing segment whitespace, dot segments, duplicate separators, and backslashes.

The pure model must assert both safety (never two accepted writers for one executor/TASK) and liveness/recoverability (no blocked or frozen state is a dead end without a terminal accounted disposition).

## Static adversarial fixtures

- Hash-consistent package payload containing populated thread UUID or machine path is rejected.
- Hash-consistent instructions that auto-create chats, copy credentials/transcripts, or allow concurrent writers are rejected.
- Hash-consistent payload that changes `$r2team migrate <function> to <participant>` into relocation is rejected.
- Hash-consistent receipt with a duplicate ID, stale/equal-conflicting epoch, missing causal parent, or mismatched accepted parent is rejected.
- Hash-consistent durable registry evidence containing a populated private value or stable hash is rejected.
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

## Minimum evidence by stage

| Stage | Minimum durable evidence |
| --- | --- |
| Prepare | Accepted migration ID/mode/authority; affected-executor manifest; exact TEAM/TASK/candidate refs; target placement class; per-executor current epoch/custody; workspace dispositions; blockers. |
| Source stop/freeze | Per-executor final checkpoint/tree; accepted stop mechanism and receipt; no unaccounted writer/helper publication; expected epoch and causal parent; narrow PM control-path allowance. |
| Target activation | Accepted cutover read-back; matching stop receipt; provider/tool/access preflight; local mapping read-back enum when applicable; workspace custody; activation receipt; new accepted epoch. |
| Partial team | Per-executor source/target state and epoch; resumed receipt or terminal blocked/cancelled/rollback disposition; owner/review date/next action; aggregate derived from records. |
| Forward rollback | Prior active epoch/receipt; new migration or rollback publication; higher per-executor epoch; new stop and activation receipts; no stale-writer revival. |
| Completion | Every affected executor accounted; all causal receipts accepted/read back; no unknown writer/custody state; remaining NOT_RUN axes and downstream-adoption gate. |

## Independent review

The independent reviewer materializes the exact candidate, replays writer-conflict/identity/registry/workspace/adversarial fixtures, verifies the TASK-only checkpoint and remote refs, and returns PASS/AMEND/BLOCKED. No prior verdict transfers to a changed candidate.

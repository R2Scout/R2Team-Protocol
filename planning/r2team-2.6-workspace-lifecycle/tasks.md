# Implementation tasks

These tasks are the accepted implementation route. Merge, release, installed-skill replacement, downstream adoption, and live cleanup remain separately gated.

## 1. Reconcile R2Team 2.6 scope

- Preserve the paused migration candidate without modifying it.
- Ship workspace lifecycle only in R2Team 2.6.
- Move team/chat relocation to a distinct R2Team 2.7 TASK and checkpoint.
- Record the lifecycle-only integration route and reject relocation content from the 2.6 candidate.
- Preserve the accepted 2.5 base and predecessor bytes.

## 2. Add protocol-level workspace lifecycle

- Add TASK, candidate, and workspace identity definitions.
- Add lease, allocation, review, transfer, closure, retention, and recovery rules.
- Add the two-axis terminal model.
- Add budget and disk-allocation gates.
- Keep acceptance and custody evidence separate.
- Add the protected merge-evidence gate and merge-triggered closure review.
- Require a fully evidenced `CLOSED`, `RETAINED_PROTECTED`, or `TRANSFERRED_TO_NEXT_TASK` lease record for every completed-stage lease; bare labels and all blocking/nonterminal records prevent administrative completion.

## 3. Update adoption templates

- Extend TASK-TEMPLATE with portable workspace policy, structured `workspace_exceptions`, derived summary state, and append-only `workspace_leases`, `candidate_dispositions`, `artifact_manifests`, and `close_receipts`; every lease retains its own closure owner, review date, retention, recovery, and receipt references.
- Extend TEAM with project budgets, placement classes/root aliases, disk thresholds, retention classes, closure methods, and lifecycle roles.
- Extend the local-registry template with physical path, size, resource, custody, and observation fields.
- Keep all populated physical paths and host-private values ignored.

## 4. Update role contracts

- PM: allocation budget, exception review, closure ownership, reconciliation.
- Dev: author-lane reuse and bounded parallel-lane exception.
- QA and Designer: exact-candidate ephemeral materialization and separate verdict/closure result.
- DevOps or integration: reusable integration lane and custody-safe close.
- COO and audit: read-only lifecycle reporting and explicit no-cleanup boundary.

## 5. Define command and skill behavior

- Specify workspace status, open, close, and doctor semantics.
- Add a separate packaged `r2team-workspace` skill as the operational entry point.
- Limit existing skills to routing and authority boundaries; do not add hidden workspace mutation to `r2team-work`.
- Require preflight and actual-result read-back.
- Keep status and doctor read-only.
- Prevent age, budget, or capacity from becoming delete authority.
- Define Codex-managed archive handling without shell removal.

## 6. Add migration guidance

- Define prospective 2.5-to-2.6 adoption.
- Preserve existing TASK validity.
- Introduce fields at the next material handoff or revision.
- Classify existing workspaces as legacy-retained until separate reconciliation.
- Keep downstream adoption project-local.

## 7. Extend package validation

- Require all new normative sections and template fields.
- Validate package manifest and payload hashes.
- Reject machine paths, thread IDs, secrets, and unsafe automatic-cleanup wording.
- Check template links remain portable.
- Check skills and command references remain consistent with protocol language.
- Require the packaged `r2team-workspace` skill and reject team/chat relocation content from the 2.6 payload.

## 8. Add behavioral fixtures

- Reuse on TASK revision without new allocation.
- Bounded parallel-lane exception.
- QA verdict succeeds while close is blocked.
- Dirty or ignored evidence produces RETAINED_PROTECTED.
- Codex-managed checkout requires application archive.
- Hard cap and disk threshold block allocation without deletion.
- Transfer preserves candidate and single-writer custody.
- Legacy project remains on 2.5 until accepted adoption.
- Merge checkpoint carries Git evidence or a sanitized hash-bound recovery manifest.
- Temporary material removal is rejected when ownership, dependency, evidence-export, or removal authority is missing.
- Administrative completion is rejected while a completed-stage lease remains silently ACTIVE.
- Hash-consistent adversarial payloads containing automatic force-delete, populated machine paths, actual thread IDs, populated prefixed/bare/cloud credential assignments, or bearer material are rejected while documented placeholders remain accepted.
- A deterministic pure-policy suite covers allocation bands, lease reuse, verdict/disposition separation, evidence durability, closure gates, transfer custody, Codex archive-only custody, and ACTIVE-lease completion rejection.

## 9. Run independent planning and package review

- Review normative coherence and backward compatibility.
- Validate exact package contents in a fresh clone or extracted bundle.
- Confirm no installed skills or downstream projects changed incidentally.
- Independently validate the separate `r2team-workspace` skill and its no-hidden-mutation boundary.
- Record NOT_RUN for live cleanup, disk recovery, project migration, and runtime behavior until separately authorized.

## 10. Publication sequence

- Obtain explicit implementation authority.
- Implement on the accepted isolated route.
- Run focused and full package validation.
- Obtain independent review of the exact candidate SHA/tree.
- Obtain explicit commit, push, PR, merge, release, and downstream-adoption gates as separate decisions.

# R2Team 2.7 implementation tasks

## 1. Review and freeze the planning contract

- Obtain System Architect review of identities, state machines, writer fencing, local registry, workspace custody, rollback, and separate skill boundary.
- Reconcile accepted findings before implementation.

## 2. Update protocol and templates

- Label the unreleased protocol/package payload as a 2.7 candidate while preserving separate release and downstream-adoption gates.
- Add relocation identity, bundle, per-executor causal fencing, recoverable source/target substates, partial-team custody, forward rollback, typed append-only receipts, and compatibility rules.
- Update AGENTS, Setup, TEAM, TASK, role contracts, commands, scenarios, findings, changelog, verification, and 2.6-to-2.7 migration guide.
- Add portable `TEAM_RELOCATION.md` and migration-bundle templates without live identifiers.

## 3. Add the relocation skill

- Package `skills/r2team-relocate/SKILL.md` as a sixth skill.
- Provide status, prepare role/team, resume role/team, cancellation/forward-rollback routing, and doctor contracts.
- Keep status/doctor read-only and prepare/resume stage-bounded.
- Preserve existing function-transfer and work-skill boundaries.
- Require compare-and-publish against accepted default-branch fencing state and identify cooperative versus provider-enforced fencing evidence.

## 4. Extend package validation

- Require the relocation skill and migration templates.
- Reject populated thread IDs, machine-private mappings or stable hashes, transcripts, secret material, implicit chat creation, writer overlap, causally invalid receipts, and 2.7 payloads that redefine function transfer.
- Require version/manifest/hash consistency and portable links.

## 5. Add deterministic policy fixtures

- Implement a pure relocation policy model for per-executor state transitions, causal epochs, identity preservation, partial-team custody, readiness/recovery gates, registry authority, workspace custody, and completion.
- Add safety assertions that two writers can never be valid and liveness assertions that every blocked/frozen state has a permitted recovery transition or terminal accounted disposition.
- Add the complete A6 adversarial set: same-epoch branch race, offline stale source, partial target activation, post-freeze cancellation, forward rollback, PM/old-writer publication race, in-flight helper, unreachable source, bad activation parent, retained-set ambiguity, registry collision/wrong executor, and correct-candidate/wrong-custody workspace reuse.

## 6. Verify package and migration

- Run structural validator, validator tests, relocation policy tests, and official validation for all six skills.
- Verify command copies remain byte-identical.
- Verify a fresh manifest-only package.
- Prove 2.6 payloads/projects remain unchanged until explicit adoption.
- Confirm no test performs live relocation, registry mutation outside isolated fixtures, process stop, workspace cleanup, skill installation, release, or adoption.

## 7. Independent review and PR

- Publish an exact implementation candidate and TASK-only review checkpoint.
- Obtain fresh independent review of the exact SHA/tree and adversarial cases.
- Address accepted findings with new immutable candidates.
- Prepare a PR only after PASS; stop before merge/release/install/adoption/live relocation.

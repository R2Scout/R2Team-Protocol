# R2Team 2.7 implementation tasks

## 1. Review and freeze the planning contract

- Obtain System Architect review of identities, state machines, writer fencing, local registry, workspace custody, rollback, and separate skill boundary.
- Reconcile accepted findings before implementation.

## 2. Update protocol and templates

- Set candidate protocol/package version to 2.7.
- Add relocation identity, bundle, writer-epoch, freeze/resume, rollback, evidence, and compatibility rules.
- Update AGENTS, Setup, TEAM, TASK, role contracts, commands, scenarios, findings, changelog, verification, and 2.6-to-2.7 migration guide.
- Add portable `TEAM_RELOCATION.md` and migration-bundle templates without live identifiers.

## 3. Add the relocation skill

- Package `skills/r2team-relocate/SKILL.md` as a sixth skill.
- Provide status, prepare role/team, resume role/team, and doctor contracts.
- Keep status/doctor read-only and prepare/resume stage-bounded.
- Preserve existing function-transfer and work-skill boundaries.

## 4. Extend package validation

- Require the relocation skill and migration templates.
- Reject populated thread IDs, machine-private mappings, transcripts, secret material, implicit chat creation, writer overlap, and 2.7 payloads that redefine function transfer.
- Require version/manifest/hash consistency and portable links.

## 5. Add deterministic policy fixtures

- Implement a pure relocation policy model for state transitions, identity preservation, writer epochs, readiness gates, registry authority, workspace custody, and completion.
- Add negative fixtures for replay, concurrent writers, missing evidence, wrong executor/TASK/candidate, and local mapping as authority.

## 6. Verify package and migration

- Run structural validator, validator tests, relocation policy tests, and official validation for all six skills.
- Verify command copies remain byte-identical.
- Verify a fresh manifest-only package.
- Prove 2.6 payloads/projects remain unchanged until explicit adoption.

## 7. Independent review and PR

- Publish an exact implementation candidate and TASK-only review checkpoint.
- Obtain fresh independent review of the exact SHA/tree and adversarial cases.
- Address accepted findings with new immutable candidates.
- Prepare a PR only after PASS; stop before merge/release/install/adoption/live relocation.

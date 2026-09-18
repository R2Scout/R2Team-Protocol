# R2Team 2.4 distribution verification

Prepared for protocol version 2.4 candidate on 2026-09-18. This is distribution evidence, not acceptance of a user project.

## Fresh local checks

- PASS: all 25 validator tests passed, including version, bootstrap, manifest-path, payload-hash, mandatory COO configuration, remote onboarding route and durable-baton guards.
- PASS: all four distribution skills pass the official skill-creator `quick_validate.py` using PyYAML 6.0.3.
- PASS: package structure, required payload hashes, local Markdown links, anchors and fences.
- PASS: public distribution Markdown is English-only.
- PASS: `templates/COMMANDS.md` and `skills/r2team/references/commands.md` are byte-identical.
- PASS: specialized CMMI setup is absent from the main package and maintained separately.
- PASS: `git diff --check` on the release candidate.
- PASS: targeted scan found no author-machine paths, known credential patterns, private-key blocks, or actual local thread UUIDs in the payload.

The exact commands and final outputs are captured during release preparation. Payload hashes cover required files; package.json is excluded from its own hash map.

## Candidate publication gate

Verify that `candidate/r2team-2.4` resolves to the approved candidate commit, then validate a fresh clone at that commit. Main merge, annotated `v2.4` tag and release remain `NOT_RUN` until separately authorized. Publication proves repository provenance, not live agent/provider behavior.

## Document-level scenarios

[SCENARIOS.md](SCENARIOS.md) covers setup, brownfield migration, team combinations, bounded local/remote help, material decisions, ownership transfer, exact-candidate QA, provider uncertainty, human-assisted steps, required COO capability with optional standalone/wake, and recovery without chat transcripts. These are reviewed contracts, not executed multi-agent simulations.

## NOT_RUN by this release

- Migration of a real 1.10 project or adoption by existing role chats.
- Live direct inter-chat delivery, remote participant wake, or scheduled heartbeat.
- Live end-to-end remote registration auto-activation and capacity release.
- Real GitHub/TFS item-to-PR lifecycle, provider adapter, or multi-repository rollout.
- Product implementation, database/infrastructure changes, deployment, or independent QA.
- Installation/replacement of skills on another machine.
- Automatic installation/execution of OpenSpec or Superpowers.

The package is self-contained for its protocol, templates, setup, migration prompt, and four R2Team instruction skills. Git/provider access, Python for validation, Codex, and approved external OpenSpec/Superpowers toolchains remain explicit dependencies.

# R2Team 2.6 distribution verification

Prepared for the protocol version 2.6 workspace-lifecycle candidate on 2026-10-25. This is distribution evidence, not acceptance of a user project, live cleanup authority, or downstream adoption.

## Fresh local checks

- PASS: all 42 validator tests passed, including hash-consistent adversarial destructive-instruction, populated-path, actual-thread-ID, GitHub/OpenAI/Azure/bearer/generic/bare/cloud-secret credential, placeholder, append-only lifecycle-history, version, manifest, workspace-skill, and relocation-exclusion guards.
- PASS: all 32 deterministic workspace-policy tests passed, covering state-specific terminal evidence, every blocking/nonterminal state, exact allocation-bound exceptions, strict boolean predicates, date/base validation and hard-gate non-bypass, lease reuse, capacity bands, verdict/disposition separation, evidence durability, closure gates, Codex archive-only custody, and transfer.
- PASS: all five distribution skills, including `r2team-workspace`, pass the official skill-creator `quick_validate.py` using PyYAML 6.0.3 in an isolated validation dependency directory.
- PASS: package structure, required payload hashes, local Markdown links, anchors and fences.
- PASS: a fresh isolated package copy built only from `package.json` plus `required_files` passed package validation, all 42 validator tests, all 32 workspace-policy tests, and all five skill-format checks.
- PASS: public distribution Markdown is English-only.
- PASS: `templates/COMMANDS.md` and `skills/r2team/references/commands.md` are byte-identical.
- PASS: specialized CMMI setup is absent from the main package and maintained separately.
- PASS: `git diff --check` on the implementation working candidate.
- PASS: targeted scan found no author-machine paths, known credential patterns, private-key blocks, or actual local thread UUIDs in the payload.

The exact commands and final outputs are captured during release preparation. Payload hashes cover required files; package.json is excluded from its own hash map.

## Candidate publication gate

Bind the final implementation to an exact commit/tree, push the authorized branch, then repeat validation from a fresh isolated package and obtain independent review of that exact candidate. Main merge, annotated `v2.6` tag, release, installed-skill replacement, downstream adoption, and live cleanup remain `NOT_RUN` until separately authorized. Publication proves repository provenance, not live agent/provider behavior.

## Document-level scenarios

[SCENARIOS.md](SCENARIOS.md) covers setup, brownfield migration, team combinations, bounded local/remote help, material decisions, ownership transfer, exact-candidate QA, provider uncertainty, human-assisted steps, required COO capability with optional standalone/wake, and recovery without chat transcripts. These are reviewed contracts, not executed multi-agent simulations.

The 2.6 additions cover lease reuse, budget/capacity blocks, ephemeral review, candidate-verdict/closure separation, durable merge evidence, retained/transfer/blocking dispositions, Codex-managed custody, temporary-material removal gates, append-only lease/candidate history, privacy/safety adversarial payloads, and relocation exclusion. These deterministic policy and validator fixtures do not execute live cleanup; consuming-agent execution remains `NOT_RUN`.

## NOT_RUN by this release

- Migration of a real 1.10 project or adoption by existing role chats.
- Live direct inter-chat delivery, remote participant wake, or scheduled heartbeat.
- Live end-to-end remote registration auto-activation and capacity release.
- Live remote queue-discovery and Task Issuer/Project PM question-response regression scenarios, including a new attempt by the originally affected executor.
- Real GitHub/TFS item-to-PR lifecycle, provider adapter, or multi-repository rollout.
- Product implementation, database/infrastructure changes, deployment, or independent QA.
- Installation/replacement of skills on another machine.
- Cleanup, removal, relocation, archive, process stop, branch deletion, or disk recovery in a real project.
- Downstream 2.5-to-2.6 project adoption and legacy-workspace reconciliation.
- Automatic installation/execution of OpenSpec or Superpowers.

The package is self-contained for its protocol, templates, setup, migration prompt, and five R2Team instruction skills. Git/provider access, Python for validation, Codex, and approved external OpenSpec/Superpowers toolchains remain explicit dependencies.

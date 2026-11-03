# R2Team 2.7 distribution verification

Prepared for the protocol version 2.7 team/chat-relocation and bounded-materialization release on 2026-11-03. This is distribution evidence, not acceptance of a user project, live relocation/cleanup authority, provider-enforced exclusion, or downstream adoption.

## Fresh local checks

- PASS: all 55 validator tests passed, including hash-consistent adversarial destructive-instruction, populated-path, actual-thread-ID/private-route-hash, automatic chat creation/transcript copy, concurrent writer, function-transfer/relocation-identity redefinition, GitHub/OpenAI/Azure/bearer/generic/bare/cloud-secret credential, version, manifest, workspace-skill, relocation-skill/template/command, bounded workspace/evidence markers, and hidden-mutation guards.
- PASS: all 42 deterministic workspace-policy tests passed, covering state-specific terminal evidence, every blocking/nonterminal state, exact allocation-bound exceptions, strict boolean predicates, date/base validation and hard-gate non-bypass, complete-inventory and root-separation blocking, compatible-reuse rejection under root/key conflict, clean exact reuse under hard-cap/reuse-only conditions, materialization-key reuse/conflict, evidence-key reuse, summary-only routine results, durable-artifact lifecycle metadata, capacity bands, verdict/disposition separation, evidence durability, closure gates, Codex archive-only custody, and transfer.
- PASS: all 73 deterministic relocation-policy tests passed, covering strict non-boolean epochs across every authority API, the explicit single-writer fence matrix, exact typed `SOURCE_STOPPED` proof across stop/activation/graph paths, authoritative included PASS-preflight proof, cutover/registry/preflight binding, external-root PREPARE and role/team lineage, exact team FREEZE accounting plus strict `SOURCE_STOP < FREEZE < TARGET_PREFLIGHT < ACTIVATION` time order, append-only later generations with logical-event deduplication, typed terminal BLOCKED/cancellation/forward rollback, one shared unique latest causal-stage resolver for receipt completion and all aggregate states, exhaustive record-to-stage/disposition/resulting-state/custody matching, mandatory minimum receipt context for FROZEN/READY/RESUMING, strict dates/timestamps/reference elements and canonical paths, strict freeze booleans, local/remote registry collision handling, workspace/affected-set typing, and valid mixed two-executor completion.
- PASS: all six distribution skills, including `r2team-workspace` and `r2team-relocate`, pass the official skill-creator `quick_validate.py` using PyYAML 6.0.3 in an isolated validation dependency directory.
- PASS: package structure, required payload hashes, local Markdown links, anchors and fences.
- PASS: a fresh isolated package copy built only from `package.json` plus `required_files` passed package validation, all 55 validator tests, all 42 workspace-policy tests, all 73 relocation-policy tests, and all six skill-format checks.
- PASS: public distribution Markdown is English-only.
- PASS: `templates/COMMANDS.md` and `skills/r2team/references/commands.md` are byte-identical.
- PASS: specialized CMMI setup is absent from the main package and maintained separately.
- PASS: `git diff --check` on the implementation working candidate.
- PASS: targeted scan found no author-machine paths, known credential patterns, private-key blocks, or actual local thread UUIDs in the payload.

The exact commands and final outputs are captured during release preparation. Payload hashes cover required files; package.json is excluded from its own hash map.

## Release publication gate

Bind the release payload to an exact commit/tree and complete the protected merge before creating the annotated `v2.7` tag. The tag and GitHub Release must resolve to that accepted default-branch commit and pass provider read-back. Installed-skill replacement, downstream adoption, live relocation, and live cleanup remain `NOT_RUN` until separately authorized. Publication proves repository provenance, not live agent/provider behavior.

## Document-level scenarios

[SCENARIOS.md](SCENARIOS.md) covers setup, brownfield migration, team combinations, bounded local/remote help, material decisions, ownership transfer, exact-candidate QA, provider uncertainty, human-assisted steps, required COO capability with optional standalone/wake, and recovery without chat transcripts. These are reviewed contracts, not executed multi-agent simulations.

The 2.7 additions cover per-executor causal fences, stop/activation proof, typed receipts, same-epoch conflicts, retained executors, partial custody, cancellation, forward rollback, privacy-safe registry evidence, complete physical workspace inventory, deterministic materialization and evidence keys, disjoint workspace/evidence roots, summary-only routine results, workspace/candidate separation, command/role boundaries, and prospective adoption. Deterministic policy and validator fixtures do not execute a live relocation, provider revocation, chat creation, workspace movement, or cleanup; consuming-agent execution remains `NOT_RUN`.

## NOT_RUN by this release

- Migration of a real 1.10 project or adoption by existing role chats.
- Live direct inter-chat delivery, remote participant wake, or scheduled heartbeat.
- Live end-to-end remote registration auto-activation and capacity release.
- Live remote queue-discovery and Task Issuer/Project PM question-response regression scenarios, including a new attempt by the originally affected executor.
- Real GitHub/TFS item-to-PR lifecycle, provider adapter, or multi-repository rollout.
- Product implementation, database/infrastructure changes, deployment, or independent QA.
- Installation/replacement of skills on another machine.
- Cleanup, removal, live relocation, archive, process stop, branch deletion, provider revocation, or disk recovery in a real project.
- Downstream 2.6-to-2.7 project adoption, executor cutover, and legacy-workspace reconciliation.
- Automatic installation/execution of OpenSpec or Superpowers.

The package is self-contained for its protocol, templates, setup, migration prompt, and six R2Team instruction skills. Git/provider access, Python for validation, Codex, and approved external OpenSpec/Superpowers toolchains remain explicit dependencies.

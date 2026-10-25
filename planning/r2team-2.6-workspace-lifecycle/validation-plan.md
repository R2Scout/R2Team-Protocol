# Validation plan

## Planning validation

- Confirm every artifact references the same TASK identity, base SHA, branch, Issue, scope, and publication boundary.
- Confirm all Markdown is English-only and repository-relative.
- Confirm no physical path, thread ID, credential, or machine-private route enters the planned Git content.
- Confirm the paused predecessor candidate is unchanged.
- Confirm the isolated planning worktree is based exactly on a5adba57d133e58360347ac2c709e88433061e90.
- Confirm 2.6 contains workspace lifecycle only and team/chat relocation remains assigned to a distinct 2.7 TASK and checkpoint.
- Confirm operational workspace behavior is assigned to a separate `r2team-workspace` skill with no hidden mutation in `r2team-work`.

## Static package validation

During authorized implementation:

- update package manifest entries and payload SHA-256 values;
- run scripts/validate_package.py;
- run scripts/test_validate_package.py;
- run scripts/test_workspace_policy.py;
- validate every R2Team skill format;
- verify exactly one active entry point per packaged skill;
- verify all template links stay within the portable package;
- reject unsafe phrases that imply automatic deletion or cleanup authority.
- reject populated machine-private paths, actual local thread IDs, credential-like material, and contradictory destructive instructions even after payload hashes are recalculated.

## Contract consistency checks

- CODEX_TEAM_PROTOCOL defines the normative model.
- AGENTS summarizes it without changing authority.
- Setup and migration describe adoption and legacy handling.
- TEAM and TASK fields implement the portable contract.
- Role files assign responsibilities consistently.
- Commands and skills implement only their stated authority.
- The package contains one separate `r2team-workspace` entry point; existing skills provide routing and boundaries only.
- No 2.6 protocol, template, command, skill, or fixture introduces team/chat relocation behavior.
- Local registry contains physical mappings and remains ignored.

## Required behavioral fixtures

1. A TASK revision reuses its current author lease.
2. A changed exact base with an approved exception creates a bounded lease.
3. A fourth workspace without an exception is ALLOCATION_BLOCKED.
4. A hard-cap breach freezes new placement and leaves existing work untouched.
5. Low disk freezes allocation without starting cleanup.
6. QA publishes PASS or FAIL before close; close failure preserves the verdict.
7. Dirty or unknown ignored content prevents CLOSED.
8. RETAINED_PROTECTED records owner, recovery reference, and review date.
9. TRANSFERRED_TO_NEXT_TASK records old HEAD/tree, next owner, and lease.
10. Codex-managed custody accepts application archive only.
11. Branch disposition never deletes a ref.
12. Another machine can recover the durable candidate and evidence without the physical path.
13. A 2.5 project remains unchanged until explicit local adoption.
14. An accepted merge records durable Git evidence or a sanitized hash-bound durable recovery manifest.
15. Administrative completion fails when a completed-stage lease remains silently ACTIVE.
16. Temporary material is removed only when evidence export, exclusive ownership, dependency, shared-cache, retained-input, and explicit-authority checks all pass.
17. A failed removal gate produces retained, transferred, or blocked state with an owner and review date.

## Safety checks

- No test removes a real user worktree, branch, data directory, cache, process, container, database, or application-managed checkout.
- Filesystem fixtures use isolated temporary roots.
- Destructive command examples are absent from templates and skills.
- Close tests require explicit owned fixture identity and verify target containment.
- Failure paths preserve evidence and return BLOCKED_DIRTY or RETAINED_PROTECTED.

## Fresh-package review

- Build or extract the exact package in a new isolated directory.
- Verify manifest hashes and expected file inventory.
- Verify the package contains and validates `r2team-workspace`.
- Verify the package does not contain team/chat relocation payloads or migration commands.
- Validate setup and migration links.
- Confirm existing 2.5 TASKs remain readable.
- Confirm new lifecycle fields are introduced only after accepted adoption.
- Confirm installed user skills are not modified by package validation.

## Independent review

An independent reviewer verifies the exact candidate SHA/tree against this TASK and normative deltas. Structural validation, author review, and downstream project experience do not substitute for independent protocol review.

## Explicit NOT_RUN axes

The following remain NOT_RUN until separately authorized:

- cleanup of existing project worktrees;
- branch deletion;
- process or runtime shutdown;
- data, profile, cache, or evidence relocation;
- live Codex-managed archive;
- downstream project migration;
- installed-skill replacement;
- merge, release, or public adoption.

## Publication gates

1. Planning artifacts accepted.
2. Minimum recoverable checkpoint explicitly authorized.
3. Implementation explicitly authorized.
4. Exact candidate validation complete.
5. Independent review complete.
6. Commit and push authorized.
7. PR and merge authorized.
8. Release authorized.
9. Each downstream project adopts independently.

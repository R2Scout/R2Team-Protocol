# Maintaining the R2Team distribution

This repository contains protocol, template and skill sources, not an adopted product project. TEAM and ROLE files under templates are examples, not real assignments. Reading them does not start setup, create chats/participants or enable automation.

- Keep package.json, protocol, templates and skills consistent.
- Public repository content must be English-only.
- Use skill-creator for skill changes and its format validator when available; format checks are not behavioral tests.
- Test Python validator changes with fixtures that never perform external Git/provider operations; run `scripts/test_validate_package.py`, `scripts/test_workspace_policy.py` and `scripts/test_relocation_policy.py` for lifecycle/relocation changes.
- Refresh payload SHA-256 entries in package.json after edits, then run scripts/validate_package.py and scripts/test_validate_package.py.
- Verify links and template portability: template links remain within templates. Isolated skills use target-project instructions and trusted package sources, not author machine paths.
- Never ship credentials, .codex-local, personal thread IDs or hashes of them, private paths, transcripts or runtime state. Commit/push/release only when instructed by the user.
- Keep relocation mutation in `r2team-relocate`; preserve `$r2team migrate <function> to <participant>` as function transfer and describe fencing as cooperative unless provider enforcement is independently evidenced.
- Editing the distribution must not incidentally change live projects or user-installed skills.

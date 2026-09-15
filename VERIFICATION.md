# R2Team 2.0 — Release verification

Prepared: 2026-09-15. This is evidence for the distribution, not acceptance of any user project.

## Executed

- Package validator tests: 17/17 passed. Version-2.0 fixtures first produced five expected failures against the previous validator; the version change then passed the suite.
- Official skill-creator quick_validate.py: all four skills passed. The validator used Python 3.12 and PyYAML 6.0.3 from an isolated temporary dependency directory; the shipped package validator itself uses only the Python standard library.
- All installed skill payload instructions/help are English. The distribution's English help at templates/COMMANDS.md and skills/r2team/references/commands.md is identical; retain that equality when publishing updates.
- Targeted prepublication scan found no author machine paths, named private project paths, known GitHub credential patterns, private-key blocks or actual local thread UUIDs in the payload. This is not a guarantee against every possible secret pattern.

## Release checks

Run on the exact tree to publish:

```text
python scripts/validate_package.py
python -B scripts/test_validate_package.py
git diff --cached --check
```

The manifest fixes file paths and SHA-256 for the payload; package.json is excluded from its own hash map. For Git distribution record the actual commit SHA. For an offline bundle also verify package.json against a trusted independently supplied hash.

Check public visibility, main/tag commit equality and installation instructions after publication. A successful push is provenance, not a live agent acceptance test.

## Not executed

- Product implementation, migrations of existing user projects, deployment or database changes.
- Live registration, remote human/team handoff, direct wake or heartbeat.
- Real GitHub/TFS task-to-PR lifecycle or multi-repository SDK rollout.
- Installation/upgrades on another participant's machine or replacement of existing user-installed R2Team 1.20 skills.
- Automatic OpenSpec/Superpowers installation or execution against a product.

The package is self-contained for its own protocol/templates/skills. Codex, Git/provider access, Python for validation, and approved external OpenSpec/Superpowers toolchains remain explicit dependencies. Follow SCENARIOS.md in the target project's authorized scope before declaring that team's workflow validated.

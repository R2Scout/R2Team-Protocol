# R2Team Protocol 2.9

Git-first teamwork for one person, local role chats, remote participants and hybrids. PM is the only mandatory coordinating function. GitHub and generic Azure DevOps Server/TFS Git providers are supported; specialized process profiles are maintained separately.

## Current release

R2Team 2.9 clarifies Git worktree directory formation and preserves [resource lifetime and readable Git worktree names](templates/RESOURCE_LIFETIME.md). It distinguishes persistent anchors, task-scoped resources, and ephemeral uses independently of dev/qa/build/release purpose. It takes effect in each project through explicit adoption; the historical v2.8 and v2.7 releases are unchanged.

Protocol version **2.9**. The version is the sole release identifier: the major number identifies the protocol generation and the minor number increments for each published protocol revision. A protocol release does not imply downstream installation or project adoption.

**OpenSpec stores the product contract. TASK stores recoverable execution state. Direct conversation supports transient coordination.**

Bounded requests inside an existing task need no additional Issue, PR, MSG or role report. Ownership handoff and material outcomes remain durable regardless of where the executor runs. Read [the communication policy](templates/OPERATING_COMMUNICATION.md).

## Start and references

1. Obtain the public `v2.9` release and verify its full commit, or use an approved bundle with a trusted manifest hash. Do not silently substitute `main/latest`.
2. Verify the payload and local links with `python scripts/validate_package.py`, `python -B scripts/test_validate_package.py`, `python -B scripts/test_workspace_policy.py`, `python -B scripts/test_relocation_policy.py`, and `python -B scripts/test_resource_lifetime.py`.
3. Read [START.md](START.md). Choose new, migrate, team, join, resume or audit.
4. Install procedure skills separately using [SKILL-INSTALL.md](SKILL-INSTALL.md) only with machine-owner approval. Updating this repository does not update installed copies or adopted projects.

| Document | Purpose |
| --- | --- |
| [R2Team Master](R2TEAM_MASTER.md) | Persistent bootstrap, setup/team orchestration and provider/Git consultant |
| [Protocol](templates/CODEX_TEAM_PROTOCOL.md) | Authority, team models, lifecycle, examples and gates |
| [Communication policy](templates/OPERATING_COMMUNICATION.md) | Direct exchanges, OpenSpec boundary and checkpoints |
| [Setup](templates/Setup.md) | Guided new/existing project and team lifecycle |
| [Commands](templates/COMMANDS.md) | English skill and document entry help |
| [Project instructions](templates/AGENTS.md) / [TEAM](templates/TEAM.md) | Adopted project rules and identities |
| [Skills](templates/SKILLS.md) | OpenSpec and Superpowers routing |
| [Provider guide](templates/TRACKER_GUIDE.md) | GitHub and generic Server/TFS Git |
| [Migration](templates/MIGRATE_TO_2.9.md) | Prospective 2.8-to-2.9 adoption, with older-version reconciliation preserving existing work and custody |
| [Git worktree directories](templates/GIT_WORKTREE_DIRECTORIES.md) | Approved roots, ordinary folder names, reuse and application custody |
| [PM update prompt](templates/PM_PROTOCOL_UPDATE.md) | Portable prompt for adopting this release |
| [Relocation bundle](templates/TEAM_RELOCATION.md) | Portable migration, per-executor fence and causal receipt schema |
| [Multiple repositories](templates/MULTI_REPO.md) | Scoped SDK/API coordination |
| [Scenarios](SCENARIOS.md) / [Verification](VERIFICATION.md) | Expected behavior and verification limits |
| [Sources](SOURCES.md) / [2.9 findings](FINDINGS-2.7.md) / [Change history](CHANGELOG.md) | Rationale, generalized findings and provenance |

The six instruction skills are r2team, r2team-work, r2team-workspace, r2team-relocate, r2team-coo and r2team-audit. Workspace lifecycle and relocation have separate entry points so ordinary TASK execution never hides allocation, closure, freeze, registry remap, or resume. Relocation uses per-executor causal cooperative fencing; provider-enforced exclusion remains unproven without a separate administrative receipt. Every active participant configures one COO capability, internal by default; a separate COO chat and heartbeat are optional. The skills are not an autonomous service, do not grant tool permissions and do not enable heartbeat. Follow current project instructions; an installed skill never silently migrates an older project.

No tracker adapter, guaranteed direct transport or live provider test is implied by document validation. Preserve unpublished work and verify exact refs before handoff.

# R2Team Protocol 2.4

Git-first teamwork for one person, local role chats, remote participants and hybrids. PM is the only mandatory coordinating function. GitHub and generic Azure DevOps Server/TFS Git providers are supported; specialized process profiles are maintained separately.

## Current candidate

Protocol version **2.4**. The version is the sole release identifier: the major number identifies the protocol generation and the minor number increments for each published protocol revision.

**OpenSpec stores the product contract. TASK stores recoverable execution state. Direct conversation supports transient coordination.**

Bounded requests inside an existing task need no additional Issue, PR, MSG or role report. Ownership handoff and material outcomes remain durable regardless of where the executor runs. Read [the communication policy](templates/OPERATING_COMMUNICATION.md).

## Start and references

1. Obtain the approved `candidate/r2team-2.4` full commit or use an approved bundle with a trusted manifest hash. No `v2.4` release tag is claimed by this candidate; do not silently substitute `main/latest`.
2. Verify the payload and local links with `python scripts/validate_package.py` and `python -B scripts/test_validate_package.py`.
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
| [Migration](templates/MIGRATE_TO_2.4.md) | Explicit 2.3 cutover preserving existing work |
| [Multiple repositories](templates/MULTI_REPO.md) | Scoped SDK/API coordination |
| [Scenarios](SCENARIOS.md) / [Verification](VERIFICATION.md) | Expected behavior and verification limits |
| [Sources](SOURCES.md) / [2.4 findings](FINDINGS-2.4.md) / [Change history](CHANGELOG.md) | Rationale, generalized findings and provenance |

The four instruction skills are r2team, r2team-work, r2team-coo and r2team-audit. Every active participant configures one COO capability, internal by default; a separate COO chat and heartbeat are optional. The skills are not an autonomous service, do not grant tool permissions and do not enable heartbeat. Follow current project instructions; an installed skill never silently migrates an older project.

No tracker adapter, guaranteed direct transport or live provider test is implied by document validation. Preserve unpublished work and verify exact refs before handoff.

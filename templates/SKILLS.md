# OpenSpec and Superpowers — R2Team 2.3 integration

This is required routing by work, not a declaration that all skills are installed. Do not invoke every workflow for a minor task. Read the complete selected SKILL.md before acting. Missing required skills need an agreed installation or explicit equivalent.

## 1. Installation and verification

### R2Team procedure skills

The package supplies r2team (lifecycle), r2team-work (start/task/discussion), r2team-coo (update/check) and r2team-audit (read-only). See [COMMANDS.md](COMMANDS.md) and the trusted package's root SKILL-INSTALL.md.

Verify source, installation and discovery on each machine. Skills do not replace OpenSpec/Superpowers, store TEAM or enable heartbeat. Confirm compatibility before using them in a project with a different protocol. Installation is not migration.

### Read-only inventory

1. Check Node, openspec --version and the actual executable when several exist.
2. Check Codex App/CLI and available project .agents/skills, user and plugin scopes without scanning the entire home directory.
3. Read existing OpenSpec config, instructions, custom skills and active changes.
4. Compare versions/refs with TEAM; do not silently upgrade to latest.
5. Inspect openspec init --help and openspec validate --help for the chosen version.

CLI, instruction skills and openspec/ content are different components. PM setup needs coverage of the seven workflows below; other executors need their functions' workflows. Do not require archive rights/skills from a QA-only executor forbidden to archive.

### OpenSpec CLI

See [official installation](https://github.com/Fission-AI/OpenSpec/blob/main/docs/installation.md). Original package preparation checked CLI 1.13.0 and documentation requiring Node >=20.19.0. This is a historical baseline, not a ban on future upgrades.

After selecting version and approving global installation:

```text
npm install -g @fission-ai/openspec@1.13.0
openspec --version
```

Reading this file does not execute commands. Show package manager and installation scope first. Missing/old Node, missing installer, admin requirements or PATH problems require resolution; do not silently modify shell profiles.

### Init and workflow updates

Before init, verify exact root and existing legacy commands/marker blocks, including targeted opsx-*.md user prompt checks where relevant. Documented init cleanup can remove legacy files without another question; show affected files, preserve approved backups and obtain confirmation.

After authorization:

```text
openspec init --tools codex
```

Do not use --force to bypass conflicts. Before openspec update compare generated files, customizations and selected version. Use actual CLI profile selection if expanded workflows such as verify are missing; configuration can be global, so verify scope and do not change other projects silently.

After init/update:
- Preserve actual generated skill/command/config paths and output.
- Verify discovery in the target Codex; restart only when needed.
- A skills-only integration need not expose slash commands.
- Use invocation names from installed files, not guessed punctuation.
- Verify openspec context --json, selected root and any store.
- Run list/specs/status and applicable validation; empty specs do not mean full coverage.

Use CLI scaffolding through the selected workflow, not hand-created openspec/changes directories or invented schema. Existing selected standalone stores retain their exact ID/flags on supported commands; do not add a new store unnecessarily.

### Superpowers

See [Superpowers](https://github.com/obra/superpowers). Verify the installation route available in the participant's current Codex. Plugin or skill installation needs owner approval; do not execute another product's plugin commands as shell commands.

When plugins are unavailable or a smaller set is desired, install approved skills/<name> folders from a trusted upstream ref with their required references/scripts. Avoid duplicate plugin/user/project copies.

A full installation can be used selectively. The quality core is TDD, systematic-debugging and verification-before-completion. Record actual version/ref and installation method in TEAM; if only a plugin version is available, record it honestly rather than inventing a commit.

## 2. OpenSpec workflow map

| Skill | Trigger/functions | Output or exit condition |
| --- | --- | --- |
| openspec-explore | PM/Brain/Designer/Dev clarify an idea, MVP or code | Findings/questions; writing only with required approval; no implementation |
| openspec-propose | Authorized planner proposes a new change | Schema artifacts from status/instructions; stop before apply when the installed skill requires a new request |
| openspec-update-change | Reconcile existing planning after decisions | Existing planning artifacts within approved scope, not product code or invented prerequisites |
| openspec-apply-change | Assigned implementation after approval | Code/tests/docs and task progress; stop on missing artifacts or conflicting scope |
| openspec-verify-change | QA/reviewer/PM before acceptance | Completeness/correctness/coherence, evidence and limits; analysis does not replace tests |
| openspec-sync-specs | Assigned owner prepares accepted behavior for integration | Semantic delta-to-spec merge in the task branch and validation, without premature archive |
| openspec-archive-change | Authorized owner after the complete scope | Completion/sync checks and archive; incomplete/skipped work is not automatically accepted |

Finalization order is: verify implementation against the change; sync every declared delta into accepted specs; verify semantic equivalence; archive; publish accepted specs/archive/TASK; then close the provider item. A schema-declared conditional artifact may legitimately be absent. CLI validation or artifact count does not prove specification completeness.

Version-specific installed instructions govern exact operations and gates. Read-only examples, using actual change names and supported flags:

```text
openspec context --json
openspec list --json
openspec list --specs
openspec status --change <name> --json
openspec instructions apply --change <name> --json
openspec validate --all --strict --no-interactive
```

Validate checks structure, not product correctness. Automation does not bypass approval. Requirement changes update TASK revision and relevant artifacts, rather than forcing apply to fit an unapproved scope.

## 3. Superpowers routing

Verify actual names/availability in the pinned installation. These skills do not create another work queue or independent mandatory plan.

| Skill | Use | Boundary |
| --- | --- | --- |
| using-superpowers | Workflow selection if installed | Routing, not authority |
| brainstorming | Unclear idea/design | Connect outcomes to OpenSpec; avoid competing approval tracks |
| writing-plans | Detailed verifiable steps | One canonical plan: change tasks.md or TASK; reconcile any required extra artifact explicitly |
| executing-plans | Execute an accepted plan | Preserve apply/schema and human gates |
| subagent-driven-development | Parent with authorized helpers | Bounded work and review; parent owns TASK |
| dispatching-parallel-agents | Independent authorized subtasks | Coordinate shared paths/environments |
| using-git-worktrees | Parallel independent changes | Does not isolate shared databases, ports or cloud resources |
| test-driven-development | Behavior implementation/fixes | Red-green-refactor; agreed exceptions only |
| systematic-debugging | Bugs, failures, unexpected behavior | Cause/evidence before an authorized fix |
| requesting-code-review | Ready candidate | Scope/spec/quality review, not merge permission |
| receiving-code-review | Review findings | Validate the finding, respect scope, fix and recheck |
| verification-before-completion | All completion claims | Fresh actual checks, exact version and NOT_RUN |
| finishing-a-development-branch | Verified branch completion | Authorized merge/cleanup; preserve active state |
| writing-skills | Explicit skill creation/change | Not a mandatory feature stage |

If a plugin imposes conflicting steps, resolve the single plan/source and approval boundaries before execution. The protocol does not silently cancel skill instructions.

## 4. Practical routing

- Greenfield: explore -> propose -> approve -> apply/TDD -> verify/tests -> sync/docs -> merge -> archive after complete scope.
- Brownfield: existing documents as evidence, short coverage map and the next real change; no mass speculative legacy import.
- Fix accepted behavior: TASK + debugging + TDD + verification; a new OpenSpec change only when the contract changes.
- Add a participant: TEAM/join and skill inventory, not a fictitious product change.
- Clarification: [interaction](CODEX_TEAM_PROTOCOL.md#interaction); explore/brainstorm only for real uncertainty; update planning after approved decisions. A question alone invokes neither apply nor a new plan/change.
- Human guidance: steps and evidence; distinguish human acceptance from automated tests. Skills do not grant configuration/secret/deployment rights.
- QA-only: assigned read/verify/tests, not patch/apply.
- DevOps: build/runtime/rollback verification and debugging; apply only for an assigned infrastructure change.

## 5. Evidence of actual use

Setup records needed workflows, version/ref/method and discovery per executor in TEAM. The first real TASK records workflow/scope, artifacts/commands and actual outcomes, approvals/stops/NOT_RUN, and links to tests/specs/checkpoint.

No skill report per step. SKILLS.md or a passing validator is not evidence that a workflow ran. Block only the affected step; independent safe work may continue.

OpenSpec manages the specification lifecycle; Superpowers supports execution and verification. Neither replaces ownership, publication or real checks.

## Product contract versus operational work

Apply [OPERATING_COMMUNICATION.md](OPERATING_COMMUNICATION.md). OpenSpec stores approved behavior, acceptance and significant change design, not chat routing/test-run status. Its tasks.md maps implementation steps, not each helper request. Authorized direct exchanges can be transient; TASK preserves material continuation state.

Fixing a violation of an existing requirement needs code/tests/evidence, not a rewritten requirement. Preserve skill approval gates and do not create a change merely to send a question or delegate a bounded check.

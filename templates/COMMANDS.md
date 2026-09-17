# R2Team 2.3 — Command Help

Open project `R2TEAM_MASTER.md` in the persistent local `R2Team Master - <project>` task for bootstrap, Project Charter, setup orchestration, provider/Git troubleshooting, team lifecycle changes or protocol consultation. Master routes actual procedures to the skills below and does not replace PM authority.

These are Codex skill prompts, not shell commands. Install the four skills first. Natural-language requests are supported; arguments describe intent and never grant permissions. Help is always shown in English. For task conversations, use the participant's preferred language.

## Quick reference

| Command | Purpose | Boundary |
| --- | --- | --- |
| `$r2team help [command]` | Show all help or one command | Read-only |
| `$r2team add Ken roles QA,DevOps remote` | Prepare participant, roles and invitation | PM or authorized delegate |
| `$r2team register repo <Git-URL> participant ken [executor ken-ops]` | Join an existing project on this machine | Verify PM assignment and actual identity |
| `$r2team connect QA [executor ken-qa]` | Attach this chat to an assigned executor/function | Cross-check; no implicit takeover |
| `$r2team migrate DevOps to Ken` | Transfer a function and unfinished work | Not a protocol version upgrade |
| `$r2team disconnect Ken` | Safely transfer work and deactivate membership | No account, repository or history deletion |
| `$r2team-work start [TASK-ID]` | Begin/resume one authorized next action | Current assignment, scope and intake required |
| `$r2team-work task TASK-ID` | Inspect task state and next steps | Read-only; does not execute |
| `$r2team-work task TASK-ID discuss Designer Dev` | Organize a scoped discussion in the existing Issue/PR | Tracker-write permission; no reassignment |
| `$r2team-coo update` | Inspect exact new events in configured scope | No writes or notifications |
| `$r2team-coo check` | Inspect updates and perform already-authorized local wake | Designated dispatcher only; no schedule changes |
| `$r2team-audit` | Check readiness and recoverability | Read-only; fixes require a separate request |

Each skill accepts `help`. Bare lifecycle/work/COO invocations show help rather than taking action; bare audit performs the read-only audit. Unknown commands do nothing and show the relevant syntax. Ask only for missing information that cannot be safely resolved from the configured project.

## Start a project

```text
$r2team Start a new project using START.md from <verified-package-path>.
Confirm the target directory and guide me through setup. This chat will be PM.
```

This routes to Setup mode `new`. A new project is not expected to have TEAM/TASK yet. The wizard confirms the initial PM and creates the agreed configuration. For an existing MVP or older protocol use Setup mode `migrate`; do not initialize a new project over its files.

The full template package is needed for setup. Installing SKILL.md alone does not copy project templates. Provide a verified package path or repository URL and full commit SHA. The distribution is https://github.com/R2Scout/R2Team-Protocol. Resolve release v2.3 to its actual commit and verify the source; do not silently use main/latest.

## Add → register → connect

### add: PM prepares the assignment

PM confirms the participant/provider identity, functions, executor IDs, combined or separate chats, allowed subagents and permissions. PM publishes the approved TEAM/role changes through the project's Git workflow and returns an invitation. A TEAM entry does not grant access to a private project; its administrator manages actual access.

One person may own several executors or a single executor with QA+DevOps. PM is the only mandatory coordinator; other functions may be local, remote or internal helpers. Locality is relative to each participant's machine.

### register: a participant joins

```text
$r2team register repo <project-Git-URL> participant ken executor ken-ops
TEAM: <path>, ref <full-commit-SHA>.
Protocol: <path>, ref <full-commit-SHA>.
PM reply channel: <Issue-or-Work-Item-URL>, recipient <account/executor>.
Cross-check my assigned QA and DevOps functions.
Request my first TASK if none is assigned. Do not start product work.
```

PM replaces placeholders with real values. The receiving agent verifies its actual provider account and the current accepted TEAM, not just an ID or stale SHA in the invitation. Missing, inactive or changed assignments are clarified with PM; no self-registration or privilege escalation.

The participant confirms a local clone destination and tool/skill installation permissions. Existing dirty work is preserved. Repeated registration reuses identity and checked inputs instead of creating duplicates. A new machine needs its own access/tool checks, not a new participant record.

The public protocol repository can be installed without an invitation. Joining a project still requires its assignment and access.

### connect: this chat adopts a function

Resolve the assigned executor. If register already selected one unambiguously, connect runs in the same onboarding pass; another call is unnecessary. For multiple chats, invoke connect with each assigned executor. A persistent subagent with its own queue may use a named TEAM executor and parent; an ephemeral helper does not register.

Cross-check in the role's own words: duties/outputs, boundaries/approvals, permitted helpers, actual specification/tool inputs, task queue and return route, remaining questions. Confirm an existing TASK or request the first from PM. Onboarding does not begin product execution.

Publish the result in the existing onboarding channel if authorized; the current publisher records material state in the organizational TASK. Without channel access ask the human to relay and mark NOT_DELIVERED. Do not create an extra ACK or MSG journal. A local thread mapping, if configured, remains ignored and outside Git.

## Work and discussion

`start` verifies current owner, active role, TASK revision, branch/head, inputs and addressed updates. It gives a 3–5-line visible intake before one authorized next action: task/route, outcome, bounds, human input, result route and Starting/BLOCKED. No task means ask PM; competing assignments require clarification, not self-selection from backlog.

`task TASK-ID` is inspection only. `task TASK-ID discuss ...` identifies the question, participating executors/accounts, criteria and authorized decider. Use the existing Issue/Work Item for requirements or PR thread for code review. Silence is not consent. A comment does not change scope; approval and an updated contract are required before dependent work.

The current publisher preserves material open questions, decisions, evidence and next_action in Git before handoff/pause. Comments alone are not recoverable from a clone. Human setup or visual confirmation gets step-by-step guidance: purpose, safe action, expected result, response verification, next step until result, explicit pause or handoff.

Use the project's OpenSpec and Superpowers routing, reading the applicable SKILL.md. Do not apply every workflow to a trivial operation or skip required approval/testing. Missing dependencies are reported and installation or an explicit equivalent agreed.

## Transfer or disconnect

`migrate` transfers a function, not the protocol version. Before reassignment/deactivation, preserve exact unfinished work, candidate SHA, open requests and next_action. Keep TASK/Issue/PR identity; update assignments through the authorized publisher. If the handoff cannot be secured, stop with a blocker instead of discarding work.

`disconnect` deactivates the agreed participant/executor/function after transfer. It does not delete the person's account, chats, repository, branches or history. Membership changes do not automatically revoke provider access; an authorized administrator handles that separately.

## COO

`update` performs one bounded read-only delta pass, even if wake permission exists. It does not mark inbox events read or persist a new cursor. Missing scope is not permission to scan the whole project.

`check` adds only previously authorized local wake: current recipient, exact ignored mapping, designated single dispatcher and a new actionable event without a prior successful or uncertain send. No mapping/tool/permission means report the missing delivery; do not guess thread IDs or blindly retry.

An internal COO helper returns findings to its parent; it does not send external notifications. A standalone COO may notify its local roles within explicit rights. A GitHub/TFS event does not start remote Codex automatically.

Both commands run once. Heartbeat stays off until separately requested, configured and manually tested. They do not mutate TASK/TEAM, assignments, rights or schedules, nor restart busy roles.

## Audit

Audit checks accessible current facts: PM/roles/rights, Git/provider consistency, TASK ownership and checkpoints, specification/documentation gaps, required evidence, skill availability and recoverability by a clean executor. Inaccessible facts stay UNKNOWN/NOT_RUN. Audit suggests minimal fixes but does not make them.

For configured multi-repository work, qualify TASK IDs with repo URLs, pin external contracts and verify consumer compatibility. Each repository retains its own PM and permissions. Local task completion does not prove the cross-project release is complete.

## Safety and compatibility

- Git holds authoritative project state; installation does not create TEAM or migrate older projects.
- Project/global instructions and real permissions remain binding. Commit/push, tracker writes, merge, deploy, costs and schedules are separate capabilities.
- Retain one publisher per TASK branch. Do not overwrite another role's changes or take over an active assignment implicitly.
- Use GitHub or Azure DevOps Server/TFS Git as configured; verify server-specific APIs, item types and state mappings rather than assuming GitHub behavior.
- Never put secrets, personal machine paths or actual thread IDs in committed templates or invitations.
- Report what was actually done, exact references, limitations and next action. Notification success is not acceptance.
- R2Team command names are a project convention, not built-in OpenAI commands. Skills use the mechanism described in [OpenAI Docs](https://learn.chatgpt.com/docs/build-skills).

## Bounded working requests

Within an existing assigned TASK, authorized chats may exchange small requests, clarifications and answers directly. Keep the current accountable owner/publisher; no new TASK/Issue/PR/MSG or duplicate provider comment is needed merely for assistance. Use the agreed provider channel when direct communication is unavailable.

Product contract/significant design changes go to OpenSpec; responsibility, blockers and material continuation facts go to the existing TASK. Publish before ownership transfer, reliance on new material decisions/results, blocking stops or changed-session end, and completion/acceptance. Preserve code, tests and meaningful evidence; do not archive transcripts. This is the same rule locally, remotely and for helpers. Direct messages grant no new authority; uncertain delivery must not be blindly retried.

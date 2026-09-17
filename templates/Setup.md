# Setup — R2Team 2.4 guided wizard

Protocol version 2.4. Run only when requested; reading/editing the distribution does not start a project. Full rules: [protocol](CODEX_TEAM_PROTOCOL.md). Entry prompts: [CODEX_TEAM_SETUP.md](CODEX_TEAM_SETUP.md).

## Wizard rules

- Ask the next material question, preferably one at a time; verify accessible facts first.
- Distinguish confirmed, proposed and UNKNOWN; silence is not consent.
- Do not guess root, remote, TASK, account, environment or PM.
- Preserve existing AGENTS, docs, skills, code, TASKs, historical messages/reports and dirty work.
- Plan -> approved diff -> write -> verify. New authority, expense, publication and conflicts need a decision.
- Execute an already approved multi-step operation as small resumable mechanical steps without repeatedly requesting identical approval. Stop on drift, failed validation, denied authority, ambiguous write, irreversible effect or a new material choice.
- Preserve material setup state in one organizational TASK: mode, answers, refs, checks, blockers and next question. Do not create another registry or a checkpoint for every trivial reply.
- Before first-write approval, a conversational summary is sufficient. Move material decisions into Git once its root/TASK exist.
- Honor the selected skill's approval/implementation gates.
- Resume from checkpoint and changed inputs; do not reinstall tools or duplicate TASK/item/PR.
- Use [interaction rules](CODEX_TEAM_PROTOCOL.md#interaction) from the first task. Setup does not prove every role adopted the rules.

<a id="modes"></a>
## 0. Choose a mode

| Mode | Purpose | Executor |
| --- | --- | --- |
| new | New product/repository and initial team | Initial PM after confirmation |
| migrate | Existing project/MVP | Existing PM or authorized migrator |
| team | Add/change/combine/transfer/disconnect people/functions/chats | Current PM |
| join | Participant or new chat adopts an assignment | Registered executor |
| resume | Continue work or replace a lost chat | Assigned executor; PM authorizes takeover |
| audit | Read-only readiness check | Repairs separately authorized |

If intent is clear, state the mode and proceed. An invitee is not starting another project.

For `new` or `migrate`, also choose `launch_mode: production | synthetic_pilot`. Collect one Project Charter for both modes: outcome, repositories/provider, constraints, desired participants/functions/executors, permissions, QA independence, communication, OpenSpec, branches/PRs, CI/deployment, multi-repo dependencies and first result. Reuse confirmed answers throughout setup. Only `synthetic_pilot` receives a Pilot Addendum covering scenario, full path, permitted writes, optional defect/deployment flow, PASS/stop criteria, retention and findings report; production records `Pilot Addendum: NOT_APPLICABLE`.

<a id="preflight"></a>
## 1. Read-only preflight

1. Confirm package source/path, target project, applicable instructions and shell.
2. Check Git root/status/branch/HEAD/remote/worktrees without printing credential-bearing URLs.
3. Read current TEAM/legacy state, PM, affected active writers/tasks and scoped automations. Leave unrelated projectless schedules alone.
4. Verify exact package commit or trusted bundle manifest hash before payload hashes. Integrity without a trusted source is not provenance. HEAD/tag does not identify dirty files. The target protocol version must match the requested version.
5. If code and organizational files are split or the root is not Git, agree canonical placement and remote. Local files are not remotely published state.
6. Missing source is BLOCKED; do not reconstruct the package from memory.
7. Audit can be read-only without an assignment; TEAM/assignment changes require PM authority.

Local preparation can be approved without a remote, but is LOCAL_ONLY. Creating a remote repository requires explicit authorization.

<a id="new"></a>
## 2. NEW

### N1. Goal and first result

Clarify users/problem, first small verifiable outcome, out-of-scope and important data/security/time constraints. Keep a short overview; do not demand a full PRD before the first task.

### N2. Git and work queue

For real SDK/API dependencies across applications, use [MULTI_REPO.md](MULTI_REPO.md). Preserve each project's PM/authority; do not merge teams/trackers automatically.

Confirm exact Git URL or authorization to create one. Choose GitHub or generic Azure DevOps Server/TFS Git using [TRACKER_GUIDE.md](TRACKER_GUIDE.md).

Confirm default branch, account rights, policies/checks and push/merge side effects such as deployment. Verify Git refs/read/push, tracker API, PR/review/policy API, browser UI, CI and environment access independently. For Server confirm collection/project/repo ID, server/API version, Work Item type and actual state mapping. TFVC migration is separate work.

Creating task-related items/branches/PRs/comments may be approved as standard project operations. Merge, tags/releases, deploy, database changes and spending remain separate authority.

Read [OPERATING_COMMUNICATION.md](OPERATING_COMMUNICATION.md). Confirm approved direct working-exchange routes/permissions or use provider discussion. Bounded assistance creates no additional TASK/Issue/PR. Record actual routing policy in TEAM without secrets/thread IDs. Do not enable heartbeat.

### N3. Minimum team

Start with one participant and one PM executor; user chooses identity. John/john-main are examples.

For each needed function choose PM execution, authorized helper, separate local chat or another person. Do not create speculative future participants. Standard profiles are not a closed list; use [ROLE-TEMPLATE.md](ROLE-TEMPLATE.md) or concise TEAM entries for custom functions.

For each executor explicitly choose existing local standalone task, new local standalone task, persistent/ephemeral subagent, or remote/manual participant. Ask about functions/prohibitions, helpers/purposes/paths, parent executor, combined/separate chats, QA independence, environments and Git/tracker rights. Ken can combine QA+DevOps. A persistent subagent with its own queue may be a named executor; an ephemeral helper is not registered.

Fill [TEAM.md](TEAM.md). Internal subagents are not separately registered participants. Create chats only on explicit request. Confirm human-action/visual-acceptance respondents, scope deciders, provider accounts, update-check subscriptions and escalation. Locality is relative; remote auto-start is not promised.

For a local standalone executor, use a portable Git invitation plus a separate ephemeral launch prompt containing PM task ID, executor, exact register/connect commands and mandatory direct onboarding return. Store bidirectional task routes only in ignored `.codex-local/THREAD_REGISTRY.md`; unconfirmed delivery is `NOT_DELIVERED`. Remote/manual participants never receive local task IDs.

Every active executor may use a bounded read-only internal COO for its own assignments unless explicitly disabled. It returns findings to that role and needs no registry. If a separate COO chat is needed, register a standalone executor; for remote participants configure watched executor IDs, TASK root and executor-scoped assignment discovery, and choose an executor-label convention when provider actors are shared. Separately scope reads, wake and organizational writes; choose one wake dispatcher. See [ROLE-COO.md](ROLE-COO.md). Scheduling and chat creation require explicit requests.

### N4. Project entry files

Show and approve the actual file diff:
1. AGENTS, full protocol, OPERATING_COMMUNICATION and TEAM.
2. R2TEAM_MASTER, Setup, CODEX_TEAM_SETUP, SKILLS and TRACKER_GUIDE.
3. PM and used role profiles or equivalent TEAM contracts.
4. One organizational setup TASK using [TASK-TEMPLATE.md](TASK-TEMPLATE.md).
5. Existing documentation index or [DOCUMENTATION-TEMPLATE.md](DOCUMENTATION-TEMPLATE.md), filled with facts.

A full template copy may retain unused role examples; they create no roles. Selective installation must keep links and future team/join instructions usable.

Create Tasks when needed; Researches/Design/Decisions only for real content. No empty Reports/Messages/cursors system.

Before local registration, merge .codex-local/ into .gitignore and verify git check-ignore. Preserve other ignore rules. Never copy credentials/runtime data into published payload.

For an empty repository, authorize a bootstrap commit/default branch first; then use task branches/item/PR. Do not try opening a PR without a base branch.

### N5. Tools, skills and OpenSpec

Follow [SKILLS.md](SKILLS.md): inventory -> source/version/scope approval -> installation if needed -> discovery checks.

Check CLI, skills and openspec content separately. Initialize only with explicit authorization when absent. Default to the canonical repo-local root; no unnecessary external store.

Use actual CLI help/output/schema paths; do not invent metadata or specs for nonexistent behavior. Preserve legacy commands/custom skills through a reviewed diff. Context contains stack, verified commands, constraints and document/task references, not the entire protocol.

### N6. First real change

1. Clarify with openspec-explore and relevant brainstorming.
2. When asked to capture a new plan, use openspec-propose and its actual schema.
3. Respect any required stop/new request before apply; "start the project" does not bypass it.
4. Link change and the single detailed plan from TASK. A small restoration of accepted behavior needs no artificial change.
5. Authorized implementation uses apply/TDD; failures use systematic-debugging.
6. Acceptance uses verify and actual tests; integration includes sync/docs; archive waits for full scope.

### N7. Publication and entry

Before execution, define the first TASK's authorized transition table: every expected PASS/FAIL/BLOCKED outcome names next status, exact next executor/role, result recipient and authorized publisher. Initialize `handoff_seq`; a remote recipient must be discoverable from the accepted default-branch TASK.

Publish approved setup through the chosen provider and verify refs/assignments. Missing push authority/access means no remote-ready claim.

Run the audit below. Report ready/NOT_RUN, first TASK, owner and next action. The confirmed initial chat continues as PM; no mandatory COO/heartbeat.

<a id="migrate"></a>
## 3. MIGRATE

Use [MIGRATE_TO_2.4.md](MIGRATE_TO_2.4.md), then applicable N5-N7. Preserve active work by default. A user-approved fresh organizational queue may retain specs/chats while retiring old tasks/messages; it must not erase OpenSpec tasks.md or falsely mark unfinished work DONE. Each retained role must actually adopt the cutover.

For an MVP, map capabilities/sources/gaps and cover the next changed area, not a speculative full import. Existing documents are evidence, not automatically correct requirements.

With existing OpenSpec, resolve root/config/changes; preserve schema/metadata/capability paths/checkbox state; clarify ambiguous change selection; use update for existing planning within its gates and status/instructions for missing artifacts. Do not init/update/upgrade over customizations without comparison.

The first cycle uses a small real TASK. Protocol migration authorizes no product refactor, database move, deployment or tracker replacement.

<a id="team"></a>
## 4. TEAM

1. Read accepted default-branch TEAM and only affected TASKs.
2. Clarify add/remove/replace participant/chat/function, combine/split functions, or transfer PM.
3. Verify provider identity/access; choose stable executor IDs; keep real chat IDs local.
4. For each function clarify work, rights, skills, helpers, environments and independence. Record respondents, channels, intake and human-guidance rules without another journal.
5. Local/remote placement does not change TASK ownership rules. Optional local mapping belongs on the relevant machine.
6. Show the minimum TEAM/ROLE/affected-TASK diff. Custom functions are valid; a role name grants no authority.
7. Secure active work/checkpoints before transfer/deactivation. Preserve IDs, branches, evidence and unresolved requests.
8. Obtain appropriate approval, publish through the normal workflow, then send a complete invitation/current assignment. Provider membership/access is separately administered.
9. New/changed standalone functions cross-check their contract. Do not claim adoption from registration alone.

Adding a participant does not itself require a product OpenSpec change.

<a id="join"></a>
## 5. JOIN

Use register/connect from [COMMANDS.md](COMMANDS.md). Verify current TEAM and provider identity, not just an invitation's stale SHA. An absent/inactive entry is a PM question, not permission to add yourself.

1. Obtain repo URL, TEAM ref, executor, onboarding channel and TASK/branch if assigned. No TASK is needed to cross-check; request one afterward.
2. Confirm local destination and access; preserve existing work.
3. Read AGENTS, current default-branch TEAM, relevant protocol/ROLE/SKILLS, then assigned task branch.
4. Verify needed tools on this machine; installation/replacement needs owner permission.
5. Check documentation gaps, boundaries, permissions, allowed helpers and shared-provider account routing. Notification is not guaranteed chat execution.
6. Reuse the registered identity for a replacement physical chat; do not rewrite TEAM merely for a local thread ID.
7. Perform [role cross-check](CODEX_TEAM_PROTOCOL.md#role-cross-check): duties, bounds, verified inputs, questions and readiness. For added functions, check only changed responsibilities.
8. Confirm a current assigned TASK or request the first through the approved channel. If unavailable ask the person to relay and mark NOT_DELIVERED. Product execution requires start/explicit instruction and intake.
9. Do not create a second PM, tracker or duplicate task.

<a id="resume"></a>
## 6. RESUME

Read current TEAM/TASK, permitted scope, candidate/verified refs, changed paths, PR and next action, not all chats.

A change of owner requires an approved handoff/takeover: preserve available work, inspect remote head, assign the new owner and reconcile the provider. No force-push/reset or replacement task just for continuation.

The same executor resumes a pause from checkpoint. Use OpenSpec status/instructions and unfinished tasks; an old report is not evidence that every step is complete.

<a id="audit"></a>
## 7. AUDIT

Read-only by default. Repairs require an approved diff; material conflicts/new permissions need a decision.

Check:
- One PM; unique active identities; permitted owner/function.
- TASK scope/acceptance/checkpoint/next action and stage-appropriate item/branch/PR.
- Docs/specs/work state actually available in Git, including active branches.
- Provider identity/status consistent; no hidden duplicate or SYNC_REQUIRED.
- Required skill source/discovery and actual tool checks, or NOT_RUN.
- Correct OpenSpec root/schema and honest specification gaps.
- Version-specific evidence and known runtime limits.
- Clear migration cutover and safe active-writer/automation coordination.
- Ignored local registry; no committed secrets/thread IDs.
- Heartbeat off unless explicitly configured; optional COO scoped with one dispatcher and no self-escalation.
- Fresh-executor recovery without transcripts.
- Actual role cross-check and first-task confirmation/request.
- Human actions, material questions and decisions survive in TASK; silence is not agreement.
- Bounded direct assistance retains ownership; responsibility transfer requires publication.
- Actual permitted notification test or NOT_RUN; inbox read is not task completion.
- Protocol, AGENTS, TEAM, roles and setup agree.

Record READY, READY_WITH_LIMITS or BLOCKED with exact evidence and next action in the existing organizational TASK. Organizational readiness is not product/production acceptance. Structural package validation is not this live audit.

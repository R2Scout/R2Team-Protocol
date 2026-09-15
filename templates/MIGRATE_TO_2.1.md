# Migration prompt: R2Team/Codex Team Protocol 1.10 to R2Team 2.1

Give this complete document to the existing project PM. It is a migration procedure, not authorization to rewrite product code, deploy or publish. Start with read-only preflight and wait for approval of the exact migration plan before writes.

## Inputs and source-version guard

Required source: **1.10**.
Target: **R2Team**, `protocol_version: "2.1"`, `package_revision: 1`.

Inspect the project's actual AGENTS, protocol, setup and state files before planning:

- If they consistently identify **1.10**, continue with this migration procedure.
- If they identify **0.10**, another version, or conflicting versions, stop after read-only preflight. Report exact sources and request a source-specific migration decision; do not invent its semantics from 1.10.
- The existing project's rules remain effective until its approved cutover.

Required inputs, discovered where possible and otherwise requested:

```text
Target project Git URL and local root:
Current default branch:
Existing PM identity/executor:
Target package source:
  Option A: accessible Git URL + trusted full commit SHA
  Option B: accessible local bundle + independently supplied package.json SHA-256
Approved migration branch/worktree:
Communication channel for the current PM and existing roles:
```

Never execute placeholders. Confirm actual paths, refs and identities.

## 1. Verify the exact target package

1. Obtain the full trusted package, not just this prompt or one protocol file.
2. Verify manifest identity, protocol version 2.1 and package revision 1. Reject another protocol/revision, a differently named profile or any unverified substitute.
3. The old v2.0 tag is not a 2.1 source. Resolve v2.1 to its commit and inspect the manifest. A dirty working tree is not identified by its HEAD SHA.
4. For a bundle, compare package.json with the independently supplied trusted hash, then verify its payload hashes. A self-reported hash without a trusted source proves consistency, not provenance.
5. Run the package structural validator and its tests when available. Read VERIFICATION.md; distinguish structural PASS from blocked tests, untested skill behavior and unverified provider operations.
6. Read the package START, [Setup.md](Setup.md), [CODEX_TEAM_PROTOCOL.md](CODEX_TEAM_PROTOCOL.md), [OPERATING_COMMUNICATION.md](OPERATING_COMMUNICATION.md), [TEAM.md](TEAM.md), [SKILLS.md](SKILLS.md), [TRACKER_GUIDE.md](TRACKER_GUIDE.md) and relevant role instructions.
7. This target is the main Git-first package. Do not substitute a separate process-profile branch with different authority or hierarchy.

If the exact package is unavailable, STOP with SOURCE_BLOCKED. Do not reconstruct the target from chat history, install an older release, or claim migration readiness. A development bundle requires explicit acceptance of that status and its known verification limits.

## 2. Read-only project preflight

Inspect only exact relevant sources; do not scan every chat or the whole message archive.

Establish:

- Actual Git roots, remote/default branch, active worktrees, local/remote heads and dirty/unpublished work.
- Current protocol/version, global and project instructions, real PM, active role chats, combined roles, people and permissions.
- Active TASKs, linked Issues/Work Items, PRs and the current publishers.
- Current OpenSpec root/config/schema, accepted specs, active changes and tasks.md progress.
- Product code, tests, architecture/ADR, operator instructions and important existing evidence.
- Material pending messages, questions, blockers, approvals and unfinished operations.
- Existing project-scoped automations and local routing; unrelated automations are out of scope.

If organizational files are outside Git, propose their canonical Git placement before claiming Git-first readiness. A no-checkout repository or unusual worktree must not be "repaired" by destructive commands.

Higher-priority/global instructions cannot be overridden by replacing project AGENTS. If they require a conflicting legacy transport, identify the conflict and request an explicit scoped resolution from the authorized owner.

## 3. Protected state and migration strategy

Default: preserve and migrate active work, retaining existing IDs and useful links.

Do not overwrite filled documents with templates or discard:

- all openspec content, metadata, configuration and active changes/tasks.md;
- code, tests, uncommitted/unpushed work, branches, PRs and candidate evidence;
- existing chat identities, participant-specific constraints and approved permissions;
- historical messages/reports or material decisions contained in them.

Organizational Tasks are not OpenSpec tasks.md.

Starting the organizational queue afresh requires explicit user approval. Preserve product/specification state and material unfinished work first. Mark retired records as historical/inactive, not DONE; deletion requires a separately approved exact list. Do not recreate role chats merely to migrate them.

## 4. Show the plan and request approval

Present a concise plan containing:

1. Verified source version 1.10, or the explicit blocker if another version was found.
2. Exact target package ref/hash, status and verification limitations.
3. Files to add/merge/change, and protected paths that will remain unchanged.
4. Mapping of existing people/chats/roles to participants, executors and functions.
5. Mapping of active work to retained TASK/item/branch/PR and its publisher.
6. Historical records to retain; material facts to extract into current checkpoints.
7. Per-role/per-task cutover points and unresolved global-instruction conflicts.
8. Permissions needed for file edits, Git publication, tracker writes, notifications and installations, separately.
9. Verification and non-destructive rollback plan.

Then ask:

"Approve this exact migration plan, the confirmed source version, target package revision 1 and the listed write scope?"

Wait for a separate affirmative response. General approval does not grant unlisted commit/push, account administration, deployment, installation or automation rights.

## 5. Apply the approved file migration

Use the approved isolated branch/worktree and preserve concurrent edits.

Merge the applicable target instructions: AGENTS, protocol, OPERATING_COMMUNICATION, TEAM, Setup, CODEX_TEAM_SETUP, SKILLS, COMMANDS, tracker guide and used role contracts. Do not copy an unrelated template tree over the project.

Record separately in the project's adopted configuration:

```yaml
protocol_name: R2Team
protocol_version: "2.1"
protocol_package_revision: 1
integration_revision: <previous project value plus one, or 1 for first adoption>
protocol_source:
  repository_url: <trusted URL, when applicable>
  commit_sha: <verified package commit, or null for an approved unpublished bundle>
  package_sha256: <trusted bundle manifest hash, when applicable>
```

These are distinct: package revision identifies the distribution; integration_revision identifies the project's adaptation. Resolve placeholders before readiness. Never publish another machine's absolute path or local thread ID.

PM remains the sole mandatory coordinating function. Preserve existing names and combined roles unless a rename is explicitly approved. Local/remote chats and authorized subagents are execution modes, not different persistence rules.

COO is optional. Preserve only explicitly confirmed permissions; do not automatically create one, give it write rights or enable heartbeat. New heartbeat is off by default. Existing automations are reviewed and changed only within the approved cutover scope.

## 6. Transform active work without adding bureaucracy

Reuse existing TASK/item/branch/PR identities when suitable. An independently owned outcome uses the normal linked TASK + tracker item + branch + PR; do not create all four again for each role or small assistance request.

For each active TASK preserve or establish:

- outcome, scope, acceptance and relevant specification references;
- owner_executor_id, active_role, status, stage and next_action;
- requirement revision, branch and tracker/PR links;
- exact candidate/verified/merged refs as applicable;
- completed/remaining work, material blockers, questions and required human actions;
- meaningful decisions, evidence and continuation instructions.

One owner publishes each task branch. TEAM on the accepted default branch governs identities/permissions; active task branches carry current task state.

Legacy MSG/REPORT records remain history. Bring their material current contents into the TASK with provenance; do not replicate the complete archive. No new mandatory message registry, ACK file, role report or separate helper-task queue.

## 7. Adopt R2Team 2.1 communication explicitly

Explain and demonstrate the three-way rule to each affected executor:

- **OpenSpec:** approved product behavior, acceptance and significant change design.
- **TASK/checkpoint:** responsibility, material results, blockers and recovery state.
- **Direct exchange/internal delegation/provider discussion:** transient coordination inside the accepted task.

A bounded working request can go directly to an authorized registered chat without another TASK/Issue/PR. Validate parent TASK/ref, requester/recipient, permitted function, candidate, write boundaries and return route. The parent owner/publisher stays responsible.

A direct message does not alter scope, permissions or ownership. Material outcomes, code, tests and required evidence remain durable. Fixing a documented requirement violation does not require rewriting that requirement. OpenSpec tasks.md is not a message ledger.

Publish at four boundaries:
1. Before ownership transfer, including local-to-local transfer.
2. Before dependent work relies on a new material decision/result.
3. At a blocking stop or end of a changed session, preserving unfinished requests.
4. At completion or an acceptance milestone.

Do not require a commit per routine answer or duplicate direct conversations in provider comments. Unknown actionable delivery is checked, not blindly retried. Failed publication stays LOCAL_ONLY/SYNC_REQUIRED.

Direct exchange requires actual project/tool permission and verified routing. Confirm whether it is enabled; otherwise use the existing provider channel. Local thread mappings stay ignored. Remote notification does not guarantee remote Codex execution.

## 8. Preserve OpenSpec and verify skills

Do not init, archive, regenerate or reset OpenSpec merely because the team protocol changes. Preserve pending changes and checkboxes. Necessary specification edits follow the installed workflow and its own gates.

If specification coverage is incomplete, record gaps and propose a bounded baseline task. Migration does not prove specification completeness.

Inventory each participant's R2Team, OpenSpec and relevant Superpowers skills. Read the actual required SKILL.md files. Do not install or replace skills without machine-owner approval; show differences first.

Installed R2Team 2.0 skills are not proof that R2Team 2.1 is installed. Use the verified v2.1 release source when an update is authorized; otherwise follow adopted project documents and report conflicting installed instructions. Do not silently claim that editing the distribution updated other machines.

Use relevant OpenSpec explore/propose/update/apply/verify/sync/archive and Superpowers TDD/debugging/verification, not all skills for every operational question. Missing capability requires an approved equivalent or BLOCKED, not invented evidence.

## 9. Migrate existing role chats

Coordinate a safe checkpoint with affected active writers. For each task decide: finish under the old protocol or cut over at the agreed point. Until then, obey the old transport and reply rules, including mandatory MSG if the verified source requires it.

Do not discard global rules by local file edit. Resolve any conflict before enabling direct working exchanges.

Give each retained role a role-specific adoption request containing:
- exact project/package refs and its current participant/executor/functions;
- changed role limits and the three-way persistence rule;
- current TASK/checkpoint or the existing channel for requesting first work;
- the instruction to cross-check and report understanding or a blocker, not immediately start product implementation.

The role explains its duties, boundaries, inputs, tools, communication route and next work in its own words. PM records actual acceptance in the existing organizational checkpoint. A successful send, copied file or TEAM entry is not acceptance.

Keep unavailable roles as PENDING/BLOCKED, not migrated. Do not create replacements or wake unrelated chats without authorization. Local mappings and remote invitations use their appropriate routes; share Git references, not inaccessible local paths.

## 10. Verify before declaring migration complete

Run applicable package/project checks and inspect the exact diff. Record PASS, BLOCKED or NOT_RUN individually.

Required review:
- Exact package revision 1 verified; protected state preserved.
- Source-version discrepancy and instruction conflicts resolved.
- One PM; valid people/executors/functions/permissions.
- Active tasks have current owner, scope, evidence and next action.
- Git/tracker agree; no hidden missing PR or publication failure.
- Direct helper request retains ownership; actual handoff requires prior publication.
- Material state survives without chat transcripts; no duplicate helper task entities.
- OpenSpec distinguishes current contract, proposed changes and execution status.
- Installed skills checked separately; actual role acceptance recorded.
- Local IDs/secrets excluded from Git; no unapproved automation.
- A fresh authorized executor can read one published checkpoint and explain how to continue.

Use a read-only tabletop check for direct-message and recovery rules if live tests are not authorized. Do not send synthetic requests, create provider objects or perform deployments merely to demonstrate migration.

Document tests are not live integration acceptance. If a mandatory check is blocked, report partial migration/limits instead of declaring all roles READY.

## 11. Publication, report and rollback

Commit/push/PR/tracker writes require explicit authority. If authorized, publish the exact reviewed changes and verify remote refs and recipient access. If not, leave local changes and report NOT_PUBLISHED; a remote rollout is not complete.

Return:
- confirmed source version and target 2.1/package revision 1;
- trusted package ref/hash and project integration revision;
- changed files, preserved state and any approved retirements;
- per-role accepted/pending/blocked status;
- active work still on old rules;
- verification outcomes and publication status;
- next action and responsible person.

Rollback is an approved forward/revert change restoring the prior process with current work preserved, never a destructive reset. Resume product work only under a clear accepted assignment after the agreed cutover.

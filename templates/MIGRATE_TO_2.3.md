# Migration prompt: R2Team 2.2 to R2Team 2.3

Use this as a controlled migration, not an instruction to overwrite an active project.

Target: R2Team `protocol_version: "2.3"` from a trusted tag/full commit or verified bundle. The protocol version is the sole release identifier.

## 1. Read-only inventory

1. Verify target project root, current branch/HEAD/remote, dirty work and worktrees.
2. Read accepted AGENTS, TEAM, protocol, communication policy, active TASKs, OpenSpec changes/specs, provider items/PRs and scoped automations.
3. Identify active publishers/executors, unpublished work, uncertain external operations and any higher-priority instructions.
4. Verify the complete 2.3 source and manifest. Do not reconstruct it from memory or substitute main/latest.

## 2. Preserve before cutover

Keep existing TASK IDs, provider items, branches, PRs, specs, evidence, decisions, failures and history. Publish recoverable state before changing ownership or deactivating an executor. Do not erase old messages/reports merely because 2.3 no longer requires them.

## 3. Proposed 2.3 changes

- Add `R2TEAM_MASTER.md` as optional permanent bootstrap/administration consultant.
- Record participant and executor separately, with explicit executor mode.
- Permit a persistent named subagent executor with `parent_executor_id`; keep ephemeral helpers unregistered.
- Separate portable invitations from ignored local task routing and require onboarding return.
- Add Project Charter plus conditional Pilot Addendum.
- Verify Git, tracker, PR/review, browser, CI and environment capabilities independently.
- Require exact provider read-back and distinguish mergeability from merge completion.
- Apply ordered OpenSpec verify/sync/equivalence/archive/publication before closure.
- Preserve repo-qualified refs for multi-repository work.

## 4. Diff and approval

Show the exact project-file diff, TEAM changes, active TASK impacts, installed-skill differences and proposed cutover boundary. Obtain PM approval before writes. Skill replacement, provider writes, branch/PR changes, merge, deployment and automation remain separate permissions.

## 5. Apply

Merge the 2.3 entry files without overwriting project-specific instructions. Update TEAM integration revision and each affected executor mode/parent/independence. Add Master only if the project wants the consultant task. Preserve heartbeat/wake defaults. Update active TASK protocol version only at the approved per-task or coordinated boundary.

## 6. Executor adoption

Each retained standalone executor reads current TEAM/role/TASK, states its identity/functions/mode/rights/helpers/return route and confirms or requests work. Local task IDs remain ignored. Persistent subagents report through their parent unless explicitly granted an independent publication route.

## 7. Verify

Run package/project checks; verify provider/ref access separately; confirm TASK owners/revisions/branches/PRs/candidates; confirm OpenSpec state; prove one clean-executor recovery path. Report `PASS`, `BLOCKED` or `NOT_RUN` with evidence. Replacing files or skills alone is not proof that project roles adopted 2.3.

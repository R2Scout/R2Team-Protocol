---
name: r2team-coo
description: "Check exact new events for configured R2Team roles and optionally issue an already-authorized local wake. Use for a scoped COO update/check pass, not broad project audits or automatic task execution."
---
# R2Team — COO pass

Show command help in English using the syntax and boundaries below. Help needs no project access and performs no actions. Operational reports use the participant's preferred language.

- `$r2team-coo help`: read-only syntax and boundaries.
- `$r2team-coo update`: one read-only delta pass, NO notifications or writes.
- `$r2team-coo check`: one delta pass with already-permitted local wake.
- Bare invocation defaults to help, not check or background monitoring.

## Sources and authority

COO monitors configured durable events, not every transient role conversation. Authorized task owners may exchange bounded working requests directly without COO relay; do not duplicate these as mandatory notifications or create message logs. Wake permission does not authorize assigning helpers, changing task ownership or relaying new product scope. Material outcomes must reach the task publisher at the project's checkpoint boundaries.


This is the R2Team 2.4 procedure skill, not a role assignment or background service. Resolve the user's exact project/repository before acting. Read applicable AGENTS.md, accepted TEAM.md from the configured default branch, relevant role instruction and the selected TASK/current checkpoint. Read project COMMANDS.md and only the relevant protocol/Setup sections; do not scan unrelated repositories or chat history. Existing project instructions govern; an older project is not silently migrated to 2.4. Report incompatible/missing protocol inputs and ask PM for direction.

Git is authoritative for assignments, scope, acceptance, open decisions and continuation checkpoints; provider comments/PRs support the workflow but are not in a clone. Use the configured GitHub or Azure DevOps Server/TFS Git provider and verified identity/API, not a hard-coded GitHub assumption. Check task branch/remote head and current owner before writes. Keep one publishing owner per TASK; other roles submit comments/artifacts to that owner. No command grants commit/push, tracker-write, merge, deploy, account administration, expenses or scheduling rights. Ask only for missing facts/authority. Do not expose credentials or commit machine paths/thread IDs.

Help and unknown/ambiguous commands are read-only. A short visible intake states outcome, boundaries and return route before execution. Return concise facts, exact references, unresolved blockers and next action. Do not claim delivery, completion, independent QA or compatibility without evidence.

## Minimal reads

For an explicitly configured multi-repository scope, use repo-qualified TASK/event IDs and verify access separately per repository. Do not discover or monitor every repository owned by the participant.

Resolve the participant's required COO mode and explicit watched participant/executor/task IDs, rights and dispatcher. The default is one internal read-only helper covering that participant's executors; same-chat and optional standalone modes are alternatives. Do not infer scope from all repositories or every team member. Missing/ambiguous scope requires clarification.
Read only changes since a confirmed checkpoint via exact TASK paths/refs, selected Issue/Work Item IDs and PR events. Same provider account's "read" flag is not per-role completion.
Return dry facts: changed ID, what changed, who needs action, source pointer and next action. No long narrative or unrequested summaries. Failed fetch preserves prior successful position and is reported, not an empty successful pass. Optional local cursor/dedup metadata belongs only in ignored local storage, not a Git journal. update does not persist a new cursor or change inbox read state.

## Resolve delivery mode before the pass

Use exactly one mode; do not infer standalone delivery merely because the command is `check`:

- **Internal subagent:** the invoking parent supplies its executor ID and bounded watched executor IDs. The helper returns findings through the parent/subagent result channel. It needs no COO registration, thread registry or `notify_local`; it never wakes another task.
- **Same-chat check:** the current role task checks its own executor IDs. Report `ACTION_FOUND_LOCAL` in that task so the role can invoke `r2team-work`; never try to wake itself.
- **Standalone COO:** a separately registered COO executor watches named executors. Only this mode uses `notify_local`, a machine-local thread registry and the configured dispatcher.

If mode or parent executor is ambiguous, return `BLOCKED: COO_MODE_AMBIGUOUS` rather than falling through to standalone wake logic. Every active participant must have one mode; absence or disabled COO is a configuration gap. Setup offers standalone chat once, records the response, and otherwise keeps internal mode. Heartbeat remains a separate opt-in. This default grants no project writes, external notification, other participant scope or second-PM authority.

## Executor-scoped assignment discovery

Known TASK IDs are not sufficient for a remote participant: a newly assigned TASK may not yet be in that participant's local watch list. Before checking known events, perform **executor-scoped assignment discovery** for every configured `watched_executor_ids` entry.

1. Resolve the accepted remote default branch and configured TASK root. On first use, make one bounded metadata-only baseline over TASK frontmatter in that root. Match exact `owner_executor_id`, actionable status/revision and current TEAM registration; do not read every TASK body or repository history.
2. Store `last_seen_default_branch_sha` only in approved ignored `.codex-local` state. On later passes fetch the accepted default branch, compare from that SHA, and inspect only added/changed TASK frontmatter plus relevant TEAM changes. Use `handoff_seq` to distinguish a new baton from a previously handled stage. A failed or non-fast-forward comparison does not advance the cursor; reconcile or repeat the bounded baseline.
3. For each new actionable match, then read the complete TASK and only its linked Issue/Work Item, PR and checkpoint. Exact TASK ownership is authoritative. When several logical executors use a **shared provider actor**, provider assignment, mention or unread state cannot identify the intended local role. Use the executor ID in TASK; a provider label such as `r2-executor:<executor-id>` may accelerate queries but never overrides Git.
4. Treat an actionable match already present at first baseline as `NEW_UNACKNOWLEDGED` unless durable intake/checkpoint evidence proves that executor accepted it. This prevents installation after assignment from silently skipping current work.
5. Keep discovery cursor and wake dedup local. Do not recreate Messages, a committed inbox, polling journal or queue file.

For a PM watcher, also inspect exact open onboarding channels declared in onboarding TASKs. Do not scan arbitrary commit comments. Recognize structured `R2_EVENT: REGISTRATION_RESULT` and `R2_EVENT: ONBOARDING_QUESTION` entries addressed by `registration_id` and `to_executor_id`.

- Valid complete evidence reports `REGISTRATION_READY` to PM.
- An addressed blocking question reports `PM_ANSWER_REQUIRED`.
- Missing, conflicting, stale or failed evidence reports `REGISTRATION_BLOCKED`.

COO remains read-only. PM or the named publisher performs any pre-authorized activation and first-TASK transition.

`update` discovers and reports but never wakes or persists a successful-notification claim. `check` may use the discovered event for one already-authorized local wake and may persist technical cursor/dedup after the read/send outcome is known.

`owner_executor_id` matching the current/internal parent's active executor plus an actionable TASK status is the assignment signal. Do not require a second provider-side assignment or local route. A linked Issue/PR can notify and discuss but cannot invalidate that accepted Git assignment.

For every match report `previous_owner_executor_id`, `owner_executor_id`, `handoff_seq`, `result_to_executor_id`, status and next action. The role returns its stage result to that declared executor by publishing the next authorized TASK checkpoint; it does not choose a recipient from chat history.

## Wake for check only

An internal COO subagent returns the delta to parent as `RETURNED_TO_PARENT` and does not send external notifications. A same-chat check returns `ACTION_FOUND_LOCAL`. Neither mode performs delivery or requires `.codex-local/THREAD_REGISTRY.md`. A standalone COO needs current notify_local authorization, exact recipient mapping and designation as the single dispatcher for the watched recipients.
For each new actionable event confirm it still belongs to that recipient, is not superseded, and has no prior successful/uncertain send. Send one short task/branch/SHA/comment pointer; include return route if project requires it. No content mutation, new scope, permissions or "done" claims.
No tool/mapping/permission => report NOT_DELIVERED and rely on durable Git/provider state. Do not guess thread IDs or send remote messages merely because a tool exists. Never restart/interrupt busy roles, create chats, or wake arbitrary participants.
Do not retry uncertain sends; after cache loss reconcile exact provider/local evidence before another send. No duplicate author and COO wake. check may update approved ignored local technical dedup only; it cannot write TASK/TEAM/comments, change assignment/rights or execute product work.

A send response proves transport only. Durable delivery is established by the recipient's visible intake plus the reply/checkpoint required by the TASK through its linked provider route. Until then report `SENT_UNCONFIRMED`; without a usable local route report `NOT_DELIVERED`.

Both commands are single-pass. Heartbeat is OFF by default and is never enabled by them. A separately requested schedule must first pass a manual scoped test and be created by an authorized owner with supported native tooling, quiet on unchanged/non-actionable state. This skill alone is not a running monitor.

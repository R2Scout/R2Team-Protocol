# COO — required capability, optional standalone function, R2Team 2.4

Find relevant new events and unresolved assignments/questions for explicitly scoped executors within delegated rights. Read exact updates, report dry facts and minimize tokens. Do not scan the entire project/archive or replay unchanged history; a manual queue check still identifies pending work.

## Form and authority

- Internal helper for every active participant by default: read-only and limited to that participant's executor IDs; returns facts to its invoking role. `RETURNED_TO_PARENT` names only this local helper return, never the TASK result recipient, Task PM, task issuer, local PM or an external chat. It is not a standalone executor and does not manage external notifications or assignments.
- Participant's standalone chat: registered COO executor, potentially serving several of that person's roles. Other participants require explicit scope. It is not a second PM.
- Local wake, provider writes and specific organizational actions may be granted separately by PM/authorized owner with the local environment owner's approval. COO never changes its own rights or scope.

Current TEAM and assignment govern under [the COO section](CODEX_TEAM_PROTOCOL.md#coo). Read access to Git/Issues grants no TASK/TEAM writes or wake rights.

## Entry

Standalone COO performs [cross-check](CODEX_TEAM_PROTOCOL.md#role-cross-check), clarifies rights and requests its first organizational assignment if none exists. An internal helper clarifies with the parent.

Confirm exact participant/executor IDs, TASK root and any known TASK/branch/Issue/PR scope; baseline or last successful default-branch checkpoint; one wake dispatcher; permitted actions/routes; manual pass or separately configured schedule; stopping conditions and response route.

An empty scope does not mean the whole project. A read-only "check updates" request remains read-only even when notify_local is available.

Resolve one mode before reading:

- an internal COO subagent returns findings directly to its invoking parent executor and needs no registry or wake permission;
- a same-chat check reports the parent's own actionable assignment in that chat and never wakes itself;
- only a separately registered standalone COO uses local thread mapping and wake.

Ambiguous mode is `BLOCKED: COO_MODE_AMBIGUOUS`, not an assumed standalone delivery attempt. Exact matching `owner_executor_id` plus actionable status is sufficient assignment; provider assignment is only a routing aid.

Every active participant has exactly one configured mode: `internal`, `same_chat`, or `standalone`. Setup offers standalone chat once and persists the response; declining keeps internal mode. This protocol default does not authorize external notifications, writes, monitoring other participants or PM decisions. Heartbeat is configured separately and is off by default.

## One pass

Use `executor_queue` for ordinary update/check, session entry and before-idle checks. Known TASKs are only a cache. Use `task_only` only when explicitly limited; report the rest of the queue as unexamined. Follow [the common queue contract](CODEX_TEAM_PROTOCOL.md#coo): current remote SHA, complete baseline plus deltas and unresolved pending items, truthful coverage. A task-local HOLD cannot justify no work for an executor. A failed/partial check is `QUEUE_CHECK_INCOMPLETE`. Never switch tasks or execute product work during this read-only pass.

1. Discover newly added or changed TASK frontmatter for configured watched executor IDs. At first use, make one bounded metadata-only baseline of the configured TASK root; later compare accepted default-branch changes from ignored local `last_seen_default_branch_sha`. Do not scan unrelated history or TASK bodies.
2. Match exact `owner_executor_id`, actionable status/revision and current TEAM registration. For PM, also inspect only exact open onboarding channels recorded by `registration_id`; never infer an inbox from arbitrary commit comments. A current actionable assignment at first baseline is new unless durable intake/checkpoint evidence proves acceptance. Only then read the full TASK and its linked provider events.
3. Check event against current TASK/owner/revision. Do not execute stale assignments. For a shared provider actor, assignee/mention/unread state cannot route between logical executors; the TASK executor ID controls. An optional `r2-executor:<id>` label accelerates queries but is not authority.
4. In internal mode return `RETURNED_TO_PARENT`; in same-chat mode return `ACTION_FOUND_LOCAL`. These are advisory findings only. The invoking role must read the discovered TASK Route Card before work; COO must not report or hand off its product result to the invoking chat. No registry lookup or delivery attempt is involved. Without authorized standalone wake, return new facts and recommended next action. No external comment without tracker_write.
5. For authorized wake, verify registered local recipient and one dispatcher. Send one pointer per new event: TASK path, branch, published SHA, exact comment URL where applicable and instruction to read inputs. No new scope or product execution.
6. Do not interrupt active roles or create replacement chats. On unavailable environment/uncertain delivery, report `NOT_DELIVERED` and the accessible Git/provider reference; do not blindly resend.
7. Optional technical cursor/dedup stays ignored in .codex-local without secrets. A failed read does not advance a successful cursor; attempted notification is not execution. Lost cache requires reconciliation, not mass wake.

No MSG, separate REPORT or Git commit per polling pass. The TASK publisher persists material state. A COO authorized to write must still obey assignment, single-writer and Git rules.

Inspect non-closed question metadata addressed to watched executors and exact linked provider routes for work they issue/arbitrate, even when another executor owns the TASK. Return ASK/LOOP to Task Issuer, ESCALATE_PM to Project PM, and an ANSWERED question to its requester for validation. Missing routes are explicit gaps. Keep these alongside pending assignments across unchanged-SHA passes; a read cursor or sent notification does not close them. Use [the question contract](OPERATING_COMMUNICATION.md#question-routes).

## Registration events

A remote registration result uses `R2_EVENT: REGISTRATION_RESULT`, its `registration_id`, exact sender and PM recipient, `READY_FOR_ACTIVATION`, evidence and questions. A blocking clarification uses `R2_EVENT: ONBOARDING_QUESTION` and the same exact route.

PM's COO reports exactly one of `REGISTRATION_READY`, `PM_ANSWER_REQUIRED`, or `REGISTRATION_BLOCKED` to PM. It does not activate TEAM or TASK. PM or the named publisher applies a pre-authorized transition when objective evidence matches; no repeated owner approval is needed. The prepared first TASK becomes `READY` only under its declared `IMMEDIATE_RESERVED` or `QUEUED_AFTER_REGISTRATION` capacity rule.

## Organizational writes

Specific delegated scope may include proposing assignments, performing approved reassignment, preparing TEAM changes, updating the provider or managing a named schedule. A proposal is not write permission. One permission does not imply all others; COO does not approve its own rights.

Merge, deployment, database/access changes, spending and product acceptance are not inherent COO powers. Contract/TEAM changes require delegated PM/owner decisions and coordinated publication. Authority is project-scoped, not account-wide.

## Schedule and reporting

Default: one manual pass, heartbeat off. A standalone COO may receive a separately configured participant-side heartbeat after route/permission/dedup checks. An internal subagent has no independent schedule; the parent invokes it as needed.

Unchanged automatic passes stay quiet. Notify only meaningful new events, results, errors or required human action. A manual response can say "No new events" or give exact facts. Successful sending does not establish product READY/PASS.

Transport success is `SENT_UNCONFIRMED`. Delivery is evidenced only after the role publishes its visible intake and required reply/checkpoint through the TASK's linked route.

Follow [interaction rules](CODEX_TEAM_PROTOCOL.md#interaction) for discussion/human action and verification-before-completion under [SKILLS.md](SKILLS.md) for claims. Diagnose routing failures before retries.

## Working conversations are not COO events

Apply [OPERATING_COMMUNICATION.md](OPERATING_COMMUNICATION.md). Authorized owners/helpers may exchange bounded requests directly without COO relay or duplicate wake. Monitor configured durable events, not transient conversation transcripts. Wake permission does not authorize delegation, scope changes or ownership transfer. The publisher consolidates material state at publication boundaries.

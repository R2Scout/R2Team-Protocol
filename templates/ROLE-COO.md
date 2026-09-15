# COO — optional organizational function, R2Team 2.1

Find only new relevant events for explicitly scoped executors and help handle them within delegated rights. Read exact updates, report dry facts and minimize tokens. Do not scan the entire project/archive or repeat unchanged information.

## Form and authority

- Internal helper of PM/authorized parent: read-only by default; returns facts to its parent. It is not a standalone executor and does not manage external notifications or assignments. Parent publishes and wakes.
- Participant's standalone chat: registered COO executor, potentially serving several of that person's roles. Other participants require explicit scope. It is not a second PM.
- Local wake, provider writes and specific organizational actions may be granted separately by PM/authorized owner with the local environment owner's approval. COO never changes its own rights or scope.

Current TEAM and assignment govern under [the COO section](CODEX_TEAM_PROTOCOL.md#coo). Read access to Git/Issues grants no TASK/TEAM writes or wake rights.

## Entry

Standalone COO performs [cross-check](CODEX_TEAM_PROTOCOL.md#role-cross-check), clarifies rights and requests its first organizational assignment if none exists. An internal helper clarifies with the parent.

Confirm exact participant/executor IDs and TASK/branch/Issue/PR scope; baseline or last successful read checkpoint; one wake dispatcher; permitted actions/routes; manual pass or separately configured schedule; stopping conditions and response route.

An empty scope does not mean the whole project. A read-only "check updates" request remains read-only even when notify_local is available.

## One pass

1. Read relevant TEAM deltas, then only new assignments, addressed questions/answers and related PR changes. Do not query another person's private inbox.
2. Check event against current TASK/owner/revision. Do not execute stale assignments. For shared provider accounts, use logical executor/function as well as notification metadata.
3. Without authorized wake, return new facts and recommended next action. No external comment without tracker_write.
4. For authorized wake, verify registered local recipient and one dispatcher. Send one pointer per new event: TASK path, branch, published SHA, exact comment URL where applicable and instruction to read inputs. No new scope or product execution.
5. Do not interrupt active roles or create replacement chats. On unavailable environment/uncertain delivery, report limits and the accessible Git/provider reference; do not blindly resend.
6. Optional technical cursor/dedup stays ignored in .codex-local without secrets. A failed read does not advance a successful cursor; attempted notification is not execution. Lost cache requires reconciliation, not mass wake.

No MSG, separate REPORT or Git commit per polling pass. The TASK publisher persists material state. A COO authorized to write must still obey assignment, single-writer and Git rules.

## Organizational writes

Specific delegated scope may include proposing assignments, performing approved reassignment, preparing TEAM changes, updating the provider or managing a named schedule. A proposal is not write permission. One permission does not imply all others; COO does not approve its own rights.

Merge, deployment, database/access changes, spending and product acceptance are not inherent COO powers. Contract/TEAM changes require delegated PM/owner decisions and coordinated publication. Authority is project-scoped, not account-wide.

## Schedule and reporting

Default: one manual pass, heartbeat off. A standalone COO may receive a separately configured participant-side heartbeat after route/permission/dedup checks. An internal subagent has no independent schedule; the parent invokes it as needed.

Unchanged automatic passes stay quiet. Notify only meaningful new events, results, errors or required human action. A manual response can say "No new events" or give exact facts. Successful sending does not establish product READY/PASS.

Follow [interaction rules](CODEX_TEAM_PROTOCOL.md#interaction) for discussion/human action and verification-before-completion under [SKILLS.md](SKILLS.md) for claims. Diagnose routing failures before retries.

## Working conversations are not COO events

Apply [OPERATING_COMMUNICATION.md](OPERATING_COMMUNICATION.md). Authorized owners/helpers may exchange bounded requests directly without COO relay or duplicate wake. Monitor configured durable events, not transient conversation transcripts. Wake permission does not authorize delegation, scope changes or ownership transfer. The publisher consolidates material state at publication boundaries.

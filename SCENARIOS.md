# R2Team 2.4 scenarios

These are acceptance scenarios for setup, team lifecycle, communication, recovery, and distribution behavior. Document review is not evidence that access, roles, integrations, or skills work on every machine.

## Setup and migration

| Input | Expected | Forbidden |
| --- | --- | --- |
| Empty folder, no remote | Confirm root/outcome/provider and authority; bootstrap Git only after approval | Guess remote or claim Git-first readiness without publication |
| GitHub, one PM with helpers | One participant/executor, needed functions/helpers, first real TASK | Create six mandatory chats/issues |
| Brownfield MVP without OpenSpec | Preserve code/docs, assess coverage/gaps, baseline changed area incrementally | Rewrite whole project or claim complete specs |
| Existing OpenSpec | Preserve config/specs/active changes/tasks; use version-compatible CLI | Reinitialize/reset/archive to fit protocol |
| 1.10 with active MSG/PR | Preserve history; choose per-task/coordinated cutover; roles adopt 2.4 | Stop old transport before cutover |
| 1.10 with retained chats and fresh queue authorized | Re-run setup around current specs; cross-check each chat; explicitly retire only approved old org artifacts | Recreate chats or erase OpenSpec tasks |
| One retained chat rejects/does not understand | Mark its adoption BLOCKED/PENDING; other roles continue only in their scope | Declare universal migration |
| Organizational docs outside Git | Agree canonical Git root/placement and publish | Treat local folder as remotely recoverable |
| Trusted target package unavailable | SOURCE_BLOCKED with exact missing source | Reconstruct 2.4 from memory/latest |
| Proposal accepted but apply not authorized | Stop at installed workflow gate | Begin product implementation during setup |
| Existing custom skills | Inventory, backup, diff, ask before replacement | Overwrite through init/update |
| Audit requested | Read-only scoped evidence report | Repair files, enable heartbeat, or migrate |

## Team flexibility

| Input | Expected | Forbidden |
| --- | --- | --- |
| John is PM and all functions | One executor with explicit functions/helpers | Artificial role tasks/chats |
| Ken joins remotely as QA+DevOps | One participant, suitable executor(s), rights and portable invitation | Second PM or required local wake |
| Any participant is initialized | One participant-level COO mode; offer standalone chat once; heartbeat separately off | Disable COO capability or repeatedly ask about a chat |
| Remote registration is complete | Structured result in exact onboarding item; PM COO reports it; pre-authorized publisher activates | Wait for an unspecified extra approval |
| Remote registration lacks capacity | Accepted participant plus first TASK `PENDING_CAPACITY` and explicit gate | Hidden waiting or unauthorized parallel start |
| Ken splits one executor into QA/DevOps chats | New executor IDs if useful; published handoff/single publisher | Treat name change as independent human QA |
| Maya remote Designer and Lee remote Dev | Same TEAM/TASK/provider model; location changes route only | Separate protocol by location |
| Custom Tester/Analyst/Architect | Define purpose/output/authority/skills/acceptance | Reject because not built-in or grant rights by title |
| Add DevOps function to existing QA | Cross-check changed duties/rights/skills and task assignment | Repeat full setup or infer deploy rights |
| Function has several instances | Address exact executor/active role in TASK | Ambiguous role-only assignment |
| One provider account backs several executors | TASK/request names executor/function; provider access verified | Treat inbox/read state as per-chat queue |
| Participant leaves | Publish/transfer affected work, deactivate assignments, preserve history | Delete history/branches/accounts automatically |
| Team shrinks to PM+helpers | Reverse assignments safely; same specs/tasks/history | Redesign protocol or lose evidence |
| Role has no first task | Cross-check and request it through PM route | Self-assign from backlog |
| No PM response route | Report precise NOT_DELIVERED/BLOCKED | Pretend acceptance/delivery |

## TASK, communication, and handoff

| Input | Expected | Forbidden |
| --- | --- | --- |
| Independent feature | One TASK + provider item + branch + PR where applicable | Separate task entity per role |
| Bounded helper request | Parent TASK/ref/candidate/scope/return route; same owner/publisher | New TASK/MSG/ACK just for help |
| Trivial factual clarification | Direct answer in current route | Ceremonial intake/commit |
| Material answer affects dependent work | Publisher records result before dependency/pause | Leave only in chat/comment |
| Direct request changes scope/owner/permission | Stop and use formal TASK/provider update/approval | Treat message as authority |
| Two roles discuss alternatives | One thread, evidence, decision owner, durable conclusion | Silence as consensus or duplicate plans |
| Non-owner supplies result | Parent publisher reviews and records material state | Concurrent TASK writes by every helper |
| Human must configure/visually confirm | Explain purpose, bounded step, expected evidence; guide to result/blocker | Request secrets or call reply automated PASS |
| Direct delivery uncertain | Inspect current state/event/candidate before retry | Blind duplicate message or side effect |
| Old owner unavailable with unpushed work | Recover published state; mark rest UNKNOWN | Claim invisible work restored |
| Local Dev to remote Dev after QA FAIL | Same TASK/PR, failure evidence and checkpoint, owner transfer | Replacement Issue or lost failure |
| Same executor changes QA to DevOps | Record stage/function/authority where material | Pretend independent reviewer/person |
| Tracker unavailable | Preserve Git checkpoint, SYNC_REQUIRED/NOT_DELIVERED | Duplicate items or claim synchronized |
| New executor resumes | Read accepted TEAM, TASK branch, spec, candidate, open requests | Depend on previous chat memory |
| Same branch already in worktree | Coordinate/branch/detached inspection | Force/destructive checkout |
| Dev hands work to remote QA | Accepted default-branch TASK checkpoint increments `handoff_seq`, assigns QA and declares result route | Chat-only request or provider assignment without Git baton |
| Remote QA passes | Publish evidence and next authorized TASK transition to declared executor | Choose recipient from memory or leave result only in comment |
| Remote QA fails | Return same TASK to declared Dev with failure evidence and candidate identity | Create unrelated replacement task or lose failure history |

## Specifications, evidence, and delivery

| Input | Expected | Forbidden |
| --- | --- | --- |
| New behavior/API/security/data/migration | OpenSpec change plus TASK/PR linkage | Requirements only in chat |
| Fix restores accepted behavior | Existing spec may suffice; TDD/debug/verify | Artificial proposal solely for process |
| Research result | Sources/findings/assumptions/UNKNOWN; PM decides | Treat research as accepted contract |
| QA starts | Exact candidate, acceptance/scenarios, coverage level | “Latest” candidate or CI-only acceptance |
| QA failure | FAIL evidence and return to implementation; blocker only if no safe next step | Mark DONE or erase prior evidence |
| Candidate changes | Assess and repeat affected checks | Reuse PASS blindly |
| PR merged | Record actual merge SHA; acceptance remains separate | Auto-DONE/deployed claim |
| QA evidence-only commit after PASS | Map verified candidate to result; assess affected checks | Automatically invalidate or blindly inherit all |
| Deployment independent | Linked deployment TASK with exact source/artifact/env/rollback | Overload code TASK or infer production authority |
| Deployment response lost | Investigate environment/provider before retry | Repeat possibly completed deployment |
| OpenSpec archive | After actual completion conditions for change scope | Archive to clear checklist |
| Partial brownfield coverage | Explicit map/gaps/UNKNOWN and priorities | Claim completeness from files/validator |

## Providers and automation

| Input | Expected | Forbidden |
| --- | --- | --- |
| GitHub provider | Verify repo/default branch/policies/identity; Issue/PR projection | Hard-code unknown IDs or bypass checks |
| Older TFS Server | Verify version/API/work-item types/states/tool compatibility | Assume Azure cloud CLI/features |
| Provider write times out | Read narrow target before retry | Create duplicate |
| Direct working exchange enabled | Actual permission and routing; content stays within accepted TASK | Assume every local/remote chat reachable |
| Provider notification to remote person | Available at next manual/authorized check | Promise remote Codex auto-start |
| COO update | Exact configured deltas, dry read-only facts, no notifications | Execute TASK or scan whole project |
| COO check | Same plus one authorized deduplicated local wake | Create scope/assignment or wake other machines |
| Internal COO finds parent's TASK | `RETURNED_TO_PARENT`; no registry or wake lookup | Treat helper as standalone dispatcher |
| Role chat checks its own TASK | `ACTION_FOUND_LOCAL`, then `r2team-work start` | Wake itself or report `NOT_DELIVERED` |
| Unknown TASK assigned remotely | Bounded frontmatter discovery by executor ID and handoff sequence | Require prior TASK ID or shared-account unread flag |
| PM awaits onboarding | Check only registered onboarding channels by registration ID | Scan arbitrary commit comments or expect the owner to forward a link |
| Sender and COO see same event | One dispatcher owns delivery | Double wake |
| Heartbeat not requested | Off | Infer it from protocol/role |
| Heartbeat requested | Explicit scheduler/scope, quiet unchanged, manual canary | Perpetual undocumented polling |
| Wake send uncertain | Report uncertainty; no blind retry | Claim delivery or resend indefinitely |

## Skill routing

| Situation | Expected skill behavior | Not proven by invocation |
| --- | --- | --- |
| Explore idea | openspec-explore and relevant brainstorming | Accepted requirement |
| Capture material change | openspec-propose; respect gates | Implementation authorization |
| Change approved plan | openspec-update-change | Code edit |
| Implement | openspec-apply-change plus TDD as applicable | QA/merge/deploy |
| Unexpected failure | systematic-debugging before fix | Root cause until evidence |
| Pre-completion | verification-before-completion against TASK/spec/candidate | Full product acceptance |
| Acceptance audit | openspec-verify-change plus QA evidence | Independent QA if same executor/person |
| Sync/archive | Authorized owner after conditions | Production deployment |
| Skill missing | BLOCKED or explicit equivalent | Permission to invent usage |
| Install/update skills | Trusted source/ref, diff, machine-owner approval | Protocol migration/project adoption |

## Distribution release

| Check | Expected |
| --- | --- |
| Public language | All maintained distribution files, help, commits, release notes in English |
| Manifest | Protocol 2.4 as the sole release identifier, required paths and matching SHA-256 |
| Links/anchors | Structural validator PASS |
| Validator suite | Current complete suite PASS |
| Skills | Four skill directories pass official quick_validate |
| Help copies | templates/COMMANDS.md and skills/r2team/references/commands.md byte-identical |
| Specialized CMMI | Absent from main package; maintained in separate TFS repository |
| Candidate publication | Candidate branch resolves to exact approved commit; no release tag implied |
| Fresh clone | Exact candidate commit validates independently |
| Runtime claims | Direct messaging, provider writes, migration, deployment, heartbeat remain NOT_RUN unless separately tested |

## Recovery tabletop

A fresh authorized executor receives only repository URL, accepted TEAM/default-branch ref, TASK branch, provider item/PR, and project access. It must identify current owner/role, scope/acceptance, exact candidate, evidence, open questions, next action, and publication status without chat history.

PASS requires all material facts in Git and provider links to resolve. UNKNOWN is preserved. The exercise does not send synthetic messages, deploy, or change live assignments unless separately authorized.

# R2Team 2.4

Git-first teamwork for one person, local role chats, remote participants, and hybrids. PM is the only mandatory coordinating function. GitHub and generic Azure DevOps Server/TFS Git are supported; specialized process profiles are separate.

**OpenSpec holds the product contract. TASK holds recoverable execution state. Direct conversation supports transient coordination.**

## Contents

[Premises](#premises) · [Sources](#sources) · [Authority](#authority) · [Entry](#entry) · [Structure](#structure) · [Team](#team) · [TASK](#task) · [Workflow](#workflow) · [Handoff](#handoff) · [Providers](#providers) · [Specifications](#specs) · [Skills](#skills) · [Automation](#automation) · [Setup](#setup) · [Migration](#migration) · [Feature example](#feature-example) · [Team examples](#team-examples) · [Validation](#validation) · [Prompts](#start-prompts)

<a id="premises"></a>
## 1. Premises and purpose

Chats, people, computers, and executors are replaceable. A project must remain resumable from published Git and linked tracker state. It may start with one PM and helpers, grow into local role chats and remote people, and shrink without changing its operating model.

Git preserves accepted contracts, people/functions/rights, assigned work, material progress, blockers, evidence, code, and next action. It does not preserve hidden reasoning, secrets, unpushed files, or every transient exchange. Recovery reaches the last published checkpoint; inaccessible local work is UNKNOWN.

At any time an authorized fresh executor should determine what the product must do, what is active, who owns it, which candidate/evidence is current, what remains open, and the next safe action.

Use one canonical Git provider per project, one current PM, recoverable access procedures, and explicit permissions. Automation is optional and separately authorized.

`protocol_version` is the sole distribution release identifier. Its major number identifies the protocol generation; increment the minor number for each published protocol revision. Do not add a separate package revision. A project's `integration_revision` remains a distinct local counter for adopted configuration changes.

<a id="sources"></a>
## 2. Basis and sources

The design combines official Git/worktree/agent guidance, provider documentation, OpenSpec, Superpowers, and community experience. It is not an official OpenAI protocol and makes no universal performance claim.

- [Codex worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees)
- [Long-running work](https://learn.chatgpt.com/docs/long-running-work)
- [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)
- [Harness engineering](https://openai.com/index/harness-engineering/)
- [OpenAI Symphony](https://github.com/openai/symphony)
- [GitHub Issue/PR linking](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)
- [Azure DevOps Work Item/Git links](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/connect-work-items-to-git-dev-ops?view=azure-devops)
- [Azure DevOps REST](https://learn.microsoft.com/en-us/rest/api/azure/devops/?view=azure-devops-rest-7.1)
- [OpenSpec concepts](https://github.com/Fission-AI/OpenSpec/blob/main/docs/concepts.md)
- [OpenSpec existing projects](https://github.com/Fission-AI/OpenSpec/blob/main/docs/existing-projects.md)
- [Superpowers](https://github.com/obra/superpowers)

Community reports support isolated branches/worktrees and explicit ownership as useful patterns, not normative consensus. The distribution root `SOURCES.md` records provenance limits; adopted template copies remain self-contained without a parent-directory link.

<a id="authority"></a>
## 3. Authority and sources of truth

Mandatory rules:

1. Git is durable authority for accepted protocol, TEAM, product contract, material TASK checkpoints, code, and maintained evidence.
2. One publishing owner controls each TASK branch/checkpoint.
3. The same TASK survives function/person handoff.
4. Notification, comment, chat, or skill never grants scope/permission.
5. Acceptance is candidate-specific and evidence-based.
6. Specifications, implementation, tests, architecture, and operator docs remain coherent.
7. Facts required for continuation cannot exist only in chat, Issue, or PR.

| Information | Authority |
| --- | --- |
| Protocol and accepted TEAM | accepted default branch |
| Scope, acceptance, owner, checkpoint | TASK on active branch |
| Accepted behavior | OpenSpec specs |
| Proposed behavior | OpenSpec change on task branch |
| Code/tests/config | task branch and PR |
| Architecture/operations | maintained docs/ADR/runbook |
| Queue/assignee | provider item as a projection of TASK |
| Review/checks | PR/check system; material outcome summarized in Git |
| Local task routing | ignored local registry |
| Secrets/large artifacts | protected store; Git keeps procedure/ref/digest |

PM controls assignment and material scope. The TASK publisher records execution state. Read TEAM from accepted default branch, not a stale task copy. Tracker drift is SYNC_REQUIRED; reconcile confirmed current state rather than overwriting newer work.

A clone must include accepted branch and referenced active branches. Comments are not in a clone, so unresolved material questions/decisions go into TASK. External artifacts require stable refs, retention, and relevant facts.

<a id="entry"></a>
## 4. Minimum entry

Project:

- initial commit, default branch, remote, verified read/push;
- one confirmed PM;
- AGENTS, TEAM, protocol, communication policy, used role contracts;
- Issue/Work Item and PR capability with known states;
- clear first outcome, acceptance, checks, and publication authority;
- required tools/skills verified or approved fallback.

Do not require six chats, a separate COO chat, heartbeat, service, or full PRD. Every active participant does require one lightweight COO capability, internal by default.

Participant: verify provider identity, participant/executor/functions, permissions, tools/skills, contract, fetch/check/publish capability, and PM response route. Apply least privilege. One person may own several functions/executors.

Tool checks distinguish Git, OpenSpec CLI, project openspec directory, and installed OpenSpec skills. Pin trusted versions. Never expose credentials.

<a id="structure"></a>
## 5. Project structure

~~~text
AGENTS.md
R2TEAM_MASTER.md        # optional persistent bootstrap/admin consultant
CODEX_TEAM_PROTOCOL.md
OPERATING_COMMUNICATION.md
TEAM.md
Tasks/TASK-042.md
openspec/{config.yaml,specs/,changes/}
docs/{README.md,architecture.md,runbook.md,ADR-001-...}
.codex-local/THREAD_REGISTRY.md   # optional and ignored
~~~

Create only useful files. Preserve existing flat Researches/Design/Decisions. Use the selected OpenSpec CLI/schema; do not invent metadata. AGENTS is a short map, not duplicated requirements.

Messages, ACKs, reports, cursors, and PROJECT_STATE are not mandatory authorities. A generated status view never replaces TEAM/TASK/specs.

<a id="team"></a>
## 6. Participants, executors, and functions

- Participant: human/provider identity.
- Executor: logical chat/agent identity that can own work.
- Function: PM, Brain, Designer, Dev, QA, DevOps, or custom role.

Only PM is mandatory. Tester, Analyst, Architect, Security, Release Manager, and any domain function are valid after defining purpose, outputs, authority, skills, acceptance, and helper limits.

~~~yaml
participants:
  - participant_id: john
    provider_identity: verified-account
    executors:
      - executor_id: john-main
        functions: [PM, Brain, Dev]
        mode: local_standalone
        parent_executor_id: null
        helpers: [research, design, test]
  - participant_id: ken
    provider_identity: verified-remote-account
    executors:
      - executor_id: ken-ops
        functions: [QA, DevOps]
        mode: remote_manual
        parent_executor_id: null
~~~

TASK owner_executor_id and active_role must match current TEAM. Locality is relative.

For every executor record mode: local standalone, remote/manual, or subagent. A persistent subagent with its own queue may be a named executor with `parent_executor_id`; an ephemeral helper is not registered. One provider/Git account may back several logical executors, so commit author alone is not executor evidence. TASK, branch, PR and checkpoint identify the executor.

Any executor may use authorized bounded helpers. Parent supplies scope, paths, candidate, evidence, and return route; reviews output; remains publisher. Helpers do not take another executor's assignment, read unrelated inboxes, change role files, or publish independently. A standalone role chat may provide bounded help without ownership transfer under [OPERATING_COMMUNICATION.md](OPERATING_COMMUNICATION.md).

Record independence: same executor, different executor under the same participant, different participant, or required independent reviewer. Chat renaming does not create independence.

Supported modes: one PM with helpers; one person with local role chats; remote people; any hybrid. Persistence and acceptance do not change.

<a id="task"></a>
## 7. TASK contract

Independent work creates/reuses one TASK, provider item, branch, and PR where applicable. Bounded consultation inside an accepted TASK creates no extra mandatory TASK/Issue/PR/MSG. Reuse the TASK across discovery, design, implementation, QA, integration, and handoff. Separate deployment TASK only for an independent lifecycle/owner/authority.

~~~yaml
protocol_version: "2.4"
task_id: TASK-042
task_revision: 3
status: IN_PROGRESS
stage: IMPLEMENTATION
owner_executor_id: john-dev
active_role: Dev
next_action: "Publish C2 and request QA retest."
tracker_item: "<URL/ID>"
branch: "task/042-notifications"
pull_request: "<URL/ID or NOT_CREATED>"
openspec_change: "realtime-notifications"
candidate: "<exact SHA/build or NOT_READY>"
verified_candidate: "<exact SHA/build or NOT_RUN>"
~~~

Increment revision for material scope/acceptance/owner contract changes, not each checkpoint. Before independent handoff, item/branch/PR refs are known or NOT_APPLICABLE.

Body: outcome; scope/bounds; acceptance; plan/OpenSpec tasks; current refs/partial results/remaining work; exact evidence/limitations; decisions/questions/blockers/human actions; handoff and next actor/action.

States: DRAFT -> READY -> IN_PROGRESS -> REVIEW -> DONE, plus HOLD/BLOCKED/CANCELLED and onboarding PENDING_REGISTRATION/PENDING_CAPACITY. Stages: DISCOVERY, DESIGN, IMPLEMENTATION, QA, INTEGRATION, DEPLOYMENT. QA FAIL returns to READY/IMPLEMENTATION with evidence/owner. BLOCKED means no safe next action; HOLD is an explicit deferral with a recorded release condition and authorized publisher. The held TASK cannot start until its accepted transition releases it, but other eligible assignments are unaffected unless an executor-wide constraint is recorded. Merge alone is not DONE.

<a id="workflow"></a>
## 8. Workflow

### 8.1 Prepare

PM checks repository/TEAM and duplicates, defines outcome/scope/acceptance/owner, creates TASK branch/checkpoint, pushes it, and records provider/PR links. Draft PR follows substantive work; if unsupported, enforce the review gate explicitly.

### 8.2 Intake

Receiver verifies owner, TASK revision, refs/candidate, inputs, write bounds, human needs, and return route. Display 3-5 lines:

~~~text
Received: TASK-042/3, PM -> Dev.
Outcome: implement approved reconnect behavior.
Boundaries: no merge, deployment, or scope expansion.
Result: candidate/evidence in TASK and reply to PM route.
Starting.
~~~

Incomplete/misaddressed/conflicting/unsafe work is BLOCKED with a precise durable blocker.

### 8.3 Execute and publish

Work in small verifiable increments, preserve unrelated changes, and use mapped skills. Publish:

1. before ownership transfer;
2. before dependent work uses a new material decision/result;
3. at blocking stop or changed-session end;
4. at completion/acceptance milestone.

Do not commit each routine answer.

### 8.4 Transfer

Current publisher rechecks remote head, records candidate/evidence/remaining work, pushes without force, updates TASK owner/role/revision and provider assignee, then notifies new owner. Old owner stops writing. Same-executor function switch still records material stage/permission change.

### 8.5 QA and integration

QA tests exact candidate against TASK/OpenSpec and reports PASS/FAIL/BLOCKED/NOT_RUN with coverage. Preserve a concise result in TASK and the provider PR/review route when both exist. Green CI does not replace UI/manual acceptance. Candidate changes invalidate affected checks.

Integrator reviews base/diff/checks/docs/specs/authority, then verifies provider completed/merged state, actual merge commit and remote default-branch result. Mergeability is not completion. Fetch the merge object before local inspection. A report-only commit need not invalidate all evidence; code/config/base changes require impact assessment. Never label merged SHA verified without mapping/test evidence.

### 8.6 Deployment

Confirm exact source/artifact digest, environment, authority, migration, rollback, and pre-state. Record version/environment/smoke and uncertainty. Do not blindly retry a possibly successful side effect.

<a id="interaction"></a>
### 8.8 Human assistance

Explain why a human step is needed and affected account/environment; give one safe bounded step and expected evidence; avoid secrets; inspect response and guide the next step; continue until verified success, blocker, or pause. Human statement is not automated PASS. Continue independent safe work where possible.

### 8.9 Clarification and bounded help

Every assigned TASK and bounded request records Task Issuer and Project PM with explicit response routes, even when they are the same executor. The direct issuer, assignment publisher, current owner and stage-result recipient are distinct responsibilities. Apply [the question contract](OPERATING_COMMUNICATION.md#question-routes): ASK for clarification, LOOP for a disagreement/consensus attempt, ESCALATE_PM directly for project-authority conflicts or unresolved disagreement. The requester need not complete ASK/LOOP before requesting PM arbitration.

Record Question Mode, Question Status (OPEN, ANSWERED, ESCALATED, CLOSED), requester/respondent, blocking impact and Decision in the existing TASK/provider route. Respondents inspect addressed requests regardless of TASK ownership; answers return to the original requester for validation and closure. Only dependent work waits. Resume authorized work after a sufficient answer; publish any required contract change first. PM decides within recorded authority and cannot manufacture evidence, override invalid QA, replace a human gate or grant unrelated rights. Reassignment explicitly updates/confirms issuer/PM routes and preserves unresolved questions/history.

Direct requests are allowed inside accepted TASK and actual rights. Include TASK/ref, sender/recipient, candidate, result, boundaries, allowed writes, and return route. Parent remains owner/publisher. Trivial clarification needs no ceremonial intake; bounded work does.

Direct exchange cannot change ownership, scope, acceptance, priority, or permission. Publish material outcome before dependency/pause. Use one conversation route rather than duplicate chat and provider threads.

### 8.10 Discussion

Use existing TASK/item or PR. State question, affected contract/candidate, participants, alternatives/evidence, decision owner, impact, needed answer. Silence is not consent. Authorized owner records outcome and updates OpenSpec/ADR where needed. Persist result, not transcript.

### 8.11 Recovery

Fresh executor reads accepted AGENTS/TEAM/role, TASK branch, relevant spec, candidate/evidence, and provider state. Material unanswered requests and next action are present. Safe lost consultation may repeat; uncertain side effects require investigation.

<a id="handoff"></a>
## 9. Parallel work and recovery

One TASK branch/checkpoint has one publisher. Independent parallel work uses separate TASK branches and reviewed integration. Helpers return artifacts to publisher.

Reassignment keeps TASK/item/branch/PR and preserves failures, candidate, questions, and unpublished status. New owner verifies remote head. If old executor is unavailable, recover only published state and mark local remainder UNKNOWN; do not force-push.

One branch can be checked out in only one worktree. Use coordinated checkout, separate branches, or detached inspection.

Disconnect after publishing affected checkpoints and replacement ownership. Preserve history. Account/access revocation is a separate action.

<a id="providers"></a>
## 10. GitHub and Azure DevOps Server/TFS Git

| Concept | GitHub | Azure DevOps Server/TFS Git |
| --- | --- | --- |
| Queue | Issue | configured Work Item |
| Review | Pull Request | Pull Request |
| Assignment | assignee + TASK | Work Item assignee + TASK |
| Discussion | Issue/PR | Work Item/PR |
| Recovery | Git TASK/spec/code | Git TASK/spec/code |

Tracker is a projection of TASK in R2Team 2.4. Summarize provider-only continuation facts into Git.

Verify Git refs/read/push, tracker API, PR/review/policy API, browser UI, CI and environment access independently. Repo/default branch/policies/checks/permissions and merge/deploy effects remain separate facts. For Server also verify version/API, actual Work Item types/states, and tool compatibility; do not assume cloud-only CLI/MCP.

Provider writes use supported concurrency and read back IDs/links/revisions/state/refs. On uncertainty inspect narrow target before retry. No bypass or duplicates. Git ref access proves no other capability; “request sent” is not completion.

<a id="specs"></a>
## 11. Specifications and documentation

- OpenSpec: accepted behavior/acceptance and proposed change.
- TASK: responsibility, plan, material execution state/evidence/blockers/next action.
- Architecture/C4/arc42: boundaries, components, data, deployment, risks.
- ADR/MADR: significant choices, alternatives, consequences.
- Runbooks/user docs: operation and use.

Use OpenSpec change for new behavior, API/security/data/migration/architecture or material contract change. A fix restoring accepted behavior may use existing spec.

Brownfield baseline is incremental: map capabilities to code/tests/docs; distinguish implemented, verified, intended, UNKNOWN; prioritize changed/risky areas. Inventory/CLI validation does not prove completeness.

Accepted specs live on default branch; proposed deltas on task branch. Do not duplicate versions unless product maintains them. OpenSpec tasks.md is not a message/status ledger. A schema-declared conditional artifact may legitimately be absent; do not infer incompleteness from file count alone.

<a id="skills"></a>
## 12. OpenSpec and Superpowers

Verify trusted skill source/ref, installed version, and machine scope. Installation/replacement needs machine-owner approval. Naming a skill does not install it.

| Activity | Skill |
| --- | --- |
| explore | openspec-explore |
| propose substantial change | openspec-propose |
| reconcile plan | openspec-update-change |
| implement | openspec-apply-change |
| verify against artifacts | openspec-verify-change |
| sync accepted deltas | openspec-sync-specs |
| archive completed history | openspec-archive-change |

Respect skill gates. Finalization order is: verify implementation against the change; sync every declared delta into accepted specs; verify semantic equivalence; archive; publish accepted specs/archive/TASK; then close the provider item.

Superpowers:

- test-driven-development for implementation/fixes where applicable;
- systematic-debugging before guessing;
- verification-before-completion before completion/commit/release claims;
- optional brainstorming/design/planning/review helpers without duplicating OpenSpec.

Verification uses TASK acceptance, OpenSpec scenarios, exact candidate, and actual commands/evidence—not remembered intent. QA/DevOps remain candidate/environment-specific.

<a id="automation"></a>
## 13. Automation

Codex may create/update TASK/item/branch/PR, run checks, publish, and notify when authorized/supported. Instructions grant no access.

Operator supplies goals, critical choices, credentials through approved mechanisms, visual/human evidence, and consequential approvals. Automation validates results and persists material state.

Direct exchange and wake differ: exchange may contain bounded work; wake only points to durable event. Provider notification does not guarantee remote Codex execution.

<a id="coo"></a>
### 13.4 COO and heartbeat

Operational queue checks, work-session entry and before-idle checks use `executor_queue` scope. Resolve the current remote default branch before discovery, including TASKs not previously watched. An explicitly limited TASK check uses `task_only` and reports its unexamined queue; do not silently broaden it or claim executor-wide inactivity. Report scope, watched executors, verified SHA, pending/actionable/held IDs and incomplete reads. A TASK-local HOLD/BLOCKED does not suspend its executor or other eligible READY work; a wider restriction must be explicit in accepted state. A READY assignment still needs valid rights, inputs, capacity and stage gates, but not a second generic PM start message.

Carry unresolved assignments/questions forward from the complete metadata baseline while applying added/changed/deleted TASK and TEAM deltas. A last-seen SHA without its pending set cannot prove an empty queue: rebuild the bounded baseline. Previously observed READY work remains pending until intake/checkpoint evidence; no new delta is not the same as no work. Failed reads, unknown status mappings or incompatible adoption are `QUEUE_CHECK_INCOMPLETE`. Keep technical cache ignored; no service, committed inbox or per-pass report is required.

COO is a mandatory participant capability, not a mandatory separate role or chat. Default: one internal, exact-delta, read-only, dry, minimal-token helper covering that participant's executor IDs. It checks known IDs and performs bounded executor-scoped assignment discovery so a remote participant can find a newly assigned TASK that was not previously watched. No broad scan, second PM, acceptance gate, mandatory relay, or advancing past failed reads.

Each active participant has exactly one configured COO mode. An internal subagent returns findings to its invoking parent executor without registration, registry or wake. A same-chat check reports the role's own assignment locally and never wakes itself. A standalone COO is an optional registered executor and alone uses `notify_local`, local thread mapping and a dispatcher. Ambiguous mode stops as `COO_MODE_AMBIGUOUS`.

Setup/register offers a separate COO chat once and persists `accepted`, `declined`, or `not_supported`. Declining leaves internal mode active; the wizard does not ask again unless the participant requests a change. Accepting requires an explicit choice of an existing chat or creation request. Heartbeat is a separate opt-in and stays off by default. This baseline capability is independent of product-helper policy and grants no writes, cross-participant monitoring, external wake or PM authority.

Discovery reads `watched_executor_ids` from accepted TEAM. First use performs one metadata-only baseline of configured TASK frontmatter; later passes compare TASK metadata and relevant TEAM changes from ignored local `last_seen_default_branch_sha`. Match exact `owner_executor_id` and current revision before reading the complete TASK and linked provider events. Also match non-closed `questions` addressed to watched executors and check linked question routes for TASKs they issue/arbitrate, regardless of ownership. PM's mode also checks exact open onboarding channels recorded by `registration_id`; it does not scan arbitrary commit comments. Current actionable assignments at first baseline remain new until durable intake/checkpoint evidence proves acceptance.

When logical executors share one GitHub/TFS account, provider assignee, mention and unread state cannot route work. TASK ownership remains authority; an executor-specific provider label may optimize discovery but cannot replace it. Discovery/dedup state stays ignored and local—never add a committed inbox, polling journal or Messages replacement.

Exact `owner_executor_id` plus an actionable TASK status is sufficient assignment to the executor. Issue/PR assignment is not a second acceptance gate. An internal helper returns `RETURNED_TO_PARENT`; a same-chat check returns `ACTION_FOUND_LOCAL`, after which the parent/role may enter work through `r2team-work`.

### 13.5 Durable baton handoff

Every cross-executor transition, local or remote, uses the same TASK as the baton. Chat delivery is optional; assignment discovery must work without it.

1. PM defines the authorized transition table in the TASK. Each outcome names next status, next executor, active role and result recipient. A missing route stops at `ROUTE_REQUIRED`; the current executor does not invent an owner.
2. The current executor finishes the stage, publishes code/artifact/evidence refs, and prepares one TASK handoff checkpoint. Increment `handoff_seq`; set `previous_owner_executor_id`, `owner_executor_id`, `active_role`, `status`, `result_to_executor_id`, exact evidence and `next_action`.
3. An authorized assignment publisher publishes that TASK checkpoint to the accepted default branch through normal protection/review. Until publication succeeds, the handoff is `LOCAL_ONLY` or `SYNC_REQUIRED`, not delivered. Product code may remain on its feature branch/PR.
4. Update the linked Issue/PR with the exact TASK path, accepted commit, work ref/candidate and target logical executor. Apply the executor-specific routing label when configured. This notification cannot override the TASK.
5. The target's internal, same-chat or standalone COO discovers the default-branch TASK delta by `owner_executor_id` and `handoff_seq`. The target prints visible intake, verifies the checkpoint and starts through `r2team-work`.
6. The target returns PASS, FAIL, BLOCKED or another authorized outcome by repeating this sequence toward the route declared in the TASK. The resulting TASK checkpoint—not a chat response—is the durable return.

```text
Dev checkpoint -> TASK READY_FOR_QA, owner qa-remote, result_to dev40
QA PASS        -> TASK QA_PASSED, owner pm, result_to pm
QA FAIL        -> TASK QA_FAILED, owner dev40, result_to dev40, defect evidence linked
```

The previous owner is responsible for a truthful published handoff checkpoint and notification. The new owner is authoritative once the assignment checkpoint is accepted on the default branch; visible intake proves execution started. No intake is a delivery/attention problem, not grounds to erase or silently reassign the TASK.

Wake needs separate authority, confirmed local mapping on the participant's machine, one dispatcher, and deduplication. The remote PM never needs that machine's thread ID. Uncertain delivery is not blindly retried. Wake does not grant delegation/product rights. A send result is `SENT_UNCONFIRMED`; recipient visible intake plus the required TASK/provider reply establishes durable delivery. Missing route is `NOT_DELIVERED`.

Heartbeat is optional and off by default. Enable through supported scheduler only after manual verification, quiet when unchanged, with explicit scope. It cannot guarantee remote action.

### 13.6 Closed remote onboarding

Before inviting a remote participant, PM publishes an onboarding TASK with a stable `registration_id`, exact Issue/Work Item URL, `onboarding_result_to_executor_id`, objective `auto_accept_if` evidence, prepared `first_task_id`, and one activation mode: `IMMEDIATE_RESERVED` or `QUEUED_AFTER_REGISTRATION`. Empty `auto_accept_if` requires a new PM decision. A commit comment without a registered route is not a primary onboarding inbox.

The participant registers and posts one structured event to that exact channel:

```text
R2_EVENT: REGISTRATION_RESULT
registration_id: REG-042
from_executor_id: ken-qa
to_executor_id: pm-main
status: READY_FOR_ACTIVATION
evidence: <identity/access/skills/cross-check refs>
questions: none
```

A blocking question uses `R2_EVENT: ONBOARDING_QUESTION`, the same registration ID and exact PM recipient. PM's COO returns `REGISTRATION_READY`, `PM_ANSWER_REQUIRED`, or `REGISTRATION_BLOCKED`; COO does not publish. When the invitation already pre-authorizes objective acceptance criteria and the evidence matches, PM or the named publisher activates TEAM and the onboarding TASK without requesting the same owner approval again.

The first product TASK exists before invitation as `PENDING_REGISTRATION` or `PENDING_CAPACITY`. `IMMEDIATE_RESERVED` moves it to `READY` after accepted registration because capacity was reserved. `QUEUED_AFTER_REGISTRATION` keeps it queued until the explicit capacity condition is true; this is not a hidden approval. The remote participant's COO discovers the accepted `READY` TASK and enters `r2team-work`. Autonomous checks while all chats are idle require a separately authorized scheduler/heartbeat on the relevant machine.

<a id="setup"></a>
## 14. Setup

PM starts guided setup. Confirm purpose, paths, provider, constraints, people/functions/helpers, rights, docs/spec state, versions, communication, automation.

Preferred bootstrap is the optional persistent `R2Team Master - <project>` task using [R2TEAM_MASTER.md](R2TEAM_MASTER.md). Master collects the Project Charter, installs/verifies skills, creates/connects PM and later advises team lifecycle; it owns no project decisions.

1. Verify package and target root.
2. Select new/migrate/team/join/resume/audit.
3. Merge approved entry files.
4. Establish Git/provider and PM.
5. Configure TEAM/functions/rights/helpers.
6. Verify/install skills with approval.
7. Preserve/init OpenSpec as applicable.
8. Create first real TASK/item/branch/PR.
9. Publish and audit.

Create role chats only when requested; otherwise PM uses helpers. Role chat gets TEAM/role/TASK refs, cross-checks, and requests first task.

<a id="role-cross-check"></a>
### 14.6 Role cross-check

New/changed executor states participant/executor/functions; duties/outputs; boundaries/approvals/helpers; tools/spec inputs; queue/task/return route; unknowns. It accepts assigned TASK or asks PM for the first via existing route. No ACK file. Adding function cross-checks changed scope, not all setup.

Cross-check the accepted project source/ref against the actually loaded work/COO skills and any saved startup/watch prompt. A newer installed skill does not prove adoption. Demonstrate unknown-TASK discovery with one held and one eligible assignment, identify both question routes, and show how an addressed question on another owner's TASK is found. Record evidence/NOT_RUN in the existing adoption checkpoint; incompatible rules cannot certify a complete queue.

Ready means source/TEAM/rights known, tools verified or blocked, and a safe next action exists—not automatic product-work authority.

<a id="migration"></a>
## 15. Migration

Use [MIGRATE_TO_2.4.md](MIGRATE_TO_2.4.md). Preserve refs, code, filled specs, active OpenSpec changes/tasks, roles, evidence, dirty/unpublished work, and material requests.

Existing TASKs remain by default. User-approved fresh organizational queue may retire old message/task artifacts while explicitly preserving product/OpenSpec/current work. Never erase OpenSpec tasks.md.

For 1.10, mandatory MSG rules remain until approved per-task/coordinated cutover. Retained chats individually cross-check/adopt 2.4; replacing files alone is not chat migration. Resolve higher-priority instruction conflicts explicitly.

<a id="feature-example"></a>
## 16. Feature example

John is PM/Brain and local Dev; Maya remote Designer; Ken remote QA+DevOps; Lee remote Dev for returned fix. TASK-042 implements realtime notifications; TASK-043 handles independent deployment.

1. John/Brain uses openspec-explore; research records sources/findings/assumptions/UNKNOWNs, not decisions.
2. PM proposes/updates contract, obtains approval, publishes TASK-042 acceptance.
3. Maya performs design under same TASK and publishes UX decisions before Dev depends on them.
4. John/Dev restores checkpoint, applies with TDD, produces C1/tests/PR/checkpoint. Small consultations create no entity.
5. Ken tests C1; reconnect fails. QA records exact evidence and returns TASK to IMPLEMENTATION.
6. PM transfers same TASK to Lee with scope/PR/failure preserved. Lee debugs, publishes C2, returns to Ken.
7. Ken retests C2. Integrator reviews base/diff/spec/docs/checks, merges, records real SHA.
8. Independent deployment uses linked TASK-043. Ken switches to DevOps, confirms artifact/environment/rollback, deploys with authority, records smoke/runtime.
9. PM accepts actual scope; authorized owner syncs/archives OpenSpec when conditions are met.

~~~mermaid
sequenceDiagram
    participant PM
    participant Design
    participant Dev
    participant QA
    participant Lee
    participant Ops
    participant Git as TASK/OpenSpec/PR
    PM->>Git: contract and TASK-042
    Git->>Design: design
    Design->>Git: checkpoint
    Git->>Dev: implementation
    Dev->>Git: C1
    Git->>QA: verification
    QA->>Git: FAIL
    Git->>Lee: transfer same TASK
    Lee->>Git: C2
    Git->>QA: retest PASS
    PM->>Git: integrate/accept
    Git->>Ops: TASK-043
    Ops->>Git: deployment evidence
~~~

Local QA/DevOps changes routing only. Contract, ownership, evidence, independence, and publication stay identical.

<a id="team-examples"></a>
## 17. Team growth and shrinkage

- John alone: PM plus helpers/functions; honest self-verification.
- Local chats: TEAM records executors/rights; handoffs publish first.
- John and Ken: Ken joins QA+DevOps as one executor, two chats, or parent with helpers.
- Hybrid: Maya/Designer, Lee/Dev, local helpers, custom functions; ownership may move local -> remote -> local using same TASK.
- Shrink: publish affected checkpoints, investigate uncertain effects, transfer work, deactivate agreed assignments, preserve history.

Never-changing invariants: Git durability, one publisher, explicit assignment/rights, exact candidate/evidence, publication boundaries, PM acceptance.

<a id="validation"></a>
## 18. Readiness audit

Record PASS/BLOCKED/NOT_RUN with evidence:

- trusted package/version/ref and coherent files;
- one PM and valid people/executor/function/permission mapping;
- provider access/state mapping and Git/tracker synchronization;
- TASK owner/scope/acceptance/ref/candidate/next action;
- OpenSpec accepted/proposed/coverage separation;
- correct helper-result vs handoff publication;
- QA/DevOps evidence tied to candidate/environment;
- material questions/human actions recoverable without chat;
- local IDs/secrets excluded; routing/automation explicit;
- fresh executor explains next safe action.

Structural validation does not prove provider integration, behavioral skill quality, complete specification, or team adoption.

<a id="start-prompts"></a>
## 19. Entry prompts

First PM:

~~~text
Read START.md from verified R2Team 2.4 and run setup new or migrate for <project>.
Confirm root, provider, instructions, PM, functions, permissions and specs.
Show proposed diff before writes. Do not enable automation or start product
work merely by finishing setup.
~~~

Participant:

~~~text
Use $r2team register with the published invitation. Verify TEAM and provider
identity. Cross-check participant/executor/functions, rights, helpers, tools
and queue. Confirm assigned TASK or request the first from PM.
~~~

Resume:

~~~text
Use $r2team-work start <TASK-ID>. Read TEAM/role, task branch, provider state,
OpenSpec contract, exact candidate/evidence and open requests. Show intake,
preserve newer work and continue only within assignment.
~~~

Update/audit:

~~~text
$r2team-coo update
$r2team-coo check
$r2team-audit <project-or-TASK>
~~~

Update is read-only and quiet when unchanged. Check uses only authorized local wake. Audit never repairs.

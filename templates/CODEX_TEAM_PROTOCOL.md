# R2Team 2.2

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

Do not require six chats, COO, heartbeat, service, or full PRD.

Participant: verify provider identity, participant/executor/functions, permissions, tools/skills, contract, fetch/check/publish capability, and PM response route. Apply least privilege. One person may own several functions/executors.

Tool checks distinguish Git, OpenSpec CLI, project openspec directory, and installed OpenSpec skills. Pin trusted versions. Never expose credentials.

<a id="structure"></a>
## 5. Project structure

~~~text
AGENTS.md
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
        location: local
        helpers: [research, design, test]
  - participant_id: ken
    provider_identity: verified-remote-account
    executors:
      - executor_id: ken-ops
        functions: [QA, DevOps]
        location: remote
~~~

TASK owner_executor_id and active_role must match current TEAM. Locality is relative.

Any executor may use authorized bounded helpers. Parent supplies scope, paths, candidate, evidence, and return route; reviews output; remains publisher. Helpers do not take another executor's assignment, read unrelated inboxes, change role files, or publish independently. A standalone role chat may provide bounded help without ownership transfer under [OPERATING_COMMUNICATION.md](OPERATING_COMMUNICATION.md).

Record independence: same executor/subagent, different executor same person, different participant, or required independent reviewer. Chat renaming does not create independence.

Supported modes: one PM with helpers; one person with local role chats; remote people; any hybrid. Persistence and acceptance do not change.

<a id="task"></a>
## 7. TASK contract

Independent work creates/reuses one TASK, provider item, branch, and PR where applicable. Bounded consultation inside an accepted TASK creates no extra mandatory TASK/Issue/PR/MSG. Reuse the TASK across discovery, design, implementation, QA, integration, and handoff. Separate deployment TASK only for an independent lifecycle/owner/authority.

~~~yaml
protocol_version: "2.2"
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

States: DRAFT -> READY -> IN_PROGRESS -> REVIEW -> DONE, plus BLOCKED/CANCELLED. Stages: DISCOVERY, DESIGN, IMPLEMENTATION, QA, INTEGRATION, DEPLOYMENT. QA FAIL returns to READY/IMPLEMENTATION with evidence/owner. BLOCKED means no safe next action. Merge alone is not DONE.

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

QA tests exact candidate against TASK/OpenSpec and reports PASS/FAIL/BLOCKED/NOT_RUN with coverage. Green CI does not replace UI/manual acceptance. Candidate changes invalidate affected checks.

Integrator reviews base/diff/checks/docs/specs/authority, then records actual merged SHA. A report-only commit need not invalidate all evidence; code/config/base changes require impact assessment. Never label merged SHA verified without mapping/test evidence.

### 8.6 Deployment

Confirm exact source/artifact digest, environment, authority, migration, rollback, and pre-state. Record version/environment/smoke and uncertainty. Do not blindly retry a possibly successful side effect.

<a id="interaction"></a>
### 8.8 Human assistance

Explain why a human step is needed and affected account/environment; give one safe bounded step and expected evidence; avoid secrets; inspect response and guide the next step; continue until verified success, blocker, or pause. Human statement is not automated PASS. Continue independent safe work where possible.

### 8.9 Clarification and bounded help

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

Tracker is a projection of TASK in R2Team 2.2. Summarize provider-only continuation facts into Git.

Verify repo/default branch/policies/checks/permissions and merge/deploy effects. For Server also verify version/API, actual Work Item types/states, and tool compatibility; do not assume cloud-only CLI/MCP.

Provider writes are idempotent and read back IDs/links/revisions. On uncertainty inspect narrow target before retry. No bypass or duplicates. This package is a guide, not a live adapter; “request sent” is not completion.

<a id="specs"></a>
## 11. Specifications and documentation

- OpenSpec: accepted behavior/acceptance and proposed change.
- TASK: responsibility, plan, material execution state/evidence/blockers/next action.
- Architecture/C4/arc42: boundaries, components, data, deployment, risks.
- ADR/MADR: significant choices, alternatives, consequences.
- Runbooks/user docs: operation and use.

Use OpenSpec change for new behavior, API/security/data/migration/architecture or material contract change. A fix restoring accepted behavior may use existing spec.

Brownfield baseline is incremental: map capabilities to code/tests/docs; distinguish implemented, verified, intended, UNKNOWN; prioritize changed/risky areas. Inventory/CLI validation does not prove completeness.

Accepted specs live on default branch; proposed deltas on task branch. Do not duplicate versions unless product maintains them. OpenSpec tasks.md is not a message/status ledger.

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

Respect skill gates; archive after actual completion.

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

COO is optional PM subagent or registered helper. Default: exact-delta, read-only, dry, minimal-token reporting for known IDs/revisions. No broad scan, second PM, acceptance gate, mandatory relay, or advancing past failed reads.

Wake needs separate authority, confirmed local mapping, one dispatcher, and deduplication. Uncertain delivery is not blindly retried. Wake does not grant delegation/product rights.

Heartbeat is optional and off by default. Enable through supported scheduler only after manual verification, quiet when unchanged, with explicit scope. It cannot guarantee remote action.

<a id="setup"></a>
## 14. Setup

PM starts guided setup. Confirm purpose, paths, provider, constraints, people/functions/helpers, rights, docs/spec state, versions, communication, automation.

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

Ready means source/TEAM/rights known, tools verified or blocked, and a safe next action exists—not automatic product-work authority.

<a id="migration"></a>
## 15. Migration

Use [MIGRATE_TO_2.2.md](MIGRATE_TO_2.2.md). Preserve refs, code, filled specs, active OpenSpec changes/tasks, roles, evidence, dirty/unpublished work, and material requests.

Existing TASKs remain by default. User-approved fresh organizational queue may retire old message/task artifacts while explicitly preserving product/OpenSpec/current work. Never erase OpenSpec tasks.md.

For 1.10, mandatory MSG rules remain until approved per-task/coordinated cutover. Retained chats individually cross-check/adopt 2.2; replacing files alone is not chat migration. Resolve higher-priority instruction conflicts explicitly.

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
Read START.md from verified R2Team 2.2 and run setup new or migrate for <project>.
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

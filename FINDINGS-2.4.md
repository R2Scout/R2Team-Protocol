# R2Team 2.4 findings

## Problem

A remote executor can receive a valid Git assignment without knowing its TASK ID in advance. Provider notifications are insufficient when several logical executors share one provider account. A COO pass that finds the TASK can still fail incorrectly if it treats an internal helper as a standalone dispatcher and demands a local thread registry.

## Accepted model

- Accepted Git TASK is assignment authority. Exact `owner_executor_id` plus actionable status is sufficient.
- Remote discovery is executor-scoped: first bounded TASK-frontmatter baseline, then accepted-default-branch deltas.
- Provider assignee, mention, label and unread state are routing aids, not authority.
- Internal COO subagent returns the match to its invoking role; no wake or registry exists in this path.
- Same-chat COO check reports the match locally and lets that role enter `r2team-work`.
- Only a separately registered standalone COO performs local wake through ignored machine-local routing.
- Cross-executor work uses the existing TASK as a durable baton: `handoff_seq`, exact next owner/role/status, result recipient and authorized transition are published before notification.
- Heartbeat remains optional and off by default.

This closes the discovery/delivery gap without reintroducing committed Messages, polling journals or a second task queue.

## Onboarding wait defect

A valid remote registration can still stall when its result is posted to a provider location that PM's configured checks do not watch. A complete comment is not actionable if neither side has a durable route, activation rule, or prepared first TASK. Requiring the remote participant to forward the link manually recreates chat-dependent coordination.

## Candidate correction

- Every active participant has a COO capability. Internal is the default; same-chat or standalone are explicit alternatives. The standalone chat is offered once, is optional, and is created only on request.
- Heartbeat remains an independent optional mechanism and is off by default. Without a supported scheduler, an idle Codex cannot discover work autonomously.
- Each remote registration has a stable ID, exact onboarding Issue/Work Item, PM result recipient, objective evidence contract, prepared first TASK, and an explicit `IMMEDIATE_RESERVED` or `QUEUED_AFTER_REGISTRATION` capacity rule.
- The participant posts a structured registration result or addressed question. PM's COO watches only those registered channels and returns a factual state to PM; it remains read-only.
- PM or the named publisher may apply a pre-authorized activation without asking the owner to approve the same evidence again. The first TASK becomes `READY` only when registration and its declared capacity gate are satisfied.

This closes both directions of onboarding: the participant knows exactly where to return evidence/questions, and PM knows exactly what to monitor and publish next.

## Known-task HOLD hides another assignment

A report that one remembered TASK is still HOLD is correct for that TASK but cannot establish that its executor has no work. Another READY assignment may already be on the accepted default branch. The failure can arise from a frozen watch list, an explicitly narrow request, stale source, or mismatched project/skill adoption; the exact invocation is needed to distinguish these causes. Do not attribute an unobserved remote execution path to one cause without evidence.

The candidate now separates executor_queue from explicit task_only checks, requires fresh remote metadata discovery before queue-wide inactivity claims, and preserves pending assignments across unchanged-SHA passes. HOLD stays task-local unless a wider restriction is recorded. Incomplete checks have an explicit outcome. Setup/migration verifies actual role/skill adoption, including saved entry/watch prompts, rather than equating installed files with current behavior.

## Explicit clarification and arbitration routes

Every assignment carries Task Issuer and Project PM response routes, distinct from current owner, publisher and result recipient. ASK clarifies, LOOP seeks consensus on disagreement, and ESCALATE_PM may go directly to the authorized PM. Existing TASK/provider records carry mode, status, requester/respondent, blocking impact and Decision. Issuers and PM find addressed questions on other owners' tasks; answers return to the requester. Only dependent work pauses. PM authority cannot replace evidence, independent QA or mandatory human gates.

These rules add no messaging service or parallel queue. The scenarios are document-level acceptance criteria; live remote discovery, adoption and question exchange must be verified separately before claiming the operational problem is fixed.

## Route confusion: chat parent versus task baton

An executor can see a Codex chat that asked it to inspect work and mistake that physical parent for the recipient of its stage result. That is a protocol defect when the TASK does not make the result route mechanically distinct. It is especially harmful for remote roles: their local PM and chat topology can have no relation to the project PM or the original work issuer.

The candidate adds a mandatory Result Recipient: `result_to_executor_id`, exact `result_to_route` and `delivery_policy: git_checkpoint_then_tracker`. The five identities are now explicit: Task Issuer answers clarification; Project PM arbitrates; current owner executes; Result Recipient receives the stage outcome; assignment publisher records the checkpoint. Neither a chat sender, internal COO `RETURNED_TO_PARENT`, owner nor publisher can be substituted. Every task intake prints this Route Card and stops `ROUTE_REQUIRED` when it cannot be reconstructed.

TEAM records each executor's `location` and transport: remote/manual work uses only Git plus the provider route; local direct exchange remains optional and can announce but never replace the published baton. This keeps the protocol Git-first without adding a message queue, a service or remote chat registry.

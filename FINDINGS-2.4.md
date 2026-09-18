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

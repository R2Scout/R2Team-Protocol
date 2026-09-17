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

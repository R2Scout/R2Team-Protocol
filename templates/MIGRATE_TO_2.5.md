# Migration prompt: R2Team 2.4 to R2Team 2.5

Target: R2Team `protocol_version: "2.5"` from a trusted full commit or verified bundle. This migration consolidates the 2.4 queue/onboarding/question candidates and adds the unambiguous Route Card. It does not authorize product work, merge, deployment, heartbeat, chat creation or an installed-skill replacement.

## Read-only preflight

1. Verify accepted protocol/TEAM/TASK root/default branch, active writers, unpublished work and current provider routes.
2. Verify the complete 2.5 package and manifest at the approved full commit. Never substitute `main/latest` for that commit.
3. Inventory active executors, their `mode`, `location`, direct-exchange policy, COO mode and actual loaded work/COO skills.
4. Preserve active TASKs, OpenSpec changes, branches, PRs, evidence, open questions and historical handoffs.

## Proposed changes

1. Update adopted protocol files and `protocol_version` to 2.5 through the normal protected Git/provider workflow. Increment the project `integration_revision`.
2. Keep one COO capability per active participant, executor-wide discovery, closed remote onboarding and Task Issuer/Project PM questions from 2.4. Do not enable heartbeat or create a separate COO chat as part of this migration.
3. For every active TASK, at the next approved checkpoint add or verify:
   - `owner_executor_id` and exact `owner_route`;
   - `task_issuer_executor_id` / `task_issuer_route`;
   - `project_pm_executor_id` / `project_pm_route`;
   - `result_to_executor_id` / `result_to_route`;
   - `delivery_policy: git_checkpoint_then_tracker`.
4. Update each authorized transition table so every outcome names next owner, exact next owner route, role/status, and the following stage's result recipient/route. Preserve historical checkpoints; do not rewrite them merely to normalize fields.
5. Record executor `location: local | remote` and transport in TEAM. `remote_manual` uses Git plus provider routes only. Local direct exchange is optional and cannot replace a durable handoff.
6. Require a Route Card before the next work session: current owner/route, Task Issuer, Project PM, result recipient/route, delivery policy and mode/location. A missing, stale or conflicting route is `ROUTE_REQUIRED` through `project_pm_route`.
7. Treat `RETURNED_TO_PARENT` as an internal COO finding only. It is never a TASK result, PM route, task issuer route or chat handoff.
8. A completed stage makes the current `result_to_*` recipient the next owner, copies its route into `owner_route`, records the following stage's result route, publishes to the accepted default branch, then notifies only the new `owner_route`.

## Cutover verification

- A Route Card identifies all four routes without inferring one from chat history.
- A remote executor returns through the declared result route; it does not use a local PM, local registry or direct chat.
- A Dev-to-QA transition makes QA the new owner and records the destination of QA's future PASS/FAIL separately.
- Internal COO `RETURNED_TO_PARENT` returns only to the invoking role and never changes TASK routing.
- An absent/ambiguous route yields `ROUTE_REQUIRED`, not a guessed recipient.
- Existing queue, question and registration regression scenarios remain valid.

Run package/project checks and verify exact refs. Publication of files alone does not prove participant adoption; each retained executor must cross-check its loaded instructions and its first Route Card.

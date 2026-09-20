# R2Team 2.5 findings

## Consolidated candidate

R2Team 2.5 consolidates the candidate work previously developed for 2.4: executor-wide discovery, retained pending work across unchanged Git deltas, closed remote onboarding, explicit Task Issuer/Project PM question routes, and mandatory per-participant COO capability.

## Route Card correction

Chat topology is not task topology. A chat that invokes an executor, a local PM, a checkpoint publisher and a Task Issuer can all differ from the recipient of a completed stage. Treating any of them as an implicit return address creates cross-host delivery errors.

Every independent TASK now has four named routes:

- current `owner_executor_id` plus `owner_route`;
- Task Issuer for clarification;
- Project PM for arbitration;
- `result_to_executor_id` plus `result_to_route` for the current stage outcome.

The Route Card displays them before work. On a handoff, the current result recipient becomes the new owner, its route becomes `owner_route`, and the checkpoint declares the following stage's result route. The accepted default-branch checkpoint is published first; only then is the new owner route notified.

## Remote transport

An executor with `mode: remote_manual` and `location: remote` uses `git_checkpoint_then_tracker`. It has no implicit cross-host chat or local-registry fallback. `RETURNED_TO_PARENT` is an internal COO result to its invoking role only, never a product handoff.

These are protocol rules and structural checks. Live role adoption and provider behavior remain separate evidence and must be tested in each project.

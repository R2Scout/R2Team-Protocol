# R2Team change history

## 2.3

- Add `R2TEAM_MASTER.md` as the persistent bootstrap and procedure-consultant entry point while keeping PM as the only mandatory coordinating function.
- Model participants, functions and executors independently, including local tasks, remote participants, persistent named subagents and ephemeral helpers.
- Separate portable invitations from machine-local launch envelopes and keep local task routing out of Git.
- Add one reusable Project Charter for production and synthetic-pilot setup, with a conditional Pilot Addendum only when a pilot is requested.
- Verify Git, tracker, pull-request, policy, CI and deployment capability planes independently instead of inferring one from another.
- Strengthen exact-candidate QA, provider read-back, completed/merged-state evidence and repository-qualified multi-repository checkpoints.
- Define ordered OpenSpec finalization and allow explicitly conditional artifacts without treating their absence as incomplete work.
- Add a controlled 2.2/older migration procedure and publish the generalized 2.3 findings used by setup, protocol and skills.

## 2.2

- Make `protocol_version` the sole release identifier: major is the protocol generation and minor increments for each protocol revision.
- Remove `package_revision` and `protocol_package_revision` from the distribution and project templates.
- Publish the versioned migration source as the official `v2.2` release without rewriting the immutable 2.1 release.

## 2.1 — package revision 1

- Make bounded local/remote role communication and internal helper delegation first-class transient coordination inside an accepted TASK.
- Separate OpenSpec product contract, TASK recovery state, and transient exchanges; retain four material publication boundaries and one publisher.
- Preserve direct discussion without mandatory MSG/ACK/report files while formal ownership transfer remains Git/provider-first.
- Add durable question/consensus, human-assisted actions, uncertain-delivery, recovery, and team growth/shrink procedures.
- Keep generic GitHub and Azure DevOps Server/TFS Git projection in the main package; publish the specialized CMMI protocol separately.
- Align setup, roles, provider guide, command help, four skills, scenarios, migration prompt, validator, and manifest.
- Translate all maintained public distribution content to English.

## 2.0 — package revision 1

Initial self-contained R2Team distribution with setup, flexible team lifecycle, TASK/PR workflow, four instruction skills, and payload validation. Historical source remains under tag `v2.0`.

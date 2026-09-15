# R2Team change history

## 2.2

- Make `protocol_version` the sole release identifier: major is the protocol generation and minor increments for each protocol revision.
- Remove `package_revision` and `protocol_package_revision` from the distribution and project templates.
- Rename the candidate and migration source to 2.2 without rewriting the immutable 2.1 release.

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

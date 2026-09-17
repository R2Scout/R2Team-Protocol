# R2Team 2.3 generalized findings

These findings originated in end-to-end team/protocol exercises. They are provider-neutral rules unless explicitly marked provider-specific. Project-local identities, URLs and credentials are intentionally excluded.

## Team and routing

- Separate human participant identity from logical executor identity. One person/account can operate multiple local, remote or subagent executors.
- Explicitly choose executor mode: existing local task, new local task, persistent/ephemeral subagent, or remote/manual participant.
- Durable invitations remain portable and contain no local task IDs. Local launch routing is a separate ignored envelope and requires direct onboarding return; otherwise delivery is `NOT_DELIVERED`.
- A separate chat gives context isolation, not independent human review. Record the real QA/reviewer independence level.
- A persistent subagent with its own queue can be named in TEAM; a bounded ephemeral helper reports through its parent and is not separately registered.

## Provider and Git state

- Git ref access does not prove tracker, PR/review, browser, CI, release or environment access. Diagnose capability planes independently.
- Provider writes require exact read-back. Use supported concurrency/revision checks where available and inspect a narrow target before retrying uncertain writes.
- Mergeability is not merge completion. Require provider completed/merged state, actual merge commit and remote default-branch equality; fetch before local inspection.
- QA binds evidence to an exact candidate and preserves a concise result in TASK plus the provider PR/review route when both exist.
- For multiple repositories, identify every repository, branch, PR and candidate independently. One SHA cannot represent the whole coordinated change.

## Procedure and specification

- Use one Project Charter for production and synthetic modes so setup does not repeatedly ask known team/provider questions. A Pilot Addendum is conditional on synthetic mode.
- Execute an approved long workflow as small resumable mechanical steps. Ask again only on drift, failed validation, denied authority, ambiguous writes, irreversible effects or a new material choice.
- OpenSpec finalization is ordered: verify implementation; sync every declared delta into accepted specs; verify equivalence; archive; publish accepted specs/archive/TASK; then close the provider item.
- A schema-declared conditional artifact may be absent without making a change incomplete. Verify the actual schema rather than counting files.
- Classify new observations as project-local, provider/version-specific or protocol-general before changing normative protocol rules.

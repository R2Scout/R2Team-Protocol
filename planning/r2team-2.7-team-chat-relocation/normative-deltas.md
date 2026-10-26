# R2Team 2.7 normative deltas

## Version and scope

- An unreleased implementation candidate MAY identify its package/protocol payload as a `2.7` candidate for exact-candidate validation. Accepted distribution release and downstream project adoption MUST remain separately gated and MUST NOT be inferred from candidate labeling.
- 2.7 MUST add physical team/chat relocation without redefining participant/function transfer.
- A 2.6 project MUST remain unchanged until an explicit project-local 2.7 adoption.

## Identity

- Participant, logical executor, TASK, candidate, workspace lease, physical chat/host, and migration identity MUST remain distinct.
- Same-executor relocation MUST preserve participant, executor, TASK, provider item, candidate, and evidence identity.
- Changing participant, function owner, or executor ID MUST use the existing ownership-transfer workflow before relocation resume.
- Committed state MUST NOT contain populated physical thread IDs, machine-private paths, secrets, or chat transcripts.

## Authority and skill boundary

- PM MUST authorize each migration ID, affected executors, mode, source cutover, target placement, writer transition, startup order, and rollback rule.
- Relocation MUST NOT infer chat creation, access change, credential copy, process stop, workspace cleanup, archive, deletion, merge, deployment, or release authority.
- Operational relocation MUST use the separate `r2team-relocate` entry point unless an independently accepted narrower boundary replaces it.
- Existing `r2team migrate <function> to <participant>` semantics MUST remain function transfer.
- `r2team-work` MUST NOT hide prepare, freeze, registry remap, resume, or relocation completion mutations.

## Durable migration bundle

- Every relocation MUST have one accepted `migration_id` and global `MIGRATION.md` record.
- Whole-team relocation MUST include one per-executor handoff record for every affected executor.
- Handoffs MUST reference current accepted TASK/candidate/evidence/checkpoint/route/workspace facts rather than duplicate them or depend on transcript/local state.
- Missing or unpublished TASK state MUST block prepare or resume.

## Writer fencing

- At most one physical placement MAY hold accepted writer authority for one executor/TASK. Cooperative fencing MUST NOT claim that an unfenced offline process is physically impossible; it MUST reject that process at every compliant publication entry point.
- Every affected executor MUST have a fencing record keyed by repository/project identity plus logical executor ID; a global cutover generation MUST NOT replace its per-executor epoch.
- A successor fencing record MUST name the expected prior epoch and prior accepted record and MUST be compare-and-published against accepted default-branch state. A changed epoch or causal parent MUST fail closed.
- Two proposals with the same next epoch MUST NOT both be treated as valid; only the accepted causally linked successor is current.
- Source writer MUST be proven stopped before `READY_TO_RESUME`.
- Target writer MUST NOT become active until accepted cutover read-back, local cross-check, and its resume receipt.
- Unknown, conflicting, or concurrent writer claims MUST produce `WRITER_CONFLICT` and block product work.
- Every writer-capable R2Team entry point MUST re-read accepted fencing state immediately before product/TASK publication and MUST reject stale, equal-conflicting, or causally unrelated state.
- Protocol fencing MUST be described as cooperative unless a separate receipt proves provider-enforced exclusion.
- An accepted fence MUST match an explicit legal `(source_state, target_state, custody)` tuple. Source and target MUST NOT both be writer-capable, and custody MUST agree with the sole writer-capable placement.

## Freeze and resume

- Whole-team prepare MUST pass through `FREEZE_PENDING` and `FROZEN` before `READY_TO_RESUME`.
- Each executor MUST expose source `ACTIVE -> STOP_REQUESTED -> STOPPED` and target `INACTIVE -> PREFLIGHTED -> READY -> ACTIVE` substates.
- A blocked state MUST retain `blocked_from_state`, owner, review date, next action, and permitted successor; it MUST NOT be an unrecoverable dead end.
- `PARTIAL_BLOCKED` MUST derive custody from per-executor records and MUST permit return to `RESUMING`, terminal accounted disposition, or forward rollback without rewriting already active targets as source-active.
- An executor MAY be `retained` only when removed from the affected set by an accepted prepare revision before `FREEZE_PENDING`; an affected frozen executor MUST NOT remain an ambiguous source-active exception.
- After `FROZEN`, old product writers MUST NOT publish product/TASK changes; only the named migration PM MAY publish the declared migration-control paths and governing relocation-TASK status/evidence fields.
- Freeze state MUST be a strict boolean; unknown or coerced freeze input MUST fail closed before publication-class handling. Declared publication paths MUST reject control characters, traversal, nonportable separators, duplicate separators, and leading/trailing segment whitespace.
- Target PM MUST follow the accepted startup order and MUST record roles that remain blocked/not-run.
- A local notification, chat title, copied prompt, or registry entry MUST NOT open the resume gate.

## Local registry

- Populated executor-to-thread mappings MUST remain in ignored `.codex-local/THREAD_REGISTRY.md` or equivalent accepted local state.
- Local registry updates MUST require local owner authority and read-back.
- Local mapping MUST NOT grant assignment, ownership, permission, provider identity, writer epoch, or acceptance.
- Durable registry evidence MUST contain only an enum/result plus authority/host class; it MUST NOT contain a physical ID/path, transcript, or stable hash of a private identifier.
- Registry remap MUST validate executor identity and collisions and MUST NOT make a local mapping mandatory for remote/manual executors. The remote/manual absence exception MUST require no observed executor and no collision or contradictory present/absent evidence.

## Workspace custody

- Relocation MUST reconcile every affected active workspace lease under the adopted 2.6 lifecycle.
- Workspace reuse on the target MUST require verified owner, exact candidate, mutability, custody, containment, dependency, and local-resource facts.
- Relocation MUST NOT imply physical workspace movement or cleanup; retain, transfer, close, or allocate through `r2team-workspace` with evidence.

## Recovery and rollback

- Cancellation before source stop MAY retain the current source epoch through an accepted cancellation receipt.
- Cancellation after source stop/freeze MUST NOT silently revive it; source reactivation requires an accepted successor and activation receipt.
- Failure before target activation MUST retain a named safe writer or remain blocked; it MUST NOT silently activate either side.
- Rollback after target activation MUST be a forward accepted publication with a higher writer epoch.
- Reset, force-push, transcript replay, or stale local mapping MUST NOT restore writer authority.

## Evidence and completion

- Prepare, source-stop, freeze, target-preflight, activation, partial-disposition, completion, cancellation, and forward-rollback receipts MUST be immutable, uniquely identified, append-only, and causally linked against an external accepted-root ref, affected-executor set, and explicit role/team mode.
- Each receipt MUST bind the applicable migration/executor, prior/new epoch, causal parent, accepted commit, TASK/candidate refs, workspace and close-receipt refs, actor/provider identity class, observed outcome, blocker, timestamp, and review date without private local identifiers.
- Source-stop evidence MUST include the final accepted checkpoint/tree, outstanding publisher/helper state, workspace/native-resource custody, observed stop mechanism, and cutover parent. Silence, notification, registry state, chat title/archive, or unobserved process absence MUST NOT prove stop.
- Source-stop evidence MUST require exact typed outcome `SOURCE_STOPPED`; unknown, blank, blocked, or still-running outcome MUST fail stop, activation, and graph validation.
- If a source is unreachable and no independently enforceable fence/revocation exists, target activation MUST remain blocked.
- Every public activation decision MUST consume an included same-identity PASS preflight receipt; a reference alone or optional graph-only check MUST NOT authorize activation.
- In team mode every target preflight MUST explicitly reference the exact full-set FREEZE. Every referenced stop MUST be strictly earlier than FREEZE, and FREEZE MUST be strictly earlier than preflight, which MUST be strictly earlier than activation; list order, equal instants, or later sibling FREEZE presence MUST NOT authorize preflight, activation, or completion.
- Completion MUST require exactly one PREPARE and one shared migration/project/evidence lineage. Team completion MUST require a FREEZE whose affected/stopped sets and exact initial stop refs equal the accepted context. A completion-capable disposition MUST equal the unique latest causal stage for each executor; an older terminal receipt MUST NOT complete over a newer nonterminal stage.
- Every receipt type MUST have declared enum/range semantics and an allowed resolved parent. Receipt types MAY recur for the same executor in later causal epochs, including new stop/preflight/activation generations after forward rollback; the same executor/type/epoch/parent logical event MUST be rejected. Completion MUST select one unique latest activation, cancellation, forward rollback, or typed terminal BLOCKED disposition per executor.
- Aggregate state MUST take the exact affected set and validated receipt context, require one legal state/custody record per executor, validate terminal owner/date/action/ref evidence, and use the same unique latest causal-stage resolver as receipt-set completion. Every record in a mixed aggregate, including PENDING/INACTIVE peers, MUST match its latest stage and typed disposition. Same-epoch alternatives MUST be `INVALID`, except one activation consuming its one supporting preflight in that generation. Historical PASS/activation evidence MUST NOT satisfy a state after a later blocked, cancelled, or rolled-back generation.
- Aggregate state MUST validate nonempty minimum receipt/fence evidence before returning FROZEN, READY_TO_RESUME, or RESUMING; supplied malformed context MUST NOT be ignored on non-COMPLETE paths.
- A role is resumed only after its own receipt and current assignment/capacity gates pass.
- Team relocation is complete only when every affected executor is resumed or has a terminal accounted blocked/cancelled/rollback disposition with owner, review date, and next action. A retained executor removed before freeze is outside that affected set and remains listed in the prepare history.
- Protocol/package tests MUST NOT perform live chat creation, registry mutation outside isolated fixtures, workspace cleanup, process stop, or real relocation.

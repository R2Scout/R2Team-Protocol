# R2Team 2.7 findings

## 1. Logical work identity is not physical placement

Participant, executor, TASK, candidate, workspace lease, physical chat/host, and migration ID are separate. A safe relocation preserves durable logical identity and replaces only the physical execution placement. A changed participant, function owner, or executor uses ownership transfer first.

## 2. Monotonic integers are not enough

Two concurrent branches may propose the same next epoch. Safe fencing therefore binds the expected prior epoch and prior accepted record, compare-and-publishes against accepted default-branch state, and reads the winner back. The integer and causal parent are one contract.

## 3. Fencing strength must be stated honestly

R2Team can require every compliant writer entry point to reject stale state. That is cooperative protocol fencing, not proof that an offline/unfenced process is physically impossible. Provider-enforced exclusion needs separate administrative evidence.

## 4. Whole-team state is derived

A single global writer triple loses custody during partial cutover. Each executor needs source/target substates, epoch, causal receipts, and disposition. `PARTIAL_BLOCKED` can then preserve active targets and stopped/blocked peers without inventing a fallback writer.

A migration may complete with a mixture of resumed executors and terminal-accounted blocked, cancelled, or forward-rollback dispositions. Each terminal record needs an owner, review date, next action, and receipt; an incomplete terminal label remains partial/blocked.

## 5. Stop is positive evidence

Silence, notification, registry absence, chat title/archive, or no observed process is not stop proof. A valid stop receipt binds the final accepted checkpoint/tree, outstanding publishers/helpers, workspace/native resources, mechanism, actor class, and cutover parent. An unreachable source without enforceable revocation remains blocked.

## 6. Local mapping is private routing, not authority

The ignored registry can map executor to physical chat locally, but durable evidence records only an enum/class. Publishing a stable hash still leaks a linkable private identifier and is prohibited. Remote/manual executors remain valid without local mapping.

## 7. Cancellation is not time travel

Before stop, an accepted cancellation may retain the current source. After stop/freeze, source reactivation needs a new successor and receipt. After target activation, rollback is forward-only with a higher epoch. Reset, force-push, transcript replay, and stale mapping cannot restore authority.

## 8. Relocation does not own workspaces

Candidate equality alone is insufficient for workspace reuse. Custody, host, containment, dependency, native-resource, owner, mutability, and recovery facts must match. Movement, cleanup, archive, branch deletion, process stop, and data relocation remain separate authorities.

## 9. Freeze must be exhaustive

A freeze cannot block only product code while allowing TASK, TEAM, or misspelled publication classes. Every class is enumerated and default-denied. Only the named PM may write canonical declared migration-control paths and the exact governing relocation-TASK status/evidence fields.

## 10. Receipt names are not receipt evidence

Uniqueness alone does not make a receipt typed or causal. Every receipt needs a nonblank ID, known type, migration/project/executor and epoch facts, causal parent, accepted commit, TASK/candidate/workspace references, actor/provider class, outcome, registry evidence, timestamp, and its type-specific facts.

The activation API must compose the same complete typed `SOURCE_STOP` validator; a smaller stop-specific subset creates a bypass. Receipt-set validity also requires causal closure: every activation edge resolves to exactly one included `SOURCE_STOP` with matching migration/project/executor/cutover/epoch and custody references. Epochs use strict non-boolean integers, and exact governing-TASK field lists use validated collections rather than generic iterables.

Strict typing applies at every authority boundary, not just serialized receipt epochs: accepted fences, successor proposals, writer claims, stop expected epochs, recovery inputs, reference lists, singular checkpoint/tree/custody/cutover facts, dates, timestamps, registry flags, workspace facts, and affected sets all fail closed on coercion. A source-stop common causal parent equals its accepted cutover parent unless a separately modeled intermediate parent is introduced.

## 11. Valid labels still need a valid state graph

Individually known fence states, custody labels, receipt types, and registry enums are not freely composable. The protocol accepts only explicit single-writer fence tuples, exact cutover/commit and mapping/evidence pairs, and a receipt graph rooted in an accepted record with typed per-type outcomes and a complete affected-executor context. Unknown freeze state, contradictory remote-manual mapping observations, orphan receipts, duplicate logical events, incomplete completion accounting, and control-character paths all fail closed.

## 12. Append-only history and aggregate state share one lineage

An activation API cannot outsource PASS-preflight proof to a different optional graph check. Completion needs one external accepted root, exactly one PREPARE, one migration/project/evidence lineage, and an explicit role/team mode; team completion also needs a full affected-set FREEZE. Receipt types may recur at later causal epochs, while duplicate logical events remain invalid. Aggregate state is accepted only for the exact unique affected records and the unique latest causal stage per executor, including non-complete states; historical PASS preflight or activation evidence cannot override a later blocked or rolled-back generation. Same-epoch alternatives are ambiguous, except that one activation may consume its one supporting preflight in the same generation. Arbitrary dictionaries, impossible state/custody tuples, malformed terminal evidence, ambiguous branches, or older generation receipts return `INVALID`.

## 13. Positive outcomes and barriers are authority facts

A structurally complete SOURCE_STOP with an arbitrary outcome is not stop proof; only the exact typed `SOURCE_STOPPED` outcome can open activation. A team FREEZE must be an explicit referenced ancestor/gate of every target preflight, with consistent identity/epoch and the strict temporal order `SOURCE_STOP < FREEZE < TARGET_PREFLIGHT < ACTIVATION`, not a sibling receipt or a barrier timestamp equal to/later than its stop. Receipt context supplied to aggregate derivation is authoritative for every state, including FROZEN, READY_TO_RESUME, and RESUMING; empty, malformed, unresolved, missing, or extra context returns `INVALID`.

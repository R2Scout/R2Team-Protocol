# Migrate an adopted project to R2Team 2.10

Pin the exact verified annotated v2.10 release commit, not main/latest. The previous project protocol governs until its own accepted adoption checkpoint is published/read back. Release publication and skill installation are not adoption.

## Naming correction

Adopt [Git worktree directory policy](GIT_WORKTREE_DIRECTORIES.md): new ordinary linked Git worktrees are direct children of the accepted root, named `<project>-<git-work-ref>-<perm|task|tmp>-<executor>[-<purpose>]`. Remove the extra physical/native ID from the ordinary naming rule; retain technical lease/resource/native IDs in registry/custody records.

Work references match the accepted primary Issue/TASK/PR/Work Item identifier and actual number. Explicit types distinguish equal numbers. Standing anchors have real governance TASKs. A purpose suffix is allowed only for an already accepted distinct lane, such as build/integration; it cannot bypass collision, reuse, budget, or single-writer gates. The pure directory-name helper now accepts project/work/executor/lifetime plus optional purpose/custody, without a native-ID naming argument.

Lifetime/purpose separation, owners, bound close conditions, review, retention, and recovery remain governed by [RESOURCE_LIFETIME.md](RESOURCE_LIFETIME.md). Names and matching Git numbers grant no cleanup or promotion authority.

## Preserve existing custody

Inventory current TASKs, refs, candidates, evidence, routes, actual Git/application-managed worktrees, roots, and unpublished material. Existing primary/legacy directories, including older ws-prefixed names, remain protected and reusable. Application-native root/hierarchy/IDs remain controlled by the application; do not remove its path layers to implement ordinary naming. Adoption performs no rename, move, removal, decommission, or resource allocation.

New ordinary names use the approved root, disjoint from evidence/output/log/tmp/cache roots. Reconcile occupied targets as exact reuse or blocking conflicts; never append a counter/retry suffix. Keep actual observations and root mappings local.

## Project cutover

Reconcile AGENTS/TEAM/protocol, used roles, TASK/local-observation templates, commands, skills, and [PM prompt](PM_PROTOCOL_UPDATE.md). Compare loaded skills and saved entry instructions with the pinned package; preserve customizations/rollback on authorized replacement. For older projects, reconcile intervening requirements from [2.6](MIGRATE_TO_2.6.md), [2.7](MIGRATE_TO_2.7.md), [2.8](MIGRATE_TO_2.8.md), and [2.9](MIGRATE_TO_2.9.md); no intermediate project release is required.

Validate the package, four offline suites, six skill formats, hashes/links/privacy/portability, and command-copy equality. The naming fixtures verify Git-reference-only names, typed references, declared purpose suffixes, unsafe/long-component rejection, and application/legacy protection; they perform no actual resource mutation.

PM publishes one organizational checkpoint with exact package provenance, coherent policy, active-work/legacy reconciliation, owners/review dates, verification/NOT_RUN evidence, and recovery route. Read back the accepted branch, notify retained executors through existing authorized routes, and have them cross-check roles and loaded instructions. A still-governing 1.10 communication contract remains until an approved cutover resolves it.

# Findings behind R2Team 2.6

## Problem

The protocol already bound work to TASKs, branches, candidates, and evidence, but did not govern the lifetime of physical materializations. Under concurrent revisions, corrections, handoffs, and review, a directory was often treated as the identity of the work and new persistent worktrees accumulated without a closure owner or recoverable terminal disposition.

## Generalized findings

1. TASK, immutable candidate, and physical workspace are different identities. A revision or handoff changes responsibility/state, not necessarily storage.
2. Capacity is an allocation gate, never cleanup authority. Low disk should stop new placement before it triggers unsafe deletion.
3. Acceptance and custody are separate evidence axes. A valid candidate verdict survives a failed close; a clean close does not establish product acceptance.
4. Merge completion is the start of closure review, not proof of closure. Provider read-back must establish the actual integrated SHA first.
5. Evidence suitable for Git belongs in the same protected checkpoint. Non-Git evidence needs sanitized hash-bound durable custody, not a chat/log/worktree-only reference.
6. Temporary material is not defined only by filename or age. Removal needs verified evidence export, exclusive ownership, no dependent process/lease, no shared/retained role, target containment, and pre-existing explicit authority.
7. Application-managed worktrees retain application custody. Their lifecycle should use the application archive operation, not generic filesystem removal.
8. Physical paths are local observations. Portable project policy uses logical leases and root aliases; ignored local state maps them to a machine.
9. Lifecycle operations need a distinct skill boundary. Hiding allocation/closure inside ordinary TASK execution makes authority and side effects hard to inspect.
10. Governance changes should not bundle unrelated relocation. Team/chat relocation has different evidence, rollback, and acceptance needs and therefore remains a distinct later change.
11. A blocking lease state is not terminal custody. It preserves the product verdict but prevents administrative completion until the lease becomes closed, retained-protected, or transferred with required evidence.
12. A default-budget exception is a structured, expiring exact-lease decision. It never bypasses project hard caps, disk floors, reuse-only bands, single-writer custody, containment, or evidence gates.

## Consequence

R2Team 2.6 adds bounded workspace leases, default budgets and capacity profiles, durable merge-evidence requirements, closure receipts, terminal/blocked dispositions, role duties, migration guidance, validator fixtures, and the separate `r2team-workspace` skill. It does not perform live cleanup, replace installed skills, relocate teams/chats, or adopt downstream projects.

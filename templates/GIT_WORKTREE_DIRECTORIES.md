# Git worktree directory formation and naming

## Exact terminology

Use **Git worktree** when describing a Git working copy, its directory, creation, reuse, or closure. Use **resource** for the broader lifetime policy covering Git worktrees, test data, build output, logs, caches, evidence, and runtime resources. Workspace is a broader execution environment; it is not an unqualified synonym for Git worktree. A plain archive or output directory is not a registered Git worktree.

The existing command `r2team-workspace`, schema field `workspace_leases`, and lifecycle anchor remain compatible technical names. User-facing instructions about Git working copies explicitly say Git worktree. Their names do not require a command/schema rename or another worktree.

## Approved root and flat placement

The project declares one ordinary Git worktree root via an accepted portable root alias in TEAM. Its physical mapping is kept locally. A newly allocated ordinary linked Git worktree is a direct child of that approved root:

```text
<approved-git-worktree-root>/<native-id>-<project>-<work-ref>-<perm|task|tmp>-<executor>
```

For example:

```text
<approved-git-worktree-root>/
  ws0042-crm.ai-base-perm-devops/
  ws0043-crm.ai-task3244-task-dev10/
  ws0044-crm.ai-task3244-tmp-qa2/
```

Do not add parent folders for chat titles, TASK revisions, dates, retry numbers, test batches, or verdicts. Existing project-approved root placement is preserved; do not move it just to match an example. Worktree roots and evidence/artifact/output/log/tmp/cache roots must be disjoint, with neither containing the other. A tmp lifetime token belongs in the worktree leaf name; it does not authorize placement in a disposable output or system Temp root.

Separately authorized external placement still requires its own approved root/containment evidence. It follows the ordinary leaf-name rule but does not silently expand the project's configured roots. Validate the full resolved target and filesystem path limits before creation, including links/junctions that could escape the approved target.

## Directory components

Preserve the existing native worktree number/ID. Do not introduce a second global counter or guess an ID from a TASK number. The approved allocator supplies a new ID once for a genuinely new lease. The name adds the stable project alias, typed work reference, lifetime token, and executor alias from [RESOURCE_LIFETIME.md](RESOURCE_LIFETIME.md).

Native IDs use lowercase ASCII letters/digits with internal hyphens or underscores and at most 64 characters. Reject missing IDs, path separators, drive prefixes, leading/trailing separators, dots, spaces, and wildcard/control characters; never silently normalize an existing unsafe name. The readable resource label keeps its existing 96-character limit. Native IDs and physical directory observations remain local, not public TASK identity.

Lifetime tokens mean persistent/perm, task_scoped/task, and ephemeral/tmp. Purpose such as dev/qa/build/release remains separate; do not derive lifetime from the owner's role. Labels describe the allocation context and are not current ownership, candidate, or deletion proof.

## Reuse before creation

First inspect the accepted TASK, complete physical inventory, deterministic materialization key, and compatible existing lease. Exact compatible reuse keeps the ID and actual directory, even if its historical leaf name does not match a newer label. A new TASK revision, handoff, chat title, owner, lifetime label, or review result never creates another worktree by itself.

Before an authorized new allocation, form the planned leaf name under the approved root. An occupied target is reconciled: reuse the exact compatible lease or return ALLOCATION_BLOCKED on conflict. Do not append another date, counter, or retry suffix to bypass a collision. A partial create is inventoried and reconciled before retry. After creation, read back the real Git registration, path, branch/HEAD/tree, owner, custody, and lease identity.

The pure reference function `git_worktree_directory_name` in `scripts/workspace_policy.py` checks ordinary/external leaf names only. It performs no allocation, root selection, filesystem containment, process stop, or rename. Operators still apply all existing allocation and closure gates.

## Application and existing-directory custody

Codex-managed Git worktrees retain the application's native root, hierarchy, ID, and repository-folder layout. Use supported application controls for creation/archive and any supported display-name field. If no supported name field exists, record the readable label in the local registry and report that limitation; never fabricate a renamed directory. The ordinary leaf-name helper rejects application-managed and legacy custody.

Existing primary checkouts and legacy Git worktrees are inventoried and labelled without forced relocation or rename. Retain their actual paths/IDs and record whether the old directory conforms, plus reconciliation ownership. Updating a current owner/lifetime label does not rename a live path. Renaming or moving a directory is a separate authorized operation using its custody owner's supported mechanism, with Git-registration, containment, process, dependency, and recovery checks. Adoption alone performs none of these operations.

Close eligibility remains governed by bound lifetime-completion receipts, evidence preservation, dependencies, custody, and removal authority. Naming and folder placement never make a resource disposable.

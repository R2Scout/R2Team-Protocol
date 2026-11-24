# Git worktree directory formation and naming

Use Git worktree explicitly for Git working copies and their directories. Resource is the broader lifetime term. Existing r2team-workspace, workspace_leases, and compatibility anchors keep their technical names. A plain archive/output directory is not a registered Git worktree.

## Approved root and Git-reference name

New ordinary linked Git worktrees are direct children of the project's approved root, mapped locally from an accepted TEAM root alias:

```text
<root>/<project>-<git-work-ref>-<perm|task|tmp>-<executor>[-<purpose>]
```

Examples:

```text
<approved-git-worktree-root>/
  crm.ai-issue3244-task-devops/
  crm.ai-issue3244-tmp-qa2/
  crm.ai-pr3250-tmp-dev20/
  crm.ai-issue3244-task-devops-build/
  crm.ai-issue3244-task-devops-integration/
```

Do not add a separate physical/native ID, counter, date, retry, chat title, revision, or verdict to the ordinary name or its parent hierarchy. Keep technical lease/resource/native IDs in registry/custody records; they are not another public folder number. Existing IDs and actual paths remain stable on reuse.

The project-approved root remains disjoint from evidence/artifact/output/log/tmp/cache roots, with neither containing the other. A tmp lifetime token does not authorize placement in output or system Temp roots. External placement needs its own accepted root/containment evidence. Resolve the actual target and filesystem limits, including links/junctions, before creation.

## Match the accepted Git work identifier

Use the primary work reference recorded in the accepted TASK and its authoritative Git/tracker route. If an Issue or Work Item governs the work, use its actual number as issue3244 or wi3244. Use task3244 or the approved canonical TASK-ID slug when TASK itself is the primary identifier. Use pr3250 when the PR is the governing work reference and no earlier Issue/TASK reference should be retained. Do not choose arbitrary numbers or derive a new ID from a title/branch.

Explicit issue/task/pr/wi types distinguish equal numbers. Standing anchors still reference an actual governance Issue/TASK; base is not a new Git work identifier. Keep full identifiers/routes in the TASK even when the directory uses their approved lowercase portable slug. Labels remain metadata, not unique candidate, ownership, or deletion proof.

Use lowercase ASCII letters, digits, and hyphens; dots are allowed inside the project alias. Directory names, including any purpose suffix, are at most 96 characters. Reject missing/non-Git references, separators, drive prefixes, spaces, wildcard/control characters, and unsafe aliases. Shorten only through approved aliases; never silently truncate identity. Apply [resource lifetime policy](RESOURCE_LIFETIME.md) independently of dev/qa/build/release purpose.

## Reuse and declared purpose lanes

First inspect the accepted TASK, complete physical inventory, deterministic materialization key, and compatible lease. Exact compatible requests reuse the existing ID and actual path, including older prefixed directories. A revision, handoff, owner/lifetime label, or naming-policy change never allocates another worktree by itself.

For legitimately separate allocations with the same work reference, lifetime, and executor, a suffix such as build or integration names the already declared purpose/lane in the accepted TASK/lease. Declare it before allocation; it is not an automatic collision fallback or authorization to create another copy. Existing budgets, exceptions, single-writer, and key-conflict gates still apply. An occupied target is reconciled as exact reuse or ALLOCATION_BLOCKED; do not append another counter/date/retry. Reconcile partial creation before retry and read back actual Git registration, path, branch/HEAD/tree, owner, and custody.

The pure helper git_worktree_directory_name accepts project_slug, work_ref, executor_slug, lifetime, and optional purpose/custody; it no longer takes a native ID for ordinary naming. It validates leaf names only, without allocation, root selection, filesystem containment, or mutation. Operators verify the accepted Git reference and purpose at authoritative sources.

## Application and legacy custody

Application-managed Git worktrees preserve the application's native root, hierarchy, ID, and repository-folder layout. Use supported app controls and display-name fields; if a name field is absent, keep the readable label locally and report the limit. Removing an ordinary extra-ID prefix does not authorize removing application-native path layers. The ordinary naming helper rejects application and legacy custody.

Existing primary and legacy directories remain inventoried and protected, even if their historical names contain ws numbers or other prefixes. Updating labels/owners does not rename a live path. Rename/movement requires separate authority, supported custody mechanisms, and Git registration, containment, process/dependency, and recovery checks. Adoption alone performs no rename, cleanup, relocation, or decommission.

Close eligibility still requires bound lifetime-completion receipts, evidence preservation, dependencies, custody, and removal authority. Neither a matching Git number nor a directory name makes material disposable.

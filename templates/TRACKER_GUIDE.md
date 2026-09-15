# GitHub and Azure DevOps Server/TFS Git — R2Team 2.1

One project uses one provider. Git stores the contract and confirmed state; the tracker displays the queue; PRs connect diff/review/checks. No universal dispatcher is implemented here: Codex uses available authorized CLI/API tools.

## Common independent-task cycle

1. Reuse existing item/TASK/PR where appropriate.
2. Create/link item, task branch and TASK.
3. After a substantive commit/push, open a Draft PR or clearly block early merge if draft is unsupported.
4. Preserve returned IDs/URLs in TASK and backlinks in the provider.
5. Assign the provider account belonging to the TEAM executor; keep exact executor/active_role in TASK.
6. For ownership handoff, check single publisher, update owner/checkpoint, publish, then notify with a commit-pinned reference.
7. QA records candidate evidence; PM checks actual acceptance.
8. Merge and DONE follow DoD; deployment is verified separately when required.
9. Preserve material discussion outcomes in Git before dependent work.

No tracker/access does not turn a local TASK into a delivered assignment. Use LOCAL_ONLY and report readiness limits.

## GitHub

Record owner/repository, canonical Git URL, default branch, accounts, required checks/review and merge strategy in TEAM.

Read-only preflight checks Git refs/status and the installed provider tool, such as gh auth status without exposing tokens and gh repo view. Scope API calls to the selected repo.

After authorization, examples are:

```text
gh issue create --repo <owner/repo> --title "<TASK-id>: <result>" --body-file <prepared-body-file>
gh pr create --repo <owner/repo> --draft --base <default-branch> --head <task-branch> --title "<TASK-id>: <result>" --body-file <prepared-body-file>
gh issue edit <number> --repo <owner/repo> --add-assignee <account>
gh pr comment <number> --repo <owner/repo> --body-file <prepared-handoff-file>
```

Use [ISSUE_PR_TEMPLATES.md](ISSUE_PR_TEMPLATES.md). Temporary request bodies are not another registry. Preserve and verify returned IDs/results; placeholders are not executable values.

Reconcile old/new assignees on transfer. Use Closes/Fixes only when merge truly completes the item. An @codex mention can trigger external execution and requires corresponding authority.

### Questions and updates

Routine coordination can use an authorized direct exchange. Shared requirements discussion uses the existing Issue; code review uses the PR thread. A question changes neither owner nor task identity.

Mention verified provider accounts and identify the logical executor/function. Review requests are for actual reviews. Participants configure relevant subscriptions/mentions/assignments/review notifications. A shared account has no per-role unread state; also inspect the TASK's material open requests. Inbox read/Done does not complete a TASK or imply agreement.

Comments are not in a clone. The publisher preserves material open questions, human actions and decisions at the publication boundaries. No full transcript or mandatory duplicate comment for direct exchanges. Read exact assignments/events, not every Issue.

## Azure DevOps Server/TFS Git

Also record collection URL, project/repo ID, server/API version, Work Item type/valid states/identity format, policies/build definition, draft support, network access and approved credential mechanism.

The repository must be Git, not TFVC. Cloud Services and on-premises Server are not interchangeable; verify supported tools rather than assuming the cloud CLI works. Use compatible REST/SDK, native Git/GCM and approved authentication.

| Operation | REST resource pattern |
| --- | --- |
| Create a Task Work Item | POST {collection}/{project}/_apis/wit/workitems/$Task?api-version={version} |
| Update item/assignment/state | PATCH {collection}/{project}/_apis/wit/workitems/{id}?api-version={version} |
| Create PR | POST {collection}/{project}/_apis/git/repositories/{repoId}/pullrequests?api-version={version} |
| PR thread | POST .../pullrequests/{prId}/threads?api-version={version} |
| Build evidence | GET {collection}/{project}/_apis/build/builds?api-version={version} |

$Task is a literal URL segment, not a PowerShell variable. Select and encode the actual process type.

Work Item operations typically use JSON Patch and application/json-patch+json. Verify System.Title/Description/AssignedTo/State fields and transitions on the server; do not submit a protocol REVIEW state without mapping.

PR source/target refs use refs/heads/<branch>. Verify the supported Development relation/artifact URI before linking Work Item and PR; do not guess it. Preserve IDs/URLs in TASK, perform supported revision/concurrency checks and read back writes. A conflict requires rereading, not overwriting another actor.

Never put credentials in URLs, shell history, TEAM, request bodies or logs. Use approved credential storage. Do not promise REST writes before verifying actual rights and capabilities.

## Errors, concurrency and retry

- Publish the authoritative checkpoint before ownership handoff/projection notification.
- On timeout/unknown creation, inspect exact ID or repo+TASK marker before retrying.
- Rejected push requires checking the remote head/owner, not force-push.
- TASK/tracker assignment or status drift is SYNC_REQUIRED; reconcile within authority.
- Preserve limitations/remaining work; do not hide missing PRs or failed delivery.

A provider assignment does not itself start remote Codex. Participants enter manually or separately configure automation. PM heartbeat is off by default.

## Bounded working exchanges

The cycle above governs independent tasks and ownership handoffs. [OPERATING_COMMUNICATION.md](OPERATING_COMMUNICATION.md) permits authorized bounded assistance through direct exchanges without new items/PRs or duplicate comments. Preserve the parent owner/publisher and material state at the four boundaries. Location does not change those requirements.

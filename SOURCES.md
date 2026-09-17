# Sources and compatibility

Prepared on 2026-09-17. R2Team's role contracts, TASK model and persistence boundaries are project conventions, not an official OpenAI standard. Version 2.3 retains bounded operational exchanges, keeps specialized process profiles outside the main distribution, and uses the protocol version as the sole release identifier.

## Reference sources used during setup design

- [Codex Build skills](https://learn.chatgpt.com/docs/build-skills): discovery, SKILL.md, repository/user/plugin scopes, installation and visibility.
- [Codex AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md): project entry instructions.
- [Scheduled tasks](https://learn.chatgpt.com/docs/automations?surface=app): thread/standalone execution, manual checks and unattended permission limits. A skill or instruction creates no schedule; verify actual heartbeat/wake availability.
- [GitHub Notifications](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/about-notifications) and [Inbox](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/viewing-and-triaging-notifications/managing-notifications-from-your-inbox): subscriptions, mentions and filters operate on accounts, not guaranteed chat execution.
- [OpenSpec installation](https://github.com/Fission-AI/OpenSpec/blob/main/docs/installation.md): Node/CLI, init/update and legacy cleanup.
- [OpenSpec getting started](https://github.com/Fission-AI/OpenSpec/blob/main/docs/getting-started.md): change lifecycle.
- [OpenSpec existing projects](https://github.com/Fission-AI/OpenSpec/blob/main/docs/existing-projects.md): delta-first adoption, existing documents as sources and incremental coverage.
- [Superpowers README](https://github.com/obra/superpowers): installation routes and workflow library.
- [Azure DevOps CLI](https://learn.microsoft.com/en-us/azure/devops/cli/?view=azure-devops): Services/Server distinction.
- [Azure DevOps REST](https://learn.microsoft.com/en-us/rest/api/azure/devops/?view=azure-devops-rest-7.1): API families and version compatibility.
- [Work Items and Git](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/connect-work-items-to-git-dev-ops?view=azure-devops): Development links to PRs.
- [Work Item update](https://learn.microsoft.com/en-us/rest/api/azure/devops/wit/work-items/update?view=azure-devops-rest-7.1): JSON Patch, revisions and relations. Match API version to the actual server.

During original package preparation, local read-only checks covered OpenSpec CLI 1.13.0 and init/profile/validate help; seven installed OpenSpec workflows and core TDD/debugging/verification skills were read. These are historical observations, not fresh validation of every upstream URL or any participant's installation.

Upstream main is mutable. Pin the selected tool version/ref in TEAM and read its current documentation/skills during project setup. These references do not promise compatibility with every Server version.

## Community context

The protocol uses isolated worktrees, explicit ownership, review, reproducible evidence and durable checkpoints. Illustrative discussion sources include:
- [OpenAI Developer Forum: agents in separate branches](https://community.openai.com/t/multiple-codex-agents-in-different-branches/1358394)
- [Reddit: multiple agents and worktrees](https://www.reddit.com/r/codex/comments/1q3496o/how_are_you_using_multiple_agents_and_worktrees/)
- [Reddit: same-branch interference](https://www.reddit.com/r/codex/comments/1rtm331/how_can_i_work_on_multiple_threads_on_the_same/)

Community posts are contextual experience, not universal consensus, benchmark evidence or a product guarantee.

## What is not supplied or started

No third-party skill copies, credentials, real thread IDs, populated TEAM, product specifications or working message logs are shipped. Copying this package installs no plugin and creates no dispatcher/schedule.

The wizard uses explicit permissions for installation and integration. Natural-language team commands are not a shipped CLI. Only documented validation scripts are executable components; live provider/agent behavior requires separate checks.

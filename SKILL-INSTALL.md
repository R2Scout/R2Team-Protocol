# Installing R2Team 2.1

Four instruction skills are supplied: r2team, r2team-work, r2team-coo and r2team-audit. They are folders with SKILL.md, not shell commands or a service. OpenSpec/Superpowers are separate dependencies described in [SKILLS.md](templates/SKILLS.md).

## A. From GitHub

The distribution repository is public; installation needs no invitation. PM supplies its URL and the full verified release commit SHA. Access to a private project repository is a separate check.

```text
$skill-installer Install from R2Scout/R2Team-Protocol
at ref <verified-full-commit-SHA-for-v2.1>:
skills/r2team
skills/r2team-work
skills/r2team-coo
skills/r2team-audit
Do not substitute main/latest.
If same-name skills exist, show the differences and ask before replacing them.
Do not migrate projects or enable automations.
```

The installer uses its supported repo/ref/path interface. Resolve `v2.1` and verify its full commit against the published release. Never include tokens in invitations.

Default destination: $CODEX_HOME/skills or ~/.codex/skills; typically C:\Users\<user>\.codex\skills on Windows. Each participant has their own installation.

## B. From a verified clone or bundle

Transfer the complete distribution without .git, runtime data or secrets, or clone the exact commit. Supply a trusted independent SHA-256 for package.json when transferring a bundle.

```text
Verify R2Team 2.1 package revision 1 at <absolute-path>.
Compare package.json to the supplied trusted hash and run scripts/validate_package.py.
Install only the four skills/ folders into this machine's Codex skill directory.
Check user/project scope duplicates, show differences and obtain approval before replacement.
Verify the copied payload hashes.
Do not register, migrate, enable heartbeat or execute product tasks during installation.
```

This option also supports a package distributed through Azure DevOps Server/TFS Git. A GitHub installer is not a TFS installer.

Alternatively, a team can approve the four folders under its project's .agents/skills/. Avoid duplicate names across scopes. Reinstallation for every chat on the same machine is unnecessary.

## Verify discovery

In a subsequent turn:

```text
$r2team help
```

The skill should be discovered and show help without project writes. If unavailable, check path/scope/name and restart Codex only when needed. File checks are not behavioral tests. See [OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills).

## Start a project

The full template package is required, not only four installed SKILL.md files.

```text
$r2team Start a new project using START.md from <verified-package-path>.
Confirm the target directory and guide the wizard. This chat will be PM after confirmation.
```

Without a local package, supply its Git URL and verified full commit. The skill obtains the package into an approved safe directory, then reads START/Setup. Missing TEAM is normal for a new project; the wizard creates it after approval, without fictitious preregistration.

## Join an existing project

PM runs add and publishes the assignment, then provides:

```text
$r2team register repo <project-Git-URL> participant ken executor ken-ops
TEAM: <path>, ref <full-SHA>.
Protocol: <path>, ref <full-SHA>.
PM response channel: <Issue/Work-Item-URL>, recipient <account/executor>.
Cross-check the assigned QA+DevOps functions.
If no TASK is assigned, request the first. Do not start product work during registration.
```

One participant can have multiple functions/chats. Another chat may use $r2team connect QA executor ken-qa. Register includes connect when the executor is unambiguous. Invitation parameters grant no rights: verify current TEAM and provider identity.

Continue with $r2team-work start; read-only updates with $r2team-coo update; see [command help](templates/COMMANDS.md). Heartbeat is off by default.

## Update an older installation

Compare installed skills with the exact new package and approve replacement while preserving local customizations. This applies to older 1.20 and R2Team 2.0 skills.

Updating procedure skills does not switch a project's protocol. Existing rules continue until [explicit migration](templates/MIGRATE_TO_2.1.md). Do not run OpenSpec init/archive merely to install skills.

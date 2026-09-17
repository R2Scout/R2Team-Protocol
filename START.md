# START — R2Team 2.3

This file starts a wizard only when explicitly requested. Reading or editing the distribution does not adopt it in a project. Preferred first entry is [R2TEAM_MASTER.md](R2TEAM_MASTER.md) in a persistent local `R2Team Master - <project>` task; direct PM setup remains a supported fallback.

```text
Read START.md from <verified R2Team package path or Git URL/full commit>.
Confirm the target project and current instructions.
Guide me through new, migrate, team, join, resume or audit.
Ask focused questions, verify known facts, and show the intended diff before writes.
Do not overwrite existing work, install tools or enable automation without authority.
```

1. Verify the package source, manifest and actual target Git root. If using Master, let it collect one Project Charter and pass confirmed answers to PM.
2. Read [Setup.md](templates/Setup.md), relevant [protocol](templates/CODEX_TEAM_PROTOCOL.md) sections and [OPERATING_COMMUNICATION.md](templates/OPERATING_COMMUNICATION.md).
3. Apply the same distinction locally and remotely: OpenSpec contract, TASK recovery state, transient working exchanges. A bounded request is not a new independent task or an ownership handoff.
4. Configure the actual GitHub or generic Azure DevOps Server/TFS Git provider using [TRACKER_GUIDE.md](templates/TRACKER_GUIDE.md). Specialized process setup is not part of this package.
5. Confirm PM only for a new project; joining an existing team does not appoint another PM.
6. Preserve existing specs, IDs, roles and work. A project on 1.10 retains its rules until approved cutover.
7. Check [SKILLS.md](templates/SKILLS.md) and [command help](templates/COMMANDS.md). Skill installation is separate; use document prompts without skills when needed.
8. Confirm approved communication routes and permissions. Direct working exchanges are optional; provider discussion is a fallback. Heartbeat remains off.
9. Save material setup state at publication boundaries in the existing organizational TASK, not a new message registry. Local-only output is not a remote-ready handoff.

For source-package verification, resolve `v2.3` to its full commit and inspect `package.json`. A tag name or dirty local tree is not sufficient provenance.

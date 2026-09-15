# Источники и совместимость

Пакет подготовлен 2026-09-15. Полный протокол R2Team 2.0 и стратегический кандидат поддерживаются одинаковыми; раздел «Основания» сохраняет ссылки и оговорки о community evidence. Редакции пакета 4–5 уточняют взаимодействие, cross-check ролей и опционального COO, не меняя номер 2.0.

## Перепроверенные для setup источники

- [Codex Build skills](https://learn.chatgpt.com/docs/build-skills): discovery, полный SKILL.md, repo/user/plugin scopes, установка и видимость.
- [Codex AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md): проектная точка входа.
- [Codex Skills](https://learn.chatgpt.com/docs/build-skills): явный вызов, repo-scoped навыки, инструкции и необязательные скрипты. Пакет содержит четыре собственных R2Team skills; их команды и протокол не являются стандартом OpenAI.
- [Scheduled tasks](https://learn.chatgpt.com/docs/automations?surface=app): запуск внутри чата или отдельно, предварительный ручной тест и ограничения unattended permissions. Доступность конкретного heartbeat/wake проверяется в среде участника; наличие инструкции или skill не создаёт расписание.
- [GitHub Notifications](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/about-notifications) и [Inbox](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/viewing-and-triaging-notifications/managing-notifications-from-your-inbox): подписки/mentions, причины и фильтры; механизм аккаунта, не гарантия исполнения чатом. Порядок фиксации вопросов/консенсуса в TASK — соглашение R2Team.
- [OpenSpec installation](https://github.com/Fission-AI/OpenSpec/blob/main/docs/installation.md): Node/CLI, init/update и риски legacy cleanup.
- [OpenSpec getting started](https://github.com/Fission-AI/OpenSpec/blob/main/docs/getting-started.md): жизненный цикл change.
- [OpenSpec existing projects](https://github.com/Fission-AI/OpenSpec/blob/main/docs/existing-projects.md): delta-first, existing docs как источники, постепенное покрытие.
- [Superpowers README](https://github.com/obra/superpowers): актуальные пути установки Codex App/CLI plugin и библиотека workflows.
- [Azure DevOps CLI](https://learn.microsoft.com/en-us/azure/devops/cli/?view=azure-devops): различие Services/Server.
- [Azure DevOps REST](https://learn.microsoft.com/en-us/rest/api/azure/devops/?view=azure-devops-rest-7.1): семейства API и version compatibility.
- [CMMI workflow](https://learn.microsoft.com/en-us/azure/devops/boards/work-items/guidance/cmmi-process-workflow?view=azure-devops): Requirements, Tasks и приёмка.
- [Bugs на досках](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/show-bugs-on-backlog?view=azure-devops): Bugs as tasks для дочерних Bugs и sprint Taskboard; тип Bug сохраняется.
- [Work Items и Git](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/connect-work-items-to-git-dev-ops?view=azure-devops): Development-связи с PR.
- [Work Item update](https://learn.microsoft.com/en-us/rest/api/azure/devops/wit/work-items/update?view=azure-devops-rest-7.1): JSON Patch, ревизия и иерархические relations. Версия API сверяется с Server.

Локально read-only проверены OpenSpec CLI 1.13.0 и help для init, config profile и validate. Полностью прочитаны семь установленных OpenSpec SKILL.md и ключевые Superpowers TDD/debugging/verification. Их фактические planning/approval gates отражены в мастере.

Upstream main изменяемый. При установке каждого проекта фиксировать реально выбранную version/ref в TEAM и прочитать текущую документацию/skills. Этот список не обещает API-совместимость любой версии TFS и не заменяет install preflight.

## Что не распространяется и не запускается

Пакет не содержит копий чужих skills, пользовательских credentials, thread IDs, заполненной TEAM, настоящих product specs или рабочих MSG. Он не устанавливает plugin сам по факту копирования, не содержит фонового dispatcher и не создаёт schedules.

Полная установка workflows выполняется мастер-процедурой с разрешениями. Команды `team ...` из стратегических обсуждений не являются поставленным CLI. Новый пакет содержит только документационный wizard и явно названные validator scripts.

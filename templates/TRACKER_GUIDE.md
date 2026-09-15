# GitHub и Azure DevOps Server/TFS с Git — R2Team 2.0

Один проект — один provider. Git хранит контракт и подтверждённое состояние, tracker показывает очередь, PR связывает diff/review/checks. Реализованного универсального dispatcher в пакете нет: Codex использует доступный CLI/API в пределах согласованных прав.

## Общий цикл

1. Найти существующие item/TASK/PR, не плодить дубли.
2. Создать или связать item, task-ветку и TASK.
3. После содержательного commit/push открыть Draft PR (или защищённый от раннего merge обычный PR).
4. Сохранить возвращённые IDs/URL в TASK и обратные ссылки в provider.
5. Назначить assignee человеку из TEAM; executor и active_role — в TASK.
6. Handoff: проверить единственного писателя, обновить owner/checkpoint → push → comment с commit-pinned ссылкой.
7. QA: evidence для candidate SHA. PM: фактические checks и принятие.
8. Merge и DONE только по definition of done. Deployment при необходимости отдельно проверяется.
9. Существенные PR/comments decisions/results перенести в Git до зависимой работы.

Отсутствие tracker не превращает локальный TASK в доставленное поручение. Допустим LOCAL_ONLY checkpoint, но готовность отмечается честно.

## GitHub

В TEAM фиксируются provider=github, owner/repo, canonical Git URL, default branch, accounts, checks/review, merge strategy.

Read-only preflight: Git remote/ref/status, `gh auth status` без вывода токена, `gh repo view` либо доступная GitHub-интеграция. API-запросы адресуются только выбранному repo.

После разрешения Codex может выполнить:

```text
gh issue create --repo <owner/repo> --title "<TASK-id>: <result>" --body-file <prepared-body-file>
gh pr create --repo <owner/repo> --draft --base <default-branch> --head <task-branch> --title "<TASK-id>: <result>" --body-file <prepared-body-file>
gh issue edit <number> --repo <owner/repo> --add-assignee <account>
gh pr comment <number> --repo <owner/repo> --body-file <prepared-handoff-file>
```

Body из [ISSUE_PR_TEMPLATES.md](ISSUE_PR_TEMPLATES.md); временные body-файлы не становятся дополнительным реестром. Сохранить stdout/ID, проверить созданный объект. Примеры не разрешают выполнять их с placeholders.

При смене человека reconcile старого и нового assignee, не оставлять случайно две ответственные записи. `Closes #...` только если merge действительно завершает Issue. Комментарий `@codex` может запускать внешнее выполнение: не добавлять без разрешения.

### Вопросы, человек и обновления GitHub

Общие уточнения/дискуссии — в связанном Issue, review конкретного diff — в PR-thread. Формы запроса человеку/роли, обсуждения и ответа — [ISSUE_PR_TEMPLATES.md](ISSUE_PR_TEMPLATES.md); правила — [протокол](CODEX_TEAM_PROTOCOL.md#interaction). Назначение вопроса не переназначает TASK и не создаёт новый Issue ради раунда обсуждения.

Автор отмечает проверенный @account адресата и logical executor/функцию. Review request используется только для review. В setup участник проверяет свои subscriptions и Notifications; например, фильтры repository, mentions, assignments, review requests и `is:unread`. Несколько ролей под одним аккаунтом не имеют независимого inbox, поэтому открытые обращения в TASK также проверяются. «Прочитано/Done» inbox не изменяет TASK и не означает согласие.

Комментарии GitHub не клонируются Git. Один текущий владелец публикации сохраняет открытые вопросы, действия человека и существенные ответы в TASK до зависимой работы/паузы/handoff. Полный экспорт стенограммы не требуется. Локальный дополнительный wake допускается только при настройке; remote update без отдельной автоматизации не запускает Codex. Не сканируй все Issue: читай назначенные TASK, адресные уведомления и конкретные новые ответы.

## Azure DevOps Server/TFS Git

Для процесса CMMI обязателен [setup-профиль](SETUP-TFS-CMMI.md): Requirement → Task → PR и Requirement → Bug → PR. Parent–Child связывает Work Items; PR связывается с дочерним Task/Bug через Development. Родительский Requirement не закрывается автоматически по одному PR.

В TEAM дополнительно:
- collection_url, project, repository_id;
- repository_url и default_branch;
- установленная версия Server, поддерживаемая api-version;
- тип Work Item, valid state transitions и identity format;
- branch policies/build definition, draft support;
- доступ/VPN и способ auth без секретов.

Первое условие — Git, не TFVC. Azure DevOps Services cloud и локальный Server не взаимозаменяемы: `az devops` официально не поддерживает Server. Для Server использовать совместимый REST API/SDK, штатный Git/Git Credential Manager и разрешённую аутентификацию.

| Операция | Ресурс REST |
| --- | --- |
| Создать Work Item Task | `POST {collection}/{project}/_apis/wit/workitems/$Task?api-version={version}` |
| Изменить item/assignment/state | `PATCH {collection}/{project}/_apis/wit/workitems/{id}?api-version={version}` |
| Создать PR | `POST {collection}/{project}/_apis/git/repositories/{repoId}/pullrequests?api-version={version}` |
| PR comment/thread | `POST .../pullrequests/{prId}/threads?api-version={version}` |
| Builds/evidence | `GET {collection}/{project}/_apis/build/builds?api-version={version}` |

`$Task` — буквальный URL segment, не PowerShell variable. Тип берётся из процесса и кодируется корректно.

Work Item create/update: JSON Patch, `Content-Type: application/json-patch+json`. Показательные поля: `System.Title`, `System.Description`, `System.AssignedTo`, `System.State`; поддерживаемость полей и transitions проверяется на сервере. Не подставлять status REVIEW как System.State без mapping.

При создании PR используются `sourceRefName: refs/heads/<task-branch>`, `targetRefName: refs/heads/<default-branch>` и description со ссылкой на TASK. Связь Work Item/PR делается поддерживаемыми development relations/полями API; формат artifact URI проверить по версии, не выдумывать.

Codex сохраняет возвращённые work item ID, PR ID/URL и связывает их с TASK. Перед PATCH можно использовать revision concurrency check по поддерживаемому API; при конфликте перечитать item, не стирать чужие изменения.

Токен/пароль не включать в Git URL, shell history, TEAM, body файлов или logs. Для Windows использовать штатную разрешённую аутентификацию/credential store. Нельзя обещать REST-запись до проверки прав и Server capabilities.

## Ошибки, конкурентность и повтор

- Сначала Git checkpoint, затем отображение/уведомление.
- При ответе timeout/unknown проверь объект по точному ID либо repo+TASK marker. Не повторяй create вслепую.
- При Git push rejected получи актуальный remote head и выясни владельца; force push не «чинит» handoff.
- TASK assignee/status vs tracker drift → SYNC_REQUIRED, reconcile в пределах полномочий.
- Сохрани ограничение/остаток в том же TASK. Не скрывай отсутствующий PR или недоставленное уведомление.

Назначение Issue/Work Item не запускает удалённый Codex само. Человек входит вручную либо отдельно настраивает разрешённую автоматизацию. PM heartbeat выключен по умолчанию; local direct wake — опциональное ускорение, не отдельный workflow.

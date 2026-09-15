# Setup-профиль: TFS с Git и CMMI — 2.0

Дополнительная ветка единого [Setup.md](Setup.md), а не второй PM или отдельный протокол. Применяется при выборе Azure DevOps Server/TFS + Git + процесса CMMI. Общие права, роли, skills и проверки сохраняются.

## 1. Схема работы

```text
Requirement
  +-- Task -- Git branch / PR
  +-- Bug  -- Git branch / PR
```

- Requirement → Task/Bug — настоящая связь Parent–Child между Work Items.
- Task/Bug → PR — Development-связь с Git Pull Request. PR не является Work Item или дочерней карточкой.
- Один исполняемый `TASK-*.md` соответствует одному основному Work Item типа Task ИЛИ Bug, своей основной ветке и PR.
- Requirement может объединять несколько самостоятельных задач/дефектов. Родитель не получает дополнительный TASK/PR лишь потому, что объединяет работу.
- Смена исполнителя, QA или DevOps не создаёт новую карточку/PR. Полномочия и active_role остаются в Git TASK.
- Новая функция поддерживается так же, как классическая: например Analyst уточняет Requirement, Tester проверяет Task/Bug.

Requirement-карточка содержит короткий смысл, критерии/ссылку и состояние. Полные требования, решения и подтверждённое состояние остаются в Git: OpenSpec, TASK и связанная документация. Не веди два независимо редактируемых текста спецификации.

<a id="preflight"></a>
## 2. Опрос и preflight

В режиме new/migrate проходить после выбора платформы; в join/resume читать уже принятую конфигурацию.

1. Подтвердить collection URL, project, repository ID, default branch и тип репозитория Git, не TFVC.
2. Проверить версию Server/API, фактический процесс CMMI или его согласованную кастомизацию. Существующий проект с другим процессом не переключать автоматически.
3. Прочитать реальные типы Requirement, Task, Bug, обязательные поля и их reference names, состояния, переходы и правила Parent–Child. Названия в кастомном процессе могут отличаться.
4. Уточнить Team, Area Path и Iteration Path, identities/Assigned To, политики PR и build checks.
5. Проверить текущий режим отображения Bugs. Для запрошенной цепочки Requirement → Bug рекомендуется **Bugs as tasks**: Bugs видны в sprint backlog/Taskboard и могут быть дочерними требованиям. Сохраняется тип Bug — это не конвертация его в Task.
6. Если Bugs сейчас отслеживаются как requirements либо вне backlog, согласовать изменение team setting и последствия видимости. Не менять тихо; не заменять требуемую Parent-связь на Related и не выдавать её за ту же иерархию.
7. Согласовать полномочия на создание/изменение Work Items, hierarchy links, board/query settings, branch/PR/comments. Права merge, deployment и изменения БД отдельно.
8. Проверить Git и read-only API с безопасной аутентификацией. `az devops` не считать поддерживаемым клиентом локального Server; использовать совместимый REST API/SDK по [TRACKER_GUIDE.md](TRACKER_GUIDE.md).
9. Установить соответствие статусов отдельно для Requirement, Task и Bug. Не переносить состояния одного типа в другой наугад.

Если нужные типы/связи/права недоступны, сохранить точный BLOCKED. Согласовать настройку процесса или явное изменение схемы с владельцем; мастер не обходит серверные правила.

<a id="team-config"></a>
## 3. Запись в TEAM

Объединить следующий блок с существующим tracker, не создавать второй. Это **проектные настройки протокола**, не готовый REST payload:

```yaml
tracker:
  provider: azure_devops_server
  process_template: CMMI
  process_model: "<verified-inherited-or-on-premises-xml>"
  collection_url: "<verified-collection-url>"
  project: "<verified-project>"
  repository_id: "<verified-repository-id>"
  repository_url: "<verified-git-url>"
  default_branch: "<verified-default-branch>"
  server_version: "<verified-server-version>"
  api_version: "<supported-api-version>"
  team: "<verified-team>"
  area_path: "<verified-area>"
  iteration_path: "<verified-iteration>"
  bug_behavior: as_tasks
  work_item_types:
    requirement: Requirement
    task: Task
    bug: Bug
  state_mapping:
    requirement: {}
    task: {}
    bug: {}
```

Все placeholder и пустые mapping заполняются фактами до объявления setup готовым. `bug_behavior: as_tasks` фиксируется лишь после проверки/согласованной настройки. Старый одиночный `work_item_type: Task` при переходе на этот профиль заменяется картой типов, чтобы баги не создавались как Task.

В mapping указать для каждого типа начальное, рабочее, проверяемое и конечное состояния, условия перехода, обработку Blocked/Cancelled и необходимые поля. Например REVIEW может оставаться рабочим состоянием с пояснением; нельзя создавать отсутствующий серверный State.

В TEAM также сохранить dashboard/query ссылки и known limits. Изменение конфигурации увеличивает project integration_revision, не версию протокола.

<a id="task-contract"></a>
## 4. Связь Git TASK с Work Items

Дополнительные поля TASK для этого профиля:

```yaml
tracker_item: "<URL of leaf Task or Bug>"
tracker_item_type: Task
parent_requirement: "<URL of parent Requirement>"
requirement_ref: "<repo-relative spec/change/document path>"
```

Для дефекта `tracker_item_type: Bug`. Фактические имена берутся из TEAM. `tracker_item` всегда указывает на назначаемую дочернюю работу, а не на родительский Requirement. В DRAFT ссылки могут ожидать создания; перед READY/handoff они должны быть проверены и опубликованы.

`requirement_ref` связывает карточку с содержательным требованием в Git — текущей spec, proposed delta или согласованным документом с явно указанным статусом. При необходимости указывается requirement/scenario ID. URL/ID, контракт и история приёмки Requirement фиксируются в этом связанном Git-документе; краткий агрегированный checkpoint можно вести в существующем docs index. Отдельный реестр Requirements не обязателен.

Перед созданием проверить, нет ли подходящего Requirement, Task/Bug или PR. Нельзя дублировать Requirement на каждую роль или копировать уже существующий Bug в новую Task-карточку только ради протокола.

<a id="new-work"></a>
## 5. Новая работа: Requirement → Task → PR

1. PM/Analyst уточняет потребность с Brain/Designer по необходимости: OpenSpec explore, затем propose или update в пределах их approval gates.
2. PM находит существующий Requirement либо согласованно создаёт новый. Сохраняет короткий outcome, критерии/ссылку на Git, Area/Iteration и проверенного owner.
3. Создаёт/использует дочерний Task, назначает человеку из TEAM и связывает Parent с Requirement.
4. Создаёт/обновляет один Git TASK с owner_executor_id, active_role, полями выше, acceptance и next_action.
5. Публикует task-ветку; после содержательного commit создаёт основной PR. Связывает PR непосредственно с дочерним Task. Дополнительная связь PR с Requirement допустима, но не заменяет эту.
6. Исполнитель читает TASK, показывает intake, применяет нужные навыки: apply/TDD/verification; сохраняет checkpoints. Skills — по [SKILLS.md](SKILLS.md).
7. QA/Tester проверяет конкретный candidate; PM принимает. Обновляются затронутые specs/docs. До merge выполняется sync, archive — после полного scope.
8. Task закрывается по собственной Definition of Done; Requirement принимается отдельно после проверки всего его scope.

Даже если в цепочке только один исполнитель, Git TASK и карточка не заменяются контекстом его чата. Для организационных/документационных работ Requirement описывает реальный согласованный результат, а PR может менять только документы.

<a id="bug-work"></a>
## 6. Исправление: Requirement → Bug → PR

1. QA/Tester/Dev фиксирует дефект и версию: expected/actual, воспроизведение, impact, evidence. Неизвестное не заменяется предположением.
2. PM/уполномоченный triage связывает дефект с нарушенным Requirement. Если требования ещё нет, сначала уточняет ожидаемое поведение и источник; не выдумывает новый Requirement ради формальной ссылки.
3. Найти существующий Bug; иначе создать Bug и установить Parent = нужный Requirement. Тип Bug не заменяется Task.
4. Для самостоятельного исправления создать/переиспользовать один Git TASK, где tracker_item указывает на Bug. Назначить executor и ограниченный scope.
5. Публиковать fix-ветку и PR, связанный непосредственно с Bug. Выполнять systematic-debugging → TDD → verification. OpenSpec change нужен при изменении контракта, а не автоматически для каждого восстановления принятого поведения.
6. QA/Tester повторяет воспроизведение и нужную регрессию на новом candidate; evidence сохраняется в Git. Не закрывать Bug только по commit или зелёному чужому build.
7. После нужных review/merge/deployment и проверки DoD закрыть Bug; сохранить решение о состоянии родительского Requirement.

**Возврат незавершённой фичи после QA** может остаться доработкой того же Task/PR с defect evidence. Новый Bug оформляется при необходимости отдельного учёта/жизненного цикла, не на каждое замечание. Если Bug уже заведён и исправляется в текущем PR, добавить к нему Development-связь и сохранить основной TASK, а не создавать конкурирующую ветку только для ссылки.

Если Bug затрагивает несколько Requirements, выбрать одного проверенного Parent, остальные связать подходящими дополнительными ссылками и перечислить в Git. Не создавать несколько Parents.

<a id="relations"></a>
## 7. Иерархия и API

Серверные операции выполнять только после проверки версии, прав и точных IDs. Для Work Item create/update обычно используется JSON Patch и Content-Type `application/json-patch+json`.

При добавлении **родителя к дочернему** Task/Bug тип ссылки — `System.LinkTypes.Hierarchy-Reverse`. При добавлении ребёнка со стороны Requirement — `System.LinkTypes.Hierarchy-Forward`. Не нужно вручную добавлять оба направления: проверить фактическую связь после одной операции.

Пример тела PATCH дочернего Work Item; значения заполняются из текущего сервера:

```json
[
  {
    "op": "test",
    "path": "/rev",
    "value": 12
  },
  {
    "op": "add",
    "path": "/relations/-",
    "value": {
      "rel": "System.LinkTypes.Hierarchy-Reverse",
      "url": "<parent Requirement REST URL>"
    }
  }
]
```

`12` — пример текущей ревизии, не постоянное значение. Перед записью перечитать item с relations, проверить existing Parent, отсутствие циклов и конкурирующего изменения. При существующем другом Parent — решение PM, а не слепое добавление/удаление.

PR связывается поддерживаемым Development/Pull Request механизмом выбранного API/UI. Простая ссылка в Description или упоминание номера не доказывает Parent–Child либо Development relation: после операции выполнить read-back. Точный artifact URI PR берётся из документации версии/API, не конструируется по догадке.

Если ответ create/link неизвестен, проверить текущий объект/relations по точным IDs до retry. Не использовать bypassRules для обхода ошибок. Tokens/пароли не включать в URL, примеры, TEAM или logs.

<a id="views"></a>
## 8. Boards, Taskboards и dashboard

- Продуктовый backlog/board — Requirements.
- Sprint backlog/Taskboard — Tasks и Bugs при согласованном Bugs as tasks.
- PR review — Azure Repos Pull Requests; dashboard только показывает ссылки/виджеты, а не заменяет PR workflow.
- Для состава команды/функций используется TEAM, не обязательные новые Work Item types.

Минимальные представления, если они нужны и разрешены: активные Requirements; мои Task/Bug; работа без Parent; блокировки; связанные/ожидающие review PR; build status. Если query не умеет надёжно находить отсутствие Development links, использовать проверенный API, не выдавать пустую выборку за отсутствие проблемы.

Настройку board columns/query/widgets согласовать с владельцем. Перетаскивание карточки меняет состояние TFS, но не обновляет Git автоматически: PM/Codex должен сверить изменение с scope и сохранить подтверждённое состояние в TASK. Несогласованное расхождение — SYNC_REQUIRED.

<a id="acceptance"></a>
## 9. Приёмка, миграция и контрольный проход

- Вход в существующий CMMI-проект сохраняет реальные IDs, Parents, ссылки, процесс и правила. Существующие Task/Bug получают Git TASK, не дубликат Work Item.
- Миграция с GitHub/другого процесса или изменение process template не выводятся из выбора профиля: нужен отдельный согласованный план.
- Requirement не закрывается из-за merge одного дочернего PR. PM сверяет все входящие в scope Task/Bug, общие критерии, затронутые specs/docs и нужные проверки.
- Дубликат/отменённый/неподтверждённый Bug закрывается только с фактическим основанием; это не FIXED и не успешный QA.
- Поздний Bug по уже принятому Requirement не означает автоматическое повторное открытие родителя: решение PM и влияние на scope фиксируются в Git.
- На PR completion не включать автоматическое закрытие всех связанных Work Items, если это преждевременно закрывает Requirement или ещё требует deployment.

В setup проверить обе цепочки: точный Parent, leaf type/assignee, TASK поля, PR Development link и status mapping. Использовать существующие реальные объекты либо отдельно разрешённый безопасный тест; не придумывать продуктовый Bug для демонстрации. Если одна цепочка ещё не проверена, отметить её NOT_RUN — не заявлять полную проверку интеграции.

Проверка структуры документов не является live-проверкой CMMI/TFS. После согласованного setup вернуться в общий мастер к инструментам/skills, первой работе и финальному audit. Второй startup/PM не создаётся.

## Источники

- [CMMI workflow](https://learn.microsoft.com/en-us/azure/devops/boards/work-items/guidance/cmmi-process-workflow?view=azure-devops)
- [Bugs as requirements / tasks](https://learn.microsoft.com/en-us/azure/devops/organizations/settings/show-bugs-on-backlog?view=azure-devops)
- [Work Items и Git development](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/connect-work-items-to-git-dev-ops?view=azure-devops)
- [Work Item update / relations](https://learn.microsoft.com/en-us/rest/api/azure/devops/wit/work-items/update?view=azure-devops-rest-7.1)

Документация API 7.1 — пример контракта, не указание использовать 7.1 на любой старой версии TFS.

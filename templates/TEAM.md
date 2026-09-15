# TEAM — конфигурация R2Team

Шаблон 2.0. Заполняет PM при setup; пустая конфигурация не готова к работе. Не копируйте личные thread IDs, абсолютные пути других машин и credentials в Git.

```yaml
protocol_name: R2Team
protocol_version: "2.0"
integration_revision: 0
setup_status: NOT_CONFIGURED
project:
  name: null
  purpose: null
protocol_source:
  repository_url: null
  commit_sha: null
  package_path: null
  package_sha256: null
pm_executor_id: null
participants: []
tracker:
  provider: null
  process_template: null
  repository_url: null
  default_branch: null
automation:
  pm_heartbeat_enabled: false
  direct_wake: optional_local
toolchain:
  openspec_cli_version: null
  openspec_schema: null
  openspec_source_ref: null
  superpowers_source_ref: null
  skill_install_method: null
```

В source заполняется реальный commit+package path либо hash точного локального bundle. Не выдавай HEAD за полный источник dirty working tree. Для уже принятой конфигурации увеличивай integration_revision при изменении правил/состава.

## Участники и исполнители

Заполняемый образец для замены participants/pm_executor_id, не действительное назначение:

```yaml
pm_executor_id: john-main
participants:
  - id: john
    tracker_actor: "<verified-provider-identity>"
    active: true
    executors:
      - id: john-main
        active: true
        roles: [PM, Brain, Designer, Dev, QA, DevOps]
        subagents:
          allowed: false
          purposes: []
          writable_paths: []
        permissions:
          git_commit: false
          git_push: false
          tracker_write: false
          pr_create_update: false
          merge: false
          deploy: false
```

При заполнении спроси нужные права и помощников, не оставляй все false и одновременно не объявляй автономную работу включённой. Допустимы permissions для конкретных refs/сред/действий; одного deploy=true без target/scope недостаточно.

Кен может быть только DevOps либо QA+DevOps; один человек может иметь несколько executors с разными функциями. PM-роли у других executors не активируются одновременно с текущим pm_executor_id.

## Профили и обязанности

| Функция | Инструкция |
| --- | --- |
| PM | [ROLE-PM.md](ROLE-PM.md) |
| Brain | [ROLE-BRAIN.md](ROLE-BRAIN.md) |
| Designer | [ROLE-DESIGNER.md](ROLE-DESIGNER.md) |
| Dev | [ROLE-DEV.md](ROLE-DEV.md) |
| QA | [ROLE-QA.md](ROLE-QA.md) |
| DevOps | [ROLE-DEVOPS.md](ROLE-DEVOPS.md) |
| COO (опциональная организационная функция) | [ROLE-COO.md](ROLE-COO.md) |

Профиль не создаёт отдельный чат. Удалённые и локальные executor используют тот же TASK. Реальный local routing — [локальный шаблон](LOCAL_REGISTRY_TEMPLATE.md), опционально и вне Git.

Таблица содержит классические профили, не enum. PM вправе добавить любую функцию, например Tester, Analyst или Architect, по [ROLE-TEMPLATE.md](ROLE-TEMPLATE.md). Зарегистрируй её описание/ссылку здесь, добавь имя в roles нужного executor и назначай active_role в TASK. Один executor может совмещать базовые и новые функции. Tester не автоматически QA: различия/совпадения определяет профиль. Только текущий pm_executor_id выполняет функцию координатора PM.

## Provider и проектные команды

Настройки GitHub/TFS — по [TRACKER_GUIDE.md](TRACKER_GUIDE.md). Записать:
- проверенный remote/default branch, identity, state mapping;
- branch policies, required checks, reviewer independence, merge strategy;
- эффекты push/merge и кто разрешает их;
- команды build/test/run с источником и ограничениями;
- среды, данные, runbook/rollback, правила секретов;
- ссылка на карту документации и known gaps.

Если process_template = CMMI, применить [SETUP-TFS-CMMI.md](SETUP-TFS-CMMI.md): согласовать карту типов Requirement/Task/Bug, состояния каждого типа, Bugs as tasks и связи Parent–Child/Development. Заменить одиночный work_item_type картой work_item_types из профиля. Конкретный серверный процесс и поля проверяются, не выводятся только из названия CMMI.

## Люди, согласование и каналы обновлений

PM фиксирует для реально нужных функций, без второго реестра участников:

- кто отвечает на продуктовые/технические вопросы и кто вправе менять scope;
- кто выполняет человеческие настройки и визуальную приёмку, для каких сред и с какими границами;
- проверенный provider account каждого человека; несколько executors одного аккаунта различаются по logical ID/функции в обращении;
- выбранные подписки/способ проверки обновлений каждым участником и опциональный local routing; реальные thread IDs остаются вне Git;
- требуемая независимость/согласования для спорных решений и маршрут эскалации.

Не записывай сюда каждое ожидание: конкретные вопросы, ответы и помощь человеку ведутся в текущем TASK по [циклу взаимодействия](CODEX_TEAM_PROTOCOL.md#interaction). Назначение вопроса не меняет владельца TASK. GitHub-уведомления не гарантируют прочтение или запуск удалённого Codex; heartbeat не включается автоматически.

## COO: форма, scope и права при необходимости

COO не обязателен. Для внутреннего помощника PM/родителя задай scope в его разрешённом поручении/subagents: по умолчанию read-only, факты возвращаются родителю, wake выполняет родитель. Для самостоятельного COO зарегистрируй обычного executor с `roles: [COO]` у соответствующего участника. Нельзя автоматически регистрировать/запускать его только из-за наличия профиля.

Пример дополнительных настроек **этого executor**, не действительное назначение. Объедини permissions с существующими, не перезаписывай их пустой заготовкой:

```yaml
coo:
  watched_participant_ids: []
  watched_executor_ids: []
  wake_dispatcher: sender
  heartbeat_enabled: false
permissions:
  notify_local: false
  tracker_write: false
  manage_assignments: false
  manage_team: false
  manage_automations: false
```

При настройке заполни точные ID и границы проекта/действий. `wake_dispatcher` для наблюдаемого набора — `sender`, `none` либо logical executor ID конкретного самостоятельного COO: выбирается один, чтобы не было двойного wake. `notify_local: true` требует согласованного local routing/маршрутов на машине участника; это не Git/provider write. Разрешения на Git-публикацию/PR и остальные операции остаются отдельными.

Права меняет PM/уполномоченный владелец с подтверждением владельца среды. COO не редактирует собственные права, не расширяет список наблюдаемых ролей и не включает расписание себе. Даже при разрешённой записи сохраняются назначенный scope, единственный publisher и необходимые approvals. Флаги описывают договорённость, а не технически настроенные разрешения инструментов: фактические ограничения среды проверяются отдельно.

Ручная проверка и heartbeat используют один ограниченный цикл [ROLE-COO.md](ROLE-COO.md). Heartbeat по умолчанию false и включается только отдельной настройкой; для внутреннего помощника расписание относится к родителю, а не к субагенту. Локальные cursor/dedup допустимы только ignored и не являются Git-источником состояния проекта.

## Фактическая готовность инструментов

| Executor / машина без личных путей | CLI version / skill source ref | Нужные skills обнаружены | Проверка и дата | Ограничения |
| --- | --- | --- | --- | --- |
| Не зарегистрирован | UNKNOWN | NOT_RUN | NOT_RUN | Setup не выполнен |

Не дублируй каждый результат работы здесь: фактические tests/build/deploy находятся в TASK. Таблица фиксирует readiness окружения. См. [SKILLS.md](SKILLS.md).

Регистрация в TEAM не означает принятия роли. При новом самостоятельном входе/новой функции требуется [cross-check](CODEX_TEAM_PROTOCOL.md#role-cross-check) самого executor и подтверждение назначенного TASK либо запрос первого у PM. В приглашении PM даёт существующий канал подключения. Открытые вопросы и итог сохраняются в организационном TASK, не в новом журнале; отсутствие назначения отличается от неисправности окружения.

## Cutover и история изменений

Кратко: источник предыдущего протокола; какие TASK ещё по старым правилам; момент принятия новой редакции и ответственные. Не удаляй inactive participants или старую историю только ради чистого списка.

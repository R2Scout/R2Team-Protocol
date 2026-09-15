# DEVOPS — профиль функции 2.0

Сборки, артефакты, инфраструктура, БД, demo/Azure/deployment в назначенном scope.

Профиль не создаёт чат. Его может выполнять PM, отдельный или совмещённый executor любого участника, либо разрешённый внутренний помощник. Назначение и права — [TEAM.md](TEAM.md) и TASK.

## Вход

Если это внутренний субагент, используй поручение родителя: узкий scope, выбранные входы и запреты. Не проходи самостоятельную регистрацию/join, не присваивай себе owner TASK. Следующий общий вход относится к самостоятельному executor.

Прочитай [AGENTS.md](AGENTS.md), [протокол](CODEX_TEAM_PROTOCOL.md), текущий TEAM, назначенный TASK/branch и нужную документацию. Проверь owner, active_role, revision, scope и next_action. Покажи intake по [CODEX_TEAM_SETUP.md](CODEX_TEAM_SETUP.md).

## Работа

При первом самостоятельном входе или добавлении этой функции выполни [cross-check роли](CODEX_TEAM_PROTOCOL.md#role-cross-check), задай неясные вопросы и подтверди уже назначенный TASK либо запроси первый у PM (для первого PM — у владельца проекта). Субагент уточняет только своё поручение у родителя. Не начинай самоназначенную работу.

Применяй [общий цикл взаимодействия](CODEX_TEAM_PROTOCOL.md#interaction): бриф до действий, пошаговое сопровождение человека, уточнения/согласование в Issue/PR и сохранение открытых вопросов/ответов в TASK. Если ты субагент, вопросы и нужные действия человека передавай родителю; внешнюю переписку и публикацию ведёт он.

Прочитай runbook, target environment и rollback. Зафиксируй source SHA/build/artifact digest и нужные approvals. До выкладки проверь QA/CI для нужного candidate. После — runtime/smoke evidence, ограничения и rollback status. Отчёт в Evidence текущего TASK.

## Навыки

verification-before-completion и systematic-debugging; openspec-explore/propose/update/apply по назначенному infra change; TDD для исполняемого поведения scripts/IaC по применимости. Обычная утверждённая сборка не требует всех planning workflows.

Читай полный SKILL.md. Доступность/установка — [SKILLS.md](SKILLS.md). Соблюдай его planning/approval/verification границы.

## Границы

Merge не означает deploy. Не меняй shared DB/secrets/access/production/расходы и не останавливай неизвестные процессы без scope. Не печатай credentials. QA-функция того же чата не даёт право rollout.

Отдельный release TASK нужен при самостоятельном контролируемом жизненном цикле. Локальное preview фичи может быть этапом той же задачи. Отдельный обязательный REPORT не нужен.

Субагенты получают узкий scope; родитель остаётся владельцем TASK. Внешние назначения/уведомления не делегируются обычным помощникам.

## Завершение или пауза

Сохрани completed/remaining/blockers, evidence и next_action в том же TASK/артефактах. Разрешённые commit/push предшествуют уведомлению tracker/PR по [TRACKER_GUIDE.md](TRACKER_GUIDE.md). При невозможной публикации — LOCAL_ONLY/NOT_DELIVERED. Для TASK 2.0 не создавай обязательный ACK, MSG или отдельный отчёт.

Читай только нужные обновления. При конфликте прав/источника/owner останови затронутую работу и верни конкретный blocker.

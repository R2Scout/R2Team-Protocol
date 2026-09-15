# R2Team Protocol 2.0

Самостоятельный Git-first протокол для людей и Codex: от одного PM с помощниками до локальных/удалённых команд и обратно. Поддерживает GitHub и Azure DevOps Server/TFS с Git, включая CMMI.

В репозитории находятся полный протокол, wizard нового/существующего проекта, шаблоны, четыре устанавливаемых skills и проверяемый manifest. Обязателен только PM; функции могут совмещаться, разделяться и передаваться. Skills не являются отдельным сервисом, не выдают права и не запускают heartbeat автоматически.

## Начать

1. Откройте публичный [R2Team-Protocol](https://github.com/R2Scout/R2Team-Protocol): приглашение для установки не нужно.
2. Клонируйте проверенную редакцию, сохраняя LF:

```text
git -c core.autocrlf=false clone https://github.com/R2Scout/R2Team-Protocol.git
cd R2Team-Protocol
git checkout --detach v2.0
git rev-parse HEAD
python scripts/validate_package.py
python -B scripts/test_validate_package.py
```

Сверьте полученный полный SHA с переданным владельцем релиза; для воспроизводимой поставки используйте этот SHA вместо изменяемой ветки. Для bundle сверяйте доверенный hash package.json перед проверкой payload.

3. Установите навыки по [SKILL-INSTALL.md](SKILL-INSTALL.md).
4. В Codex:

```text
$r2team Начни новый проект через START.md из <путь-к-этому-репозиторию>.
Проведи мастер, подтверди целевой проект и права. Этот чат будет PM.
```

Без skills можно попросить прочитать [START.md](START.md) напрямую. Для существующего проекта выберите migrate, для приглашённого участника — register/join; не запускайте новый проект поверх существующего.

## Навигация

| Файл | Назначение |
| --- | --- |
| [START.md](START.md) | Единый вход в wizard |
| [Полный протокол](templates/CODEX_TEAM_PROTOCOL.md) | Основания, роли, процесс, примеры, диаграммы |
| [COMMANDS.md](templates/COMMANDS.md) | Help команд и приглашение register |
| [SKILL-INSTALL.md](SKILL-INSTALL.md) | Установка из Git/bundle, передача людям, обновление |
| [Setup.md](templates/Setup.md) | new / migrate / team / join / resume / audit |
| [AGENTS.md](templates/AGENTS.md) и [TEAM.md](templates/TEAM.md) | Проектные инструкции и конфигурация |
| [SKILLS.md](templates/SKILLS.md) | Когда и как применять OpenSpec/Superpowers |
| [TRACKER_GUIDE.md](templates/TRACKER_GUIDE.md) | GitHub и TFS Git |
| [SETUP-TFS-CMMI.md](templates/SETUP-TFS-CMMI.md) | Requirement → Task/Bug → PR |
| [Миграция на 2.0](templates/MIGRATE_TO_2.0.md) | Сохранение спецификации, работы и существующих ролей |
| [Несколько репозиториев](templates/MULTI_REPO.md) | Опциональная координация SDK/API без нового обязательного PM |
| [SCENARIOS.md](SCENARIOS.md) | Критерии проверки рабочих процедур |
| [VERIFICATION.md](VERIFICATION.md) | Что проверено и что не проверялось |
| [SOURCES.md](SOURCES.md), [CHANGELOG.md](CHANGELOG.md) | Основания и происхождение версии |

В templates также находятся классические ROLE-профили, опциональный COO, шаблон произвольной функции, TASK и документов. Они не создают участников или задачи сами.

## Четыре skill

```text
$r2team help
$r2team add Кен roles QA,DevOps remote
$r2team register repo <Git-URL> participant ken executor ken-ops
$r2team-work start
$r2team-coo update
$r2team-audit
```

Это примеры, не последовательность обязательных операций. Команды после имени skill — обычное поручение Codex, а не PowerShell/CLI.

## Принципы поставки

- Один основной источник TASK/spec/checkpoint в Git; tracker/PR для обсуждения и review. Существенные решения и открытые ожидания из comments фиксируются в Git.
- Новые проекты получают шаблоны через wizard; существующие — согласованный diff, не копирование поверх заполненных файлов.
- Папка skills содержит процедуры, не состояния проектов. Пользовательские пути/секреты/thread registry не публикуются.
- OpenSpec и Superpowers — внешние зависимости, не скопированы сюда. Их точные версии/источники, наличие и допустимые эквиваленты проверяются в setup. Для установки нужны доступ к источникам и разрешения владельца машины.
- Исторические пакеты 1.10/1.20 не нужны для запуска 2.0 и не поставляются. Действующие проекты не мигрируют от установки skill.
- Heartbeat PM/COO по умолчанию выключен. Wake только по отдельным текущим правам и локальному маршруту; удалённый Codex не запускается от Git-уведомления автоматически.

## Проверка

Python 3.10+; package validator не требует сторонних библиотек. Он проверяет состав/хэши, UTF-8, ссылки/anchors/fences и отсутствие локального runtime-реестра, но не доказывает полномочия, корректность продукта или поведение живых агентов. Перед изменением manifest сначала проверяйте прежний источник. После согласованного изменения обновляйте хэши всех payload-файлов.

Протокол — соглашение R2Team, не официальный стандарт OpenAI. Репозиторий публичный; установка протокола не предоставляет доступ к проектам пользователей. Встроенный help skills — на английском; основной протокол и wizard — на русском.

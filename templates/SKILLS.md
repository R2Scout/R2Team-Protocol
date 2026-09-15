# OpenSpec и Superpowers — рабочая интеграция R2Team 2.0

Это обязательная маршрутизация навыков по работе, а не декларация «все установлены». Нельзя запускать все навыки подряд для каждой мелочи. Полный SKILL.md выбранного навыка читается до действий; при отсутствии навыка сообщается blocker и согласуется установка или явный эквивалент.

## 1. Установка и проверка

### R2Team — собственные навыки процедуры

Пакет 2.0 содержит четыре папки skills: `r2team` (setup/team/register/connect), `r2team-work` (start/task/discuss), `r2team-coo` (update/check), `r2team-audit` (read-only). Help — [COMMANDS.md](COMMANDS.md); инструкция поставки SKILL-INSTALL.md находится в корне проверенного setup-пакета. На каждой машине проверяются источник, установка и обнаружение. Они не заменяют OpenSpec/Superpowers, не хранят TEAM и не включают heartbeat. Для исходного проекта другой версии сначала согласовать совместимость; установка skill не мигрирует протокол.

### 1.1 Inventory без изменений

На каждой нужной машине:
1. Проверить Node и `openspec --version`, реальный executable при нескольких установках.
2. Определить локальный Codex App/CLI и доступные skills. Проверить проектные `.agents/skills`, user/plugin scopes без широкого сканирования домашней папки.
3. Прочитать существующие OpenSpec config, инструкции, custom skills и активные changes.
4. Сверить версии/ref с TEAM. Не обновлять инструменты «до latest» без решения.
5. Проверить команды `openspec init --help` и `openspec validate --help` для выбранной версии.

CLI, skills и папка openspec — три разные вещи. Для setup PM нужны все семь основных workflows ниже. Другому executor нужны workflows его функций; PM фиксирует покрытие команды, не требует навыка archive от QA-only, которому запрещено архивировать.

### 1.2 OpenSpec CLI

Источник — [официальная установка OpenSpec](https://github.com/Fission-AI/OpenSpec/blob/main/docs/installation.md). На дату подготовки пакета проверен локальный CLI 1.13.0; документация требует Node >=20.19.0. Это проверенная исходная версия, а не бессрочное требование не обновляться.

После согласования версии и глобальной установки пример:

```text
npm install -g @fission-ai/openspec@1.13.0
openspec --version
```

Команды не исполняются только из-за чтения файла. Сначала показать выбранный package manager и scope. Если Node отсутствует/устарел, нет подходящего менеджера, нужны admin-права или ломается PATH — остановиться, не редактировать shell profile автоматически.

### 1.3 Init / обновление проектных workflows

Перед init проверь точный root и существующие legacy команды/marker blocks, включая точечную проверку user Codex prompts `opsx-*.md`. По документации `init --tools` может удалять legacy-файлы без дополнительного вопроса. Покажи точный список затрагиваемого и сохрани согласованную резервную копию; при наличии legacy дождись подтверждения.

После разрешения:

```text
openspec init --tools codex
```

Не применять `--force` для обхода конфликтов. Для существующей интеграции сравнить генерируемые файлы, custom изменения и выбранную версию прежде `openspec update`. Профиль workflows выбирается по фактическому CLI; при отсутствии verify — `openspec config profile`, выбрать нужные expanded workflows и согласованно выполнить `openspec update`. Настройка profile может быть глобальной: проверить область и не менять другие проекты молча.

После init/update:
- сохранить фактический вывод: созданные skills/commands/config и пути;
- проверить видимость skills в целевом Codex, перезагрузить сессию только при необходимости;
- не считать отсутствие slash-command ошибкой у skills-only интеграции;
- брать имя вызова из установленных файлов, а не угадывать пунктуацию;
- проверить `openspec context --json`, нужный root и отсутствие случайного чужого store;
- выполнить list/specs/status и validate по реальному содержимому; пустые specs не «полная спецификация».

Не создавай `openspec/changes/<name>` вручную вместо CLI: metadata/schema создаёт `openspec new change` внутри соответствующего workflow. Не подменяй template/instructions своей схемой.

### 1.4 Superpowers

Источник — [Superpowers README](https://github.com/obra/superpowers). На дату проверки upstream предлагает Codex plugin:
- App: Plugins → Superpowers → Install;
- CLI: `/plugins` → найти Superpowers → Install Plugin.

Наличие плагина в конкретной среде нужно проверить, а установку согласовать. Не запускать Claude-команды `/plugin install` как Codex shell-команды.

Если plugin недоступен или нужен минимальный набор, используй доступный skill-installer для согласованных папок `skills/<name>` из проверенного ref upstream. Сохраняй связанные references/scripts, а не только один SKILL.md. Не устанавливай вторую копию того же навыка поверх plugin без проверки коллизий.

Предпочтительно установить полный Superpowers один раз и выбирать навыки по работе. Минимум для качества: TDD, systematic-debugging, verification-before-completion. Версия/source ref и метод установки фиксируются в TEAM. Если невозможно зафиксировать plugin commit, сохрани фактическую plugin version и provenance как есть, не придумывай SHA.

## 2. OpenSpec: где вызывается каждый workflow

| Навык | Триггер и функция | Что сохраняется / условие выхода |
| --- | --- | --- |
| `openspec-explore` | PM/Brain/Designer/Dev: уточнить идею, изучить MVP/код/старые docs | Findings и вопросы; запись только с требуемым подтверждением; без реализации |
| `openspec-propose` | PM/уполномоченный планировщик: новый согласованный change | Артефакты schema по status/instructions; после proposal — пауза до нового запроса на apply, если так требует skill |
| `openspec-update-change` | План изменился или нужно согласовать существующие артефакты | Изменения только существующих planning files; подтверждение по skill; не создание недостающих и не код |
| `openspec-apply-change` | Назначенный Dev, после разрешённого перехода к реализации | Код/tests/docs и tasks progress; missing artifacts/scope conflict → остановка |
| `openspec-verify-change` | QA/reviewer/PM перед приёмкой change | Completeness/correctness/coherence, evidence, непроверенное; эвристический анализ не заменяет tests |
| `openspec-sync-specs` | Назначенный владелец PR перед интеграцией изменённого поведения | Семантический merge delta → main specs в task-ветке, validate; без преждевременного archive |
| `openspec-archive-change` | PM/уполномоченный исполнитель после полного scope | Проверка completion и sync, архив; не выдавать incomplete/skip за принятый результат |

В стандартном repo-local режиме пути определяются CLI. Для уже выбранного standalone store сохраняются точный store ID и flags на всех поддерживающих командах. Новый store без нужды не добавляется.

Примеры read-only команд (с именами из фактического списка):

```text
openspec context --json
openspec list --json
openspec list --specs
openspec status --change <name> --json
openspec instructions apply --change <name> --json
openspec validate --all --strict --no-interactive
```

CLI validate проверяет формат, не соблюдение продукта. Не перепрыгивать planning approval ради автоматизации. Если requirements изменились, PM уточняет TASK revision и артефакты, не заставляет apply «подогнать» scope.

## 3. Superpowers: карта всей применимой библиотеки

Точное наличие и имена проверяются в установленной версии. Эти навыки не создают вторую очередь задач или обязательные дополнительные планы.

| Навык | Когда и кто | Ограничение |
| --- | --- | --- |
| `using-superpowers` | При входе/выборе workflow, если установлен | Маршрутизация, не изменение полномочий |
| `brainstorming` | PM/Brain/Designer: неясная идея/дизайн | Не запускать второй параллельный процесс согласования; результат связать с OpenSpec |
| `writing-plans` | PM/Dev: подробные проверяемые шаги | Один канонический план: change tasks.md или TASK; если skill требует иной артефакт, явно согласовать mapping, не вести две независимые версии |
| `executing-plans` | Последовательное выполнение утверждённого плана | Не обходить apply/schema и human gates |
| `subagent-driven-development` | Родитель с разрешёнными помощниками | Узкие задания, review результата; TASK владеет родитель |
| `dispatching-parallel-agents` | Независимые подзадачи с разрешённым делегированием | Не делить одну запись/среду между неконтролируемыми писателями |
| `using-git-worktrees` | Параллельные независимые изменения | Worktree не изолирует общие БД, порты и облако |
| `test-driven-development` | Dev/другой исполнитель, пишущий поведение или fix | Red → green → refactor; исключение только явно согласованное |
| `systematic-debugging` | Любая функция при bug/failure/unexpected behavior | Сначала причина и evidence, затем разрешённый fix |
| `requesting-code-review` | Dev/PM при готовом candidate | Review по scope/spec/code quality; не merge-разрешение |
| `receiving-code-review` | Dev при замечаниях QA/PR | Проверить замечание, согласовать scope, исправить и перепроверить |
| `verification-before-completion` | Все функции перед утверждением результата | Свежая проверка, фактический вывод, версия, NOT_RUN |
| `finishing-a-development-branch` | Владелец после проверки | Merge/cleanup только по проектным правам; не удалять активную ветку до сохранения состояния |
| `writing-skills` | Только создание/изменение собственных навыков | Отдельное поручение; не обязательный этап продуктовой фичи |

Если полный plugin добавляет обязательные собственные шаги, прочитай их и выяви конфликт до работы. Не заявляй, что протокол отменяет правила навыка; согласуй единственный источник планов/границы или выбери совместимый набор.

## 4. Спецификация и документация на практике

- Greenfield: exploration → proposal → approval → apply+TDD → verify+tests → sync+docs → merge → archive после полного scope.
- Brownfield: текущие docs как источники; короткая карта покрытия; ближайший реальный change. Не массовый импорт всего legacy.
- Bug существующего принятого поведения: TASK + debugging + TDD + verification; OpenSpec change только если меняется контракт.
- Чистое добавление участника: TEAM/join, inventory skills; не выдуманный product change.
- Уточнение/обсуждение: [общий цикл](CODEX_TEAM_PROTOCOL.md#interaction); explore/brainstorming только при реальной неопределённости, update-change после принятого изменения плана. Вопрос сам не запускает apply и не требует второго плана/нового change.
- Помощь человеку: пошаговые действия и проверка ответа; verification-before-completion отличает человеческую приёмку от автоматического теста. Ни один skill не расширяет права на настройки/секреты/deploy и не отменяет ожидание необходимого решения.
- QA-only: verify/read/tests по назначению; не patch/apply.
- DevOps: build/runtime/rollback verification и debugging; OpenSpec apply только при назначенной реализации infra change.

## 5. Как проверяется, что навыки действительно работают

Setup записывает в TEAM version/ref/method/доступность каждого нужного workflow для executor. В первом реальном TASK evidence содержит:
1. какой workflow применён и к какому scope;
2. артефакты/команды и фактический результат;
3. остановки/approval/NOT_RUN;
4. ссылки на tests/specs/checkpoint.

Не заводи отдельный skill-report на каждый шаг. Файл SKILLS и зелёный validator — не доказательство выполнения навыка. Блокируется только затронутый этап; независимую безопасную работу можно продолжать.

OpenSpec — жизненный цикл спецификации; Superpowers — дисциплина исполнения и проверки. Ни одно не заменяет TASK ownership, Git-публикацию и реальные проверки.

# Заготовка TASK — R2Team 2.0

Используй тело ниже для `Tasks/TASK-<id>-<name>.md`, убрав это пояснение. ID выбирается без коллизий с существующими. Не создавай новую задачу только из-за передачи роли.

```yaml
---
protocol_version: "2.0"
id: "<unique-task-id>"
revision: 1
status: DRAFT
stage: DISCOVERY
owner_executor_id: "<registered-executor>"
active_role: PM
tracker_item: null
tracker_item_type: null
parent_requirement: null
requirement_ref: null
branch: null
pr: null
openspec_change: null
base_sha: null
candidate_sha: null
verified_sha: null
merged_sha: null
next_action: "<one-specific-action>"
---
```

## Outcome

Для [TFS+CMMI](SETUP-TFS-CMMI.md) tracker_item — дочерний Task или Bug; tracker_item_type — его проверенный тип, parent_requirement — URL родителя Requirement, requirement_ref — путь к содержательному требованию в Git. Эти поля заполняются до READY/handoff. Для других профилей дополнительные поля можно не использовать.

Проверяемый результат задачи.

## Scope and boundaries

Включено/исключено; пути/среды; разрешённые действия. Кто меняет scope и назначение.

## Acceptance

Requirements/scenarios либо короткие критерии. Нужная независимость QA и условия DONE.

## Plan

Ссылка на OpenSpec tasks.md при наличии change; иначе несколько шагов. Не копировать подробный план второй раз.

## Current checkpoint

- Completed:
- Remaining:
- Blockers:
- Open requests, только если есть: кому (человек/executor), какой ответ/действие, версия/среда, что блокирует и ссылка на Issue/PR-thread. Это краткое состояние, не отдельный реестр сообщений.

Для setup сюда входят mode, последний завершённый шаг, подтверждённые ответы/ссылки и следующий вопрос. Не требуется отдельный setup-state файл.

## Evidence

- Что проверено и на какой версии:
- Команда/сценарий и фактический результат:
- Проверяющий и функция:
- UNKNOWN/NOT_RUN:
- Ссылки и существенные результаты в Git:
- Для deployment: environment, source SHA, artifact digest, runtime checks, rollback:
- Для человеческой приёмки: кто, что и для какой версии подтвердил; что роль проверила сама. Не называть такую приёмку автоматическим тестом.

## Decisions and handoff

Короткие принятые решения и передачи: от кого → кому, active_role, причина, commit. Существенное содержание комментариев переносится сюда или в specs/docs.

Для обсуждения сохрани нужные позиции, существенные варианты/возражения, принятый итог и уполномоченного принимающего; молчание не согласие. Если ответа нет, ожидание остаётся в Current checkpoint. Изменение контракта требует новой revision и согласованных specs до зависимой работы.

Уточнения, действия человека и дискуссии проходят по [общему циклу](CODEX_TEAM_PROTOCOL.md#interaction). Комментарии не входят в Git: перед передачей/паузой сохрани достаточно информации для восстановления без переписки. Публикующий владелец TASK один; остальные отвечают через provider.

`revision` меняется при изменении контракта, не каждый checkpoint. Git commit определяет версию состояния. Реальные task/item/PR links обязательны к самостоятельному handoff; DRAFT без них не готовое поручение.

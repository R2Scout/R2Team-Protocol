# История R2Team

## 2.0 — 2026-09-15

Первый самостоятельный выпуск в R2Scout/R2Team-Protocol. Основан на локальном R2Team 1.20, package_revision 6; исходный SHA-256 package.json: `18a5a2eb09ad5c0e29c9b9ace9d57e1c51d2cead1a652cba408fdbb0ba8efbce`.

- Единый комплект протокола, wizard, шаблонов, help и четырёх skills.
- Публичная поставка без приглашения для установки; встроенный help всех skills на английском.
- PM как единственная обязательная роль; произвольные и совмещённые функции, local/remote/hybrid исполнение.
- Git-first TASK + tracker/PR, intake, сопровождение человека, уточнения/консенсус, checkpoints и handoff.
- OpenSpec/Superpowers в рабочих стадиях; документация и ADR отдельно от спецификаций.
- add/register/connect/migrate/disconnect; update/check COO с delta-only и отдельными правами wake.
- Единый startup для GitHub и TFS Git/CMMI, перенос существующей спецификации и чатов через явный cutover.
- Опциональная связь нескольких репозиториев через владельца SDK/API, pinned contracts и связанные TASK/PR.
- Validator переведён на 2.0. Старые пакеты и замороженные миграционные патчи в исходном репозитории не изменяются.

Установка/публикация пакета не является миграцией существующих проектов. Нативный CLI, фоновый сервис, GitHub/TFS live workflow и unattended scheduling не входят в данный выпуск.

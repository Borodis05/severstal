# FastAPI Tasks API

Простой REST API для работы с задачами (Tasks) на FastAPI + Postgres.

## Быстрый старт (Docker)

1) Заполни `.env` (или используй `.env.example` как шаблон).
2) Запусти:

```bash
docker compose up --build
```

API будет доступен на:

```
http://localhost:8000
```

Swagger UI:

```
http://localhost:8000/docs
```

## Миграции

Миграции запускаются автоматически сервисом `migrations` при `docker compose up`.

Если нужно вручную:

```bash
docker compose run --rm migrations
```

## Запуск тестов (Docker)

Тесты запускаются в контейнере:

```bash
docker compose run --rm tests
```

## Переменные окружения

Минимально нужны:

```
POSTGRES_USER
POSTGRES_PASSWORD
POSTGRES_DB
CORS_ORIGINS
```

Шаблон находится в `.env.example`.

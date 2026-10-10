# Таск трекер на FastAPI + PostgreSQL

ДЗ «БД + CRUD»: задачи хранятся в PostgreSQL, для Task сделан полный CRUD.

## Запуск

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # вписать свои данные от БД
uvicorn main:app --reload
```

Таблица `tasks` создается сама при запуске.

## Эндпоинты

- `POST /tasks` — создать задачу
- `GET /tasks` — все задачи
- `GET /tasks/{id}` — одна задача
- `PATCH /tasks/{id}` — изменить задачу
- `DELETE /tasks/{id}` — удалить задачу

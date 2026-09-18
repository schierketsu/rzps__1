# 1 ЗАДАНИЕ

## Запуск

```bash
docker compose up -d --build
```

## Проверка

```bash
docker ps
```

## Остановка

```bash
# Обычная остановка контейнеров
docker compose down
# Остановка с удалением volumes (чистка БД)
docker compose down -v
```

## Проверка существующих данных

```bash
docker volume ls
```

## Доступ

http://localhost:8080

## Подключение к PostgreSQL

| Параметр     | Значение         |
| ------------ | ---------------- |
| Система      | PostgreSQL       |
| Сервер       | `db`             |
| Пользователь | `postgres_admin` |
| Пароль       | `example`        |
| База данных  | `testdb`         |

## Создание пользователя и выдача прав

```sql
CREATE USER app_user WITH PASSWORD 'AppPassword123';
GRANT CONNECT ON DATABASE testdb TO app_user;
GRANT USAGE ON SCHEMA public TO app_user;
```

### Вывод списка пользователей

```sql
SELECT usename FROM pg_user;
```

```bash
python -m venv venv


.\venv\Scripts\activate

python -m pip install psycopg[binary]
```

установка `psycopg[binary]` падала при включённом VPN.

## Быстрая сводка команд

| Действие                    | Команда                        |
| --------------------------- | ------------------------------ |
| Запуск с пересборкой        | `docker compose up -d --build` |
| Список контейнеров          | `docker ps`                    |
| Остановка                   | `docker compose down`          |
| Остановка + чистка БД       | `docker compose down -v`       |
| Список volumes              | `docker volume ls`             |
| Создать venv                | `python -m venv venv`          |
| Активировать venv (Windows) | `.\venv\Scripts\activate`      |
| Установить psycopg          | `pip install psycopg[binary]`  |

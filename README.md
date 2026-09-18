#запуск
docker compose up -d --build

#проверка
docker ps

#остановка контейнеров
docker compose down
#остановка контейнеров с чисткой бд
docker compose down -v

#проверка сущ. данных
docker volume ls

http://localhost:8080

Система PostgreSQL
Сервер db
Пользователь postgres_admin
Пароль example
База данных testdb

CREATE USER app_user WITH PASSWORD 'AppPassword123';
GRANT CONNECT ON DATABASE testdb TO app_user;
\ c testdb
GRANT USAGE ON SCHEMA public TO app_user;

SELECT usename FROM pg_user;
на вывод пользователей

![alt text](image-1.png)

виртуальное окружение
python -m venv venv
.\venv\Scripts\activate
python -m pip install psycopg[binary]
(падало с впн)

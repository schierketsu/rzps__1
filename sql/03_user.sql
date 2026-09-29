-- Пользователь для приложения (НЕ администратор)
CREATE USER app_user WITH PASSWORD 'AppPassword123';

-- Может подключаться к базе testdb и обращаться к схеме public
GRANT CONNECT ON DATABASE testdb TO app_user;
GRANT USAGE ON SCHEMA public TO app_user;

-- Может читать, добавлять и изменять данные.
-- НЕ может удалять строки (DELETE) и менять структуру (CREATE/DROP/ALTER).
GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO app_user;

-- Нужно для SERIAL: при INSERT новый id берётся из последовательности
GRANT USAGE ON ALL SEQUENCES IN SCHEMA public TO app_user;

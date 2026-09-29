FROM python:3.13-slim

WORKDIR /app

# Библиотека для работы с PostgreSQL
RUN pip install --no-cache-dir "psycopg[binary]"

# Код приложения и конфиг подключения
COPY app.py config.json ./

CMD ["python", "app.py"]

import json
from getpass import getpass

import psycopg


def load_config():
    with open("config.json", "r", encoding="utf-8") as file:
        return json.load(file)


def main():
    config = load_config()

    username = input("Введите логин БД: ")
    password = getpass("Введите пароль БД: ")

    connection_params = {
        "host": config["host"],
        "port": config["port"],
        "dbname": config["database"],
        "user": username,
        "password": password
    }

    try:
        with psycopg.connect(**connection_params) as connection:
            with connection.cursor() as cursor:

                cursor.execute("SELECT VERSION();")

                result = cursor.fetchone()

                print("\nПодключение успешно!")
                print("Версия PostgreSQL:")
                print(result[0])

    except Exception as error:
        print("\nОшибка подключения:")
        print(error)


if __name__ == "__main__":
    main()
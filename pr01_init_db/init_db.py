# Практическая работа 1. Создание файла БД и таблицы для сущности "Задача"
import os
import sqlite3

# база лежит рядом со скриптом, откуда бы его ни запускали
here = os.path.dirname(os.path.abspath(__file__))
DATABASE_NAME = os.path.join(here, "todo.db")

db_conn = sqlite3.connect(DATABASE_NAME)   # 1. подключение (файл создастся сам)
cur = db_conn.cursor()                     # 2. курсор для запросов

# 3. DDL: структура таблицы todo
cur.execute(
    "CREATE TABLE IF NOT EXISTS todo ("
    " id INTEGER PRIMARY KEY,"
    " title TEXT NOT NULL,"
    " status TEXT DEFAULT 'new')"
)

db_conn.commit()   # 4. фиксируем изменения в файле
db_conn.close()    # 5. освобождаем файл

print("Готово: таблица todo создана в файле", DATABASE_NAME)

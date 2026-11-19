# Практическая работа 1. Проверка: какие таблицы и колонки есть в базе
import os
import sqlite3

DATABASE_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "todo.db")

if not os.path.exists(DATABASE_NAME):
    print("Файл базы не найден, сначала запусти init_db.py")
else:
    db_conn = sqlite3.connect(DATABASE_NAME)
    cur = db_conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
    found = cur.fetchall()
    print("Таблицы в базе:", found)
    # PRAGMA table_info возвращает описание колонок
    for col in cur.execute("PRAGMA table_info(todo)"):
        print("  колонка:", col[1], "| тип:", col[2], "| по умолчанию:", col[4])
    db_conn.close()

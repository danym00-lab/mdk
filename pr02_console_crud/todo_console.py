# Практическая работа 2. Консольный CRUD для таблицы todo
import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "todo.db")


def open_db():
    link = sqlite3.connect(DB_PATH)
    # если практику 2 запускают без практики 1 - таблицу создадим здесь
    link.execute("CREATE TABLE IF NOT EXISTS todo ("
                 "id INTEGER PRIMARY KEY, title TEXT NOT NULL, status TEXT DEFAULT 'new')")
    return link


def show_all():
    link = open_db()
    records = link.execute("SELECT id, title, status FROM todo ORDER BY id").fetchall()
    link.close()
    if len(records) == 0:
        print("Пока задач нет.")
        return
    print("--- задачи ---")
    for rec in records:
        flag = "+" if rec[2] == "done" else "-"
        print(f"#{rec[0]} ({flag}) {rec[1]}  статус: {rec[2]}")


def menu():
    print()
    print("s - список задач")
    print("a - новая задача")
    print("v - отметить выполненной")
    print("d - удалить задачу")
    print("q - выйти")


while True:
    menu()
    cmd = input("> ").strip().lower()
    if cmd == "s":
        show_all()
    elif cmd == "q":
        print("Выход из программы.")
        break
    else:
        print("Такой команды нет (или она ещё не сделана).")

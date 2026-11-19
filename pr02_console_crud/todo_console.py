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


def add_new():
    text = input("Что нужно сделать? ").strip()
    if text == "":
        print("Пустую задачу добавить нельзя.")
        return
    link = open_db()
    cur = link.cursor()
    # значение передаём через ?, а не склеиваем строку - защита от SQL-инъекций
    cur.execute("INSERT INTO todo (title) VALUES (?)", (text,))
    link.commit()
    print("Добавлено, номер задачи:", cur.lastrowid)
    link.close()


def read_number():
    show_all()
    raw = input("Номер задачи: ").strip()
    try:
        return int(raw)
    except ValueError:
        print("Нужно ввести число.")
        return None


def finish_task():
    num = read_number()
    if num is None:
        return
    link = open_db()
    cur = link.execute("UPDATE todo SET status = 'done' WHERE id = ?", (num,))
    link.commit()
    changed = cur.rowcount   # 0 - такой строки нет
    link.close()
    print("Задача выполнена!" if changed else "Задачи с таким номером нет.")


def remove_task():
    num = read_number()
    if num is None:
        return
    sure = input(f"Удалить задачу #{num}? да/нет: ").strip().lower()
    if sure not in ("да", "y", "yes"):
        print("Не удаляем.")
        return
    link = open_db()
    cur = link.execute("DELETE FROM todo WHERE id = ?", (num,))
    link.commit()
    changed = cur.rowcount
    link.close()
    print("Задача удалена." if changed else "Задачи с таким номером нет.")


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
    elif cmd == "a":
        add_new()
    elif cmd == "v":
        finish_task()
    elif cmd == "d":
        remove_task()
    elif cmd == "q":
        print("Выход из программы.")
        break
    else:
        print("Такой команды нет.")

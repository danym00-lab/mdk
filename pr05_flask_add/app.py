# Практическая работа 5. Добавление задач через веб-форму
import os
import sqlite3

from flask import Flask, redirect, render_template, request

# база общая с практикой 2: задачи, добавленные в консоли, видны на странице
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(project_dir, "pr02_console_crud", "todo.db")

site = Flask(__name__)


def fetch_todos():
    link = sqlite3.connect(DB_PATH)
    link.row_factory = sqlite3.Row   # строки как словари: t['title'] вместо t[1]
    link.execute("CREATE TABLE IF NOT EXISTS todo ("
                 "id INTEGER PRIMARY KEY, title TEXT NOT NULL, status TEXT DEFAULT 'new')")
    result = link.execute("SELECT id, title, status FROM todo ORDER BY id").fetchall()
    link.close()   # данные уже прочитаны, соединение можно закрыть
    return result


@site.route("/")
def todo_list():
    return render_template("index.html", todos=fetch_todos())


@site.route("/add", methods=["POST"])
def add_todo():
    text = request.form.get("task_text", "").strip()
    # required в форме можно обойти, поэтому проверяем ещё и на сервере
    if text:
        link = sqlite3.connect(DB_PATH)
        link.execute("INSERT INTO todo (title) VALUES (?)", (text,))
        link.commit()   # без commit задача не сохранится в файл
        link.close()
    # редирект после POST: F5 не отправит форму второй раз
    return redirect("/")


if __name__ == "__main__":
    site.run(debug=True)

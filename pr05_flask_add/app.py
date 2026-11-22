# Практическая работа 5. Добавление задач через веб-форму
import os
import sqlite3

from flask import Flask, redirect, render_template, request, url_for

# база общая с практикой 2: задачи, добавленные в консоли, видны на странице
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_FILE = os.path.join(base_dir, "pr02_console_crud", "todo.db")

web_app = Flask(__name__)


def load_all_todos():
    """Читает все задачи из базы. Возвращает список строк."""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    conn.execute(
        "CREATE TABLE IF NOT EXISTS todo ("
        "id INTEGER PRIMARY KEY, title TEXT NOT NULL, status TEXT DEFAULT 'new')"
    )
    rows = conn.execute("SELECT id, title, status FROM todo ORDER BY id").fetchall()
    conn.close()
    return rows


@web_app.route("/")
def show_todos():
    return render_template("index.html", todos=load_all_todos())


@web_app.route("/add", methods=["POST"])
def create_todo():
    task_title = request.form.get("task_text", "").strip()

    # серверная валидация: если поле пустое — возвращаем форму с ошибкой
    if not task_title:
        return render_template(
            "index.html",
            todos=load_all_todos(),
            error="Название задачи не может быть пустым."
        )

    conn = sqlite3.connect(DB_FILE)
    conn.execute("INSERT INTO todo (title) VALUES (?)", (task_title,))
    conn.commit()   # без commit задача не сохранится в файл
    conn.close()

    # редирект после POST: F5 не отправит форму второй раз
    return redirect(url_for("show_todos"))


if __name__ == "__main__":
    web_app.run(debug=True)
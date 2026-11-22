# Практическая работа 6. Обработка ошибок и защита соединений
import os
import sqlite3

from flask import Flask, render_template, request, redirect, url_for

# база общая с практикой 2
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_FILE = os.path.join(base_dir, "pr02_console_crud", "todo.db")

web_app = Flask(__name__)


def open_db():
    """Открывает соединение с базой и настраивает доступ к полям по имени."""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def get_all_tasks():
    """Читает все задачи. При ошибке возвращает пустой список."""
    conn = open_db()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, status FROM todo ORDER BY id")
        return cursor.fetchall()
    except sqlite3.Error as err:
        print(f"[ОШИБКА БД] {err}")
        return []
    finally:
        conn.close()


def create_new_task(title):
    """Вставляет новую задачу. Возвращает (успех, сообщение)."""
    conn = open_db()
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO todo (title) VALUES (?)", (title,))
        conn.commit()
        return True, None
    except sqlite3.Error as err:
        conn.rollback()
        print(f"[ОШИБКА БД] {err}")
        return False, "Не удалось сохранить задачу."
    finally:
        conn.close()


@web_app.route("/", methods=["GET", "POST"])
def show_todos():
    if request.method == "POST":
        task_title = request.form.get("task_text", "").strip()

        # серверная валидация
        if not task_title:
            return render_template(
                "index.html",
                todos=get_all_tasks(),
                error="Название задачи не может быть пустым."
            )

        success, message = create_new_task(task_title)
        if not success:
            return render_template(
                "index.html",
                todos=get_all_tasks(),
                error=message
            )

        # редирект после POST: F5 не отправит форму второй раз
        return redirect(url_for("show_todos"))

    return render_template("index.html", todos=get_all_tasks())


if __name__ == "__main__":
    web_app.run(debug=True, port=5000)
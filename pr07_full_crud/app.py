# Практическая работа 7. Мини-проект «Список задач» — полный CRUD
import os
import sqlite3

from flask import Flask, render_template, request, redirect, url_for

# база общая с практикой 2
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_FILE = os.path.join(root_dir, "pr02_console_crud", "todo.db")

web_app = Flask(__name__)


# ============================================================
# РАБОТА С БАЗОЙ
# ============================================================

def open_db():
    """Открывает соединение с базой."""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def load_tasks():
    """R: читает все задачи."""
    conn = open_db()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, status FROM todo ORDER BY id")
        return cursor.fetchall()
    except sqlite3.Error as err:
        print(f"[ОШИБКА load] {err}")
        return []
    finally:
        conn.close()


def add_task(title):
    """C: добавляет новую задачу. Возвращает (успех, сообщение)."""
    conn = open_db()
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO todo (title) VALUES (?)", (title,))
        conn.commit()
        return True, None
    except sqlite3.Error as err:
        conn.rollback()
        print(f"[ОШИБКА add] {err}")
        return False, "Не удалось сохранить задачу."
    finally:
        conn.close()


def flip_status(task_id):
    """U: переключает статус new <-> done. Возвращает число затронутых строк."""
    conn = open_db()
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE todo
            SET status = CASE WHEN status = 'done' THEN 'new' ELSE 'done' END
            WHERE id = ?
            """,
            (task_id,)
        )
        conn.commit()
        return cursor.rowcount
    except sqlite3.Error as err:
        conn.rollback()
        print(f"[ОШИБКА flip] {err}")
        return 0
    finally:
        conn.close()


def remove_task(task_id):
    """D: удаляет задачу. Возвращает число удалённых строк."""
    conn = open_db()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM todo WHERE id = ?", (task_id,))
        conn.commit()
        return cursor.rowcount
    except sqlite3.Error as err:
        conn.rollback()
        print(f"[ОШИБКА remove] {err}")
        return 0
    finally:
        conn.close()


# ============================================================
# МАРШРУТЫ FLASK
# ============================================================

@web_app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task_title = request.form.get("task_text", "").strip()
        if not task_title:
            return render_template(
                "index.html",
                todos=load_tasks(),
                error="Название задачи не может быть пустым."
            )

        success, message = add_task(task_title)
        if not success:
            return render_template(
                "index.html",
                todos=load_tasks(),
                error=message
            )

        return redirect(url_for("index"))

    return render_template("index.html", todos=load_tasks())


@web_app.route("/toggle/<int:task_id>", methods=["POST"])
def toggle_task(task_id):
    affected = flip_status(task_id)
    if affected == 0:
        return render_template(
            "index.html",
            todos=load_tasks(),
            error=f"Задача #{task_id} не найдена."
        )
    return redirect(url_for("index"))


@web_app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    affected = remove_task(task_id)
    if affected == 0:
        return render_template(
            "index.html",
            todos=load_tasks(),
            error=f"Задача #{task_id} не найдена."
        )
    return redirect(url_for("index"))


if __name__ == "__main__":
    web_app.run(debug=True, port=5000)
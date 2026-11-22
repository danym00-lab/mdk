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



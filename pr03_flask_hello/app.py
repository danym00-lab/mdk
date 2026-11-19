# Практическая работа 3. Первые маршруты на Flask
from flask import Flask

server = Flask(__name__)

MENU = '<p><a href="/">Главная</a> | <a href="/about">Об авторе</a></p>'


@server.route("/")
def start():
    return (
        "<h2>Hello! Это мой первый сервер на Flask</h2>"
        + MENU
        + "<p>Скоро здесь будет список задач из базы SQLite.</p>"
    )


@server.route("/about")
def author():
    return (
        "<h2>Об авторе</h2>"
        + MENU
        + "<ul><li>Мартынов Данила Денисович</li><li>Группа 3-ИСП9-54</li></ul>"
    )


if __name__ == "__main__":
    # debug=True - сервер сам перезапускается при сохранении кода
    server.run(debug=True)

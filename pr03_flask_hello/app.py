# Практическая работа 3. Первый маршрут на Flask
from flask import Flask

server = Flask(__name__)


@server.route("/")
def start():
    return "Hello! Это мой первый сервер на Flask."


if __name__ == "__main__":
    # debug=True - сервер сам перезапускается при сохранении кода
    server.run(debug=True)

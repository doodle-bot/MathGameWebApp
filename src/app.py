from flask import Flask, render_template, jsonify, request
from src.services.games_service import MathGame


__author__ = "Devin Markham"


app = Flask(__name__)


@app.route("/hello")
def hello():
    return render_template("index.html")


@app.route("/games/addition")
def addition_game():
    return render_template("game.html", game_type="Addition")


@app.route("/games/subtraction")
def subtraction_game():
    return render_template("game.html", game_type="Subtraction")


@app.route("/games/multiplication")
def multiplication_game():
    return render_template("game.html", game_type="Multiplication")


@app.route("/games/division")
def division_game():
    return render_template("game.html", game_type="Division")


@app.route("/gamedata/addition")
def addition_data():
    game = MathGame("+", lambda a, b: a + b, max_num=20)
    game_data = game.make_game()
    return jsonify(game_data)


@app.route("/gamedata/subtraction")
def subtraction_data():
    def handle(a, b):
        if a < b:
            return b, a
        return a, b

    game = MathGame("-", lambda a, b: a - b, max_num=20, handle_a_b=handle)
    game_data = game.make_game()
    return jsonify(game_data)


@app.route("/gamedata/multiplication")
def multiplication_data():
    game = MathGame("*", lambda a, b: a * b, max_num=12)
    game_data = game.make_game()
    return jsonify(game_data)


@app.route("/gamedata/division")
def division_data():
    def handle(a, b):
        if a == 0:
            a += 1
        return a * b, a

    game = MathGame("/", lambda a, b: int(a / b), min_num=1, max_num=12, handle_a_b=handle)
    game_data = game.make_game()
    return jsonify(game_data)


@app.route("/gameresults/<gametype>", methods=['POST'])
def game_results(gametype):
    print(request.get_json())

    return "gotit"

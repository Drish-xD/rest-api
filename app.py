from flask import Flask, jsonify, redirect
import random, json


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"


@app.route("/quotes")
def quotes():
    file = open("./Data/quotes.json", "r", encoding="utf8")
    quotes = json.load(file)
    return jsonify(quotes)
    file.close()


@app.route("/quotes/random")
def random_quote():
    file = open("./Data/quotes.json", "r", encoding="utf8")
    quotes = json.load(file)
    return jsonify(random.choice(quotes))
    file.close()


if __name__ == '__main__':
    app.run(debug=False, port=2000)

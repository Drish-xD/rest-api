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


@app.route("/jokes")
def jokes():
    file = open("./Data/jokes.json", "r", encoding="utf8")
    jokes = json.load(file)
    return jsonify(jokes)
    file.close()


@app.route("/jokes/random")
def random_joke():
    file = open("./Data/jokes.json", "r", encoding="utf8")
    jokes = json.load(file)
    return jsonify(random.choice(jokes))
    file.close()


@app.route("/jokes/mature")
def jokes_by_mature():
    file = open("./Data/jokes.json", "r", encoding="utf8")
    jokes = json.load(file)
    mature_jokes = [x for x in jokes if x['mature'] == True]
    return jsonify(mature_jokes)
    file.close()


if __name__ == '__main__':
    app.run(debug=False, port=2000)

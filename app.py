from flask import Flask, jsonify, redirect, json
import random


app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello_world():
    return redirect("https://drish-xd.is-a.dev/rest-api/")


# Quotes API

@app.route("/quotes", methods=['GET'])
def quotes():
    file = open("./Data/quotes.json", "r", encoding="utf8")
    quotes = json.load(file)
    file.close()
    return jsonify(quotes)


# Get a random quote

@app.route("/quotes/random", methods=['GET'])
def random_quote():
    file = open("./Data/quotes.json", "r", encoding="utf8")
    quotes = json.load(file)
    file.close()
    return jsonify(random.choice(quotes))


# Get n random quotes

@app.route("/quotes/random/<int:n>", methods=['GET'])
def random_quotes(n):
    file = open("./Data/quotes.json", "r", encoding="utf8")
    quotes = json.load(file)
    file.close()
    return jsonify(random.choices(quotes, k=n))


# Seach Quotes by Author

@app.route("/quotes/author/<string:author>", methods=['GET'])
def quotes_author(author):
    file = open("./Data/quotes.json", "r", encoding="utf8")
    quotes = json.load(file)
    quotes_author = [x for x in quotes if author in x["author"] or author in x["author"].lower() or author in x["author"].upper()]
    file.close()
    return jsonify(quotes_author)


# Jokes API

@app.route("/jokes", methods=['GET'])
def jokes():
    file = open("./Data/jokes.json", "r", encoding="utf8")
    jokes = json.load(file)
    file.close()
    return jsonify(jokes)


# Get a random joke

@app.route("/jokes/random", methods=['GET'])
def random_joke():
    file = open("./Data/jokes.json", "r", encoding="utf8")
    jokes = json.load(file)
    file.close()
    return jsonify(random.choice(jokes))


# Get n random jokes

@app.route("/jokes/random/<int:n>", methods=['GET'])
def random_jokes(n):
    file = open("./Data/jokes.json", "r", encoding="utf8")
    jokes = json.load(file)
    file.close()
    return jsonify(random.choices(jokes, k=n))


# Seach Jokes by Type

@app.route("/jokes/<string:type>", methods=['GET'])
def jokes_by_type(type):
    file = open("./Data/jokes.json", "r", encoding="utf8")
    jokes = json.load(file)
    jokes_list = [x for x in jokes if x['type'] == type]
    file.close()
    return jsonify(jokes_list)


# Get a random joke by type

@app.route("/jokes/<string:type>/random", methods=['GET'])
def random_joke_by_type(type):
    file = open("./Data/jokes.json", "r", encoding="utf8")
    jokes = json.load(file)
    mature_jokes = [x for x in jokes if x['type'] == type]
    file.close()
    return jsonify(random.choice(mature_jokes))


# Get n random jokes by type

@app.route("/jokes/<string:type>/random/<int:n>", methods=['GET'])
def random_jokes_by_type(type, n):
    file = open("./Data/jokes.json", "r", encoding="utf8")
    jokes = json.load(file)
    mature_jokes = [x for x in jokes if x['type'] == type]
    file.close()
    return jsonify(random.choices(mature_jokes, k=n))


if __name__ == '__main__':
    app.run(debug=False)

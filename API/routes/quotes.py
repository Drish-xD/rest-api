import random

from flask import Blueprint, json, jsonify

from .auth import token_required

quotes = Blueprint('quotes', __name__)

# Quotes API

@quotes.route("/quotes", methods=['GET'])
@token_required
def quotes_all(current_user):
    file = open("./API/Data/quotes.json", "r", encoding="utf8")
    allquotes = json.load(file)
    file.close()
    return jsonify(allquotes)


# Get a random quote

@quotes.route("/quotes/random", methods=['GET'])
@token_required
def random_quote(current_user):
    file = open("./API/Data/quotes.json", "r", encoding="utf8")
    quote = json.load(file)
    file.close()
    return jsonify(random.choice(quote))


# Get n random quotes

@quotes.route("/quotes/random/<int:n>", methods=['GET'])
@token_required
def random_quotes(current_user, n):
    file = open("./API/Data/quotes.json", "r", encoding="utf8")
    quotes = json.load(file)
    file.close()
    return jsonify(random.choices(quotes, k=n))


# Seach Quotes by Author

@quotes.route("/quotes/author/<string:author>", methods=['GET'])
@token_required
def quotes_author(current_user, author):
    file = open("./API/Data/quotes.json", "r", encoding="utf8")
    quotes = json.load(file)
    quotes_author = [x for x in quotes
                     if author in x["author"]
                     or author in x["author"].lower()
                     or author in x["author"].upper()]
    file.close()
    return jsonify(quotes_author)

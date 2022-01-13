import random

from flask import Blueprint, json, jsonify

from .auth import token_required

jokes = Blueprint('jokes', __name__)


# Jokes API

@jokes.route("/jokes", methods=['GET'])
@token_required
def jokes_all(current_user):
    file = open("./API/Data/jokes.json", "r", encoding="utf8")
    alljokes = json.load(file)
    file.close()
    return jsonify(alljokes)


# Get a random joke

@jokes.route("/jokes/random", methods=['GET'])
@token_required
def random_joke(current_user):
    file = open("./API/Data/jokes.json", "r", encoding="utf8")
    joke = json.load(file)
    file.close()
    return jsonify(random.choice(joke))


# Get n random jokes

@jokes.route("/jokes/random/<int:n>", methods=['GET'])
@token_required
def random_jokes(current_user, n):
    file = open("./API/Data/jokes.json", "r", encoding="utf8")
    jokes = json.load(file)
    file.close()
    return jsonify(random.choices(jokes, k=n))


# Seach Jokes by Type

@jokes.route("/jokes/<string:type>", methods=['GET'])
@token_required
def jokes_by_type(current_user, type):
    file = open("./API/Data/jokes.json", "r", encoding="utf8")
    jokes = json.load(file)
    jokes_list = [x for x in jokes if x['type'] == type]
    file.close()
    return jsonify(jokes_list)


# Get a random joke by type

@jokes.route("/jokes/<string:type>/random", methods=['GET'])
@token_required
def random_joke_by_type(current_user, type):
    file = open("./API/Data/jokes.json", "r", encoding="utf8")
    jokes = json.load(file)
    jokes_list = [x for x in jokes if x['type'] == type]
    file.close()
    return jsonify(random.choice(jokes_list))


# Get n random jokes by type

@jokes.route("/jokes/<string:type>/random/<int:n>", methods=['GET'])
@token_required
def random_jokes_by_type(current_user, type, n):
    file = open("./API/Data/jokes.json", "r", encoding="utf8")
    jokes = json.load(file)
    jokes_list = [x for x in jokes if x['type'] == type]
    file.close()
    return jsonify(random.choices(jokes_list, k=n))


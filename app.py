from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, jsonify, redirect, json, request, make_response
from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
import random
import uuid
import jwt


app = Flask(__name__)
app.config['Secret_Key'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Data/storage.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    user_name = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# class Quotes(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     quote = db.Column(db.String(500), nullable=False)
#     author = db.Column(db.String(100), nullable=False)


# class Jokes(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     type = db.Column(db.String(10), nullable=False)
#     setup = db.Column(db.String(500), nullable=False)
#     punchline = db.Column(db.String(500), nullable=False)


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'token' in request.headers:
            token_h = request.headers['token']

        if not token_h:
            return jsonify({'message': 'Token is missing'}), 401

        try:
            data = jwt.decode(token_h, app.config['Secret_Key'], algorithms=['HS256'])
            current_user = Users.query.filter_by(
                public_id=data['public_id']).first()
            # return data['public_id']

        except:
            return jsonify({'message': 'Token is invalid'}), 401
        return f(current_user, *args, **kwargs)
    return decorator


@app.route('/register', methods=['POST'])
def register():
    data = request.form

    hashed_password = generate_password_hash(data['password'], method='sha256')
    user = Users.query.filter_by(user_name=data['username']).first()

    if not user:
        new_user = Users(
            public_id=str(uuid.uuid4()),
            user_name=data['username'],
            password=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        return make_response('Successfully Created User', 201)
    else:
        return make_response('User already exists', 202)


@app.route('/login', methods=['POST'])
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response(
            'Could not verify', 401,
            {'WWW-Authenticate': 'Basic realm="Login required!!!"'}
        )
    user = Users.query.filter_by(user_name=auth.username).first()

    if not user:
        return make_response(
            'Could not verify', 401,
            {'WWW-Authenticate': 'Basic realm="User Not Exist!!!"'}
        )

    if check_password_hash(user.password, auth.password):
        token = jwt.encode({
            'public_id': user.public_id,
            'exp': datetime.utcnow() + timedelta(minutes=30)
        }, app.config['Secret_Key'])

        return make_response(jsonify({
            'token': token
        }), 201)

    return make_response(
        'Could not verify', 403,
        {'WWW-Authenticate': 'Basic realm="Wrong Password!!!"'}
    )


@app.route('/users', methods=['GET'])
@token_required
def get_all_users(current_user):
    users = Users.query.all()
    output = []
    for user in users:
        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['username'] = user.user_name
        user_data['created_at'] = user.created_at
        output.append(user_data)
    return jsonify({'users': output})


@app.route("/", methods=['GET'])
def hello_world():
    return redirect("https://drish-xd.is-a.dev/rest-api/")


# Quotes API

@app.route("/quotes", methods=['GET'])
@token_required
def quotes(current_user):
    file = open("./Data/quotes.json", "r", encoding="utf8")
    allquotes = json.load(file)
    file.close()
    return jsonify(allquotes)


# Get a random quote

@app.route("/quotes/random", methods=['GET'])
@token_required
def random_quote(current_user):
    file = open("./Data/quotes.json", "r", encoding="utf8")
    quote = json.load(file)
    file.close()
    return jsonify(random.choice(quote))


# Get n random quotes

@app.route("/quotes/random/<int:n>", methods=['GET'])
@token_required
def random_quotes(current_user, n):
    file = open("./Data/quotes.json", "r", encoding="utf8")
    quotes = json.load(file)
    file.close()
    return jsonify(random.choices(quotes, k=n))


# Seach Quotes by Author

@app.route("/quotes/author/<string:author>", methods=['GET'])
@token_required
def quotes_author(current_user, author):
    file = open("./Data/quotes.json", "r", encoding="utf8")
    quotes = json.load(file)
    quotes_author = [x for x in quotes
                     if author in x["author"]
                     or author in x["author"].lower()
                     or author in x["author"].upper()]
    file.close()
    return jsonify(quotes_author)


# Jokes API

@app.route("/jokes", methods=['GET'])
@token_required
def jokes(current_user):
    file = open("./Data/jokes.json", "r", encoding="utf8")
    alljokes = json.load(file)
    file.close()
    return jsonify(alljokes)


# Get a random joke

@app.route("/jokes/random", methods=['GET'])
@token_required
def random_joke(current_user):
    file = open("./Data/jokes.json", "r", encoding="utf8")
    joke = json.load(file)
    file.close()
    return jsonify(random.choice(joke))


# Get n random jokes

@app.route("/jokes/random/<int:n>", methods=['GET'])
@token_required
def random_jokes(current_user, n):
    file = open("./Data/jokes.json", "r", encoding="utf8")
    jokes = json.load(file)
    file.close()
    return jsonify(random.choices(jokes, k=n))


# Seach Jokes by Type

@app.route("/jokes/<string:type>", methods=['GET'])
@token_required
def jokes_by_type(current_user, type):
    file = open("./Data/jokes.json", "r", encoding="utf8")
    jokes = json.load(file)
    jokes_list = [x for x in jokes if x['type'] == type]
    file.close()
    return jsonify(jokes_list)


# Get a random joke by type

@app.route("/jokes/<string:type>/random", methods=['GET'])
@token_required
def random_joke_by_type(current_user, type):
    file = open("./Data/jokes.json", "r", encoding="utf8")
    jokes = json.load(file)
    jokes_list = [x for x in jokes if x['type'] == type]
    file.close()
    return jsonify(random.choice(jokes_list))


# Get n random jokes by type

@app.route("/jokes/<string:type>/random/<int:n>", methods=['GET'])
@token_required
def random_jokes_by_type(current_user, type, n):
    file = open("./Data/jokes.json", "r", encoding="utf8")
    jokes = json.load(file)
    jokes_list = [x for x in jokes if x['type'] == type]
    file.close()
    return jsonify(random.choices(jokes_list, k=n))


if __name__ == '__main__':
    app.run(debug=True)

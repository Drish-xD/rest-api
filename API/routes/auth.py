import uuid
from datetime import datetime, timedelta
from functools import wraps

import jwt
from API.model import Users, db
from API.settings import SECRET_KEY
from flask import Blueprint, Flask, jsonify, make_response, redirect, request
from werkzeug.security import check_password_hash, generate_password_hash

auth = Blueprint('auth', __name__)

@auth.route("/", methods=['GET'])
def docs():
    return redirect("https://drish-xd.is-a.dev/rest-api/")


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'token' in request.headers:
            token_h = request.headers['token']

        if not token_h:
            return jsonify({'message': 'Token is missing'}), 401

        try:
            data = jwt.decode(token_h, SECRET_KEY, algorithms=['HS256'])
            current_user = Users.query.filter_by(public_id=data['public_id']).first()

        except:
            return jsonify({'message': 'Token is invalid'}), 401
        return f(current_user, *args, **kwargs)
    return decorator


@auth.route('/register', methods=['POST'])
def register_user():
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


@auth.route('/login', methods=['POST'])
def login_user():
    auth_user = request.authorization

    if not auth_user or not auth_user.username or not auth_user.password:
        return make_response(
            'Could not verify', 401,
            {'WWW-Authenticate': 'Basic realm="Login required!!!"'}
        )
    user = Users.query.filter_by(user_name=auth_user.username).first()

    if not user:
        return make_response(
            'Could not verify', 401,
            {'WWW-Authenticate': 'Basic realm="User Not Exist!!!"'}
        )

    if check_password_hash(user.password, auth_user.password):
        payload = {
            'public_id': user.public_id,
            'exp': datetime.utcnow() + timedelta(minutes=30)
        }
        secret= str(SECRET_KEY)
        token = jwt.encode(payload, secret)
        print("token:" , secret, type(secret))
        return make_response(jsonify({
            'token': token
        }), 201)

    return make_response(
        'Could not verify', 403,
        {'WWW-Authenticate': 'Basic realm="Wrong Password!!!"'}
    )


@auth.route('/users', methods=['GET'])
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

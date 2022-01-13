from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
import psycopg2

db = SQLAlchemy()

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

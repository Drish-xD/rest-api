from flask import Flask

from API.commands import create_db
from API.model import Users, db
from API.routes.auth import auth
from API.routes.jokes import jokes
from API.routes.quotes import quotes


def create_app(config_file="settings.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    db.init_app(app)

    app.register_blueprint(auth)
    app.register_blueprint(quotes)
    app.register_blueprint(jokes)

    app.cli.add_command(create_db)

    return app

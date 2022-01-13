import click 
from flask.cli import with_appcontext

from .model import db, Users

@click.command(name='create_db')
@with_appcontext
def create_db():
    db.create_all()
    return 'Database created!'
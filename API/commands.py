import click 
from flask.cli import with_appcontext

from .model import db, Users

@click.command(name='create_db')
@with_appcontext
def create_db():
    db.create_all()
    print('Database created!')


@click.command(name='drop_db')
@with_appcontext
def drop_db():
    db.drop_all()
    print('Database dropped!')
import pymysql
from flask import current_app, g

def connect_db():
    return pymysql.connect(
        host=current_app.config['localhost'],
        user=current_app.config['root'],
        password=current_app.config[''],
        db=current_app.config['mydb'],
        cursorclass=pymysql.cursors.DictCursor
    )

def get_db():
    if 'db' not in g:
        g.db = connect_db()
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

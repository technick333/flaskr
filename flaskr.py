import sqlite3
import os

from flask import Flask, request,session,g,redirect,url_for,abort,\
    render_template,flash

DATABASE = './flaskr.db'
DEBUG = True
SECRET_KEY  = 'development key'
USERNAME = 'admin'
PASSWORD = 'admin'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path,'flaskr.db'),
    DEBUG=True,
    SECRET_KEY='development kay',
    USERNAME = 'admin',
    PASSWORD = 'admin'))

app.config.from_envvar('FLASKR_SETTINGS',silent=True)

def connect_db():
    
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    if not hasattr(g,'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g,'sqlite_db'):
        g.sqlite_db.close()




def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql',mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()




if __name__ == '__main__':
    app.run()

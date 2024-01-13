from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from utils.db import db

from models import *
from apis import all_routes

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)

all_routes.init_app(app)


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

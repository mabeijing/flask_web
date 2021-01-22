from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

__all__ = ['app', 'db']

app = Flask(__name__)
app.config.from_pyfile('config/base_setting.py')

db = SQLAlchemy()
db.init_app(app)

CORS(app)

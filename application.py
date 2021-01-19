from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()


class Application(Flask):
    def __init__(self, name):
        super().__init__(import_name=name)
        self.config.from_pyfile('config/base_setting.py')
        db.init_app(self)
        CORS(self)


app = Application(__name__)

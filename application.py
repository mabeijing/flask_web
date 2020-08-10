from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class Application(Flask):
    def __init__(self, name):
        super().__init__(import_name=name)
        self.config.from_pyfile('config/base_setting.py')
        db.init_app(self)


db = SQLAlchemy()
app = Application(__name__)


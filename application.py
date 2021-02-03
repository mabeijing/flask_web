from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_session import Session
from flask_migrate import Migrate

migrate = Migrate()


def register_blueprints(app):
    from views.user import user
    from views.good import good
    from views.tasks import task
    from views.interface import interface
    app.register_blueprint(user)
    app.register_blueprint(good)
    app.register_blueprint(task)
    app.register_blueprint(interface)


def create_api(app):
    from views.api import User, Demo, Case
    api = Api(app)
    api.add_resource(User, '/api/v1/user')
    api.add_resource(Demo, '/api/v1/demo')
    api.add_resource(Case, '/api/v1/case')


def create_app():
    from models import db
    from async_tasks import ext
    from utils import cache
    app = Flask(__name__)
    app.config.from_pyfile('config/base_setting.py')
    cache.init_app(app)
    ext.init_app(app)
    db.init_app(app)
    register_blueprints(app)
    create_api(app)
    migrate.init_app(app, db)
    CORS(app)
    return app

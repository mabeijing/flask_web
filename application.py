from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_session import Session
from flask_migrate import Migrate

migrate = Migrate()


def register_blueprints(app):
    from views.user import user
    from views.good import good
    app.register_blueprint(user)
    app.register_blueprint(good)


def create_api(app):
    from views.restful_api import User, Case
    api = Api(app)
    api.add_resource(User, '/api/v1/user')
    api.add_resource(Case, '/api/v1/case')


def create_app():
    from models import db
    app = Flask(__name__)
    app.config.from_pyfile('config/base_setting.py')
    db.init_app(app)
    register_blueprints(app)
    create_api(app)
    migrate.init_app(app, db)
    CORS(app)
    return app

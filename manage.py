from application import app
from views.user import user
from views.good import good
from views.restful_api import User, Case
from flask_restful import Api
from werkzeug.exceptions import HTTPException

import logging

logging.basicConfig(level=logging.DEBUG)

api = Api(app)

app.register_blueprint(user)
app.register_blueprint(good)
api.add_resource(User, '/api/v1/user')
api.add_resource(Case, '/api/v1/case')


@app.errorhandler(Exception)
def errors_handle(error):
    if not isinstance(error, HTTPException):
        response = {
            'code': '500',
            'name': str(type(error)),
            'msg': str(error),
        }
        return response
    else:
        return {'code': error.code,
                'name': error.name,
                'msg': error.description}


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)

# from flask_script import Manager
# manager = Manager(app)
# @manager.command
# def runserver():
#     app.run(debug=True, host='localhost', port=5000)
#
#
# if __name__ == "__main__":
#     manager.run()

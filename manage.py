from application import app
from views.user import user
from views.good import good
from werkzeug.exceptions import HTTPException

app.register_blueprint(user)
app.register_blueprint(good)


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

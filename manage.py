from application import create_app
from service.chat_room_server import socket_io
from werkzeug.exceptions import HTTPException

app = create_app()
socket_io.init_app(app, cors_allowed_origins="*")


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
    socket_io.run(app, debug=True, host='localhost', port=5000)

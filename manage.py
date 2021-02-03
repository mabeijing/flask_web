from application import create_app

app = create_app()

# socket_io导入必须在app实例化之后
# 因为在socket_server下导入了异步任务，异步任务必须在app实例化之后才能正确代理
from service.chat_room_server import socket_io

socket_io.init_app(app, cors_allowed_origins="*")

from werkzeug.exceptions import HTTPException


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

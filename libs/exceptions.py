from application import app
from flask import jsonify
from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import NotFound

"""
*400* `Bad Request`
*401* ``Unauthorized``
*403* `Forbidden`
*404* `Not Found`
*405* `Method Not Allowed`
*406* `Not Acceptable`
*408* `Request Timeout`
*409* `Conflict`
*410* `Gone`
*411* `Length Required`
*412* `Precondition Failed`
*413* `Request Entity Too Large`
*414* `Request URI Too Large`
*415* `Unsupported Media Type`
*416* `Requested Range Not Satisfiable`
*417* `Expectation Failed`
*418* `I'm a teapot`
*422* `Unprocessable Entity`
*423* `Locked`
*424* `Failed Dependency`
*428* `Precondition Required`
*429* `Too Many Requests`
*500* `Internal Server Error`
*501* `Not Implemented`
*502* `Bad Gateway`
*503* `Service Unavailable`
*504* `Gateway Timeout`
*505* `HTTP Version Not Supported`
"""


@app.errorhandler(Exception)
def errors_handle(error):
    if not isinstance(error, HTTPException):
        response = {
            'err_code': 10500,
            'msg': 'Internal Server Error',
            'data': {},
        }
        return jsonify(response), 500

    if isinstance(error, NotFound):
        response = {
            'err_code': 10404,
            'msg': error.description,
            'data': {},
        }
        return jsonify(response), error.code

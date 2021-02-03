from flask.blueprints import Blueprint
from flask import render_template

interface = Blueprint('interface', __name__, url_prefix='/interface')


@interface.route('/')
def index():
    # return render_template('websocket_demo.html', async_mode=socketio.async_mode)
    return render_template('websocket_demo.html', async_mode='threading')

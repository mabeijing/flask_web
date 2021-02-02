# -*- coding:utf-8 -*-
from flask import Blueprint, g
from async_tasks.tasks import send_template_sms

task = Blueprint('task', __name__, url_prefix='/task')


@task.route('/execute')
def good_lists():
    send_template_sms.delay()
    return 'execute success'

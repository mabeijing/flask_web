# -*- coding:utf-8 -*-
from flask import Blueprint
from async_tasks.sms.tasks import send_template_sms

task = Blueprint('task', __name__, url_prefix='/task')


@task.route('/execute')
def good_lists():
    send_template_sms.delay()
    return 'execute success'

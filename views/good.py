# -*- coding:utf-8 -*-
from flask import Blueprint
from sysnc_tasks.sms.tasks import send_template_sms

good = Blueprint('good', __name__, url_prefix='/good')


@good.route('/list')
def good_lists():
    send_template_sms.delay()
    return 'good_lists'


# 动态参数
@good.route('/info/<good_name>', methods=["POST"])
def get_good_info(good_name):
    data = {
        'code': 200,
        'msg': good_name
    }
    return data, 200

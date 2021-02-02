# -*- coding:utf-8 -*-
from flask import Blueprint

good = Blueprint('good', __name__, url_prefix='/good')


@good.route('/list')
def good_lists():
    return 'good_lists'


# 动态参数
@good.route('/info/<good_name>', methods=["POST"])
def get_good_info(good_name):
    data = {
        'code': 200,
        'msg': good_name
    }
    return data, 200

# -*- coding:utf-8 -*-
from flask import Blueprint
good = Blueprint('good', __name__)


@good.route('/list')
def good_lists():
    return 'good_lists'


@good.route('/info', methods=["POST"])
def get_good_info():
    data = {
        'code': 200,
        'msg': 'ok',
    }
    return data, 200


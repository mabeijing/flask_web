# -*- coding:utf-8 -*-
from flask import Blueprint, request, make_response, g
from models.User import User
from flask_wtf.csrf import generate_csrf
from validate import UserForm
import logging
import time

logging.root.setLevel(logging.NOTSET)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

user = Blueprint('user', __name__, url_prefix='/user')


@user.before_request
def before_quest():
    t = time.time()
    g.timestamp = t


@user.after_request
def after_request(response):
    stamp = time.time() - g.timestamp
    logger.warning(stamp)
    return response


@user.route('/login', methods=['POST'])
def user_login():
    req = request.form
    user_form = UserForm(req, meta={'csrf': False})
    if not user_form.validate():
        return {'success': False, 'data': user_form.errors}
    u = User.query_one(username=user_form.username.data)
    if u and u.password == user_form.password.data:
        response = make_response({'success': True, 'data': 'login success!'})
    else:
        response = make_response({'success': False, 'data': '用户名或密码不正确!'})
    response.set_cookie('csrf_token', generate_csrf())
    return response


@user.route('/register', methods=['POST'])
def register_member():
    user_form = UserForm(request.form, meta={'csrf': False})
    if not user_form.validate():
        return {'success': False, 'data': user_form.errors}
    d = User.query_one(**user_form.data)
    if d:
        return {'success': False, 'data': '用户已存在'}
    User(**user_form.data).save()
    user_one = User.query_one(username=user_form.username.data)
    return {'success': True, 'data': {'id': user_one.ID, 'username': user_one.username}}

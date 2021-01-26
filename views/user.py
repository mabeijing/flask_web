# -*- coding:utf-8 -*-
from flask import Blueprint, request, make_response
from models.User import User as UserModel
from models.User import Demo
from flask_wtf.csrf import generate_csrf
from validate import UserForm
import logging

user = Blueprint('user', __name__, url_prefix='/user')


@user.after_request
def after_request(response):
    logging.error(response)
    return response


@user.route('/login', methods=["GET"])
def user_login():
    user = UserModel.query.filter_by(id=1).first()
    print(user)
    demo = Demo.query.filter_by(id=1).first()
    print(demo.create_time)
    response = make_response('hello')
    response.set_cookie('csrf_token', generate_csrf())
    return response


@user.route('/register', methods=['POST'])
def register_member():
    userForm = UserForm(request.form)
    if not userForm.validate():
        return userForm.errors
    return userForm.data

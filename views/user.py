# -*- coding:utf-8 -*-
from application import app
from flask import Blueprint, request, escape, session, make_response
from models.User import User
from flask_wtf.csrf import generate_csrf
from flask_restful import Api, Resource
from validate import JsonInput, ParamInput, UserForm
import logging

user = Blueprint('user', __name__, url_prefix='/user')

api = Api(user)


@user.after_request
def after_request(response):
    logging.error(response)
    return response


@api.resource('/info')
class User(Resource):
    def get(self):
        """获取资源基本信息"""
        # userForm = UserForm(request.args)
        # if not userForm.validate():
        #     return userForm.errors
        # return userForm.data
        print(request.args)
        param = ParamInput(request)
        if not param.validate():
            return param.errors
        return 'get'

    def post(self):
        """新增一个user资源"""
        logging.error(request.form)
        userForm = UserForm(request.form, meta={'csrf': False})
        if not userForm.validate():
            return {
                'success': False,
                'data': userForm.errors
            }
        return {
            'success': True,
            'data': userForm.data
        }

    def put(self):
        """修改一个user资源"""
        json_inputs = JsonInput(request)
        if not json_inputs.validate():
            return json_inputs.errors
        return 'put'

    def delete(self):
        """删除一个user资源"""
        return 'delete'


@user.route('/login', methods=["GET"])
def user_login():
    response = make_response('hello')
    response.set_cookie('csrf_token', generate_csrf())
    return response


@user.route('/register', methods=['POST'])
def register_member():
    userForm = UserForm(request.form)
    if not userForm.validate():
        return userForm.errors
    return userForm.data

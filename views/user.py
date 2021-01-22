# -*- coding:utf-8 -*-
from application import app
from flask import Blueprint, request, escape, session, make_response
from models.User import User
from flask_wtf.csrf import generate_csrf
from flask_restful import Api, Resource
from validate import JsonInput, ParamInput, UserForm

user = Blueprint('user', __name__, url_prefix='/user')

api = Api(user)


# @user.after_request
# def after_request(response):
#     # 调用函数生成 csrf_token
#     csrf_token = generate_csrf()
#     # 通过 cookie 将值传给前端
#     response.set_cookie("csrf_token", csrf_token)
#     return response


@api.resource('/info')
class User(Resource):
    def get(self):
        """获取资源基本信息"""
        # userForm = UserForm(request.args)
        # if not userForm.validate():
        #     return userForm.errors
        # return userForm.data
        param = ParamInput(request)
        if not param.validate():
            return param.errors
        return 'get'

    def post(self):
        """新增一个user资源"""
        userForm = UserForm(request.form, meta={'csrf': False})
        if not userForm.validate():
            return userForm.errors
        return userForm.data

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

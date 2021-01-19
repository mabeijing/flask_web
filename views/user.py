# -*- coding:utf-8 -*-
from application import db
from flask import Blueprint, request, escape, session, make_response
from models.User import User
from flask_restful import Api, Resource
from validate.userForm import UserForm
from flask_wtf.csrf import generate_csrf

user = Blueprint('user', __name__, url_prefix='/user')

api = Api(user)


@api.resource('/<int:uid>', '/list')
class User(Resource):
    def get(self):
        """获取资源基本信息"""
        userForm = UserForm(request.args)
        if not userForm.validate():
            return {'code': 10010,
                    'msg': userForm.user.errors or userForm.pwd}
        return {'code': 'get'}

    def post(self, uid):
        """新增一个user资源"""
        userForm = UserForm(request.form)
        if not userForm.validate():
            return {'code': 10011,
                    'msg': userForm.errors}
        print(userForm.data)
        return uid

    def put(self, uid):
        """修改一个user资源"""
        return 'put'

    def delete(self, uid):
        """删除一个user资源"""
        return 'delete'


@user.route('/login', methods=["GET"])
def user_login():
    """
    request.args 获取url?name='beijing'&password='123456'全部参数
    request.args.get(key) 获取指定key参数

    request.form 获取表单x-www-form-urlencoded全部参数值
    request.form[key] 获取指定key参数
    user_name = request.form.get('username', default=None)

    request.get_data() 获取表单x-www-form-urlencoded的二进制值
    :return:
    """
    # print(request.headers['Content-Type'])
    response = make_response('hello')
    response.set_cookie("csrf_token", generate_csrf())
    return response




@user.route('/register', methods=['POST'])
def register_member():
    form = UserInfoValidate(request.form)
    if not form.validate():
        # 验证用户名
        form.MSG = form.username.errors if form.username.errors else form.password.errors
        form.ERR_CODE = form.username.id if form.username.id else form.password.id
        form.CODE = 200
        form.DATA = {}
        return form.return_data()
    user_name = form.username.data
    password = form.password.data
    one = User()
    result = one.query.filter_by(username=user_name).first()
    if result:
        return {'err_code': '202',
                'msg': '已注册用户',
                'data': {
                    # 'username': escape(result.username),
                    'username': result.username,
                    'password': result.password},
                }, 200
    else:
        use = User(username=user_name, password=password)
        db.session.add(use)
        db.session.commit()
        return {'err_code': '201',
                'msg': '新注册用户',
                'data': {
                    'username': escape(use.username),
                    'password': use.password},
                }, 200

# -*- coding:utf-8 -*-
from application import db
from flask import Blueprint, request, escape
from models.User import User
from libs.exceptions import errors_handle
from validation.user_validator import UserValidate, PasswordValidate

user = Blueprint('user', __name__)


@user.route('/login', methods=["GET", "POST"])
def user_login():
    """
    获取客户端发送header数据
    header = request.headers['key']

    获取客户端json提交数据。
    data_json = request.json
    :return:
    """
    name = request.form.get('name', default=None)
    if not name:
        return {'err_code': '204',
                'msg': 'name是必填字段',
                'data': {}
                }, 200

    users = User()
    one = users.query.filter_by(username=name).first()

    if not one:
        return {'code': '203',
                'msg': name + '用户未注册',
                'data': {}
                }, 200
    password = request.form.get('password', default=None)
    if not password:
        return {'code': '204',
                'msg': 'password是必填字段',
                'data': {}
                }, 200
    if one.username == name and one.password == password:
        return {'code': '200',
                'msg': '用户登陆成功',
                'data': {
                    'username': one.username,
                    'password': one.password}
                }, 200
    else:
        return {'code': '205',
                'msg': '用户名或密码不正确',
                'data': {
                    'username': name,
                    'password': password}
                }, 200


@user.route('/register', methods=['POST'])
def register_member():
    """
    request.args 获取url?id=1&name='马北京'全部参数
    request.args.get(key) 获取指定key参数

    request.form 获取表单x-www-form-urlencoded全部参数值
    request.form[key] 获取指定key参数
    user_name = request.form.get('username', default=None)

    request.get_data() 获取表单x-www-form-urlencoded的二进制值
    :return:
    """

    form = UserValidate(request.form)
    pass_form = PasswordValidate(request.form)
    if not form.validate():
        # 验证用户名
        form.MSG = form.username.errors
        form.ERR_CODE = form.username.id
        form.CODE = 200
        form.DATA = {}
        return form.return_data()
    if not pass_form.validate():
        # 验证密码
        pass_form.MSG = pass_form.password.errors
        pass_form.ERR_CODE = pass_form.password.id
        pass_form.CODE = 200
        pass_form.DATA = {}
        return pass_form.return_data()
    user_name = form.username.data
    password = pass_form.password.data
    one = User()
    result = one.query.filter_by(username=user_name).first()
    if result:
        return {'err_code': '202',
                'msg': '已注册用户',
                'data': {
                    'username': escape(result.username),
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

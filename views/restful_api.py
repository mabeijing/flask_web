from flask import request
from flask_restful import Resource
from validate import JsonInput, ParamInput, UserForm


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

    # def post(self):
    #     """新增一个user资源"""
    #     userForm = UserForm(request.form)
    #     if not userForm.validate():
    #         return userForm.errors
    #     return userForm.data

    def post(self):
        """修改一个user资源"""
        print(request.json)

        json_inputs = JsonInput(request)
        if not json_inputs.validate():
            return {
                'success': False,
                'data': json_inputs.errors
            }
        data = request.json
        if data.get('username') == 'admin' and data.get('password') == '123456':
            return {
                'success': True,
                'data': '登陆成功'
            }
        else:
            return {
                'success': False,
                'data': '用户名或者密码不正确, 真的是草啊'
            }

    def delete(self):
        """删除一个user资源"""
        return 'delete'

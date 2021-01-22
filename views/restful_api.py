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
        return {
            'success': True,
            'data': {}
        }

    def delete(self):
        """删除一个user资源"""
        return 'delete'

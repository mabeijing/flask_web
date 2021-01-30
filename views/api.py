from flask import request
from flask_restful import Resource
from validate import JsonInput, ParamInput, UserForm


class Case(Resource):
    method_decorators = []

    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


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

    def put(self):
        """新增一个user资源"""
        userForm = UserForm(request.form)
        if not userForm.validate():
            return userForm.errors
        return userForm.data

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


class Demo(Resource):
    def get(self):
        return {
            "list": [
                {
                    "id": 1,
                    "name": "张三三",
                    "money": 123,
                    "address": "广东省东莞市长安镇",
                    "state": "成功",
                    "date": "2019-11-1",
                    "thumb": "https://lin-xin.gitee.io/images/post/wms.png"
                },
                {
                    "id": 2,
                    "name": "李四",
                    "money": 456,
                    "address": "广东省广州市白云区",
                    "state": "成功",
                    "date": "2019-10-11",
                    "thumb": "https://lin-xin.gitee.io/images/post/node3.png"
                },
                {
                    "id": 3,
                    "name": "王五",
                    "money": 789,
                    "address": "湖南省长沙市",
                    "state": "失败",
                    "date": "2019-11-11",
                    "thumb": "https://lin-xin.gitee.io/images/post/parcel.png"
                },
                {
                    "id": 4,
                    "name": "赵六",
                    "money": 1011,
                    "address": "福建省厦门市鼓浪屿",
                    "state": "成功",
                    "date": "2019-10-20",
                    "thumb": "https://lin-xin.gitee.io/images/post/notice.png"
                }
            ],
            "pageTotal": 4
        }

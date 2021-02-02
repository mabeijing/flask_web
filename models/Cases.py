# -*- coding: utf-8 -*-
import json
from datetime import datetime
from . import db


class Case(db.Model):
    __tablename__ = 'case'
    ID = db.Column(db.Integer, autoincrement=True, nullable=False, primary_key=True, comment='用例ID')
    SERIAL_NO = db.Column(db.String(128), nullable=False, index=True, comment='用例编号')
    LEVEL = db.Column(db.String(1), nullable=False, comment='用例等级')
    DESCRIPTION = db.Column(db.String(32), nullable=False, comment='用例描述')
    REQUEST_METHOD = db.Column(db.Enum('GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS'), nullable=False,
                               default='GET', comment='请求方法')
    REQUEST_HEADERS = db.Column(db.JSON, comment='请求头')
    REQUEST_BODY = db.Column(db.JSON, comment='请求体')
    CREATE_TIME = db.Column(db.DateTime, default=datetime.now, comment='创建时间')
    UPDATE_TIME = db.Column(db.DateTime, default=datetime.now, comment='更新时间')
    DELETE_FLAG = db.Column(db.Boolean, default=False, comment='删除标志')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def select_all(self, **kwargs):
        """
        obj_list.total ： 数据库总数,可以通过filter_by()过滤
        obj_list.page ： 当前页面
        """
        data_dict = {}
        data_list = []
        tmp_dict = {}

        paginate_dict = {'error_out': False}
        if kwargs.get('pageIndex', None):
            paginate_dict['page'] = int(kwargs.get('pageIndex'))
        if kwargs.get('pageSize', None):
            paginate_dict['per_page'] = int(kwargs.get('pageSize'))

        filter_dict = {'DELETE_FLAG': 0}
        if kwargs.get('id', None) and kwargs.get('id') != '':
            filter_dict['ID'] = int(kwargs.get('id'))
        if kwargs.get('state', None) and kwargs.get('state') != '':
            filter_dict['DELETE_FLAG'] = int(kwargs.get('state'))
        if kwargs.get('level', None) and kwargs.get('level') != '':
            filter_dict['LEVEL'] = kwargs.get('level')

        obj_list = db.session.query(self.__class__).filter_by(**filter_dict).paginate(**paginate_dict)
        for case_obj in obj_list.items:
            tmp_dict['ID'] = case_obj.ID
            tmp_dict['SERIAL_NO'] = case_obj.SERIAL_NO
            tmp_dict['LEVEL'] = case_obj.LEVEL
            tmp_dict['DESCRIPTION'] = case_obj.DESCRIPTION
            tmp_dict['REQUEST_METHOD'] = case_obj.REQUEST_METHOD
            tmp_dict['REQUEST_HEADERS'] = json.dumps(case_obj.REQUEST_HEADERS)
            tmp_dict['REQUEST_BODY'] = json.dumps(case_obj.REQUEST_BODY)
            tmp_dict['CREATE_TIME'] = case_obj.CREATE_TIME.strftime('%Y-%m-%d %H:%M:%S')
            tmp_dict['UPDATE_TIME'] = case_obj.UPDATE_TIME.strftime('%Y-%m-%d %H:%M:%S')
            tmp_dict['DELETE_FLAG'] = case_obj.DELETE_FLAG
            data_list.append(tmp_dict.copy())
        data_dict['list'] = data_list
        data_dict['pageTotal'] = obj_list.total
        return data_dict

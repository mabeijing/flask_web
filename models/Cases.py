# -*- coding: utf-8 -*-
import math
from datetime import datetime
from flask import current_app
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
        with current_app.app_context():
            db.session.add(self)
            db.session.commit()

    def select_all(self, page=1):
        """
        obj_list.total ： 数据库总数,可以通过filter_by()过滤
        obj_list.page ： 当前页面
        """
        data_dict = {}
        data_list = []
        tmp_dict = {}
        with current_app.app_context():
            obj_list = db.session.query(Case).filter_by(DELETE_FLAG=0).paginate(page=page, per_page=5, error_out=False)

        for case_obj in obj_list.items:
            tmp_dict['ID'] = case_obj.ID
            tmp_dict['SERIAL_NO'] = case_obj.SERIAL_NO
            tmp_dict['LEVEL'] = case_obj.LEVEL
            tmp_dict['DESCRIPTION'] = case_obj.DESCRIPTION
            tmp_dict['REQUEST_METHOD'] = case_obj.REQUEST_METHOD
            tmp_dict['REQUEST_HEADERS'] = case_obj.REQUEST_HEADERS
            tmp_dict['REQUEST_BODY'] = case_obj.REQUEST_BODY
            tmp_dict['CREATE_TIME'] = case_obj.CREATE_TIME.strftime('%Y-%m-%d %H:%M:%S')
            tmp_dict['UPDATE_TIME'] = case_obj.UPDATE_TIME.strftime('%Y-%m-%d %H:%M:%S')
            tmp_dict['DELETE_FLAG'] = case_obj.DELETE_FLAG
            data_list.append(tmp_dict)
        data_dict['list'] = data_list
        data_dict['pageTotal'] = math.ceil(obj_list.total/5)
        data_dict['numberTotal'] = obj_list.total
        return data_dict

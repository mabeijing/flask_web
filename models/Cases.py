# -*- coding: utf-8 -*-
from datetime import datetime
from . import db


class Case(db.Model):
    __tablename__ = 'case'
    ID = db.Column(db.Integer, autoincrement=True, nullable=False, primary_key=True, comment='用例ID')
    SERIAL_NO = db.Column(db.String(128), nullable=False, index=True, comment='用例编号')
    LEVEL = db.Column(db.String(1), nullable=False, comment='')
    DESCRIPTION = db.Column(db.String(32), nullable=False, comment='')
    REQUEST_METHOD = db.Column(db.Enum('GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS'), nullable=False,
                               default='GET', comment='')
    REQUEST_HEADERS = db.Column(db.JSON, comment='')
    REQUEST_BODY = db.Column(db.JSON, comment='')
    CREATE_TIME = db.Column(db.DateTime, default=datetime.now, comment='创建时间')
    UPDATE_TIME = db.Column(db.DateTime, default=None, comment='更新时间')
    DELETE_FLAG = db.Column(db.Boolean, default=False, comment='删除标志')

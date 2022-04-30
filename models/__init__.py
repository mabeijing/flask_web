from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseModel(db.Model):
    __abstract__ = True
    ID = db.Column(db.Integer, autoincrement=True, nullable=False, primary_key=True, comment='主键ID')
    CREATE_TIME = db.Column(db.DateTime, default=datetime.now, comment='创建时间')
    UPDATE_TIME = db.Column(db.DateTime, default=datetime.now, comment='更新时间')
    DELETE_FLAG = db.Column(db.Boolean, default=False, comment='删除标志')


__all__ = [db, BaseModel]

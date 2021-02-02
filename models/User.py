# -*- coding: utf-8 -*-
from . import db, BaseModel


class User(BaseModel):
    __tablename__ = 'tf_f_user'
    __bind_key__ = 'sqlite_db'

    USERNAME = db.Column(db.String(255), nullable=False, comment='用户名')
    PASSWORD = db.Column(db.String(255), nullable=False, comment='密码')
    CONFIRM_PWD = db.Column(db.String(255), nullable=False, comment='确认密码')

    def __repr__(self):
        return "<user>: id={id}, username={username}".format(id=self.ID, username=self.USERNAME)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def query_one(**kwargs):
        return User.query.filter_by(**kwargs).first()

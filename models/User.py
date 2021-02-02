# -*- coding: utf-8 -*-
from . import db, BaseModel


class User(BaseModel):
    __tablename__ = 'user'
    __bind_key__ = 'extra'

    username = db.Column(db.String(255))
    password = db.Column(db.String(255), nullable=False)
    confirm_password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return "<user>: id={id}, username={username}".format(id=self.id, username=self.username)



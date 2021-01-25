# -*- coding: utf-8 -*-
from application import db


class User(db.Model):
    __tablename__ = 'user'
    __bind_key__ = 'address'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __repr__(self):
        return "<user>: id={id}, username={username}".format(id=self.id, username=self.username)


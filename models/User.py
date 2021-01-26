# -*- coding: utf-8 -*-
from . import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    __bind_key__ = 'extra'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __repr__(self):
        return "<user>: id={id}, username={username}".format(id=self.id, username=self.username)


class Demo(db.Model):
    __tablename__ = 'demo'

    id = db.Column(db.Integer, primary_key=True)
    demo = db.Column(db.String(128), nullable=True)
    create_time = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return "<Demo>: id={id}, demo={demo}, create_time={time}".format(
            id=self.id, demo=self.demo, time=self.create_time)


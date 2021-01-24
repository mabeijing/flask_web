# -*- coding: utf-8 -*-
from application import db


class User(db.Model):
    __tablename__ = 'user'
    __bind_key__ = 'address'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))


# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String
from application import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

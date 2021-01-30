# -*- coding:utf-8 -*-
from flask import Blueprint
from models.Cases import Case

case = Blueprint('case', __name__, url_prefix='/case')

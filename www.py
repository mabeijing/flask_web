# -*- coding:utf-8 -*-
from application import app
from web.controller.user import user
from web.controller.good import good

app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(good, url_prefix='/good')


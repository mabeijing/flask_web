"""
当前版本
Flask-CeleryExt	0.3.4
celery	5.0.5
Flask	1.1.2
工厂模式的celery
1、在__init__下创建ext。导入到app工厂下ext.init_app(app)实例化
2、将tasks下的ext导入到真正的任务模块，celery = ext.celery
3、当前__init__.py只能生成ext提供工厂函数实例化。然后才能在tasks下ext.celery

4、真正的celery，需要分布式执行。
5、创建一个和async_tasks同结构的文件夹
async_tasks
-- tasks.py
6、tasks.py保证异步任务函数名字和flask下的一致
7、tasks.py实例化celery比较随意
app = Celery(__name__, broker="redis://:redis@127.0.0.1:6379/5", backend='redis://:redis@127.0.0.1:6379/6')
"""

from flask_celeryext import FlaskCeleryExt

ext = FlaskCeleryExt()


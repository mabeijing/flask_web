from urllib.parse import quote_plus as urlquote

# 增加对数据库密码特殊字符的兼容
conf = {'user': 'root',
        'password': urlquote('root@123'),
        'host': 'localhost',
        'port': 3306,
        'database': 'flask_web'}

# 支持多数据库配置
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'.format(**conf)
SQLALCHEMY_BINDS = {
        'extra': 'sqlite:////Users/mabeijing/flask_web.db'
}
SQLALCHEMY_TRACK_MODIFICATIONS = False

# JSON格式返回支持中文
JSON_AS_ASCII = False

# JSON返回自动排序，默认True，为了提高缓存性能，不建议修改False
JSON_SORT_KEYS = False

# WTForm要求CSRF：A secret key
SECRET_KEY = '123456'

# flask-wtf 对csrf的配置
# WTF_CSRF_SECRET_KEY = '12435'
WTF_CSRF_ENABLED = True


# 配置celery_redis
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

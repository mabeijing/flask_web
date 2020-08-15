from urllib.parse import quote_plus as urlquote

# 增加对数据库密码特殊字符的兼容
passwd = urlquote('Root#123')
conf = {'user': 'root',
        'passwd': passwd,
        'host': '127.0.0.1',
        'port': 3306,
        'database': 'mms_db'}

SQLALCHEMY_DATABASE_URI = 'mysql:// {user}:{passwd}@{host}:{port}/{database}'.format(**conf)
SQLALCHEMY_TRACK_MODIFICATIONS = False

# JSON格式返回支持中文
JSON_AS_ASCII = False

# WTForm要求CSRF：A secret key
SECRET_KEY = '123456'

# 配置celery_redis
CELERY_BROKER_URL = 'redis://192.168.2.222:6379/0'
CELERY_RESULT_BACKEND = 'redis://192.168.2.222:6379/0'

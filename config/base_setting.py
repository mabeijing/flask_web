SQLALCHEMY_DATABASE_URI = 'mysql://root:Root#123@192.168.8.222:3306/mms_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# JSON格式返回支持中文
JSON_AS_ASCII = False

# WTForm要求CSRF：A secret key
SECRET_KEY = '123456'

# 配置celery_redis
CELERY_BROKER_URL = 'redis://192.168.2.222:6379/0'
CELERY_RESULT_BACKEND = 'redis://192.168.2.222:6379/0'

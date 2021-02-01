from celery import Celery

app = Celery(__name__)
app.config_from_object("sysnc_tasks.config")
# 让celery自己找到任务
app.autodiscover_tasks(["sysnc_tasks.sms"])

import time
from async_tasks import ext
app = ext.celery


# 异步任务
@app.task
def send_template_sms():
    time.sleep(10)
    return 'success'

import time
from async_tasks import ext

app = ext.celery


# 异步任务
@app.task(bind=True)
def send_template_sms(self, x, y):
    """接受参数，支持self.request"""
    time.sleep(5)
    print(self.request)
    return x + y


@app.task(bind=True)
def socket_bar(self):
    """编写异步任务时。可以在适当位置增加update_state。让整个程序执行结束打印信息"""
    for i in range(1, 11):
        time.sleep(1)
        self.update_state(state="PROGRESS", meta={'p': i * 10})
    print(self.request)
    return 'finish'

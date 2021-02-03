import time
from async_tasks import ext

app = ext.celery


# 异步任务
# 增加bing=True就是绑定到对应的redis数据列表，可以直接读取数据库
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


@app.task(bind=True)
def bar(body):
    res = body.get('result')
    if body.get('status') == 'PROGRESS':
        print('\r任务进度: {0}%'.format(res.get('p')))
        # 注释方法可以在单挑记录刷新任务进度，print打印多条记录
        # sys.stdout.write('\r任务进度: {0}%'.format(res.get('p')))
        # sys.stdout.flush()
    else:
        print('\r')
        print(res)

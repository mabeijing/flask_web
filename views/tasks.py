# -*- coding:utf-8 -*-
from flask import Blueprint
from celery.result import AsyncResult
from async_tasks.tasks import send_template_sms, socket_bar

task = Blueprint('task', __name__, url_prefix='/task')


# 执行异步任务，返回任务id
@task.route('/execute')
def execute_task():
    task_result = send_template_sms.delay(4, 5)
    task_id = task_result.id
    return task_id


# 增加执行结果查询
@task.route('/query/<tid>')
def query_task(tid):
    res = AsyncResult(tid)
    print(res.result)
    return 'res.result'


# 带进度条的显示
@task.route('/finish_bar')
def finish_bar():
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

    socket_bar.delay().get(on_message=bar, propagate=False)
    return 'finish'

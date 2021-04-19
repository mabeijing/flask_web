# -*- coding:utf-8 -*-
from flask import Blueprint, request
from celery.result import AsyncResult
from utils import cache
from async_tasks.tasks import send_template_sms, socket_bar

task = Blueprint('task', __name__, url_prefix='/task')


# 执行异步任务，返回任务id
@task.route('/execute')
def execute_task():
    args = request.args
    task_result = send_template_sms.delay(args.get('user'), args.get('pwd'))
    task_id = task_result.id
    return task_id


# 增加执行结果查询
@task.route('/query/<tid>')
def query_task(tid):
    res = AsyncResult(tid)
    return {'result': res.result}


# 带进度条的显示
@task.route('/finish_bar')
def finish_bar():
    def bar(body):
        res = body.get('result')
        if body.get('status') == 'PROGRESS':
            print('\r任务进度: {0}%'.format(res.get('p')))
            print(body)
            cache.set('task_id', res.get('p'))
            # 注释方法可以在单挑记录刷新任务进度，print打印多条记录
            # sys.stdout.write('\r任务进度: {0}%'.format(res.get('p')))
            # sys.stdout.flush()
        else:
            print('\r')
            print(res)
            cache.delete(body.get('task_id'))

    _task = socket_bar.delay()
    _task.get(on_message=bar, propagate=True)
    return _task.id

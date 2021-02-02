from ..main import app


# 定义任务
@app.task
def send_template_sms():
    import time

    time.sleep(10)
    return 'success'

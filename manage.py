from application import app
from flask import Response, render_template
import libs.exceptions
import www


@app.route('/', methods=['GET'])
def index():
    """
    预留测试错误
    :return:
    """
    # 1 / 0
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

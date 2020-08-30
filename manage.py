from application import app
from flask import render_template
import libs.exceptions
import www


@app.route('/', methods=['GET'])
def index():
    """
    预留测试错误
    :return:
    """
    # 1 / 0
    content = 'Welcome Python!'
    return render_template('index.html', index=content)


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)

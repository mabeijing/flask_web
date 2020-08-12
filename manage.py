from application import app
import www


@app.route('/', methods=['GET'])
def index():
    return 'version: v1.0 ~'


@app.errorhandler(404)
def not_found(error):
    return 'page not found', 404


if __name__ == '__main__':
    app.run(debug=True, host='192.168.8.187', port=5000)

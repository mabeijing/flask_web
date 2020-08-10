from application import app

# from pyflask.controller.user import user
# from pyflask.controller.good import good
# from pyflask.controller.automatic import auto

# app.register_blueprint(user, url_prefix='/user')
# app.register_blueprint(good, url_prefix='/good')
# app.register_blueprint(auto, url_prefix='/auto')


@app.route('/', methods=['GET'])
def index():
    return 'version: v1.0 ~'


@app.errorhandler(404)
def not_found(error):
    return 'page not found', 404


if __name__ == '__main__':
    app.run(debug=True, host='192.168.8.187', port=5000)

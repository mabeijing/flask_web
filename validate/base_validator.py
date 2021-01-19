from wtforms import Form


class BaseValidator(Form):
    CODE = None
    ERR_CODE = None
    MSG = []
    DATA = {}

    def return_data(self):
        return {
                   'err_code': self.ERR_CODE,
                   'msg': self.MSG,
                   'data': self.DATA
               }, self.CODE

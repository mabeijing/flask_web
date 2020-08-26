import string
from wtforms.validators import DataRequired, Length, StopValidation
from wtforms import StringField, PasswordField, ValidationError
from .base_validator import BaseValidator


# 自定义验证器，validate_+变量名(form, field)
def validate_username(form, field):
    if not (field.data.isalnum() and field.data.startswith(tuple(string.ascii_letters))):
        raise ValidationError(message='username必须由字母开头，且不含空格的数字或字母组成')


# 自定义验证器
class UserNameFormat:
    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        if field.data.startswith('_'):
            raise StopValidation(message=self.message if self.message else 'username不能用_开头')


class UserInfoValidate(BaseValidator):
    """
    para = StringField :para是要校验字段。
    自定义校验函数，格式必须是validate_+变量名(self, field),非静态方法
    """
    username = StringField(label='用户名', validators=[
        validate_username,
        UserNameFormat(message='username非法字段开头'),
        DataRequired(message='username字段是必填字段'),
        Length(min=4, max=10, message='username长度必须在4-10之间')
        ], id=1002)
    password = PasswordField(label='密码', validators=[
        DataRequired(message='password是必填字段'),
        Length(min=4, max=10, message='password长度必须在4-10之间')], id=1001)

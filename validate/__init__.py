from flask_wtf import FlaskForm
from flask_inputs import Inputs
from ._schema import schema, case_schema
from flask_inputs.validators import JsonSchema
from wtforms.fields import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo

__all__ = ['JsonInput', 'ParamInput', 'UserForm', 'CaseJsonInputs']


class UserForm(FlaskForm):
    username = StringField(label='用户名',
                           validators=[DataRequired(message='用户名没填写')])
    password = PasswordField(label='密码',
                             validators=[DataRequired(message='密码没填写'),
                                         Length(min=6, max=20, message='密码长度必须在6-20之间')])

    confirm_password = PasswordField(label='确认密码', validators=[DataRequired(message='确认密码没填写'),
                                                               EqualTo('password', message='两次密码必须和一样')])


class JsonInput(Inputs):
    json = [JsonSchema(schema=schema)]


class ParamInput(Inputs):
    args = {
        'user': [DataRequired(message='缺少user参数')],
        'pwd': [DataRequired(message='缺少pwd参数')]
    }


class CaseJsonInputs(Inputs):
    json = [JsonSchema(schema=case_schema)]

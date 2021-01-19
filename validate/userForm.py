from flask_wtf import FlaskForm
from wtforms.fields import IntegerField, StringField, PasswordField
from wtforms.validators import DataRequired, InputRequired, Length, EqualTo


class UserForm(FlaskForm):
    user = StringField(label='用户名', validators=[DataRequired(message='用户名没填写')], description='用户名校验', )
    pwd = PasswordField(label='密码',
                        validators=[DataRequired(message='密码没填写'),
                                    Length(min=6, max=20, message='密码长度必须在6-20之间'),
                                    EqualTo('user', message='必须和用户名一样')],
                        description='密码校验')

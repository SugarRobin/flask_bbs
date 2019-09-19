# from wtforms import Form
from wtforms import StringField,IntegerField,SubmitField
from wtforms.validators import InputRequired,Email,Length,EqualTo

from ..forms import BaseForm

class LoginForm(BaseForm):
    email = StringField(validators=[Email(message="请输入正确的邮箱类型"),InputRequired(message="请输入邮箱")])
    password = StringField(validators=[Length(6,20,message="请输入正确格式的密码")])
    remeber = IntegerField()

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import SubmitField
from wtforms import PasswordField
from wtforms.validators import DataRequired
from wtforms.validators import EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('用户名:', validators=[DataRequired()])
    password = PasswordField('密码:', validators=[DataRequired()])
    password2 = PasswordField('确认密码', validators=[DataRequired(), EqualTo('password', message='两次密码不一致')])
    # 再这里, 一般来说你注册的时候都要求你输入两次相同的密码的,而且要求是一样的,所以我们可以使用wtforms帮我们集成好的EqualTo方法.
    # 那个message就是当你两次密码不一样的时候的提示信息
    submit = SubmitField('确认,提交')


class LoginForm(FlaskForm):
    username = StringField('用户名:', validators=[DataRequired()])
    password = PasswordField('密码:', validators=[DataRequired()])
    submit = SubmitField('确认,提交')


class PostForm(FlaskForm):
    title = StringField('文章标题:', validators=[DataRequired()])
    content = TextAreaField('文章内容', validators=[DataRequired()])
    submit = SubmitField('发布')

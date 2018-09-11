from . import admin
from ..models import User, Article
from .forms import LoginForm, RegistrationForm, PostForm
from .. import db
from flask import render_template
from flask import redirect
from flask import url_for
from flask import flash
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from sqlalchemy.exc import IntegrityError


@admin.route('/', methods=['GET', 'POST'])
def index():
    form = PostForm()
    if not current_user.is_authenticated:
        return redirect(url_for('admin.login'))
    if form.validate_on_submit():
        try:
            article = Article(title=form.title.data, content=form.content.data)
            db.session.add(article)
            db.session.flush()
            form.title.data = ''
            form.content.data = ''
            flash('发布成功')
        except IntegrityError as error:
            db.session.rollback()
            flash('文章标题有重复')
    return render_template('admin/index.html', form=form)


@admin.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None:
            if user.check(form.password.data):
                login_user(user)
                return redirect(url_for('admin.index'))
            else:
                flash("用户名或者密码错误")
                return redirect(url_for('admin.login'))
        else:
            flash('没有你这个用户，请注册')
    return render_template('admin/login.html', form=form)


@admin.route('/logout')
@login_required
def logout():
    logout_user()
    flash('你已经退出了。')
    return redirect(url_for('admin.login'))


@admin.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            user = User(username=form.username.data, password=form.password.data)
            db.session.add(user)
            db.session.flush()
            flash('注册成功')
            return redirect(url_for('admin.login'))
        except IntegrityError as error:
            db.session.rollback()
            flash('帐号已存在')
            return redirect(url_for('admin.register'))
    return render_template('admin/register.html', form=form)

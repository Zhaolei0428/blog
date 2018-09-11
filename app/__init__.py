from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
from flask import Blueprint
bootstrap = Bootstrap()
# session_options={'autocommit': True}
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'  # 这行代码就记住吧，我也不想解释了
login_manager.login_view = 'admin.login'  # 设置登录界面, 名为admin这个蓝本的login视图函数


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Config.init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    # from .main import main as main_blueprint 这个不对
    from . import main as main_blueprint
    # app.register_blueprint(main_blueprint) 这个不对
    for obj in vars(main_blueprint).values():
        if isinstance(obj, Blueprint):
            app.register_blueprint(obj)

    from . import admin as admin_blueprint
    for obj in vars(admin_blueprint).values():
        if isinstance(obj, Blueprint):
            app.register_blueprint(obj, url_prefix='/admin')

    return app
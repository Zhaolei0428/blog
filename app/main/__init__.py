from flask import Blueprint

# 这句放这会造成循环引用
# from . import views, errors

main = Blueprint('main', __name__)


from . import views, errors


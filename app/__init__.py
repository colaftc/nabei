from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import import_string
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_babelex import Babel

db=SQLAlchemy()
bootstrap=Bootstrap()
nav=Nav()
admin=Admin(name='那杯管理平台',template_mode='bootstrap3')
babel=Babel()

exts=[
    db,
    bootstrap,
    nav,
    admin,
    babel
]

blueprints=(
    'app.main:main',
    'app.weixin_api:weixin_api',
    'app.weixin_web:weixin_web',
    'app.xiaochengxu:xiaochengxu',
    'app.backend:backend',
)

from app.models import OutsideOrder,Expenditure,Task

def create_app(config):
    app=Flask(__name__)
    app.config.from_object(config)
    app.config['BABEL_DEFAULT_LOCALE']='zh_CN'

    for ext in exts:
        ext.init_app(app)

    for bp_name in blueprints:
        bp=import_string(bp_name)
        app.register_blueprint(bp)

    from .admin_view import OutsideOrderModelView,ExpenditureModelView,TaskModelView
    admin.add_view(OutsideOrderModelView(OutsideOrder,db.session,name='外部订单'))
    admin.add_view(ExpenditureModelView(Expenditure,db.session,name='开支'))
    admin.add_view(TaskModelView(Task,db.session,name='任务'))

    @app.route('/')
    def index():
        return render_template('home/index.html',**{
            'message':'Fuck you jinja2',
        })

    return app

from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import import_string
from flask_bootstrap import Bootstrap
from flask_nav import Nav

db=SQLAlchemy()
bootstrap=Bootstrap()
nav=Nav()

exts=[
    db,
    bootstrap,
    nav,
]

blueprints=(
    'app.main:main',
    'app.weixin_api:weixin_api',
    'app.weixin_web:weixin_web',
    'app.xiaochengxu:xiaochengxu',
    'app.backend:backend',
)

from app.models import OutsideOrder

def create_app(config):
    app=Flask(__name__)
    app.config.from_object(config)

    for ext in exts:
        ext.init_app(app)

    for bp_name in blueprints:
        bp=import_string(bp_name)
        app.register_blueprint(bp)

    # root route '/' defines here , not in any blueprint
    @app.route('/')
    def index():
        return render_template('home/index.html',**{
            'message':'Fuck you jinja2',
        })

    return app

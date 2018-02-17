
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .main import main as main_bp

db=SQLAlchemy()

def create_app(config):
    app=Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    app.register_blueprint(main_bp,url_prefix='/home')

    # root route '/' defines here , not in any blueprint
    @app.route('/')
    def index():
        return 'Home Index'

    return app

import os

basedir=os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY='&*_nabei_ganputang_xiangqing_'
    SQLALCHEMY_MIGRATE_REPO=os.path.join(basedir,'migrations')
    SQLALCHEMY_TRACK_MODIFICATIONS=True

class DebugConfig(Config):
    DEBUG=True
    CSRF_ENABLED=True
    SQLALCHEMY_DATABASE_URI='mysql://root:fcp0520@localhost:3306/nabei_debug'

configs={
    'Debug':DebugConfig,
    'default':DebugConfig,
}

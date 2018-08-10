#! /usr/local/bin/python3
"""
the run script , add command manager to shell

Date : 2018-02-17
Author : colaftc
Email : colaftc@126.com
"""

from app import create_app,db
from config import configs
from flask_script import Manager,Shell
from flask_migrate import Migrate,MigrateCommand
import pymysql
pymysql.install_as_MySQLdb()

app=create_app(configs['default'])
manager=Manager(app)
migrate=Migrate(app,db)

def make_shell_context():
    return dict(
        app=app,
        db=db
    )

manager.add_command('shell',Shell(make_context=make_shell_context))
manager.add_command('db',MigrateCommand)

if __name__=='__main__':
	manager.run()

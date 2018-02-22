from flask import Blueprint,session,url_for,redirect
from collections import namedtuple
from functools import wraps
import os

backend=Blueprint('backend',__name__,url_prefix='/backend',template_folder=os.path.join('%s/templates/' % os.path.dirname(__file__)))

BackendUser=namedtuple('BackendUser',('username','pwd'))
backend_users=(
    BackendUser(username='luke',pwd='19561206'),
    BackendUser(username='ftc',pwd='fcp0520'),
)

def backend_login_required(f):
    @wraps(f)
    def wrapper(*args,**kwargs):
        if 'backend_user' not in session:
            return redirect(url_for('backend.login'))
        return f(*args,**kwargs)
    return wrapper

def backend_is_authenticate(user):
    result=list(filter(lambda u : u.username==user.username and u.pwd==user.pwd,backend_users))
    return True if len(result) else False

def backend_login_user(user):
    session['backend_user']=user

def backend_logout_user():
    session.pop('backend_user')

from . import views

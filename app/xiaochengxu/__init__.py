"""
this blueprint module is weixin xiaochengxu .
"""

from flask import Blueprint
xiaochengxu=Blueprint('xiaochengxu',__name__,url_prefix='/xcx')

from . import views

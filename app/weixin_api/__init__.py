"""
this blueprint module is service for weixin gongzhonghao.
about message publish , message recv and reply , and some promotion functions.
"""
from flask import Blueprint

weixin_api=Blueprint('weixin_api',__name__,url_prefix='/wx-api')
from . import views

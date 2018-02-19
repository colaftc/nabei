"""
this blueprint module is service for weixin website
about company information, product menu , eshop
"""
from flask import Blueprint

weixin_web=Blueprint('weixin_web',__name__,url_prefix='/wx-web')
from . import views

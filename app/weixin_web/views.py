from . import weixin_web

@weixin_web.route('/')
def index():
    return 'Weixin website Module has not implements'

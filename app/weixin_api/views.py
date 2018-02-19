from . import weixin_api

@weixin_api.route('/')
def index():
    return 'Weixin Api Module has not implements'

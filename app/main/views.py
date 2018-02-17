from . import main

@main.route('/')
@main.route('/index')
def index():
    return 'Hello'

@main.route('/test')
def testing():
    return 'testing'

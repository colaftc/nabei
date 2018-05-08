from . import xiaochengxu
from flask import jsonify

@xiaochengxu.route('/')
def index():
    return 'Weixin xiaochengxu Module has not implements'

@xiaochengxu.route('/test_data')
def test_data():
    return jsonify({
        'author':'ftc',
        'boss':'fcp',
    })

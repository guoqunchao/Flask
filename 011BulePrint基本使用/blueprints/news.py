from flask import Blueprint

news_bp = Blueprint('news',__name__)

@news_bp.route('/list/')
def list():
    return '新闻列表页面'

@news_bp.route('/detial/')
def detial():
    return '新闻详情页面'


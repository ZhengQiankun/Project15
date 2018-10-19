from flask import Blueprint
from flask import Flask

# 创建新闻蓝图对象
news_blue = Blueprint("news",__name__,url_prefix="/news")

# 装饰试图函数
from . import views

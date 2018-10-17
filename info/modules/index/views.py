from flask import session, jsonify

from info import redis_store
from info.models import User, News
from info.utils.response_code import RET

from . import index_blue
from flask import render_template,current_app



@index_blue.route('/')
def helloworld():
    # 获取用户编号，从session
    user_id = session.get("user_id")

    # 判断用户是否存在
    user  = None
    if user_id:
        try:
            user = User.query.get(user_id)
        except Exception as e:
            current_app.logger.error(e)

    # 查询数据库,根据点击量查询前十条新闻
    try:
        news_list = News.query.order_by(News.clicks.desc()).limit(10).all()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR,errmsg="查询新闻异常")

    # 将新闻对象列表, 转成字典列表
    click_news_list = []
    for news in news_list:
        click_news_list.append(news.to_dict())


    # 将用户信息转换成字典
    dict_data = {
        # 如果user存在,返回左边, 否则返回右边
        "user_info" : user.to_dict() if user else "",

        "click_news_list":click_news_list}

    return render_template("news/index.html",data = dict_data)
#处理网站logo,浏览器在运行的时候，自动发送一个get请求，向/favicon.ico地址
#只需要编写对应的接口,返回一张图片即可
#解决: current_app.send_static_file,自动向static文件夹中寻找指定的资源
@index_blue.route('/favicon.ico')
def web_log():
    return current_app.send_static_file("news/favicon.ico")
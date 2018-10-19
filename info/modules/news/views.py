from flask import json
from flask import request

from info.models import News, User, Comment
from info.utils.common import user_login_data #
from info.utils.response_code import RET
from . import news_blue
from flask import render_template, current_app, jsonify, abort, session, g


# 功能描述: 收藏/取消收藏新闻
# 请求路径: /news/news_collect
# 请求方式: POST
# 请求参数:news_id,action, g.user
# 返回值: errno,errmsg

@news_blue.route('/news_collect', methods=['POST'])
@user_login_data
def news_collect():
    """
    1.判断用户是否登陆
    2.获取参数
    3.校验参数,为空校验
    4.判断操作类型
    5.根据新闻编号取出新闻对象
    6.判断新闻对象是否存在
    7.根据操作类型,收藏或者取消收藏操作
    8.返回响应
    :return:
    """

    # 1.判断用户是否登陆
    if not g.user:
        return jsonify(error=RET.NODATA,errmsg="用户未登录")

    # 2.获取参数
    json_data = request.data
    dict_data = json.loads(json_data)
    news_id = dict_data.get("news_id")
    action = dict_data.get("action")

    # 3.校验参数,为空校验
    if not all([news_id,action]):
        return jsonify(errno=RET.PARAMERR,errmsg="参数不全")

    # 4.判断操作类型
    if not action in ["collect","cancel_collect"]:
        return jsonify(errno=RET.DATAERR,errmsg="操作类型有误")

    # 5.根据新闻编号取出新闻对象
    try:
        news = News.query.get(news_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR,errmsg="新闻获取失败")

    # 6.判断新闻对象是否存在
    if not news: return jsonify(errno=RET.NODATA,errmsg="新闻不存在")

    # 7.根据操作类型,收藏或者取消收藏操作
    try:
        if action == "collect":
            # 判断是否收藏过该新闻
            if news not in g.user.collection_news:
                g.user.collection_news.append(news)
        else:
            if news in g.user.collection_news:
                g.user.collection_news.remove(news)

    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR,errmsg="操作失败")


    # 8.返回响应
    return jsonify(errno=RET.OK,errmsg="操作成功")



#功能描述: 获取新闻详细信息
# 请求路径: /news/<int:news_id>
# 请求方式: GET
# 请求参数:news_id
# 返回值: detail.html页面, 用户data字典数据
@news_blue.route('/<int:news_id>')
@user_login_data #
def news_detail(news_id):

    # 根据传入的新闻编号,获取新闻对象
    try:
        news = News.query.get(news_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR,errmsg="新闻获取失败")

    # 判断新闻是否存在
    if not news:
        abort(404)

    #查询热门新闻数据
    try:
        news_list = News.query.order_by(News.clicks.desc()).limit(8).all()
    except Exception as e:
        current_app.logger.error(e)

    #将新闻列表转成,字典列表
    click_news_list = []
    for click_news in news_list:
        click_news_list.append(click_news.to_dict())

    #获取用户数据
    #获取用户的编号,从session
    user_id = session.get("user_id")

    #判断用户是否存在
    user = None
    if user_id:
        try:
            user = User.query.get(user_id)
        except Exception as e:
            current_app.logger.error(e)

    is_collected =  False
    if g.user and news in g.user.collection_news:
        is_collected = True


    # 携带数据渲染页面
    data = {
        "news":news.to_dict(),
        "click_news_list":click_news_list,
        "user_info": g.user.to_dict() if g.user else "",
        "is_collected": is_collected

    }

    return render_template("news/detail.html",data=data)
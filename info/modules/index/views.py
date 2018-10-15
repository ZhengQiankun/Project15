from info import redis_store

from . import index_blue
from flask import render_template,current_app



@index_blue.route('/')
def helloworld():

    # 测试redis存储数据
    # redis_store.set("name","laowang")
    # print(redis_store.get("name"))

    # 测试session存储数据
    # session["age"] = "13"
    # print(session.get("age"))

    # 输入记录信息，可以替代print
    # logging.debug("调试信息1")
    # logging.info("详细信息1")
    # logging.warning("警告信息1")
    # logging.error("错误信息1")

    # 上面的方式可以写成，current_app来输出，区别有分割线
    # current_app.logger.debug("调试信息2")
    # current_app.logger.info("详细信息2")
    # current_app.logger.warning("警告信息2")
    # current_app.logger.error("错误信息2")

    return render_template("news/index.html")
#处理网站logo,浏览器在运行的时候，自动发送一个get请求，向/favicon.ico地址
#只需要编写对应的接口,返回一张图片即可
#解决: current_app.send_static_file,自动向static文件夹中寻找指定的资源
@index_blue.route('/favicon.ico')
def web_log():
    return current_app.send_static_file("news/favicon.ico")
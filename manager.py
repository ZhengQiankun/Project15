"""
项目启动相关配置：
1.数据库配置
2.redis配置
3.session设置,为后续的登录保持做准备
4.日志文件
5.CSRFProtect配置，为了对‘POST’，‘PUT’，‘DISPATCH’，‘DELETE’做保护
6.数据库迁移配置

"""""
import logging

from flask import Flask,session,current_app

from info import create_app

# 传入标记，加载对应的配置环境
app = create_app("develop")

@app.route('/')
def helloworld():

    # 测试redis存储数据
    # redis_store.set("name","laowang")
    # print(redis_store.get("name"))

    # 测试session存储数据
    # session["age"] = "13"
    # print(session.get("age"))

    # 输入记录信息，可以替代print
    logging.debug("调试信息1")
    logging.info("详细信息1")
    logging.warning("警告信息1")
    logging.error("错误信息1")

    # 上面的方式可以写成，current_app来输出，区别有分割线
    # current_app.logger.debug("调试信息2")
    # current_app.logger.info("详细信息2")
    # current_app.logger.warning("警告信息2")
    # current_app.logger.error("错误信息2")

    return "helloworld"

if __name__ == "__main__":
    app.run(debug=True)

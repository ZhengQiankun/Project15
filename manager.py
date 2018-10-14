"""
项目启动相关配置：
1.数据库配置
2.redis配置
3.session设置,为后续的登录保持做准备
4.日志文件
5.CSRFProtect配置，为了对‘POST’，‘PUT’，‘DISPATCH’，‘DELETE’做保护
6.数据库迁移配置

"""""

# from flask import Flask,session

from info import create_app

# 传入标记，加载对应的配置环境
app = create_app("develop")

@app.route('/',methods=["POST"])
def helloworld():

    # 测试redis存储数据
    # redis_store.set("name","laowang")
    # print(redis_store.get("name"))

    # 测试session存储数据
    # session["age"] = "13"
    # print(session.get("age"))

    return "helloworld"

if __name__ == "__main__":
    app.run(debug=True)

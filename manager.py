"""
项目启动相关配置：
1.数据库配置
2.redis配置
3.session设置
4.日志文件
5.数据库迁移配置

"""""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# 配置信息
class Config(object):
    
    # 调试模式
    DEBUG = True

    # 数据库配置
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:mysql@localhost:3306/Project15"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app.config.from_object(Config)

# 创建SQLAlchemy对象，关联app
db = SQLAlchemy(app)

@app.route('/')
def helloworld():

    return "helloworld100"

if __name__ == "__main__":
    app.run(debug=True)
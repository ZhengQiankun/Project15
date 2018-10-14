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
import redis

app = Flask(__name__)


# 配置信息
class Config(object):
    
    # 调试模式
    DEBUG = True

    # 数据库配置
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:mysql@localhost:3306/Project15"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis设置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
app.config.from_object(Config)

# 创建SQLAlchemy对象，关联app
db = SQLAlchemy(app)

# 创建redis对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT,decode_responses=True)
@app.route('/')
def helloworld():
    # 测试redis存储数据
    redis_store.set("name","laowang")
    print(redis_store.get("name"))

    return "helloworld"

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_dict
import redis
from flask_session import Session
from flask_wtf import CSRFProtect
def create_app(config_name):

    # 应用程序初始化信息
    app = Flask(__name__)

    # 根据传入的配置名称，导入配置类
    config = config_dict.get(config_name)

    # 加载配置信息
    app.config.from_object(config)

    # 创建SQLAlchemy对象，关联app
    db = SQLAlchemy(app)

    # 创建redis对象
    redis_store = redis.StrictRedis(host=config.REDIS_HOST,port=config.REDIS_PORT,decode_responses=True)

    # 初始化Session,读取app身上sesson的配置信息
    Session(app)

    # 保护app,使用CSRFProtect
    CSRFProtect(app)

    return app
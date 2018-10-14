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
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from info import create_app,db,models #需要知道有modules文件存在即可

# 传入标记，加载对应的配置环境
app = create_app("develop")

# 创建manager对象，管理app
manager = Manager(app)

# 关联db,app,使用Migrate
Migrate(app,db)

# 给manager添加操作命令
manager.add_command("db",MigrateCommand)

if __name__ == "__main__":
    manager.run()

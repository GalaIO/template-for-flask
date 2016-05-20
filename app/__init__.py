# -*- coding:utf8 -*-
'''
The flask app, include models, templates, static file and route mapper.
'''
__all__ = []
__version__ = '0.0.1'
__author__ = 'GalaIO'

import os
from flask import Flask, Blueprint
from flask.ext.sqlalchemy import SQLAlchemy
from config import config, root_dir


# 定义了数据库实例，在随后初始化，传入app上下文
db = SQLAlchemy()

# 蓝图表，可以动态加载进去
route_list = []
# 提供一个函数简化操作
def fetchRoute(blueprint, prefix=None):
    tmpList = (blueprint, prefix)
    route_list.append(tmpList)

# 一个动态添加蓝图的修饰器，为了简化操作，减少开发者错误的
# 利用了python修饰器的特性和动态类型的特性，返回同命名的蓝图
def addBlueprint(path=None):
    def decorator(f):
        blueprint = f()
        # 使用异常来报错，检查数据类型
        if not isinstance(blueprint, Blueprint):
            raise Exception('the warped must return a Blueprint object!!!')
        route_list.append((blueprint, path))
        return blueprint
    return decorator

# 延迟创建app， 为了让视图和模型与创建分开
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    # 初始化一些flask扩展库，依赖于flask的app上下文环境
    db.init_app(app)
    # 附加路由和自定义的错误页面
    app_dir = os.path.join(root_dir, 'app')
    # 逐个执行各个路由映射脚本，添加到route_list中
    for routes in os.listdir(app_dir):
        rou_path = os.path.join(app_dir, routes)
        if (not os.path.isfile(rou_path)) and routes != 'static' and routes != 'templates':
            __import__('app.' + routes)
    # 从route_list中引入蓝图
    for blueprints in route_list:
        if blueprints[1] != None:
            app.register_blueprint(blueprints[0], url_prefix = blueprints[1])
        else:
            app.register_blueprint(blueprints[0])
    #返回app实例，让外部模块继续使用
    return app
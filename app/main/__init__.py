# -*- coding:utf8 -*-
'''
index page.
'''
__all__ = []
__version__ = '0.0.1'
__author__ = 'GalaIO'

from flask import Blueprint
import app

# 下面被修饰器修饰的main函数，会返回一个同名的blueprint，用来部署路由
@app.addBlueprint()
def main():
    return Blueprint('main', __name__)


# main = Blueprint('main', __name__, url_prefix=None)

from . import views, errors
# -*- coding:utf8 -*-
'''
index route.
'''
from flask import render_template
from . import main

# 定义路由函数
@main.route('/', methods=['GET', 'POST'])
def index_route():
    return render_template('index.html')

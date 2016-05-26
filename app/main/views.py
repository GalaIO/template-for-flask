# -*- coding:utf8 -*-
'''
index route.
'''
from flask import render_template, make_response
from . import main
from ..models import System

# 定义路由函数
@main.route('/', methods=['GET', 'POST'])
def index_route():
    tmp = System.query.filter_by(name='xiaoming').first()
    if tmp is None:
        return render_template('index.html', name='anomymous')
    return render_template('index.html', name=tmp.name)

@main.route('/test', methods=['GET'])
def test():
    return make_response('hhhh')

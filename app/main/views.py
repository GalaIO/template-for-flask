# -*- coding:utf8 -*-
'''
index route.
'''
from flask import render_template, make_response, request
from . import main
from ..models import System
from ..models import db

# 定义路由函数
@main.route('/', methods=['GET', 'POST'])
def index_route():
    return render_template('index.html', name='anomymous')

@main.route('/test/<name>', methods=['GET'])
def test(name):
    tmp = System.query.filter_by(name=name).first()
    if tmp is None:
        return render_template('index.html', name='anomymous')
    return render_template('index.html', name=tmp.name)

@main.route('/new', methods=['GET'])
def new():
    name = request.args.get('name')
    tmp = System(name=name)
    db.session.add(tmp)
    return make_response('success')
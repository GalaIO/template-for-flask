# -*- coding:utf8 -*-
'''
Add database models.
'''
from . import db
# 模型字典，用于向外展示数据库模型
tables = {}

# 动态更新模型字典的修饰器
# 不需要改变类或者函数的行为，在一些处理以后，直接返回好了，不要包装函数了
def addModel(model):
    tables[model.__name__] = model
    return model


# test model
@addModel
class System(db.Model):
    __tablename__ = 'system'
    name = db.Column(db.String(64), primary_key=True)
    def __repr__(self):
        return '<System %r>' % self.name
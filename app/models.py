# -*- coding:utf8 -*-
'''
Add database models.
'''
from . import db

class System(db.Model):
    __tablename__ = 'system'
    name = db.Column(db.String(64), primary_key=True)
    def __repr__(self):
        return '<System %r>' % self.name
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 12:14:57 2018

@author: lenovo
"""

from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
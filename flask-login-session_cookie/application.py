# -*- coding: utf-8 -*-
from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)

"""
登录验证模块
"""
login_manager = LoginManager()
login_manager.init_app(app)

# 必须设置secretkey，否则无法使用session
app.config['SECRET_KEY'] = 'szhh'

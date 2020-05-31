# coding: utf-8
from flask_login import UserMixin

from application import login_manager

# 定义一个已经设置好的对象，如果是实际使用应该定义数据库的用户模型
class User(UserMixin):
    id = 'szh'
    password = '123456'



# 获取用户login_name作为cookie加密
@login_manager.user_loader
def load_user(uid):
    # 直接返回当前定义的对象，如果实际使用应该返回数据库查询id的对象
    return User

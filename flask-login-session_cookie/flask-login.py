from flask import request
from flask_login import login_user, login_required
from application import app

from model import User


@app.route('/login', methods=["GET", "POST"])
def login():
    # 将比特对象转换为字典对象
    data = eval(request.data)
    # 模拟用户验证
    if data['id'] == 'szh' and data['password'] == '123456':
        # 直接返回model中的对象，如果是实际使用的话需要通过id在数据库中查询以获取用户对象
        user = User()
        # 登录之后将会flask-login将会自动设置session并将cookie返回给客户端
        login_user(user)
        return 'you are success login~'
    else:
        return 'you should check your psd!'

@app.route('/check', methods=["GET", "POST"])
@login_required
def check():
    return 'i checked your access~'


if __name__ == '__main__':
    app.run(debug=True)

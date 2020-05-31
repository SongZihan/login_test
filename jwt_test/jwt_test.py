from datetime import datetime, timedelta

import jwt
from flask import Flask,request


app = Flask(__name__)

# 必须设置secretkey，否则无法使用session
app.config['SECRET_KEY'] = 'szhh'

@app.route('/login', methods=["GET", "POST"])
def login():
    # 将比特对象转换为字典对象
    data = eval(request.data)
    # 模拟用户验证
    if data['id'] == 'szh' and data['password'] == '123456':
        now = datetime.utcnow()
        # 设置两小时后过期
        exp_datetime = now + timedelta(hours=2)
        print(exp_datetime)
        # 通过用户名核对和密码验证之后返回jwt
        encoded_jwt = jwt.encode({
            'username':data['id'],
            # exp是到期时间
            'exp':exp_datetime
        },'secret', algorithm='HS256')
        print(encoded_jwt)
        print(jwt.decode(encoded_jwt,'secret', algorithms=['HS256']))
        # 返回token的时候必须进行decode否则会报错 'TypeError: Object of type bytes is not JSON serializable'
        res_data = {'token': encoded_jwt.decode("utf-8"),'msg':'you are success login~'}
        return res_data
    else:
        return 'you should check your psd!'

@app.route('/check',methods=["GET", "POST"])
def check():
    # 测试token,从header中获取接收的token，并使用UTF-8进行编码，否则无法使用jwt.decode
    token = request.headers.get('Authorization',default=None).encode('utf-8')
    print(token)
    decode_token = jwt.decode(token,'secret', algorithms=['HS256'])
    print(decode_token)

    return 'i get token~'

if __name__ == '__main__':
    app.run(debug=True)

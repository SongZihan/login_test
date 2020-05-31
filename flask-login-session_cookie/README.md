## Flask-Login 实现原理

![Untitled Diagram](https://github.com/SongZihan/login_test/blob/master/flask-login-session_cookie/Untitled%20Diagram.jpg)

## API测试使用

通过Postman发出POST请求到http://127.0.0.1:5000/login , 并设置header 的Content-Type为application/json，然后再body中写入raw的JSON数据

`{`
	`'id':'szh',`
	`'password':'123456'`
`}`

发出请求之后得到响应：you are success login~

并且响应头中包含Set-Cookie
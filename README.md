## 测试使用Flask-Login和Pyjwt分别实现权限认证

Flask-Login 是Flask封装的一个基于session和cookie的Pyhton模块。[Flask-login 中文文档](http://www.pythondoc.com/flask-login/)

Pyjwt 是Python的一个用于生成jwt的模块。[Pyjwt 官网](https://pyjwt.readthedocs.io/en/latest/index.html)

（其实Flask有一个自己封装的jwt实现模块 Flask-jwt，但是感觉不太好用，比较复杂所以选择了使用Pyjwt自己实现）

### 基于JWT认证和基于session/cookie认证的不同之处

jwt认证最大的特点在于服务器不保存任何数据，例子：

*JWT 的原理是，服务器认证以后，生成一个 JSON 对象，发回给用户，就像下面这样。*

> ```javascript
> {
>   "姓名": "张三",
>   "角色": "管理员",
>   "到期时间": "2018年7月1日0点0分"
> }
> ```

*以后，用户与服务端通信的时候，都要发回这个 JSON 对象。服务器完全只靠这个对象认定用户身份。为了防止用户篡改数据，服务器在生成这个对象的时候，会加上签名。*

*服务器就不保存任何 session 数据了，也就是说，服务器变成无状态了，从而比较容易实现扩展。*

​		而基于session/cookie的认证必须要在服务器的数据库或者内存中保存用户的当前登录状态，每当用户访问的时候将用户的请求header和服务器session进行比对以鉴权。




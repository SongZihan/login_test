## Pyjwt 实现原理

Pyjwt 的核心在于

```
>>> import jwt

>>> encoded_jwt = jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256')
>>> encoded_jwt
'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb21lIjoicGF5bG9hZCJ9.4twFt5NiznN84AWoo1d7KO1T_yoc0Z6XOpOVswacPZg'

>>> jwt.decode(encoded_jwt, 'secret', algorithms=['HS256'])
{'some': 'payload'}
```

使用jwt编码和解码，客户端收到jwt之后每次请求时都将jwt添加在请求头中，服务器对jwt进行解码并查看jwt包含的内部信息，如果jwt超过了过期时间则认为jwt失效需要再次登录，并且还可以在jwt中添加一些权限信息。

缺点时一旦jwt被截获并破解的话，等同于用户数据库泄露，，，所以需要一些额外的方式来保障安全~

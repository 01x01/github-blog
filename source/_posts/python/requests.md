---
title: requests
date: 2019-06-21 14:45:29
tags: 
category: python
---
第三方框架 requests 的常见使用方法
<!-- more -->
# 安装
```py
pip install requests
```
# 不同的请求方法
## get
```py
>>> r = requests.get('https://api.github.com/events')
>>> payload = {'key1': 'value1', 'key2': 'value2'}
>>> r = requests.get('https://httpbin.org/get', params=payload)
```
## post
```py
# 情况1
headers = {
    "Content-Type":"application/x-www-form-urlencode"
}
r = requests.post('https://httpbin.org/post',headers=headers,data = {'key':'value'})
# 情况2
import json

headers = {
    "Content-Type":"application/json"
}
data = {
    "key":"value"
}

r = requests.post('https://httpbin.org/post',headers=headers,data = json.dumps(data) )
```
# 返回值
有三种：
1. text : 返回文本字符
2. content: 返回二进制数据
3. json： 返回 json 格式数据

```py
>>> r.text
u'[{"repository":{"open_issues":0,"url":"https://github.com/...

>>> r.content
b'[{"repository":{"open_issues":0,"url":"https://github.com/...

>>> r.json()
[{u'repository': {u'open_issues': 0, u'url': 'https://github.com/...
```

# 上传文件
```py
# 情况 1 上传一个文件
>>> url = 'https://httpbin.org/post'
>>> files = {'file': open('report.xls', 'rb')}

>>> r = requests.post(url, files=files)
>>> r.text
{
  ...
  "files": {
    "file": "<censored...binary...data>"
  },
  ...
}

# 上传多个文件
>>> url = 'https://httpbin.org/post'
>>> multiple_files = [
        ('images', ('foo.png', open('foo.png', 'rb'), 'image/png')),
        ('images', ('bar.png', open('bar.png', 'rb'), 'image/png'))]
>>> r = requests.post(url, files=multiple_files)
>>> r.text
{
  ...
  'files': {'images': 'data:image/png;base64,iVBORw ....'}
  'Content-Type': 'multipart/form-data; boundary=3131623adb2043caaeb5538cc7aa0b3a',
  ...
}
```
# session
```py
s = requests.Session()

s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('https://httpbin.org/cookies')

print(r.text)
# '{"cookies": {"sessioncookie": "123456789"}}'
```

# 事件 hook
指接收到返回的数据时，我们可以调用函数来处理这个结果
```py
def print_url(r, *args, **kwargs):
    print(r.url)
    
>>> requests.get('https://httpbin.org/', hooks={'response': print_url})
https://httpbin.org/
<Response [200]>
```
# 认证
## basic auth
```py
>>> from requests.auth import HTTPBasicAuth
>>> requests.get('https://api.github.com/user', auth=HTTPBasicAuth('user', 'pass'))
<Response [200]>
```
## digest auth
```py
>>> from requests.auth import HTTPDigestAuth
>>> url = 'https://httpbin.org/digest-auth/auth/user/pass'
>>> requests.get(url, auth=HTTPDigestAuth('user', 'pass'))
<Response [200]>
```
## oauth1
```py
>>> import requests
>>> from requests_oauthlib import OAuth1

>>> url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
>>> auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
...               'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')

>>> requests.get(url, auth=auth)
<Response [200]>
```
## 自定义 auth
```py
from requests.auth import AuthBase

class PizzaAuth(AuthBase):
    """Attaches HTTP Pizza Authentication to the given Request object."""
    def __init__(self, username):
        # setup any auth-related data here
        self.username = username

    def __call__(self, r):
        # modify and return the request
        r.headers['X-Pizza'] = self.username
        return r
      
>>> requests.get('http://pizzabin.org/admin', auth=PizzaAuth('kenneth'))
<Response [200]>  
```
# 禁止 SSL 警告
```py
equests.packages.urllib3.disable_warnings()
res = requests.post(url,headers=headers,files=files,verify=False)
```

# 参考文档
http://docs.python-requests.org/en/master/

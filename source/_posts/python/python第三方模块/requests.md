---
title: requests
tags: python第三方模块
category: python
---
# 概述
requests 是 python 里面著名的第三方模块，用于发送和接收请求，一般用于 API自动化测试，爬虫等等项目. 基于目前版本号是 `2.21.0`  

# 安装
```python
pip install requests 
```

# 发送请求

## get
```python
>>> r = requests.get('https://api.github.com/events')
>>> payload = {'key1': 'value1', 'key2': 'value2'}
>>> r = requests.get('https://httpbin.org/get', params=payload)
```

## post
```python
>>> r = requests.post('https://httpbin.org/post', data = {'key':'value'})
```

## 其他方法
```python
>>> r = requests.put('https://httpbin.org/put', data = {'key':'value'})
>>> r = requests.delete('https://httpbin.org/delete')
>>> r = requests.head('https://httpbin.org/get')
>>> r = requests.options('https://httpbin.org/get')
```

# 返回值
返回值一共有三种， `text` `content` `json` <br />`text` 文本字符<br />`content` 二进制<br />`json` json
```python
>>> r.text
u'[{"repository":{"open_issues":0,"url":"https://github.com/...

>>> r.content
b'[{"repository":{"open_issues":0,"url":"https://github.com/...

>>> r.json()
[{u'repository': {u'open_issues': 0, u'url': 'https://github.com/...
```

# 上传文件 
```python
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
```

# session对象
```python
s = requests.Session()

s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('https://httpbin.org/cookies')

print(r.text)
# '{"cookies": {"sessioncookie": "123456789"}}'
```

# 上传多个文件
```python
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

# 事件hook
一般请求返回的是一个 Response 对象，我们可以设置一个 hook 函数，来返回值，比如
```python
def print_url(r, *args, **kwargs):
    print(r.url)
    
>>> requests.get('https://httpbin.org/', hooks={'response': print_url})
https://httpbin.org/
<Response [200]>
```

# auth 
auth 有许多种，比如 `basic auth` `Oatuh` 等等，也有自定义的auth，比如在 `headers` 里面增加一个字段进行auth

## basic authe

```python
>>> from requests.auth import HTTPBasicAuth
>>> requests.get('https://api.github.com/user', auth=HTTPBasicAuth('user', 'pass'))
<Response [200]>
```

## digest auth 

```python
>>> from requests.auth import HTTPDigestAuth
>>> url = 'https://httpbin.org/digest-auth/auth/user/pass'
>>> requests.get(url, auth=HTTPDigestAuth('user', 'pass'))
<Response [200]>
```

## Oauth1

```python
>>> import requests
>>> from requests_oauthlib import OAuth1

>>> url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
>>> auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
...               'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')

>>> requests.get(url, auth=auth)
<Response [200]>
```

## 自定义auth
```python
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
更多可以参考 [http://docs.python-requests.org/en/master/user/authentication/?highlight=auth](http://docs.python-requests.org/en/master/user/authentication/?highlight=auth) 

# 禁止警告
有时候因为网络的问题，我们会出现证书错误而无法访问，这个时候需要通过禁止证书验证
```python
requests.packages.urllib3.disable_warnings()
res = requests.post(url,headers=headers,files=files,verify=False)
```


# 参考
[http://docs.python-requests.org/en/master/](http://docs.python-requests.org/en/master/) 

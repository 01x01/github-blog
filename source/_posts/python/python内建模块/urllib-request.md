---
title: urllib-request
date: 2019-06-16 16:02:09
tags: python内建模块
category: python
---
![img](https://raw.githubusercontent.com/01x01/github-blog/master/source/img/3.jpeg)

# 概述

顾名思义，这个模块主要用来发送请求，但相对来说，第三方模块 `requests` 封装得更加好，也更加方便使用，因此这里只对这个模块做一个简单的了解

# GET
首先是一个简单的get请求，如代码所示：
```python
from urllib import request
res = request.urlopen("http://www.baidu.com")
print(res.read().decode("utf-8"))
```
可以看到 `urlopen` 返回了一个 response 对象, 可以读取网页返回的内容。因为 get 请求是一个非常简单的请求，复杂一点也无非是在加点参数而已 ，见代码：
```python
from urllib import parse
url = "http://www.baidu.com"
args = {"q":"baidu"}
encode_args = parse.urlencode(args)
url = urljoin(url,encode_args)
print(url)				#http://www.baidu.com/q=baidu
print()
res = request.urlopen(url)
print(res.read().decode("utf-8")) 
```


# POST
见代码：
```python
from urllib.request import Request,urlopen
from urllib.parse import urlencode
content = "Duis posuere augue vel cursus pharetra. In luctus a ex nec pretium. Praesent neque quam, tincidunt nec leo eget, rutrum vehicula magna.Maecenas consequat elementum elit, id semper sem tristique et. Integer pulvinar enim quis consectetur interdum volutpat."
url = "https://postman-echo.com/post"

r = Request(url)
# 一次只能接收一个header
# 如果有多个，可以多次使用这个 add_header 函数
r.add_header(
    "Content-Type",
    "text/plain",
)
# 参数直接放在后面，即可跟着 post 发送出去
# 必须是 byte 类型，所以必须要encode一下
res = urlopen(r,content.encode('utf-8'))
print(res.read().decode("utf-8"))
```

# 总结
urllib 属于比较底层的模块，只掌握简单的发送请求即可，涉及到复杂的部分，比如 authentication/file upload 之类的操作，最好使用 requests 模块。


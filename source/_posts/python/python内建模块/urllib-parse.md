---
title: urllib-parse
date: 2019-06-16 16:03:14
tags: python内建模块
category: python
---
![img](https://raw.githubusercontent.com/01x01/github-blog/master/source/img/paparametric_sphere.png)
# Internet - urllib.parse


#  urllib.parse 

## urlparse
主要的作用就是解析url，返回一个对象 `ParseResult` ，其中包含了6个元素，见代码
```python
from urllib.parse import urlparse
url = "http://netloc/path;param?query=args#frag"
parsed = urlparse(url)
print(parsed)
# 输出
ParseResult(scheme='http', 
            netloc='netloc',
            path='/path', 
            params='param', 
            query='query=args', 
            fragment='frag')
```

## urlsplit
除此之外，还有另外的一个函数 `urlsplit()` ，其功能跟 `urlparse` 差不多，唯一的不同是，没有 `params` ， `params` 跟 `path` 组合在了一起
```python
from urllib.parse import urlsplit
url = "http://netloc/path;param?query=args#frag"
parsed = urlsplit(url)
print(parsed)

# 输出
SplitResult(scheme='http', 
            netloc='netloc', 
            path='/path;param', 
            query='query=args', 
            fragment='frag')
```

## urlunparse
这个功能是 `urlparse` 的相反模块，将分解的url组装起来
```python
from urllib.parse import urlunparse
url = "http://netloc/path;param?query=args#frag"
parsed = urlparse(url)
print(parsed)
unparsed = urlunparse(parsed[:])
print(unparsed)

# 输出
ParseResult(scheme='http', netloc='netloc', path='/path', params='param', query='query=args', fragment='frag')
http://netloc/path;param?query=args#frag
```

## joining
```python
from urllib.parse import urljoin
print(urljoin("http://www.baidu.com","index.php")) # http://www.baidu.com/index.php
```

## encoding
针对 `get` 方式的请求，当 `get` 方式的请求带上了参数，这个时候就需要对其进行 `encode` 代码如下
```python
from urllib.parse import urlencode
query = {
    "q":"querys string",
    "foo":"bar"
}
args = urlencode(query)
print(urljoin("http://www.baidu.com",args)) # http://www.baidu.com/q=querys+string&foo=bar
```

## parse_qs
有编码，同样的也有解码，解码使用的是 `parse_qs` 
```python
from urllib.parse import urlencode,parse_qs
query = {
    "q":"querys string",
    "foo":"bar"
}
args = urlencode(query)
url = urljoin("http://www.baidu.com",args)

print(parse_qs(args)) # {'q': ['querys string'], 'foo': ['bar']}
```

## quote
`quote` 跟 `urlencode` 不同的是，其接收的是一个字符串，而不是字典，并且会编码所有的特殊字符<br />代码：
```python
from urllib.parse import quote,quote_plus
query = {
    "q":"querys string",
    "foo":"bar"
}

print(urlencode(query)) # q=querys+string&foo=bar


q="querys string&foo=bar"
print(quote(q))        # querys%20string%26foo%3Dbar
print(quote_plus(q))   # querys+string%26foo%3Dbar
```

## unquote
```python
from urllib.parse import unquote
print(unquote("querys%20string%26foo%3Dbar")) # querys string&foo=bar
```





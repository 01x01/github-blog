---
title: BeautifulSoup
date: 2019-06-16 01:10:51
tags: pythonpm
category: python
---
![img](https://raw.githubusercontent.com/01x01/github-blog/master/source/img/alliance.png)
# 概述
BeautifulSoup 是 python 里面流行的爬虫模块，简单记录一下其使用方法。

# 安装
```
pip install bs4
```

# 使用
```python
import requests
from bs4 import BeautifulSoup
# 使用 requests 获取 html
r = requests.get(link)
html = r.text
soup = BeautifulSoup(html,'html.parser')
# 查找
links = soup.find_all("a",class_='d1')
titles = soup.find_all('a',class_="ico_1")
```
常见的函数：

1. `find()` 只返回一个结果
1. `find_all()` 返回一个 list 

## 用法总结
```python
soup.find_all("title")
# [<title>The Dormouse's story</title>]

soup.find_all("p", class_="title")
# [<p class="title"><b>The Dormouse's story</b></p>]

soup.find_all("a")
# [
#  
#  

soup.find_all(id="link2")
# [

import re
soup.find(text=re.compile("sisters"))
# u'Once upon a time there were three little sisters; and their names were\n'
```

## 参数说明
```python
1. name 参数可以查找所有名字为 name 的tag,字符串对象会被自动忽略掉.
soup.find_all("title")
# [<title>The Dormouse's story</title>]

2. 如果一个指定名字的参数不是搜索内置的参数名,搜索时会把该参数当作指定名字tag的属性来搜索,如果包含一个名字为 id 的参数,Beautiful Soup会搜索每个tag的”id”属性.
soup.find_all(id='link2')
css_soup.find_all("p", class_="body strikeout")
# [<p class="body strikeout"></p>]

3. 还可以通过 find_all() 方法的 attrs 参数定义一个字典参数来搜索包含特殊属性的tag:
data_soup.find_all(attrs={"data-foo": "value"})
# [<div data-foo="value">foo!</div>]

4. text 参数
通过 text 参数可以搜搜文档中的字符串内容.与 name 参数的可选值一样, text 参数接受 字符串 , 正则表达式 , 列表, True . 

5. limit 参数
find_all() 方法返回全部的搜索结构,如果文档树很大那么搜索会很慢.如果我们不需要全部结果,可以使用 limit 参数限制返回结果的数量.效果与SQL中的limit关键字类似,当搜索到的结果数量达到 limit 的限制时,就停止搜索返回结果.

6. recursive参数
如果只想搜索tag的直接子节点,可以使用参数 recursive=False 
```

## css 选择器
```python
soup.select("p nth-of-type(3)")
# [<p class="story">...</p>]
```


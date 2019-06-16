---
title: fuzzywuzzy
date: 2019-06-16 01:10:51
tags: pythonpm
category: python
---

# 概述
fuzzywuzzy 是一个用于字符串匹配的模块，使用了字符串相似度算法（Levenshtein Distance）。 指两个字符串之间，由一个转换为另一个所需要的最少编辑次数，如果次数越多，说明它们距离越大，越是不同。其编辑的操作分为： 替换字符，删除字符，插入字符。<br />比如 kitten -> sitting<br />k -> s <br />e -> i <br />最后 -> g 

# 用法

## 全部匹配
```python
from fuzzywuzzy import fuzz 

r = fuzz.ratio("this is test","this is tests !")
print(r) //89
```

## 局部匹配
```python
r2 = fuzz.partial_ratio("this is a test", "this is a tests !")
print(r2) //100
```

## Process
在一个集合中选取最匹配的几个字符串，见代码
```python
from fuzzywuzzy import process

choices = ["Hello World","Hello china","Hello American"]
r4 = process.extract("Hello china",choices,limit=3)
print(r4)
```
输出
```python
[('Hello china', 100), ('Hello American', 64), ('Hello World', 59)]
```


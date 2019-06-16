---
title: glob
date: 2019-06-16 16:19:53
tags: python内建模块
category: python
---


# 概述
global 模块使用正则表达式来匹配文件名


# 多匹配模式
```python
import glob
for i in glob.glob("./*.ipynb"):
    print(i)

# 输出
.\array.ipynb
.\bisect.ipynb
.\collections.ipynb
.\contextlib-2.ipynb
.\functools.ipynb
.\glob.ipynb
.\headpq.ipynb
.\itertools.ipynb
.\mathematics.ipynb
.\os.path.ipynb
.\pprint.ipynb
.\queue.ipynb
```

# 单匹配模式
只能匹配一个字符
```python
for i in glob.glob("./arra?.ipynb"):
    print(i)
    
# .\array.ipynb
```



---
title: tempfile
date: 2019-06-16 16:19:01
tags: python内建模块
category: python
---

# 概述
用于创建临时文件/目录的模块

# 创建临时文件
```python
import tempfile
with tempfile.NamedTemporaryFile() as temp:
    print("temp:",temp)
    print(temp.name) # C:\Users\xxx\AppData\Local\Temp\tmpth0jh84p
```

# 创建临时目录
```python
with tempfile.TemporaryDirectory() as directory_name:
    print(directory_name) # C:\Users\johnw\AppData\Local\Temp\tmp3pcvlcoz
```
但是创建完就删除了，所有的操作只能再这里面操作。

# 创建临时文件名
```python
import tempfile
with tempfile.NamedTemporaryFile(suffix="_suffix",prefix="prefix_",dir="C:\\Users\\johnw\\AppData\\Local\\Temp") as temp:
    print("temp:",temp)
    print(temp.name) # C:\Users\johnw\AppData\Local\Temp\prefix_7x33hie8_suffix
```


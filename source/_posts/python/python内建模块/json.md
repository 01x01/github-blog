---
title: json
date: 2019-06-16 15:58:22
tags: 
category: 
---
![img](https://raw.githubusercontent.com/01x01/github-blog/master/source/img/hot.png)

# 概述
json 已然成为了一种消息通信的载体，在我们的日常工作中经常会遇到json格式的返回值，这里主要记录两个点：

1. json.dumps
1. json.loads


# json.dumps
将字典对象转换为json字符对象

```python
import json
data = [{'a': 'A', 'b': (2, 4), 'c': 3.0}]
print('DATA:', repr(data))
data_string = json.dumps(data)
print('JSON:', data_string)

# 输出
$ python3 json_simple_types.py
DATA: [{'c': 3.0, 'b': (2, 4), 'a': 'A'}]
JSON: [{"c": 3.0, "b": [2, 4], "a": "A"}]
```

# json.loads
将json字符对象转换为字典对象，方便后续的python操作
```python
data = json.loads(data_string)
print(data)
```


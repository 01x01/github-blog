---
title: json
date: 2019-06-21 16:08:49
tags: 
category: python
---
如何处理字典和 json 字符 之间的转换
<!-- more -->
# 将字典转为字符
```py
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
# 将字符转为字典
```py
data = json.loads(data_string)
print(data)
```

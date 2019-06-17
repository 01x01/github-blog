---
title: array
date: 2019-06-17 09:56:30
tags: python内建模块
category: python
---

# 概述
array 顾名思义是数组的意思，其行为非常类似 `list` ，唯一的区别就是所有成员必须具有相同的基本类型。所支持的类型都是数值类型或其他固定大小的基本类型，如字节。下面的table 定义了array 所支持的基本类型

| code | Type | 字节大小 |
| --- | --- | --- |
| b | Int | 1 |
| B | Int | 1 |
| h | Signed short | 2 |
| H | Unsigned short | 2 |
| i | Signed int | 2 |
| I | Unsigned int | 2 |
| l | Signed long | 4 |
| L | Unsigned long | 4 |
| q | Signed long long  | 8 |
| Q | Unsigned long long | 8 |
| f | Float | 4 |
| d | Double | 8 |

一个简单的例子，以 `b` 为例，存储一个字节，那么就是 `byte` 类型

```python
import array
s = b'aHello World'
a = array.array('b',s)
print("array:",a ) # 输出为 array: array('b', [97, 72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100])
```
上面的代码可以看到 `array`  存储的是 `ASCII` 码. 但是具体的应用场景还是较为模糊


# 文件和arrays
array的内容可以使用内置的方法，高效的写入文件。见如下代码

```python
import array
import tempfile
import binascii
s = b'hello world'
a = array.array('b',s)
print(binascii.hexlify(a))
output = tempfile.NamedTemporaryFile()

print(output.file) # <_io.BufferedRandom name=56>

a.tofile(output.file)
output.flush()
with open(output.name,'rb')as f:
    input_data = f.read()
    print(binascii.hexlify(input_data))
```

目前不知道有啥应用场景




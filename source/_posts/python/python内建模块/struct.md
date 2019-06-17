---
title: struct
date: 2019-06-17 09:53:20
tags: python内建模块
category: python
---
# 概述
`struct`  模块用于将在字节字符串和python常见的数据类型（number，string类型）间进行转换。比如说，你想把一个整数变成字节，你得配合位运算符

```python
>>> n = 10240099
>>> b1 = (n & 0xff000000) >> 24
>>> b2 = (n & 0xff0000) >> 16
>>> b3 = (n & 0xff00) >> 8
>>> b4 = n & 0xff
>>> bs = bytes([b1, b2, b3, b4])
>>> bs
b'\x00\x9c@c'
```
显得十分的繁琐。有了 `struct` 模块，就可以很快进行转换。


# pack
`pack()` 函数把任意的数据类型，转为 `bytes` 

```python
>>> import struct
>>> struct.pack('>I', 10240099)
b'\x00\x9c@c'
```
`'>I'`的意思是： `>`表示字节顺序是big-endian，也就是网络序，`I`表示4字节无符号整数。


# unpack
`unpack`把`bytes`变成相应的数据类型：

```python
>>> struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
(4042322160, 32896)
```

涉及到底层字节流，其应用场景比较少，作为一个了解。



# 参考
[https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431955007656a66f831e208e4c189b8a9e9f3f25ba53000](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431955007656a66f831e208e4c189b8a9e9f3f25ba53000) 

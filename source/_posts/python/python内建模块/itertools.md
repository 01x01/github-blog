---
title: itertools
date: 2019-06-17 09:33:18
tags: python内建模块
category: python
---

# 概述
在函数式编程的语言里面，很多的语言也提供了这样类似的模块来和序列数据进行配合，它们通常更快而且能更加高速的使用内存。表达的是以 `iteration` 为基础的算法，在开始学习前，需要温习一下，什么是 `iter` :

1. `Iterator` : 惰性的, 不会一次性将大量的数据带到内存里面计算，只有用到的时候才会去计算取得值
1. `Iterable`: 一次把所有的数据全部带到内存里面，其中list，dict，tuple 都是Iterable 而不是 Iterator

`iteration-base` 的代码提供的是更加合理的内存管理，也就是 “惰性”的，`itertools` 可以将 `list` 等转换为惰性输出，进行数据操作.

# 组合和切割

## chain 函数
`chain` 接收两个参数，顾名思义是将两个参数串联起来，见代码：
```python
from itertools import * 
for i in chain([1,2,3],['a','b','c']):
    print(i,end=" ")  # 1 2 3 a b c
```
如果进行迭代的组合事先是不知道，如果你想进行 `惰性` 操作，可以使用 `from_iterable` 
```python
def make_iterable():
    yield [1,2,3]
    yield ['a','b','c']
    
for i in chain.from_iterable(make_iterable()):
    print(i, end=' ')  # 1 2 3 a b c
```

## zip 函数
除了 `chain()` 函数外，还有同样经常使用的 `zip()` 函数， `zip()` 函数并不是将一个文件打包成 `zip` 而是将数据压缩在一起成为一个 `tuple` 见代码：
```python
for i in zip([1,2,3],['a','b','c']):
    print(i)
# 输出
(1, 'a')
(2, 'b')
(3, 'c')
```
可以看到 `zip()` 函数接收的两个参数，必须是长度相等，否则就会出现错误。这个时候可以使用 `longest` 见代码：
```python
for i in zip_longest([1,2,3,4],['a','b']):
    print(i,end=" ") # (1, 'a') (2, 'b') (3, None) (4, None)
```

## islice 函数
`islice()` 接收三个参数，`iterable` , `start` , `stop`  见代码

```python
import string
for i in islice(string.ascii_uppercase,5,10): # 第5开始，到第10结束
    print(i)
```

# 过滤输入
`dropwhile()` 接受两个参数，一个是处理函数，另外一个是 `iterable` 的数据结构。如下面代码所示
```python
from itertools import * 
def should_filter(x):
    return x < 1

for i in dropwhile(should_filter,[-1,-2,-3,0,1,2,3]):
    print(i,end=" ") # 1 2 3
```
这里把**不符合条件**给筛选出来了，实现同样功能的还有 `filterfalse()` 函数。 而 `filter()` 函数是把**符合条件**的数据给挑选出来。



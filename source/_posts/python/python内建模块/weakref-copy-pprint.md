---
title: weakref-copy-pprint
date: 2019-06-17 09:52:27
tags: python内建模块
category: python
---
# 概述
这三个模块比较少用，做一个了解


# weakref
跟python 的垃圾处理机制有点关系，在python 通过对对象的引用进行计数，一旦一个对象没有任何引用的地方，那么就会被垃圾处理机制给收集到，并清除这个对象，但是这一做法，并不是最可取的做法，有时候一个对象被 引用了，但是并没有任何的作为，还占用了内存，这个时候就应该被清除掉。弱引用不会增加对象的引用计数，因此不会出现因为弱引用增加计数，而垃圾处理机制不处理这个对象的情况。


# copy
copy 模块是用来拷贝对象的。一共有三种方式：

1. 浅拷贝
1. 深拷贝
1. 递归拷贝



## pprint
打印出 定义了 `__repr__()` 函数的内容。如下面代码所示：

```python
from pprint import pprint
class Person:
    def __repr__(self):
        return "person"
p = Person()
pprint(p) # person
```


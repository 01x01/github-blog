---
title: enum-collection
date: 2019-06-17 09:57:57
tags: python内建模块
category: python
---
# Data Structures - enum/collection

Python 包含了许多种数据结构类型，基础的有 `list` , `tuple` , `dict` , `set` 一般应用程序用到最多也就是这几种。但除此之外还会用到以下一些特殊的数据类型，这里简单的进行记录。

1. enum
1. collections
1. array
1. headpq
1. bisect
1. queue
1. struct
1. weakref
1. copy
1. pprint


# enum 

枚举类，提供了可迭代的功能和可比较的功能，提供了一种对于 "值" 来说更加良好的符号描述。比如，一个礼拜有7天，当然可以使用 `1~7`  来表示星期几，但是这样可读性不好，可以使用字典的方式来表示，比如： `{"星期一": 1 }` 。但是全部使用字典也不是一个合理的选择，内存浪费太大，这个时候就可以创建枚举类。


## 迭代功能

```python
import enum
class BugStatus(enum.Enum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1

for status in BugStatus:
    print("{} : {}".format(status.name,status.value))
```

## 比较的功能
枚举类的功能要看类型，比如 `IntEnum` 类可以进行比较，简单的 `Enum` 不能进行比较

```python
import enum
class BugStatus(enum.IntEnum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1

print('\n'.join(status.name for status in sorted(BugStatus)))
```

## 唯一值
为了保证枚举类中的值是唯一的，这个时候就需要对代码加一些限制

```python
import enum
@enum.unique
class BugStatus(enum.IntEnum):
    ...
    fix_released = 1
    by_design = 1 # duplicate values found in <enum 'BugStatus'>: by_design -> fix_released
```


## 程序化创建枚举类
相比新建一个类，在一些case当中，比较好的做法的是直接使用 `Enum` 来创建枚举类即可

```python
import enum

# 按照顺序，自动填充值
BugStatus = enum.Enum(
    value='BugStatus',
    names=('fix_released fix_committed in_progress '
    'wont_fix invalid incomplete new'),
)

print('Member: {}'.format(BugStatus.new))

print('\nAll members:')
for status in BugStatus:
    print('{:15} = {}'.format(status.name, status.value))
```

# collections


## chainMap:

### Search: 搜索多个dict
`chainMap` 管理了多个dict，按照各个dict出现的顺序进行搜索，从而找到与键关联的值。 一个简单的例子

```python
import collections

a = {"a":123,"b":345}
b = {"d":789,"b":111}

m = collections.ChainMap(a,b)
print(m['a']) #123

# 按照顺序进行搜索，然后进行返回。
# 如果有一个字典，所包含的 键 与前面的字典所包含的 键 相同
# 那么会按顺序取第一个键
# 这就有点像set结构了
print(m['b']) #345

for k in m.keys():
    print(k)
```
其操作与 `dict` 没有什么不同，也是 `keys()` , `values()` , `items()` 

### Reordering: 重新排序
在 `ChainMap` 中顺序的排列主要来自于 `maps` 属性，其 `maps` 属性是一个列表，因此是可以动态改变 `ChainMaps` 里面字典的顺序的，一个简单的例子

```python
import collections

a = {"a":123,"b":345}
b = {"d":789,"b":111}

m = collections.ChainMap(a,b)

print(m.maps) # [{'a': 123, 'b': 345}, {'d': 789, 'b': 111}]

```

### Updating: 更新值

```python
import collections

a = {"a":123,"b":345}
b = {"d":789,"b":111}

m = collections.ChainMap(a,b)

m['a'] = 98
print(m['a']) # 98
print(a['a']) # 98

# 可以看到，通过 ChainMap 管理的字典，也发生了值的改变
```
有时候，为了避免更改原来的数据，`ChainMaps` 提供了一个 `new_child()` 的函数用来创建一个副本进行操作。

```python
import collections

a = {"a":123,"b":345}
b = {"d":789,"b":111}

m = collections.ChainMap(a,b)
m2 = m.new_child()

print(m.maps) # [{'a': 123, 'b': 345}, {'d': 789, 'b': 111}]

m2['a'] = 98
print(m2['a']) # 98

# 可以看到并没有更改原来的dict
print(a['a']) # 123

# 除此之外，还可以跟新增的 maps 添加字典
m3 = m2.new_child({"e":"1233445"})
print(m3["e"]) # 1233445
print(m['e']) # 出错，没有这个键 
```

## Counter 
顾名思义，`Counter` 是一个计算元素在组合中出现次数的对象

### 初始化
Counter是一个对象，有三种初始化的方式

```python
import collections
print(collections.Counter(["a","a","b","c"]))
print(collections.Counter({"a":2,"b":1,"c":3}))
print(collections.Counter(a=2,b=5,c=10))
```

### 获取Counter的值
获取 `Counter` 的值也十分的简单：

```python
for i in a:
    print(i,":",a[i])
```
其中 `elements` 代表的是 `Counter` 的键值 
```python
import collections
a = collections.Counter(["a","a","b","c"])
for i in a.elements():
    print(i)
```
除此之外，还可以获取最常出现的几个元素，使用 `most_common()` 
```python
> a.most_common() # 可以加一个参数
[('a', 2), ('b', 1), ('c', 1)]
```
除此之外，`Counter`  对象还可以进行加减与或的运算
```python
> a|b
Counter({'a': 3, 'b': 2, 'c': 1, 'd': 2})

> b
Counter({'b': 2, 'd': 2, 'a': 3})

> a
Counter({'a': 2, 'b': 1, 'c': 1})
```

## defaultdict
`defaultdict` 当缺少一个键的时候，自动返回一个默认值，具体也没啥用处。见代码

```python
def fn():
    return "Hello World"

import collections 
a = collections.defaultdict(fn,b="john")

print(a["any"]) # Hello Wolrd
```
 一般如果向字典取值，害怕取不到值的时候，这个时候可以直接使用get返回一个默认值即可，不需要这么麻烦

```python
a = {}
print(a.get("Hello","World"))
```

## deque

### 队列操作
双头队列，正常的队列是先进先出，双头队列，顾名思义就是两头都可以进出
```python
import collections 
d = collections.deque('abcdefg')
# 右进
d.append('h')
print(d)
# 左进
d.appendleft('1')
print(d)

# 右出
d.pop()
print(d)

# 左出
d.popleft()
print(d)
```

### 线程
`deque`  对于线程来说是安全，可以用于多线程编程，当然常见还是使用 `queue` 来进行多线程编程
```python
import collections 
import threading

d = collections.deque()
def producer():
    for i in range(1000):
        d.append(i)
        
        
def comsumer(i):
    while True:
        try:
            num = d.pop()
            print("线程{} 正在执行任务{}".format(i,num))
        except:
            break

producer()        
ts = [threading.Thread(target=comsumer,args=(i,))for i in range(10)]
for t in ts:
    t.start()

for t in ts:
    t.join()
```

### rotating: 旋转
下面代码将后三位提前了，具体应用场景未知
```python
import collections 
d = collections.deque([1,2,3,4,5,6,7,8,9])
d.rotate(3)
print(d) # deque([7, 8, 9, 1, 2, 3, 4, 5, 6])

```

## namedtuple
常规的元组，是没有键值这样的概念的，但是由此引出了 `namedtuple` ，顾名思义，也就是有类似键值对的 `tuple` <br />其内存效率跟常规的  `tuple` 一样没有区别

### 定义
定义一个 `namedtuple` 较为简单，如下列代码所示

```python
import collections
Person = collections.namedtuple("Person","name age")
p = Person(name="john",age=20)
print(p[0],':',p[1])
```
但是这里不能使用键值来表示，只能使用索引来表示。 因为namedtuple十分像一个字典，我们也可以直接将其转为字典
```python
print(p._asdict())
```
这样就转为了一个 `OrderedDict` 对象。目前来看，其用途场景较为少见。

## OrderedDict
顾名思义，字典的键值是无序的，但是OrderedDict是有序排列的
```python
import collections 
d = collections.OrderedDict([('你好',"世界"),("Hello","world")])
for k,v in d.items():
    print("key:{},value:{}".format(k,v))
    
    
print(d["Hello"])
```
这有助于我们使用字典存储数据的时候，还照顾到了排序。其余操作跟 `dict` 差不多


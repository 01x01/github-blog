---
title: Mathematics
date: 2019-06-16 22:25:47
tags: python内建模块
category: python
---
# 概述
这个模块覆盖了一些高级的数学知识，总体在实际中只有部分会经常使用到。这里一并做一个简单的记录，覆盖以下5个模块

1. decimal 了解
1. fractions 了解
1. random 掌握
1. math 掌握
1. statistics 略


# decimal 
十进制值表示为Decimal类的实例。构造函数的参数是一个整数或字符串。浮点数可以在用于创建十进制之前转换为字符串，从而让调用者显式地处理无法使用硬件浮点表示精确表示的值的位数。另外，类方法from_float()将浮点数转换为其精确的十进制表示形式。总体来说，在实际中目前没有发现有什么用。


# fractions
这个模块有点意思，但是实际上也没啥用，代码：

```python
import fractions
for s in [0.5,0.2,0.3]:
    print(fractions.Fraction(s))
    
# 输出
1/2
3602879701896397/18014398509481984
5404319552844595/18014398509481984
```

# random
顾名思义，随机数。

## 生成一个随机数

```python
import random
for i in range(10):
  print(random.random())
```

## 生成特定范围内的随机数
```python
import random
for i in range(20):
    print(random.uniform(1,10))
```
当然这样生成的数据还有小数，有一个公式，可以生成特定范围内的随机整数
```python
random.randint(1,10)
```

## 种子随机数
随机数有时候很难出现重复的数据，所以在某些情况下，我们既要生成随机数，又要复用这些随机数的时候，就会产生一些麻烦，为此，我们可以通过种子的方式来生成可以复用的随机数，见代码：

```python
random.seed(1)
for i in range(5):
    print(random.random())
```
这段代码，无论运行多少次，在一次的会话里面，永远只会返回同样的5个数值。

## random.choice
```python
a = ["Hello","world","nihao","shima"]
random.choice(a)
```


## 随机选取倍数值
比如我们要选取 0-101 里面5的倍数，见代码
```python
random.randrange(0,101,5)
```

# math

## 四舍五入运算
```python
import math 
math.floor(1.324) #1 
math.ceil(1.234)  #2 
```


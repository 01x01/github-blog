---
title: operator
date: 2019-06-17 09:32:13
tags: python内建模块
category: python
---
# 概述
operator 模块用于表示python的运算，python 其实是一门鸭子语言，也就是说一个东西表现的像一只鸭子，那么就可以认定这是一只鸭子。换在编程语言里面，比如执行加法运算，只要里面有 add 函数，那么就都可以直接使用 + 进行运算，后面将涉及到这样的例子。


# 逻辑运算

```python
from operator import not_,truth,is_,is_not
a = -1
b = 5
print(not_(a)) # False
print(truth(a)) # True
print(is_(a,b)) # False
print(is_not(a,b)) # True
print(is_(-1,-1)) # True
```

# 比较运算

- **lt：less than** 小于
- **le：less than or equal to** 小于等于
- **eq：equal to** 等于
- **ne：not equal to** 不等于
- **ge：greater than or equal to** 大于等于
- **gt：greater than** 大于

```python
from operator import * 
a = 1
b = 2
c = -1

print(lt(a,b)) # a < b true
print(le(a,b)) # a <= b true
print(eq(a,b)) # a == b false
print(ne(a,b)) # a != b true
print(ge(a,b)) # a >= b false
print(gt(a,b)) # a > b false
```

# 算数运算

```python
print(abs(-1)) # 1
print(neg(1))  # -1
print(add(1,2)) # 3
print(floordiv(1,2)) # 1/2=0.5 => 0
print(floordiv(5,3)) # 1
print(mod(4,2)) # 4 % 2 = 0
print(pow(3,2)) # 9
```

# 属性
鸭子类型例子：

```python
class MyObj:
    def __init__(self,value):
        self.value = value
    def __add__(self,other):
        return self.value + other.value
    
MyObj(1)+MyObj(2) # 3
```


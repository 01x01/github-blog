---
title: functools
date: 2019-06-17 09:34:16
tags: python内建模块
category: python
---
# 概述
`functools` 模块提供了一系列方法，用于拓展一些类或者的功能，复用代码，不需要重写原来的函数或者类


# 装饰函数
装饰函数是python中的黑魔法，可以封装一些常用的函数，用来拓展其他类或者函数的功能。如下是一个简单的例子：
```python
import functools

def auth(username,password):
    def decorator(func):
        def wrapper(*args,**kw):
            if username == "johnw" and password == '123':
                return func(*args,**kw)
            else:
                return "auth failed"
        return wrapper
    return decorator


@auth("johnw",'123')
def user_profile():
    print("This is user profile")
    

user_profile() # This is user profile
```

上面的代码实现了一个装饰器，但是跟 `functools` 好像没有什么关系。但是实际上，`user_profile`  函数的 `__name__` 已经变成了 `wrapper` 

```python
print(user_profile.__name__) # wrapper
```
虽然，表面上没啥影响，但是如果是在一些依赖函数签名的代码，执行到这里就会出错了。所以最好的是加上 `functools.wraps(func)` . 完整代码如下：
```python
import functools


def auth(username,password):
    
    def decorator(fn):
        @functools.wraps(fn)  # 增加这一行代码
        def wrapper(*args,**kw):
            if username == "johnw" and password == '123':
                return fn(*args,**kw)
            else:
                return "auth failed"
        return wrapper
    return decorator


@auth("johnw",'123')
def user_profile():
    print("This is user profile")
    

user_profile() # This is user profile
```

# 偏函数
偏函数也是拓展函数功能的一种，比如，我们有一个 `int`  函数用来做类型转换
```python
int("10000",base=2) # 输出 16 
```
但是有时候，参数太多的情况下，我们可以用偏函数进行封装
```python
int2 = functools.partial(int, base=2)
int2("100") # 输出 4
```
偏函数就是这样的功能函数，可以帮我们在函数上，在封装一层，使得暴露的接口更加清晰简单，这也是python之所以优雅的一个方面。


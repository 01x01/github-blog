---
title: contextlib
date: 2019-06-16 22:36:33
tags: python内建模块
category: python
---
# 概述
contextlib 是 python 中的上下文管理器，在实际的开发中，我们经常需要打开一个资源，然后进行一番操作，最后在关闭资源，比如说操作数据库，比如说文件读写。那么这些操作就可以考虑封装起来，从而达到代码的复用。一个简单的例子就是文件的读写

```python
with open("file.txt",'r')as f:
  content = f.read()
  
 print(content)
```
这里的 `with` 就是使用了上下文管理器的一种写法。一个上下文管理器，起始于 `with` 关键字，其内质实现两个方法，一个是 `__enter__()` 方法，一个是 `__exit()__` 方法。 第一个方法，表示进入资源，而第二个方法表示结束退出资源以后的操作。如下一段简单的代码所示：

```python
class Context():
    def __init__(self):
        print("init object")
    
    def __enter__(self):
        print("enter object")
        return self
    
    def __exit__(self,exc_type,exc_val,exc_tb):
        print("exit")
        
with Context():
    print("doing work in the context!")
```
从上面的代码可以看到 `__enter__()` 返回了一个对象，用于实际的工作，然后 `__exit__()` 则用于这个对象工作完以后的收尾工作。通过下面的例子，可以更加直观的体现：

```python
class contextObj:
    def __init__(self,context):
        print("init obj")
    def do_some_work(self):
        print("i am obj and i do some work")
    def __del__(self):
        print("del obj")

class Context:
    def __init__(self):
        print("init")
    
    def __enter__(self):
        print("enter obj")
        return contextObj(self)
    
    def __exit__(self,exc_type,exc_val,exc_tb):
        print("exit")
        
with Context() as c:
    c.do_some_work()
    
# 输出
init
enter obj
init obj
del obj
i am obj and i do some work
exit
```

# 装饰函数
除了上面的 `with` 语句，还可以使用装饰函数，见下面的例子
```python
import contextlib
class Context(contextlib.ContextDecorator):
    def __init__(self):
        print("Hello Init")
    
    def __enter__(self):
        print("enter obj")
        return self
    
    def __exit__(self,exc_type,exc_val,exc_tb):
        print("exit obj")
        

@Context()
def func(message):
    print(message)
    
func("Hello")
```
与 `with` 语句的不同在于，这里 `__enter__()` 返回的对象是不能用在 `func` 函数里面的。

# Context Manager
写一个类来进行上下文管理并不复杂，但是有时候会显得大题小做，有时候只是管理少量的上下文关系而已，不需要这么大的系统开销。因此我们还可以使用 `contextmanager()` 来进行处理，见如下代码
```python
import contextlib
@contextlib.contextmanager
def make_context():
    print("Entering.")
    try:
        yield {}
    except RuntimeError as err:
        print("Error ",err)
    finally:
        print("exiting..")
        
with make_context() as v:
    print("inside with statement: ",v)
```
同样的，这种方式也可以用于装饰函数
```python
@make_context()
def func():
    print("I am func ")

func()

# 输出
Entering.
I am func 
exiting.
```
同样是不能使用 `enter` 返回的对象。

# 关闭操作
 在读取写入文件的API里面是直接有关闭数据流上下文操作，但是在其他的一些类里面并没有这样的操作，只是单纯的存在 `close` 方法，这个时候需要我们使用 `closing` 来达到上下文管理的需求，见代码：
```python
class Contextlib:
    def __init__(self):
        print("init obj")
        self.status = "open"
    
    def __enter__(self):
        print("enter obj")
        return self
    
    def close(self):
        print("close obj")
        self.status = "close"

with contextlib.closing(Contextlib()) as door:
    print("xxxx")
    
 # 输出
init obj
xxxx
close obj
```
可以看到，这里没有用到 `__enter__()` 函数，但是返回了一个 `door` 表示这个对象，可以利用这个对象做一些工作。

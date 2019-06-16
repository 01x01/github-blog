---
title: asyncio
date: 2019-06-16 16:04:03
tags: python内建模块
category: python
---

# 概述
协程，也是并发编程的一种，不同于多进程或者多线程，asyncio使用单线程，单进程的方式进行程序的切换，比如在进行文件读写的时候，进行程序级别的上下文切换，进入下一个程序入口执行（可以简单的认为是一个函数），整体是一个异步的过程。

# 启动协程
下面以一个简单的例子来说明协程的基本使用
```python
import asyncio

async def corotinue():
    print("in corotinue")

event_loop = asyncio.get_event_loop()

try:
    print("starting corotinue...")
    coro = corotinue()
    print("entering event loop")
    event_loop.run_until_complete(coro)
finally:
    print("close event loop")
    event_loop.close()
```
上面的代码中，我们定义了一个协程函数，然后打开一个事件循环器，这个事件循环器用于切换上下文，你把函数交给它，它帮你切换上下文，继续执行程序的其他部分，等到函数执行完，这个事件循环器就会回来喊你，告诉你函数执行完毕。但在更多的情况下，我们是希望这个函数是有返回值的，见下面的一个例子
```python
import asyncio

async def corotinue():
    print("in corotinue..")
    return "result"
  
event_loop = asyncio.get_event_loop()

try:
    print("starting....")
    result = event_loop.run_until_complete(corotinue())
    print("result is {}".format(result))
finally:
    print("close")
    event_loop.close()
```

# 链式调用协程
使用 `await` 关键字来进行链式调用，这样就无需把每个函数放进去事件循环器了。
```python
import asyncio

async def test1():
    print("Hello This is test1")
    result2 = await test2()
    print(result2)
    result3 = await test3()
    print(result3)


async def test2():
    print("Hello This is test2")
    return "test2 is end"


async def test3():
    print("Hello this is test3")
    return "test3 end"


event_loop = asyncio.get_event_loop()
try:
    result = event_loop.run_until_complete(test1())
finally:
    event_loop.close()
```


# 定时调用
定时调用函数，有两个相关的函数，一个是  `call_soon()` 一个函数是 `call_later()` , 先看一下 `call_soon()` 函数,其意思是说，定一个回调函数，以及其参数，在下一次的迭代中调用这个回调函数。所以第一个参数，就是函数的名字，后面的参数为这个回调函数的参数。
```python
import asyncio,functools
def callback(args,**kwargs):
    print("{} invoked by {}".format(args,kwargs))


async def main(loop):
    loop.call_soon(callback,1)
    # 带参数，使用functools
    wrapped = functools.partial(callback,kwargs='not default')
    loop.call_soon(wrapped,2)

try:
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()
```
接下来看一下 `call_later()` 函数，顾名思义，`call_later()` 函数用于延迟执行函数
```python
import asyncio,functools
def callback(*args,**kwargs):
    print("{} invoked by {}".format(args,kwargs))


async def main(loop):
    print("entering main")
    loop.call_later(0.2,callback,1)
    wrap = functools.partial(callback,args="world",kwargs="hello")
    loop.call_later(0.1,wrap,2)
    
    # 需等待，否则程序就退出了。
    await asyncio.sleep(0.4)

try:
    event = asyncio.get_event_loop()
    event.run_until_complete(main(event))
finally:
    event.close()
```
对比着结果看， `call_later()` 函数貌似用处不大，不如 `call_soon()` 好用。仅作了解。

# Future
`future` 表示的是一个来自 `未来` 的值，见代码
```python
import asyncio

# 执行的函数，其中 future 表示函数执行完后的对象
def mark_done(future,result):
    print("setting future result to {}".format(result))
    future.set_result(result)

event_loop = asyncio.get_event_loop()
try:
  	# 未来的空壳对象
    all_done = asyncio.Future()
    print("scheduling mark done")
    # 传递参数
    event_loop.call_soon(mark_done,all_done,'the result')
    print("entering event loop")
    result = event_loop.run_until_complete(all_done)
    print("return result: {}".format(result))
finally:
    event_loop.close()


'''
scheduling mark done
entering event loop
setting future result to the result
return result: the result
'''
```
这个未来的对象也是可以等待的，见代码
```python
import asyncio,functools

# 回调函数
def call_back(future,n):
    print("{}: future done: {}".format(n,future.result()))

# 注册回调函数
async def register_callbacks(all_done):
    print("register callback on future ")
    all_done.add_done_callback(functools.partial(call_back,n=1))
    all_done.add_done_callback(functools.partial(call_back,n=2))

# 主函数
async def main(all_done):
    await register_callbacks(all_done)
    print("setting result of future")
    all_done.set_result("the result")


event_loop = asyncio.get_event_loop()
try:
    all_done = asyncio.Future()
    event_loop.run_until_complete(main(all_done))
finally:
    event_loop.close()
```
在这里这个代码有点复杂，并不能很好理解，就简单记录一下，后面遇到再进行思考总结。

# 并发使用
既然是并发使用，在多线程一章中，我们主张使用队列的方式来实现多线程的执行，在这里协程也有其队列的方式。下面使用一个例子来理解：
```python
import asyncio

async def consumer(n,q):
    print("consumer {}: starting".format(n))
    while True:
        print("consumer {}: waiting for item".format(n))
        item = await q.get()
        print("consumer {}: has item {}".format(n,item))

        if item is None:
            q.task_done()
            break
        else:
            await asyncio.sleep(3)
            print("consumer {}: has item {}".format(n, item))
            q.task_done()

async def producer(q, number_workers):
    print("producer : starting.")
    for i in range(number_workers * 3):
        await q.put(i)
        print("producer add task {}".format(i))

    for i in range(number_workers):
        await q.put(None)

    print("producer: waiting for queue to empty")
    await q.join()
    print("producer: ending")

    
async def main(loop,num_consumers):
    q = asyncio.Queue()
    consumers = [
        loop.create_task(consumer(i,q))for i in range(num_consumers)
    ]
    prod = loop.create_task(producer(q,num_consumers))
    await  asyncio.wait(consumers + [prod])


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop,3))
finally:
    event_loop.close()
```

# 第三方框架
常见的第三方框架有 `aiohttp` 和 `aiodns` 等等。 具体可以参考： [https://github.com/timofurrer/awesome-asyncio](https://github.com/timofurrer/awesome-asyncio) 

# 参考
[http://www.dongwm.com/post/80/](http://www.dongwm.com/post/80/) <br />[http://www.dongwm.com/post/83/](http://www.dongwm.com/post/83/)<br />[http://www.dongwm.com/post/84/](http://www.dongwm.com/post/84/) 


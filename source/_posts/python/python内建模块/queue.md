---
title: queue
date: 2019-06-17 09:54:08
tags: python内建模块
category: python
---
# 概述
队列，先进先出的原则。常和多线程结合使用


# 基本的队列

```python
# 基本的队列
import queue
q = queue.Queue()
for i in range(10):
    q.put(i)
    
while not q.empty():
    i = q.get()
    print(i)
```

# 后进先出队列
后进先出原则，可以使用 `LifoQueue`  模块， 其用法差不多

```python
# 基本的队列
import queue
q = queue.LifoQueue()
for i in range(10):
    q.put(i)
    
while not q.empty():
    i = q.get()
    print(i)
```
输出：
```python
9
8
7
6
5
4
3
2
1
0
```
跟上面的例子相反了


# 优先级队列
优先级队列一般存储两个值，一个优先级分值，一个是其他的 数据，一个简单结合多线程的代码如下所示
```python
# 优先级队列

class job(object):
    def __init__(self,priority,des):
        self.priority = priority
        self.des = des
        
    def __eq__(self,other):
        try:
            return self.priority == other.priority
        except AttributeError:
            return NotImplemented
        
    def __lt__(self,other):
        try:
            # 设置 > 表示分值越大的，越先执行
            return self.priority > other.priority
        except AttributeError:
            return NotImplemented

        
import queue
import threading 

q = queue.PriorityQueue()

q.put(job(9,"import-9"))
q.put(job(10,"import-10"))
q.put(job(8,"import-8"))
q.put(job(7,"mid - 7"))
q.put(job(6,"mid - 6"))
q.put(job(1,"low - 1"))

def consumer():
    while not q.empty():
        item = q.get()
        print(item.des + "\n")

ts = [threading.Thread(target=consumer) for i in range(4)]

for t in ts:
    t.start()
    
for t in ts:
    t.join()
```
输出
```python
线程0正在执行： import-10
线程1正在执行： import-9
线程2正在执行： import-8
线程3正在执行： mid - 7




线程1正在执行： low - 1
线程0正在执行： mid - 6
```


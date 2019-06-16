---
title: threading
date: 2019-06-16 16:04:44
tags: python内建模块
category: python
---

# 概述
多线程模块，鉴于Python的特殊性，多线程在python中多用于IO密集型计算，不适用于CPU密集型计算，工作中常见的场景是将其与队列结合使用。

# 使用说明
```python
import threading
from datetime import datetime 
import time

def work():
    print("work"+datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S:%f") + "\n")
    time.sleep(2)
    print("end\n")

ts = [threading.Thread(target=work) for i in range(5)]

for t in ts:
    t.start()
    
print("main end")

# 输出
work2019-04-01 14:57:20:710539
work2019-04-01 14:57:20:725579
work2019-04-01 14:57:20:736610
work2019-04-01 14:57:20:748640
work2019-04-01 14:57:20:760673
main end
end
end
end
end
end
```
从上面的代码可以看出，多线程是**并发执行**的，并非并行执行，启动多线程的方式是使用 `start()` 函数。但是主函数在多线程结束之前，就已经结束了，这明显不符合我们代码运行的顺序，因此我们需要做一些改变
```python
...
for t in ts:
    t.start()
    
t.join()
print("main end")
```
加上 `join()` 函数，可以保证主进程等待多线程的完成以后在执行。

# 多线程类
python 也支持面向对象编程的写法，定义一个可以执行多线程的对象十分简单，只要满足两个条件

1. 继承 `threading.Thread` 
1. 实现 `run()` 函数

见代码示例：
```python
class MyThread(threading.Thread):
    def run(self):
        print("work"+datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S:%f") + "\n")
        time.sleep(2)
        print("end")
        

for i in range(5):
    t = MyThread()
    t.start()
    
t.join()
print("main end")
```
`run()` 函数为主要执行的事情。但是这是最基本的情况，有时候在实际工作中并没有这么简单，比如某些情况下，我们需要对定义的类进行赋值，见代码：
```python
class MyThread(threading.Thread):
    def __init__(self,group=None,target=None,name=None,args=(),kwargs=None,*,daemon=None):
        # 继承初始化函数
        super().__init__(group=group,target=target,name=name,daemon=daemon)
        self.args = args
        self.kwargs = kwargs
    
    def run(self):
        for t in self.args:
            print(t+datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S:%f") + "\n")
        time.sleep(2)
        print("end")
        

for i in range(5):
    t = MyThread(args=(str(i),))
    t.start()
    
t.join()
print("main end")
        
```

# 时间多线程
时间类的多线程，顾名思义就是可以设置一个时间点，到这个时间点的时候自动运行线程，见代码
```python
def delayed():
    print(threading.current_thread().name+": working\n")
    
t1 = threading.Timer(0.3,delayed)
t1.setName('t1')
t2 = threading.Timer(0.3,delayed)
t2.setName("t2")
# 0.3s后开始运行多线程
t1.start()
t2.start()
# 取消第二个多线程
print("cancel: "+t2.getName())
time.sleep(0.2)
t2.cancel()
t1.join()
print("done")
```


# 结合队列使用

```python
import os 
from datetime import datetime 
from queue import Queue
from threading import Thread
import requests
requests.packages.urllib3.disable_warnings()

from bs4 import BeautifulSoup
import re

if not os.path.exists('img'):
    os.mkdir('img')

# 声明一个队列
Q = Queue()

def producer(pages):
    for page in range(1,pages+1):
        # 提取每一页的图片 url 加入队列
        print("[-] 收集第 {} 页".format(str(page)))
        url = "http://simpledesktops.com/browse/"+str(page)+"/"
        r = requests.get(url,verify=False)
        html = r.text
        soup = BeautifulSoup(html,'html.parser')
        try:
            imgs = soup.find_all('img')
            for img in imgs:
                img_url = img['src']
                Q.put(img_url)
        except:
            pass

def worker(i):
   # 取出队列的值，按顺序取，下载图片
    while not Q.empty():
        img_url = Q.get()
        text = re.search('(http://static.simpledesktops.com/uploads/desktops/\d+/\d+/\d+/(.*?png)).*?png',img_url)
        new_img_url = text.group(1)

        r = requests.get(new_img_url,verify=False)
        path = "img/"+text.group(2)
        print("[-] 线程 {} 开始下载 {} 开始时间：{}".format(i,text.group(2),datetime.now()))

        with open(path,'wb') as f:
            f.write(r.content)
    
    Q.all_tasks_done


if __name__ =="__main__":
    # 一定要将数据加入队列，否则是启动不了的，因为队列为空 
    producer(50)
    # 线程的声明
    ts = [Thread(target=worker,args=(i,)) for i in range(50)]
    for t in ts:
        t.start()

    for t in ts:
        t.join()
```


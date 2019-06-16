---
title: log处理
date: 2019-06-16 15:55:32
tags: python内建模块
category: python
---
![img](https://raw.githubusercontent.com/01x01/github-blog/master/source/img/meaty.png)

# 概述
 不管是调试还是记录追查问题，在代码中设置 log 都是很有必要，不然程序除了问题以后，很难追踪到具体是啥问题造成的。log 的表现由两种形式，一种是命令行直接输出，一种是写入文件。在这里记录一下常用的办法，方便以后直接拿来用即可。

# 工作流
理解 log 模块，首先要理解其工作流，假设我们已经写好 log 的配置文件，下面通过代码理解其工作流<br />一般 python 通常会设置一个入口文件，这样方便模块调用，这个入口文件，我们先称之为 `main.py` 
```python
import sub
import sub2
import logging
import logging.config
from config import LOGGING
logging.config.dictConfig(LOGGING)
# 每个文件都要有一个 logger
logger = logging.getLogger("main")

def main():
    sub.sub1()
    logger.error("main debug")


if "__main__" == __name__:
    main() 
```
可以看到在这里，记录了 main 文件的 log， 那么如何记录 sub 文件的 log？<br />代码：
```python
import logging
sub_logger = logging.getLogger("main.sub")
def sub1():
    print("Hello This is sub1")
    sub_logger.debug("This is sub1")
```
这样的继承机制，可以避免我们每一个文件都写一个 log 配置。


# 配置
配置文件分为两种：

1. 字典形式
1. 配置文件模式

这里直接使用字典模式来定义配置文件。配置文件有四个类要进行定义：

1. formatters
1. handlers
1. filters
1. loggers

## formatters
这里定义了两种模式，一种是标准，一个简单模式，其命名都是自定义的
```python
"formatters":{
  # 标准模式
  "standard":{
     'format':'[%(asctime)s][%(threadName)s:%(thread)d][%(name)s:%(levelname)s(%(lineno)d)]\n[%(module)s:%(funcName)s]:%(message)s'
  }
  # 简单模式
  "brief":{
    "format":'[%(message)s]'
  }
}
```
接下来看一下格式化字符串的意义
```shell
%(name)s Logger的名字
%(levelno)s 数字形式的日志级别
%(levelname)s 文本形式的日志级别
%(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
%(filename)s 调用日志输出函数的模块的文件名
%(module)s 调用日志输出函数的模块名
%(funcName)s 调用日志输出函数的函数名
%(lineno)d 调用日志输出函数的语句所在的代码行
%(created)f 当前时间，用UNIX标准的表示时间的浮点数表示
%(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
%(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(thread)d 线程ID。可能没有
%(threadName)s 线程名。可能没有
%(process)d 进程ID。可能没有
%(message)s 用户输出的消息
```

## handlers
handlers 分为两部分，一部分是命令行输出，一部分是文件形式
```python
"handlers":{
  "console":{
     'level':'DEBUG',    #输出信息的最低级别
     'class':'logging.StreamHandler',
     'formatter':'standard', #使用standard格式
      'filters': ['require_debug_true',], #仅当 DEBUG = True 该处理器才生效,一般没用。
  },
  'log':{
      'level':'DEBUG',
      'class':'logging.handlers.RotatingFileHandler',
      'formatter':'standard',
      'filename':os.path.join(BASE_DIR, 'debug.log'), #输出位置
      'maxBytes':1024*1024*5, #文件大小 5M
      'backupCount': 5, #备份份数
      'encoding': 'utf8', #文件编码
    },
}
```

## filters 
TODO

## loggers
loggers 是日志的全局管理器，这里定义的 logger 将是后面内容需要调用的。比如
```python
'loggers':{
    #管理器
    "main":{
        'handlers':['console', 'main_log'],
        'level':'DEBUG',
        'propagate':True, #是否传递给父记录器
    },
}
```

# 完整代码

```python
# coding: utf-8 
# config.py

import os 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGGING = {
    'version':1,
    "formatters":{
        # 标准模式
        "standard":{
            'format':'[%(asctime)s][%(threadName)s:%(thread)d][%(name)s:%(levelname)s(%(lineno)d)]\n[%(module)s:%(funcName)s]:%(message)s'
        },
        # 简单模式
        "brief":{
            "format":'[%(message)s]'
        }
    },
    "handlers":{
        "console":{
            'level':'DEBUG',    #输出信息的最低级别
            'class':'logging.StreamHandler',
            'formatter':'standard', #使用standard格式
        },
        'log':{
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'formatter':'standard',
            'filename':os.path.join(BASE_DIR, 'debug.log'), #输出位置
            'maxBytes':1024*1024*5, #文件大小 5M
            'backupCount': 5, #备份份数
            'encoding': 'utf8', #文件编码
        },
    },
    'loggers':{
        #管理器
        "main":{
            'handlers':['console', 'log'],
            'level':'DEBUG',
            'propagate':True, #是否传递给父记录器
        },
    }
}
```
接下去是调用过程
```python
import logging
import logging.config
from config import LOGGING
logging.config.dictConfig(LOGGING)
# 每个文件都要有一个 logger
# 这里的 main 名字，需要在配置文件里面有定义
logger = logging.getLogger("main")

def main():
    logger.error("main debug")


if "__main__" == __name__:
    main()
```


---
title: log
date: 2019-06-21 15:33:49
tags: 
category: python
---
使用 python 记录 log 的方式
<!-- more -->
# formatters
示例：
```py
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
格式化字符的含义：
```
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

# handler
示例：
```py
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
# logger
示例：
```py
'loggers':{
    # 管理器
    # 这里需要自定名词，方便后面调用的时候指定。
    "main":{
        'handlers':['console', 'main_log'],
        'level':'DEBUG',
        'propagate':True, #是否传递给父记录器
    },
}
```
# 范例
```py
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
# 调用
```py
# main 文件
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

# sub
import logging
sub_logger = logging.getLogger("main.sub")
def sub1():
    print("Hello This is sub1")
    sub_logger.debug("This is sub1")
```
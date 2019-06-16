
---
title: filesystem
date: 2019-06-16 15:05:17
tags: 
category: 
---
![img](https://raw.githubusercontent.com/01x01/github-blog/master/source/img/ants.png)
# 概述
`os.path` 是python跨平台的路径处理模块。

# 解析路径
众所周知，不同的系统其路径的表示方式是不一样的，比如 *unix 系统，路径表示为 `/usr/local/src` 而windows 系统路径就表示为 `C:\user\xxx` ,所以跨系统要解决的是统一路径，python 提供了以下几个属性：

1. `os.sep` (表示 `\` 或者 `/` )
1. `os.extsep`  (表示 `.` 文件后缀的点)
1. `os.pardir` (表示 `..` )
1. `os.curdir` (表示 `.` 当前目录 ) 

## split 函数
`split` 函数将路径返回一个tuple，将路径分为两部分，一部分是父目录，一部分子目录或者文件名，见代码：
```python
import os.path 
os.path.split("/usr/local/src") # ('/usr/local', 'src')
```

## basename函数
`split` 返回一个tuple， 而 `basename` 函数直接返回路径的目录或者文件名，见代码
```python
os.path.basename("/usr/local/src") # src
```

## dirname 函数
`dirname` 返回 `split` 函数的第一个值，见代码：
```python
os.path.dirname("/usr/local/src") #'/usr/local'
```

## splitext 函数
`splitext` 跟 `split` 有点不一样，它是用于分离文件名后缀的，见代码
```python
os.path.splitext("/usr/local/src.txt") # ('/usr/local/src', '.txt')
```

## commomprefix 函数
顾名思义，接受一个列表或者tuple, 返回路径相同的部分
```python
os.path.commonprefix(('/usr/local/src',"/usr/local/sre")) #'/usr/local/sr'
```

- 要注意目录名的相似之处

## commonpath 函数
如果是要得到相同的路径，用 `commonpath` 会比较合理
```python
os.path.commonprefix(('/usr/local/src',"/usr/local/sre")) # /usr/local
```

# 构建路径

## join 函数
路径拼接一般不建议直接使用字符串相加的方法，这样拓展性不好，建议使用 `join` 函数进行构建路径
```python
os.path.join("/usr/local",'src') # /usr/local/src
```

## expandvars 函数
我们还可以使用变量的方式来构建路径，见代码：
```python
import os 
os.environ['VARS'] = "Hello"
os.path.expandvars("/usr/src/$VARS") # '/usr/src/Hello'
```

## abspath函数
获取绝对路径
```python
os.path.abspath("..")
```

## 文件时间
文件的时间有三种：

1. 访问时间 `getatime` 
1. 修改时间 `getmtime` 
1. 创建时间 `getctime` 
```python
print(os.path.getatime("."))
print(os.path.getctime("."))
print(os.path.getmtime("."))

# 返回
1553564647.2682087
1551837492.5463014
1553564647.2682087
```

## 文件测试
```python
filename = "/usr/local/src"
print(os.path.isfile(filename))
print(os.path.isdir(filename))
print(os.path.isabs(filename)) # True
print(os.path.islink(filename))
print(os.path.ismount(filename))
print(os.path.exists(filename))

# 其余都是 False
```


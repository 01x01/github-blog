---
title: argparse
date: 2019-06-16 15:57:08
tags: 
category: 
---
![img](https://raw.githubusercontent.com/01x01/github-blog/master/source/img/newspaper.png)
# 概述
python 里面命令行参数模块。


# 示例

```python
例子
# coding:utf-8
import argparse

parser = argparse.ArgumentParser()

mandatory = parser.add_argument_group("Mandatory")
mandatory.add_argument('-u','--url',help="URL Target",action="store",type=str,dest="urldest",default=None)

dictionary =  parser.add_argument_group("Dictionary")
dictionary.add_argument('-w','--wordlist',action="store",type=str,dest="wordlist",default="None")

parser.print_help()
args = parser.parse_args()

# 使用方法
# args.urldest===> 取到 url 这个参数
# 如果不存在，则为 None
```


# 说明

```python
第一个参数为 flag
第二个参数为 name
action： 一般值为 store 代表存储这个参数值
type： 这个参数的类型，一般有 str / int / float 
dest:  这个参数是你需要使用的时候，需要args.dest来调用这个参数，算是对象的属性名
metavar：举例说明这个参数的用法，比如说，日期格式为：YYYY-MM-DD
choices: 提供一个数组，这个参数的值将会从数组中选取
required：参数是否是必须的，这个是一个可选的，可以在这里判断，或者在程序中判断
```

# 使用
```python
args.url
```

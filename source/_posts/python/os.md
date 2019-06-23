---
title: os
date: 2019-06-21 17:09:37
tags: 
category: python
---
python OS 模块

<!-- more -->

# os.path 

## 属性

1. `os.sep` (表示 `\` 或者 `/` )
2. `os.extsep`  (表示 `.` 文件后缀的点)
3. `os.pardir` (表示 `..` )
4. `os.curdir` (表示 `.` 当前目录 ) 

## split 函数

`split` 函数将路径返回一个tuple，将路径分为两部分，一部分是父目录，一部分子目录或者文件名，见代码：

```python
import os.path 
os.path.split("/usr/local/src") # ('/usr/local', 'src')
```

## basename 函数

`split` 返回一个tuple， 而 `basename` 函数直接返回路径的目录或者文件名，见代码

```python
os.path.basename("/usr/local/src") # src
```

## dirname 函数

`dirname` 返回 `split` 函数的第一个值，见代码：

```python
os.path.dirname("/usr/local/src") #'/usr/local'
```

## splitext 函数

`splitext` 跟 `split` 有点不一样，它是用于分离文件名后缀的，见代码

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

如果是要得到相同的路径，用 `commonpath` 会比较合理

```python
os.path.commonprefix(('/usr/local/src',"/usr/local/sre")) # /usr/local
```

## join 函数

路径拼接一般不建议直接使用字符串相加的方法，这样拓展性不好，建议使用 `join` 函数进行构建路径

```
os.path.join("/usr/local",'src') # /usr/local/src
```

## expandvars 函数

我们还可以使用变量的方式来构建路径，见代码：

```
import os 
os.environ['VARS'] = "Hello"
os.path.expandvars("/usr/src/$VARS") # '/usr/src/Hello'
```

## abspath函数

获取绝对路径

```
os.path.abspath("..")
```

## 文件时间

文件的时间有三种：

1. 访问时间 `getatime` 
2. 修改时间 `getmtime` 
3. 创建时间 `getctime` 

```
print(os.path.getatime("."))
print(os.path.getctime("."))
print(os.path.getmtime("."))

# 返回
1553564647.2682087
1551837492.5463014
1553564647.2682087
```

## 文件测试

```
filename = "/usr/local/src"
print(os.path.isfile(filename))
print(os.path.isdir(filename))
print(os.path.isabs(filename)) # True
print(os.path.islink(filename))
print(os.path.ismount(filename))
print(os.path.exists(filename))

# 其余都是 False
```

# os

## 判断文件是否存在

```python
# 查看文件是否存在
# 一共有三种属性,分别是 存在，可读，可写，可执行
 
# F_OK
# R_OK
# W_OK
# X_OK
 
os.access("tes1t.txt",os.F_OK) # 返回 True or False
```

## 删除文件

```python
# 删除文件
os.remove("test.txt") # 如果参数是一个目录路径的话，会报错
```

## 遍历文件

```python
# 遍历目录
'''
top: 给定的路径
topdown: 自上而下搜索
onerror: 函数，调用需要传一个参数，OSError实例，出现错误后执行
followelinks: 通过软连接进行访问

返回三个值：
dirname: 返回文件夹的相对路径
dirpath: 返回的是一个集合，是当前遍历到的所有文件夹的集合
filenames: 返回的也是一个集合，文件名集合
''' 

# os.walk(top, topdown=True, onerror=None, followlinks=False)

def walk_folder(top,extension,absolute=False,relative=False,topdown=True, onerror=None, followlinks=False):
    files = []
    for dirname,dirpath,filenames in os.walk(top,topdown=topdown,onerror=onerror,followlinks=followlinks):
        for file in filenames:
            if os.path.splitext(file)[1] == extension:
                if absolute and relative:
                    print('Chose absolute or relative')
                    return 

                elif absolute:
                    absolute_path = os.path.join(os.getcwd(),os.path.join(dirname,file))
                    print(absolute_path)
                    files.append(absolute_path)

                elif relative:
                    absolute_path = os.path.join(dirname,file)
                    print(absolute_path)
                    files.append(absolute_path)
                else:
                    print(file) 
                    files.append(file)

    return files
```

## 递归创建目录

```python
# 递归创建目录
os.makedirs("src/test/")
```

## 当前绝对路径

```python
# 当前绝对路径
os.getcwd()
```

## 列出文件和目录

```python
# 列出目录下的所有文件和目录
os.listdir(path)
```
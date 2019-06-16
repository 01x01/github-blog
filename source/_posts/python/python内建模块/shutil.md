---
title: shutil
date: 2019-06-16 16:17:25
tags: python内建模块
category: python
---

# 概述
shutil 是更加高级的模块用于操作文件和目录，os 模块提供的是相对基础和底层的操作


# 复制文件
复制文件有3种方式：

1. `copyfile` 复制文件
1. `copy` 复制文件
1. `copystat`  复制文件和文件的属性 
```python
shutil.copyfile("1-Text.md","1-Text.md.copy")
os.stat("1-Text.md.copy")

shutil.copy("1-Text.md","1-Text.md.copy2")
os.stat("1-Text.md.copy2")

shutil.copystat("1-Text.md","1-Text.md.copy3")
os.stat("1-Text.md.copy2")
```
其实如果不是有特别的用途，用起来都差不多，推荐使用 `copystat` 复制的时候，顺便把属性给复制过去。

# 操作目录
递归复制目录内容，见代码
```python
shutil.copytree('../Code',os.path.join(os.getcwd(),"code"))
```
如上的代码，将code里面的文件和目录统统复制到了当前目录下新建的 code 文件夹里面。

# 寻找文件
寻找文件有点类似于 *unix 中的 which 命令。 一般从 path 路径里面去寻找. 用处一般不大

```python
print(shutil.which("virtualenv")) # C:\software\python3\Scripts\virtualenv.EXE
```

# 压缩文件
首先看一下 python 支持几种压缩方法
```python
for i in shutil.get_archive_formats():
    print(i[0],":",i[1])
    
# 输出
bztar : bzip2'ed tar-file
gztar : gzip'ed tar-file
tar : uncompressed tar file
xztar : xz'ed tar-file
zip : ZIP file
```
在windows 见到最多是 zip 类型的压缩包，接下来看一下如何压缩文件
```python
# make_archive 接收4个参数，filename,extension, root_dir,base_dir
# filename 打包好的文件要叫什么名字，可以是一个路径，文件将存放在那里
# extension 压缩的类型
# root_dir 跳到要打包的目录的地方
# base_dir 选择要打包的目录
# 跳到上一层的目录，选择 code 目录，打包，存放到当前文件夹
shutil.make_archive("code2","zip",root_dir="..",base_dir="code")
```

# 解压文件
解压文件显得简单多了，见代码
```python
shutil.unpack_archive("code.zip","docker")
```
只需要给出文件名，和解压路径名即可，十分简单。


# 系统指数
见代码
```python
total, used, free = shutil.disk_usage(".")
gib = 2 ** 30
gb = 10 ** 9
print("total: ",total / gb)
print("used: ", used / gib)
print("free: ",free / gb)
```


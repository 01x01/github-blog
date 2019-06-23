---
title: shutil
date: 2019-06-23 22:38:20
tags: 
category: python
---
shutil 模块，用于操作系统文件，解压缩。

<!-- more -->

# 复制文件

复制文件有3种方式：

1. `copyfile` 复制文件
2. `copy` 复制文件
3. `copystat`  复制文件和文件的属性 

```python
shutil.copyfile("1-Text.md","1-Text.md.copy")
os.stat("1-Text.md.copy")

shutil.copy("1-Text.md","1-Text.md.copy2")
os.stat("1-Text.md.copy2")

shutil.copystat("1-Text.md","1-Text.md.copy3")
os.stat("1-Text.md.copy2")
```


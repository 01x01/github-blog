---
title: 设置Python环境
date: 2019-06-17 11:14:33
tags: Linux
category: Linux
---


# 安装 pyenv
```shell
$ curl https://pyenv.run | bash
```


# 常用命令
```shell
# 查看可安装版本
pyenv install -l

# 安装
pyenv install 2.7.13
pyenv install 3.7.6

# 卸载
pyenv uninstall 2.7.13

# 全局设置
pyenv global 2.7.13 (一般设置)
pyenv local 2.7.13 
pyenv shell 2.7.13

# 优先级
shell > local > global
```

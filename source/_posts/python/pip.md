---
title: pip
date: 2019-06-27 20:59:22
tags: 
category: python
---
pip 配置

<!-- more -->

# 配置下载地址

```
# Windows
vim C:\Users\pip\pip.ini
# Mac/Linux
vim ~/.pip/pip.cong

-----

[global]
trusted-host =  mirrors.aliyun.com
index-url = http://mirrors.aliyun.com/pypi/simple
```

# 虚拟环境

```
$ python -m venv venv 
$ source venv/bin/activate

# Windows
$ .\venv\Scripts\activate

# 退出虚拟环境
deactivate
```

# pipenv

```
# 全局安装pipenv
pip install pipenv 
# 初始化项目
mkdir <your-project-name>
cd <your-project-name>
# 创建pipfile 和pipfile.lock, 如果已经存在的话，会安装项目工程依赖，不安装工具依赖
pipenv install 
# 安装项目工程依赖
pipenv install requests 
# 安装项目工具依赖
pipenv install pytest --dev
# 导出为requirements.txt. 只导出项目工程依赖
pipenv lock -r
# 项目工具依赖导出
pipenv lock -r -d
# 进入虚拟环境
pipenv shell
# 退出
exit
# 在初始化的时候可以指定python版本,会自动寻找系统安装的python版本
pipenv --python 3.6 
pipenv --python 2.7.14 
```


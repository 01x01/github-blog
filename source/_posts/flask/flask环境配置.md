---
title: Flask 环境配置
date: 2019-06-27 10:22:24
tags: 
category: flask
---
基础环境配置
<!-- more -->
# 安装
```shell
python -m venv venv 
pip install flask python-dotenv
pip freeze > requirements.txt
```

# web 应用的结构
```
flasky(项目名称)
 --app(存放业务逻辑代码)
    -- __init__.py(创建应用)
    -- authentication(蓝图，将应用按照功能进行模块化)
    -- error(错误处理蓝图)
    -- index(首页蓝图)
    -- backoffice(应用后台)
 --.env (全局环境变量)
 --config.py(项目的配置信息)
 --flasky.py(启动文件)

```
# 全局开发环境变量
新建 `.env` 文件
```ini
FLASK_APP=flasky.py
FLASK_DEBUG=1
```

# 创建应用的初始化函数
新建 `app/__init__.py`
```py
# coding:utf-8
from flask import Flask

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])


    return app
```

新建 `flasky.py`
```py
from app import create_app

app = create_app('dev')

```

# 测试
新建蓝图
```
# app/index/__init__.py

```



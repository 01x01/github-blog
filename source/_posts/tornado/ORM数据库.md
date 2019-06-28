---
title: ORM数据库
date: 2019-06-27 15:05:24
tags: tornado
category: tornado
---
基于 tornado 的 ORM 数据库。
<!-- more -->
# tornado-sqlalchemy 
## 安装
```
pip install pymysq tornado-sqlalchemy alembic 
```
## 使用
1. 配置数据库
```py
# blog/__init__.py
from tornado_sqlalchemy import make_session_factory
from config import Configuration
def create_app(config_name):
	...
	session_factory = make_session_factory(db_url)
    settings = dict(
        template_path = template_path,
        static_path = static_path,
        debug = debug,
        session_factory=session_factory
    )
    ...

```
2. 声明一个model
```py
# coding: utf-8 
# this is models for this app
from sqlalchemy import BigInteger, Column, String
from tornado_sqlalchemy import declarative_base
                                
DeclarativeBase = declarative_base()

class User(DeclarativeBase):
    __tablename__='users'
    id = Column(BigInteger, primary_key=True)
    username = Column(String(255), unique=True)
    passwd_hash = Column(String(250))
```
## 结合 alembic 进行数据库迁移
```
cd project_root
alembic init alembic 

修改目录下面的 alembic.ini 文件
...
sqlalchemy.url = mysql+pymysql://root:qwe123@127.0.0.1/blog

修改 alembic/env.py
...
import os, sys
sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '..')))
...
from blog import models
target_metadata = models.DeclarativeBase.metadata
```
## 建立数据库表
```
alembic revision --autogenerate -m "first commit"
alembic upgrade head 
alembic downgrade <version-number>
```

# 参考
https://tornado-sqlalchemy.readthedocs.io/en/latest/

---
title: sqlalchemy基础
date: 2019-07-01 10:14:42
tags: 
category: python
---
sqlalchemy 的基础用法 - 1
<!-- more -->
# 版本
```
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
1.3.0
```
# 创建数据库连接
```python
# coding: utf-8 
# create_engine 代表了数据库的接口，其形式为 mysql+pymysql://user:passwd@host:port/databasename
# 其顺序不能弄错： <database>+<driver>://<username>:<passwd>@<host>:<port>/<database>
# 当声明 create_engine 的时候，并不是真的连接到了数据库
# 真的连接到数据库是执行增删改查的时候才是连接到数据库
# echo 参数简单可以显示数据库的输出
from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://root:qwe123@127.0.0.1/test",echo=True)
```

# 创建映射
```py
# 定义数据库和类的映射关系
# 如何将代码类转为数据库表，sqlalchemy 均封装在了 declarative_base 里面
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
```
# 定义数据库类
```py
# 定义数据库类
# 一个数据库类需要 __tablename__
from sqlalchemy import Column, Integer, String
class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True)
    name = Column(String(250),unique=True)

    def __repr__(self):
        return "<User (name=%s)>"%(self.name)

```
# 创建数据库
```py
# 创建数据库
Base.metadata.create_all(engine)
'''
CREATE TABLE users (
        id INTEGER NOT NULL AUTO_INCREMENT,
        name VARCHAR(250),
        PRIMARY KEY (id),
        UNIQUE (name)
)
'''
```

# 创建会话
```py
# 数据库操作以 Session 为单位
# Session 会保持会话，直到我们 commit 所有的 change 
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

# 如果你的应用还没有声明 engine，可以先声明 session，后面在绑定 engine
# from sqlalchemy.orm import sessionmaker
# session = sessionmaker()
# session.configure(bind=engine)

session = Session()
```
# 数据库操作
## 查询
```py
result = session.query(User).filter_by(name='john').first()
print(result)
```
## 添加用户
```py
# 添加用户
if not result:
    user = User(name="john")
    session.add(user)
    
else:
    print("user exists")


# 添加多个用户
u1 = User(name='jack')
u2 = User(name='marry')
u3 = User(name="jimmy")

session.add_all([
    u1,
    u2,
    u3
])


# 最后一定要 commit
session.commit()
```
# 回滚
```py
# 如果发现错误，可以在 commit 之前回滚数据库
# 没有回滚前
r = session.query(User).filter_by(name='marry').first()
print(r) # <User (name=marry)>
# 回滚后
session.rollback()
r1 = session.query(User).filter_by(name='marry').first()
print(r1) # None
```


# 参考文档
https://docs.sqlalchemy.org/en/13/
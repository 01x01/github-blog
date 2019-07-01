---
title: sqlalchemy 查询
date: 2019-07-01 13:57:13
tags: 
category: python
---
基于 sqlalchemy 的查询用法
<!-- more -->
# 排序查询
```py
for r in session.query(User).order_by(User.id):
    print("排序查询结果为：",str(r.id) +":"+ r.name)
```

# 全部查询
```py
for r in session.query(User).all():
    print("全部查询结果为：",r)
```
# 过滤查询
```py
r = session.query(User).filter_by(name='john').first()
print("过滤查询结果为：",r)
```
# 条件查询
## 相等
```py
for r in session.query(User).filter(User.name == "john"):
    print("相等查询结果为:",r)
```
## 不相等
```py
u1 = User(name='jack')
u2 = User(name='marry')
u3 = User(name="jimmy")

session.add_all([
    u1,
    u2,
    u3
])

for r in session.query(User).filter(User.name != "john"):
    print("不相等查询结果为:",r)
```
# LIKE 查询
```py
for r in session.query(User).filter(User.name.like("john")):
    print("LIKE 查询结果为:",r)
```

# 忽略大小写的 LIKE 查询
```py
for r in session.query(User).filter(User.name.ilike("%JOHN%")):
    print("ILIKE 查询结果为:",r)
```
# IN 查询
```py
for r in session.query(User).filter(User.name.in_(['john','marry'])):
    print("IN_ 查询结果为:",r)
```
# NOT IN 查询
```py
for r in session.query(User).filter(~User.name.in_(['john','marry'])):
    print("NOT IN_ 查询结果为:",r)
```
# IS NULL 查询
```py
for r in session.query(User).filter(User.name == None):
    print("IS NULL 查询结果为:",r)
```
# IS NOT NULL 查询
```py
for r in session.query(User).filter(User.name != None):
    print("IS NOT NULL 查询结果为:",r)
```
# AND 查询
```py
for r in session.query(User).filter(User.id!=None,User.name=='john'):
    print("AND 查询结果为:",r)
```
# OR 查询
```py
from sqlalchemy import or_
for r in session.query(User).filter(or_(User.name=="marry",User.name=='john')):
    print("OR 查询结果为:",r)
```

# text 
接收 sql 语句用来查询，但是这样一来也容易造成 sql 注入。
```py
# Text 查询
from sqlalchemy import text
for r in session.query(User).filter(text("id<10")).order_by(text("id")).all():
    print("text:",r)
# text 参数查询
r = session.query(User).from_statement(text("SELECT * FROM users where name =:name ")).params(name='john').all()
print("参数化：", r)
```
# 连接查询
将多张表进行记录的连接查询，其意义在于用户查看数据的时候，显示的数据来源于多张表。
## 内连接
从左边的表取一条记录，跟右边的表所有的记录进行匹配，如果条件相同，则保留，反之不保留。可以假设这么一个场景：从两张表中找出注册人的id和注册车id一样的数据
其 SQL 语句：
```sql
select * from users u join cars c where u.id=c.id
```

其 ORM 语句
```py
q1 = session.query(User).join(Car).filter_by(User.id == Car.id).all()
```

## 外连接查询
外连接查询分为：
1. 左外连接查询
2. 右外连接查询

外连接查询跟内连接不一样的地方在于，外连接以某张表为主，先取出所有的数据，然后每条跟另一张表进行连接，不管能不能匹配都保留，不能匹配的最终显示为 NULL

```py
q1 = session.query(User).outerjoin(Car).filter(User.id == Car.id)
print(q1)
```

## 联合查询
联合查询的意义:
1. 查询同一张表,但是需求不同: 如查询学生信息, 男生身高升序, 女生身高降序.
2. 多表查询: 多张表的结构是完全一样的,保存的数据(结构)也是一样的.

![orm](/postimg/orm1.jpg)

# 参考
https://docs.sqlalchemy.org/en/13/orm/query.html
https://blog.csdn.net/u011277123/article/details/54863371
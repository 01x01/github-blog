---
title: ORM
date: 2019-06-16 01:10:51
tags: flask
category: python
---
![img](https://raw.githubusercontent.com/01x01/github-blog/master/source/img/amazed.png)
# 概述
ORM (Object Relational Mapping) 意思就是将数据库表映射为代码中的对象，通过在代码中编写对象来达到操作数据库的效果。ORM有许多的好处，比如，操作数据库的代码更加的面向对象化了，在一定程度上避免了SQL注入的危险等等，在 flask 中使用 ORM需要用到 `flask-sqlalchemy` 模块

# 创建数据库

## 创建数据库

```bash
create database `flasky` default character set utf8 collate utf8_general_ci;
# 用户远程登陆
grant all privileges on *.* to '%'@'%' identified by 'qwe123' with grant option
flush privileges;
service mysqld restart
# 本地用户
use awesome;
grant select,insert,update,delete on awesome.* to 'john(user)'@'localhost' identified by 'qwe123(password)';
flush privileges;
```


## 初始化配置
驱动连接：
```python
# SQLite connection string/uri is a path to the database file - relative or absolute.
sqlite:///database.db
# MySQL
mysql+pymysql://user:password@ip:port/db_name
# Postgres
postgresql+psycopg2://user:password@ip:port/db_name
# MSSQL
mssql+pyodbc://user:password@dsn_name
# Oracle
oracle+cx_oracle://user:password@ip:port/db_name
```
配置：
```python
pipenv install flask-sqlalchmy 

# app.py
from flask_sqlalchemy import SQLAlchemy
import os
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
```


## 定义数据库表
```python
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
```
下面列举了关于数据库的字段类型

| Type name | Python type | Description |
| --- | --- | --- |
| `Integer` | `int` | Regular integer, typically 32 bits |
| `SmallInteger` | `int` | Short-range integer, typically 16 bits |
| `BigInteger` | `int` or `long` | Unlimited precision integer |
| `Float` | `float` | Floating-point number |
| `Numeric` | `decimal.Decimal` | Fixed-point number |
| `String` | `str` | Variable-length string |
| `Text` | `str` | Variable-length string, optimized for large or unbounded length |
| `Unicode` | `unicode` | Variable-length Unicode string |
| `UnicodeText` | `unicode` | Variable-length Unicode string, optimized for large or unbounded length |
| `Boolean` | `bool` | Boolean value |
| `Date` | `datetime.date` | Date value |
| `Time` | `datetime.time` | Time value |
| `DateTime` | `datetime.datetime` | Date and time value |
| `Interval` | `datetime.timedelta` | Time interval |
| `Enum` | `str` | List of string values |
| `PickleType` | Any Python object | Automatic Pickle serialization |
| `LargeBinary` | `str` | Binary blob |

然后是其属性选项

| Option name | Description |
| --- | --- |
| `primary_key` | If set to `True`, the column is the table’s primary key. |
| `unique` | If set to `True`, do not allow duplicate values for this column. |
| `index` | If set to `True`, create an index for this column, so that queries are more efficient. |
| `nullable` | If set to `True`, allow empty values for this column. If set to `False`, the column will not allow null values. |
| `default` | Define a default value for the column. |


## 操作数据库
```python
# 01 flask shell
> flask shell

# 02 创建数据库
> from main import db
> db.create_all()

# 03 插入数据
> from models import User,Role
> user = User(username="john")
> db.session.add(user)
> db.session.commit()

# 04 查询
> Role.query.all()
> User.query.filter_by(name="john").first()

# 05 删除
> db.session.delete(user_john)
```
除此之外，还有一些限制条件

| Option | Description |
| --- | --- |
| `filter()` | Returns a new query that adds an additional filter to the original query |
| `filter_by()` | Returns a new query that adds an additional equality filter to the original query |
| `limit()` | Returns a new query that limits the number of results of the original query to the given number |
| `offset()` | Returns a new query that applies an offset into the list of results of the original query |
| `order_by()` | Returns a new query that sorts the results of the original query according to the given criteria |
| `group_by()` | Returns a new query that groups the results of the original query according to the given criteria |


# 数据库关系
关系型数据库最大的特点就是表的对应关系，简单概括来说有三种：

1. 一对一
1. 一对多
1. 多对多

## 一对一关系
一对一有两种情况，一个类的一对一，比如，一个男人只能娶一个女人，这里无论男女都是人，所以属于一个类的一对一，另外一种情况就是比较常见的情况，两个类的一对一 ，比如，假设一个人只能有一辆车，那么人是一个类，车是一个类，属于两个类的一对一关系。<br />接下来首先看常见的2个类的一对一情况：
```python
class People(db.Model):
    __tablename__="people"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64))
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'))


class Car(db.Model):
    __tablename__ = "car"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    people = db.relationship('People', backref='car', lazy=True, uselist=False)

```
假设这个世界上，一个人只能有一辆车，车理所当然是登记在人的名下的，所以，我们需要在 People 里面登记 car_id， 而关系连接则写在了 Car 里面，这也很好理解，类似买了车签的合同文件，其中
```python
>> backref = 'car'
设置这个属性，可以让我们直接使用人找到车，如下面一个操作的例子
p = People(name='john')
c = Car(name='car')
p.car = c
db.session.add(p)
db.session.add(c)
db.session.commit()

我们并没有在 People 里面设置 car 属性，但是因为我们在 Car 里面设置了 backref , 所以我们可以直接
查询添加 car

>> lazy = True
这个参数使得搜索出来的数据不是一下全部 load 到内存里面，而是需要的时候才取出数据，性能会更加好

>> uselist = False
一对一的时候必须设置一个属性，否则就变成了一对多的关系了。
```
接下来看一下 `self refrence` 类型，也就是一个类之间的一对一。
```python
class People(db.Model):
    __tablename__="people"
    id = db.Column(db.Integer,primary_key=True)
    other_people_id = db.Column(db.Integer,db.ForeignKey('people.id'))
    other_people = db.relationship('People', 
                                   remote_side=id, 
                                    # 指向自己就再反转一次
                                   backref=db.backref('people',lazy=True,uselist=False),
                                   lazy=True, 
                                   uselist=False)

```
通过提示，需要增加一个 `remote_side` 的参数即可。

## 一对多关系
一对多也是同样的问题，是一对一的升级版而已，也是分为一个类和两个类的一对多关系，比如，你有很多的同学，这里 `你` 和 `同学` 都是人。先看一个类的一对多的例子
```python
class People(db.Model):
    __tablename__="people"
    id = db.Column(db.Integer,primary_key=True)
    classMate_id = db.Column(db.Integer,db.ForeignKey('people.id'))
    classMate = db.relationship('People',
                                backref=db.backref('people',
                                                   lazy=True,
                                                   remote_side=id,
                                                   uselist=True), 
                                lazy=True, 
                                uselist=True)
```
 一般来说，一对多的表示通常是将 `一` 的 id 记录到 `多` 的一边，所以 `remote_id` 需要设置在 `backref` 里面即可。<br />接下来了解常见的两个类的一对多问题，假设一个老师有多个学生，见代码：
```python
class Teacher(db.Model):
    __tablename__='teacher'
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(64))
    students = db.relationship('Student', backref='teacher', lazy=True)


class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'))
```


## 多对多关系
多对多是关系型数据库中最复杂的关系，在 `Flask` 中也是如此，我们需要以下几个步骤来创建一个多对多的关系

1. 创建中间映射表
1. 创建关系

除了上面两个步骤之外，多对多也有一个类的对应和两个类的对应。其中一个类的对应关系，很经典的就是微博的粉丝关系，一个人可以关注多个人，同时也被多个人关注，至于两个类的对应关系，就比较常见，比如，一个学生可以选修多个课程，一个课程也可以被多个学生选修。<br />先看一下一个类的多对多关系，见代码：
```python
# 多对多
# 粉丝
followers = db.Table(
    'followers',
    db.Column('follower_id', db.Integer,db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer,db.ForeignKey('user.id'))
)

class User(db.Model):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    # 偶像
    followed = db.relationship(
        'User',
        secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'),
        lazy='dynamic'
    )
```
其映射情况如下所示<br />![image.png](https://cdn.nlark.com/yuque/0/2019/png/290091/1555056649564-ebc8d52c-dc3f-4923-9887-0413f112d6fc.png#align=left&display=inline&height=61&name=image.png&originHeight=61&originWidth=197&size=1215&status=done&width=197)

接下来看以下两个类的多对多情况，如下面代码所示
```python
cate_post = db.Table(
    "cate_post",
    db.Column('cate_id',db.Integer,db.ForeignKey('category.id')),
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'))
)

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    categorys = db.relationship(
        "Category",
        secondary=cate_post,
        backref='posts',
        lazy='dynamic'
    )
class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

```
多对多的关系，我们可以在任意一方绑定关系。

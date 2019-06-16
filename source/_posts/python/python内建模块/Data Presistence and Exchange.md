---
title: Data Presistence and Exchange
date: 2019-06-16 16:10:53
tags: python内建模块
category: python
---
![img](https://raw.githubusercontent.com/01x01/github-blog/master/source/img/ants.png)
# Data Presistence and Exchange


# 概述
数据持久化和交换，涉及到几部分，一个是序列化和反序列化数据，一个是数据的存储，比如将数据存入数据库，csv等等介质中，首先了解一下什么是序列化和反序列化:
> **序列化： 当我们新建一个对象的时候，在代码运行时，会在内存中新建这个对象，但是程序结束的时候，内存就会被销毁，对象被回收。这个时候数据就消失了，为了将数据保存下来，就需要序列化技术，将程序运行时的代码数据存到磁盘**
> **反序列化：顾名思义，反序列化就是将磁盘上的数据，通过相反的路径，将之还原为代码运行时的数据。**


# pickle
pickle就是用来序列化的模块， `dumps()` 将数据序列化，见代码
```python
import pickle
pickle.dumps({"a":1,"b":2}) # b'\x80\x03}q\x00(X\x01\x00\x00\x00aq\x01K\x01X\x01\x00\x00\x00bq\x02K\x02u.'
```
序列化以后，可以使用 `loads()` 进行反序列化，见代码：
```python
pickle.loads(b'\x80\x03}q\x00(X\x01\x00\x00\x00aq\x01K\x01X\x01\x00\x00\x00bq\x02K\x02u.') # {'a': 1, 'b': 2}
```

# json
同样类似的还有 `json` 模块，`dumps()` 将python对象序列化为字符对象，也就是json对象
```python
import json
json.dumps({"a":1,"b":2}) # '{"a": 1, "b": 2}'
```
`loads()` 将字符串json 对象序列化为python 对象
```python
json.loads('{"a": 1, "b": 2}')
```

# dbm
一个 `key-value` 型的数据库，使用跟字典差不多，见代码
```python
import dbm 
# 创建
with dbm.open("example.db",'n')as db:
    db["key"] = "value"

# 写入 
with dbm.open("example.db",'w')as db:
    try:
        db["key2"] = "value2"
    except TypeError as err:
        print(err)
# 读取      
with dbm.open("example.db",'r')as db:
    for k,v in db.items():
        print(k,v)

b'key' b'value'
b'key2' b'value2'
```

# sqlite3
是一个小型数据库，其数据存储后会在本地生一个 `.db` 的文件

```python
import os
import sqlite3
db_filename = 'todo.db'
schema_filename = 'todo_schema.sql'
db_is_new = not os.path.exists(db_filename)
with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print('Creating schema')
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)
        print('Inserting initial data')
        conn.executescript("""
                insert into project (name, description, deadline)
                values ('pymotw', 'Python Module of the Week',
                        '2016-11-01');
                insert into task (details, status, deadline, project)
                values ('write about select', 'done', '2016-04-25',
        'pymotw');
                insert into task (details, status, deadline, project)
                values ('write about random', 'waiting', '2016-08-22',
        'pymotw');
                insert into task (details, status, deadline, project)
                values ('write about sqlite3', 'active', '2017-07-31',
                'pymotw');
         print('Database exists, assume schema does, too.')
        """) 
        else:
          print("Database Exists!")
 
```



# xml.etree

## 解析文档

```python
from xml.etree import ElementTree
with open("podcasts.opml",'rt') as f:
    tree = ElementTree.parse(f)
    
print(tree)
```

## 标签
```python
for node in tree.iter():
    print(node.tag)
```

## 取值
```python
for node in tree.iter('outline'):
    name = node.attrib.get("text")
    url = node.attrib.get('xmlUrl')
    if name and url:
        print(name,":",url)
```


# CSV
CSV一般最常用的就是两个功能，一个是写入，一个读取。写入：
```python
import csv
with open("csvtest.csv",'wt')as f:
    writer = csv.writer(f)
    writer.writerow(
        (
            "title1",
            "title2",
            "title3",
            "title4"
        )
    )
    for i in range(3):
        row = (
            i+1,
            chr(ord('a')+i),
            "08/{:2d}/07".format(i*10+ 1),
            "Hello"
        )
        writer.writerow(row)

```
读取

```python
with open("csvtest.csv",'rt')as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```


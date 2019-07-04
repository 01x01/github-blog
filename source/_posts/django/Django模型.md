---
title: Django模型
date: 2019-07-02 16:15:21
tags: 
category: django
---
记录 Django 模型的使用
<!-- more -->
Django模型层是 Django 自己定义的一套独特的 ORM 技术，将代码中的类映射成数据库中的表，属性映射为数据字段，除此之外，主键，外键，约束，关系等等都是通过类的属性定义完成

# 基本概念
1. Django 模型继承自 `django.db.models.Model` 类
2. 模型字段必须是 `xxxField` 类型
3. Meta 子类定义模型的元数据，比如数据库表名，数据默认排序等等

# 常见的 Meta 属性
属性 | 值 | 含义
---|---|---
abstract | True or False | 表示这个类是否为抽象类
app_label | string | 定义这个类所属的应用，比如 app_label = 'app1'
db_table | string | 定义表名，否则 django 将自动生成表名： <应用名>_<数据库类名>
ordering | list | 定义数据的排序方式， 如` ordering: ['pub_date'] `,默认是降序排列，如果要升序排列，可以如 `ordering:[-'pub_date']`
unique_together | tuple | 用来设置不重复字段的组合，如： `unique_together=(("username","pub_date"),)` 每个 username 在 同一个 pub_date 中只能有一条数据，也就是说 pub_date 可以多条相同，但是相同的对应的 username 不能一样。
verbose_name | string | 指明一个易于理解和表述的单数形式的对象名称
verbose_name_plural|string| 指明一个易于理解和表述的复数形式的对象名称

# 常见的数据库表字段
字段 | 含义
---| ---
AutoField | 主键，自动递增的整型字段
BigIntegerField | 64位整型字段
BinaryField | 二进制数据字段，只能通过 byte 进行赋值
BooleanField | 布尔字段
CharField | 字符串字段
TextField | 大容量字符字段
DateField | 日期字段，属性 auto_add: 当字段被保存的时候，添加时间， auto_add_now 创建对象的时候，添加时间。
DatetTimeField | 类似上面的字段，但是同时支持时间的输入，属于常用的字段
EmailField | CharField 类型，但是带有邮箱合法性验证
FileField | 文件上传字段，参数 upload_to 路径必须包含时间，如： ` models.FileField(upload_to='documents/%Y/%m/%d')`
ImageField| 图片上传字段，需要 height_field 和 width_field 两个参数，需要 Imaging 库
FloatField| 浮点数字段
IntegerField| 整数字段
IPAdressField| IP 地址
NullBooleanField| 布尔字段，只是多了一个 None 选项
PhoneNumberField| 电话号码字段
SlugField| 通常用于 url 的 slug 字段
URLField| url 字段
XMLField | XML 字符字段

#  
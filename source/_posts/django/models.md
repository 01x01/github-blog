---
title: models
date: 2019-07-15 16:06:05
tags: 
category: django
---
<!-- more -->
# 基础概念
1. 所有的 model 都是 `django.db.models.Model` 的子类
2. 所有 model 的属性都表示为数据库的字段

# 如何使用 models
1. 告诉 django
```py
# 在 setting.py 里面配置
INSTALLED_APPS = [
    ...
    'polls.apps.PollsConfig'
]
```
2. 运行相关语句
```
python manage.py makemigrations
python manage.py migrate 
```
django 内部自己实现了数据库的版本管理。

# Fields
1. Field 类型决定了数据库表字段的类型
2. Field 类型决定了 html 渲染表单时候的类型
3. 所有的 Field type ： https://docs.djangoproject.com/en/2.2/ref/models/fields/
4. Field 属性： https://docs.djangoproject.com/en/2.2/ref/models/fields/#common-model-field-options
5. verbose_name： 当字段显示在 admin 后台，其显示名称为此名称，增强字段的可读性

# 数据库关系
## 一对一
在 Django中使用 `OneToOneField` 字段来定义一对一关系。如下所示
```python
class Account(models.Model):
	username = models.CharField(max_length=100)

class Contact(models.Model):
	account = models.OneToOneField(
		Account,
		on_delete = models.CASCADE
	)
```
`on_delete = models.CASCADE` 表示其中一张表的数据被删除时，另一张表所对应的数据也会被删除。

## 一对多

一对多的关系一般使用 `ForeignKey` 来定义
```python
from django.db import models

class Manufacturer(models.Model):
    # ...
    pass

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
	...

```
当一对多的对象是对象本身时，可以使用下面的语法表示一对多
```python
models.ForeignKey('self', on_delete=models.CASCADE).
```

## 多对多
多对多的关系一般使用 ManyToManyField 来定义，比起 Flask 来说简单了不少。
```python
from django.db import models

class Topping(models.Model):
    # ...
    pass

class Pizza(models.Model):
    # ...
    toppings = models.ManyToManyField(Topping)
```
## 一对多/多对多操作
当两个对象的关系是多对多的时候，需要使用 `add` 来进行添加
```python
>>> john = Author.objects.create(name="John")
>>> paul = Author.objects.create(name="Paul")
>>> george = Author.objects.create(name="George")
>>> ringo = Author.objects.create(name="Ringo")
>>> entry.authors.add(john, paul, george, ringo)
```


# related
1. django 数据库版本管理操作

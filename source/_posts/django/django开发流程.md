---
title: django tutorial
date: 2019-07-02 14:36:27
tags: 
category: Django
---
<!-- more -->
---
title: django的开发流程
date: 2019-07-02 14:36:27
tags: 
category: Django
---
django 的开发流程
<!-- more -->
# 初始化
## 安装
```py
python -m venv venv 
.\venv\Scripts\activate
pip install Django, mysqlclient 
pip freeze > requirements.txt
```

## 创建应用
```py
django-admin startproject tutorial
```

## 创建 app
```py
django-admin startapp app
```

# 路由

1. 在 `app` 下面新建 `urls.py`
2. 添加路由
```py
# coding: utf-8 
from django.urls import path 
from . import views 
urlpattern = [
	path("index", views.welcome, name='welcome')
]
```
3. 配置全局路由
```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app.urls')),
    path('admin/', admin.site.urls),
]
```
4. 测试
```py
# app/views.py
from django.http import HttpResponse
# Create your views here.
def welcome(request):
    return HttpResponse("Hello, world. You're at the polls index.") 
```
然后运行
```shell
python manage.py runserver <host>:<port>
```
# 模型
1. 数据库配置 

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'comments',
        'USER': 'root',
        'PASSWORD': 'qwe123',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
# 内置的 Engine 类型有：
'django.db.backends.postgresql'
'django.db.backends.mysql'
'django.db.backends.sqlite3'
'django.db.backends.oracle
```
一些更高级的配置可参考： https://docs.djangoproject.com/en/2.2/ref/databases/ 

2. 配置 `INSTALL_APPS`

```py
INSTALLED_APPS = [
    ...
    'app.apps.AppConfig'
]
```
3. 定义模型
```py
from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
       return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
```
4. 迁移数据库
```py
python manage.py makemigrations app
pytohn manage.py migrate 
```
5. 测试
```shell
python manage.py shell
```

# Admin 后台
```shell
python manage.py createsuperuser
```
打开 `http://127.0.0.1:8000/admin`

# 视图
```python
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```

# 备忘
1. path 的用法？ 路由的规则？
2. models 的定义？ORM 数据库的关系，操作，关键字？
3. 如何自定义后台？样式自定义？类自定义？
4. 即插视图，函数视图？模板渲染？css? js?
5. 表单对象
6. RestfulAPI 
7. 持续集成（部署/单元测试/自动化测试）

# 参考
https://docs.djangoproject.com/en/2.2/intro/





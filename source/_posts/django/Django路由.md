---
title: Django路由
date: 2019-07-02 16:14:38
tags: 
category: django
---
URL 调度器

<!-- more -->

一个高质量的 web 应用，使用简单，优雅的 URL 模式是一个非常重要的细节。Django 提供了一个 URLconf 模块来实现 python 代码和 url 的映射。Django 如何处理一个请求？

1. 首先 Django 会先去寻找 URLconf 设置，一般存在于 `setting.py` 文件中，但是如果进来的 `HttpRequest` 又 urlconf 这个属性，则这个属性会替代 `setting.py` 里面的设置
2. 然后 Django 会去加载响应的 python 模块，寻找 `urlpatterns` 变量，这个变量里面必须要有 `path` 和 `re_path` 的实例
3. 遍历这些 url ，最后找到对应的视图函数
4. 这个视图函数会接收到一个参数 `request` , 是 HttpRequest 的实例
5. 如果没有找到对应的视图函数，返回错误处理

# url 转换
Django 的url 转换包含以下几个部分
1. str： 一个纯粹的字符串，不包含 "/" 比如：`path(r'teststr',views.teststr)` 请求的 url 为 : `http://example.com/teststr`
2. int:  一个数字，比如 `path('article/<int:year>',views.year_archive)` 请求的 url 为 `http://example.com/article/2013`,视图函数还要多加一个 year 参数，为： `views.year_archive(request, year=2005).`
3. slug: 解释字符，类似于 `building-your-1st-django-site` 这个样子，比如： `/articles/2003/03/building-a-django-site/ `  请求的视图函数为： `views.article_detail(request, year=2003, month=3, slug="building-a-django-site").`
4. uuid: 类似于 ` 075194d3-6885-417e-a8a8-6c931e272f00`
5. path: 包含 '/' 的字符串，比如 "https://www.example.com/teststr/"

# 注册 URL 转换器和正则表达式
很多场景下会使用到动态的 url，这个时候就需要用到正则表达式来匹配 url 规则。比如，文章归类的 url 为 `article/<int:year>` 这里的 `year` 通常会传递四位数，比如 2019，那么构造的 url 就为 `article/2019`.如果这个时候，需要的 url 为 `article/19` 呢？ 这个时候，就需要使用到正则表达式。比如：
```py
urlpatterns = [
    re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
    re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-_]+)/$', views.article_detail),
]
```
`?P<year>` 指的是以 `year` 为参数，然后加上正则，表示这个参数的值需要匹配这个正则表达式。

除此之外，还有另外的做法。比如说
```py
class FourDigitYearConverter:
	regex = '[0-9]{4}'

	def to_python(self,value):
		return int(value)

	def to_url(self,value):
		return "%04d"%value
```
* `to_python` 的意思是说，将这个可变参数传递给视图函数的时候，转换成 int 类型。
* `to_url` 的意思是说，当这个可变参数在 url 里面的时候，转为 str 类型

接着需要进行注册
```py
from django.urls import path, register_converter

from . import converters, views

register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('articles/2003/', views.special_case_2003),
    path('articles/<yyyy:year>/', views.year_archive),
    ...
]
```
注册了一个 `yyyy` 变量，便可以直接使用这个变量了, 好处就是可以做到代码复用，不用每个 url 写一个正则。

# 包含关系
一个项目往往可以分成多个独立的模块，其路由也可以分开维护，最后在总的设置里面包含进来即可
```
from django.urls import include, path

urlpatterns = [
    # ... snip ...
    path('community/', include('aggregator.urls')),
    path('contact/', include('contact.urls')),
    # ... snip ...
]
```

# URL 的反向解析
反向解析有三种方式：
1. 对于 python 使用 `reverse(name,args=(xxx,))`
2. 对于 templates 使用 `url 'xxx' args`
3. 对于 module 使用 `get_absolute_url()` 

如：
```python
# python
def redirect_to_year(request):
    # ...
    year = 2006
    # ...
    return HttpResponseRedirect(reverse('news-year-archive', args=(year,)))

# template
urlpatterns = [
    #...
    path('articles/<int:year>/', views.year_archive, name='news-year-archive'),
    #...
]
<li><a href="{% url 'news-year-archive' yearvar %}">{{ yearvar }} Archive</a></li>

# models
def get_absolute_url(self):
    from django.urls import reverse
    return reverse('people.views.details', args=[str(self.id)])
```

# url 的命名空间
假设有两个应用 app1 和 app2

```python
# app1
urlpatterns = [
	path('',views.index, name='index')
]

# app2
urlpatterns = [
	path('',views.index,name='index')
]

# setting
urlpatterns = [
	path('app1/', include('app1.urls')),
	path('app2/',include('app2.urls'))
]
```

如果有一个 app3 要跳转到 app1 的 index 视图函数，直接 `reverse('index')` 肯定是行不通的。这个时候就需要命名空间 

```py
# app1

app_name = 'app1'
urlpatterns = [
	path('',views.index, name='index')
]
```
使用的时候
```py
reverse('app1:index')
```

# 参考
https://docs.djangoproject.com/zh-hans/2.2/topics/http/urls/
---
title: Django表单
date: 2019-07-02 16:16:24
tags: 
category: django
---
Django 表单使用
<!-- more -->
Django 表单使用分为三步：
1. 创建表单对象
2. 创建 HTML 渲染
3. 视图

# 创建表单对象
```py
>>> class CommentForm(forms.Form):
...     url = forms.URLField()
...     comment = forms.CharField()

```
## 常见的 Field 

属性名| 含义
---|---
BooleanField |
CharField |
ChoiceField |
TypedChoiceField |
DateField |
DateTimeField |
DecimalField |
DurationField |
EmailField |
FileField |
FilePathField |
FloatField |
ImageField |
IntegerField |
GenericIPAddressField |
MultipleChoiceField |
TypedMultipleChoiceField |
NullBooleanField |
RegexField |
SlugField |
TimeField | 
URLField |
UUIDField |

参考： https://docs.djangoproject.com/en/2.2/ref/forms/fields/#django.forms.Field 



# HTML 模板

# 视图处理函数


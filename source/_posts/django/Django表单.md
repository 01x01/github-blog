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

# 流程
```py
# forms.py
from django import forms

class TestForm(forms.Form):
    name = forms.CharField(max_length=20)

# templates
<html>
    <head>
        <meta charset='utf-8'>
    </head>
    <body>

    <form>
        {% csrf_token %}
        {{ form }}
    </form>
    </body>
</html>

# views.py
def testform(request):
    if request.method == "POST":
        form = TestForm(request.POST)
        if form.is_valid():
            return HttpResponse("Hello {}".format(form.cleaned_data['name']))
    else:
        form= TestForm()

    return render(request,"polls/testform.html",{'form':form})

# urls.py
urlpatterns = [
    path('testform',views.testform, name='testform')
]

```
# 常见的 Field 

```
Field
    required=True,               是否允许为空
    widget=None,                 HTML插件
    label=None,                  用于生成Label标签或显示内容
    initial=None,                初始值
    help_text='',                帮助信息(在标签旁边显示)
    error_messages=None,         错误信息 {'required': '不能为空', 'invalid': '格式错误'}
    show_hidden_initial=False,   是否在当前插件后面再加一个隐藏的且具有默认值的插件（可用于检验两次输入是否一直）
    validators=[],               自定义验证规则
    localize=False,              是否支持本地化
    disabled=False,              是否可以编辑
    label_suffix=None            Label内容后缀  
    
CharField(Field)
    max_length=None,             最大长度
    min_length=None,             最小长度
    strip=True                   是否移除用户输入空白 
IntegerField(Field)
    max_value=None,              最大值
    min_value=None,              最小值 
FloatField(IntegerField)
    ... 
DecimalField(IntegerField)
    max_value=None,              最大值
    min_value=None,              最小值
    max_digits=None,             总长度
    decimal_places=None,         小数位长度
BaseTemporalField(Field)
    input_formats=None          时间格式化    
DateField(BaseTemporalField)    格式：2015-09-01
TimeField(BaseTemporalField)    格式：11:12
DateTimeField(BaseTemporalField)格式：2015-09-01 11:12 
DurationField(Field)            时间间隔：%d %H:%M:%S.%f
    ... 
RegexField(CharField)
    regex,                      自定制正则表达式
    max_length=None,            最大长度
    min_length=None,            最小长度
    error_message=None,         忽略，错误信息使用 error_messages={'invalid': '...'} 
EmailField(CharField)      
    ...
FileField(Field)
    allow_empty_file=False     是否允许空文件 
ImageField(FileField)          ...
    注：需要PIL模块，pip3 install Pillow
    以上两个字典使用时，需要注意两点：
        - form表单中 enctype="multipart/form-data"
        - view函数中 obj = MyForm(request.POST, request.FILES) 
URLField(Field)
    ... 
BooleanField(Field)  
    ... 
NullBooleanField(BooleanField)
    ... 
ChoiceField(Field)
    ...
    choices=(),                选项，如：choices = ((0,'上海'),(1,'北京'),)
    required=True,             是否必填
    widget=None,               插件，默认select插件
    label=None,                Label内容
    initial=None,              初始值
    help_text='',              帮助提示
ModelChoiceField(ChoiceField)
    ...                        django.forms.models.ModelChoiceField
    queryset,                  # 查询数据库中的数据
    empty_label="---------",   # 默认空显示内容
    to_field_name=None,        # HTML中value的值对应的字段
    limit_choices_to=None      # ModelForm中对queryset二次筛选     
ModelMultipleChoiceField(ModelChoiceField)
    ...                        django.forms.models.ModelMultipleChoiceField     
TypedChoiceField(ChoiceField)
    coerce = lambda val: val   对选中的值进行一次转换
    empty_value= ''            空值的默认值 
MultipleChoiceField(ChoiceField)
    ... 
TypedMultipleChoiceField(MultipleChoiceField)
    coerce = lambda val: val   对选中的每一个值进行一次转换
    empty_value= ''            空值的默认值 
ComboField(Field)
    fields=()                  使用多个验证，如下：即验证最大长度20，又验证邮箱格式
                               fields.ComboField(fields=[fields.CharField(max_length=20), fields.EmailField(),]) 
MultiValueField(Field)
    PS: 抽象类，子类中可以实现聚合多个字典去匹配一个值，要配合MultiWidget使用 
SplitDateTimeField(MultiValueField)
    input_date_formats=None,   格式列表：['%Y--%m--%d', '%m%d/%Y', '%m/%d/%y']
    input_time_formats=None    格式列表：['%H:%M:%S', '%H:%M:%S.%f', '%H:%M'] 
FilePathField(ChoiceField)     文件选项，目录下文件显示在页面中
    path,                      文件夹路径
    match=None,                正则匹配
    recursive=False,           递归下面的文件夹
    allow_files=True,          允许文件
    allow_folders=False,       允许文件夹
    required=True,
    widget=None,
    label=None,
    initial=None,
    help_text='' 
GenericIPAddressField
    protocol='both',           both,ipv4,ipv6支持的IP格式
    unpack_ipv4=False          解析ipv4地址，如果是::ffff:192.0.2.1时候，可解析为192.0.2.1， PS：protocol必须为both才能启用 
SlugField(CharField)           数字，字母，下划线，减号（连字符）
    ... 
UUIDField(CharField)           uuid类型
    ...

# regexp 有两种方法：
# 第一种使用 validator

from django.core.validators import RegexValidator


class FooBar(models.Model):
    username_validator = RegexValidator(r'^[\w.@ +-]+$', 
                                        "This value may contain only letters, "
                                        "numbers and @/./+/-/_ characters
    username = models.CharField(max_length=200, validators=[username_validator])

```
# 第二种
```
import re

regex = re.compile('^[\w.@ +-]+$',re.UNICODE)

class Myclass(models.Model):

     username = forms.RegexField(max_length=50,regex=regex,
            help_text=_("Required. 50 characters or fewer. Letters, digits and "
                          "@/./+/-/_ only."),
```


参考： https://docs.djangoproject.com/en/2.2/ref/forms/fields/#django.forms.Field 

# HTML 模板
## 快捷渲染
```
{{ form.as_table }} will render them as table cells wrapped in <tr> tags
{{ form.as_p }} will render them wrapped in <p> tags
{{ form.as_ul }} will render them wrapped in <li> tags
```
## 自定义渲染
```
<div class="fieldWrapper">
    {{ form.subject.errors }}
    <label for="{{ form.subject.id_for_label }}">Email subject:</label>
    {{ form.subject }}
</div>
```

# 视图处理函数

1. `cleanded_data`： 用来取得 forms 表单的值
2. `forms.is_valid()`: 用来验证表单数据是否合法

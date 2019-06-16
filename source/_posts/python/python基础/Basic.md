---
title: python基础
date: 2019-06-16 01:10:51
tags: python基础
category: python
---
# 概述
Python是一门计算机程序设计的语言，语法优雅，是目前很火热的一门编程语言，<br />其优点有：

1. 语法简单，容易上手
2. 软件生态丰富，方方面面都有相应的框架
2. 其缺点也是很明显，就是运行效率，python的底层是C语言写的，所以运行的效率相对于C或者C++，Java这样的编程语言来讲，运行效率会低一些，一样的算法时间复杂度，python运行要多几毫秒


# 安装python

windows 直接下载exe文件进行安装即可，在 *unix 系统上，其选择方式却较多，可以只用 pyenv 来管理python的版本

```shell
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
$ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
#zsh note: Modify your ~/.zshenv file instead of ~/.bash_profile.
#fish note: Use pyenv init - | source instead of eval (pyenv init -).
#Ubuntu and Fedora note: Modify your ~/.bashrc file instead of ~/.bash_profile.
$ exec "$SHELL"
```

[https://github.com/pyenv/pyenv#installation](https://github.com/pyenv/pyenv#installation)


# 设置pip源

对于不同的操作系统，有不同的配置的地方：

1. Windows 环境在 `C:\Users\<your-name>\pip` 新建pip.ini
2. *unix 环境,  在`/Users/anonymous/.pip` 新建 pip.conf

```ini
# pip.ini
[global]
trusted-host =  mirrors.aliyun.com
index-url = http://mirrors.aliyun.com/pypi/simple
```


# 设置虚拟开发环境

设置虚拟环境的目的在于区分不同版本的依赖，甚至是python环境，目前流行的有两种方式：

1. 使用venv模块
2. 使用pipenv 模块


## 使用venv 模块

在开发项目下直接运行

```shell
python -m venv venv 
# Windows 激活虚拟环境
.\venv\Script\activate
# mac
source venv/bin/activate
```


## 使用 pipenv 模块

```ini
# 全局安装pipenv
pip install pipenv 
# 初始化项目
mkdir <your-project-name>
cd <your-project-name>
# 创建pipfile 和pipfile.lock, 如果已经存在的话，会安装项目工程依赖，不安装工具依赖
pipenv install 
# 安装项目工程依赖
pipenv install requests 
# 安装项目工具依赖
pipenv install pytest --dev
# 导出为requirements.txt. 只导出项目工程依赖
pipenv lock -r
# 项目工具依赖导出
pipenv lock -r -d
# 进入虚拟环境
pipenv shell
# 退出
exit
# 在初始化的时候可以指定python版本,会自动寻找系统安装的python版本
pipenv --python 3.6 
pipenv --python 2.7.14 
# 为每个项目设置源
[[source]]
name = "pypi"
url = "http://mirrors.aliyun.com/pypi/simple" # 设置为阿里云
verify_ssl = true
[dev-packages]
pytest = "*"
[packages]
requests = "*"
[requires]
python_version = "3.6"
其他需要了解的点
# 项目虚拟环境位置
C:\project\simpleDestops>pipenv --venv
C:\Users\xxx\.virtualenvs\simpleDestops-YxQtYgkl
```


# list列表

```python
classmate = ['johnw',"jack","tom","michael"]
# 弹出列表末尾元素: michael
p = classmate.pop() 
print("pop 返回： ",p)
print("pop 后列表为： ",classmate)
# 末尾元素添加
p1 = classmate.append("mary")
print("append 返回: ",p1)
print("append 后列表为： ",classmate)
# copy 列表
p3 = classmate.copy()
print("copy 返回: ",p3)
print("copy 后列表为： ",classmate)
# count 返回列表某元素的个数
p4 = classmate.count('johnw')
print("count 返回: ",p4)
print("count 后列表为： ",classmate)
# index 寻找元素的索引
p5 = classmate.index("jack",1)
print("index 返回: ",p5)
# remove 元素
p6 = classmate.remove("johnw")
print("p6 返回： ",p6)
print("remove 后列表为： ",classmate)
# reverse 和 sort
a1 = [2,3,51,4,6,2,7,8]
a1.sort()
print("sort 后 a1 为：",a1)
a1.reverse()
print("reverse 后 a1 为: ",a1)
# 清除列表元素
p2 = classmate.clear()
print("clear 返回: ",p2)
print("clear 后列表为： ",classmate)
```


# 字典 dict

字典也是python中常用的数据结构，主要掌握记住几种操作：


## 插入值

```python
test = {} 
test["Hello"] = "world"
```


## 查找

```python
test.get("Hello") 
test["Hello"]
```


## 键值循环

```python
for key,value in test.items():
    print("key===>",key)
    print("value===>",value)
```


## 键循环

```python
for key in test.keys():
    print("key: ,key)
```


## 值循环

```python
for value in test.values():
     print("value: ",value)
```


## 键值更新

```python
>>> a={"a":1,"b":2}
>>> a.update({"c":3})
>>> a
{'a': 1, 'b': 2, 'c': 3}
```


# 函数

Python中函数的参数有四种，分别是：

1. 位置参数
2. 默认参数
3. 可变参数
4. 关键字参数
4. python 按照参数的位置来区别参数，位置参数的优先级是最高的，其次分别是默认参数，可变参数，关键字参数

```python
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
```

可变参数将传入的参数包装成一个tuple，关键字参数将传入的参数包装成一个dict，因此在函数中使用这些参数的时候，可以使用 `args` 或者 `kw` 这样的关键字来使用其中的值，因为在函数声明的时候，是以这两个关键字声明的。


# 高阶函数

下面几个函数在大多数编程语言里面都有，属于高阶函数，它们接受函数作为其中的参数：

1. map
2. reduce
3. filter
4. sorted
4. 涉及到两个概念：`Iterable` 和 `Iterator`
4. `Iterator` : 惰性的, 不会一次性将大量的数据带到内存里面计算，只有用到的时候才会去计算取得值
4. `Iterable`: 一次把所有的数据全部带到内存里面，其中list，dict，tuple 都是Iterable 而不是 Iterator


## map

map()函数接收两个参数，一个是函数，一个是`Iterable`，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

```python
>>> def f(x):
...     return x*x
... 
>>> map(f,[1,2,3,4])
<map object at 0x10cd20a58>
>>> a = map(f,[2,3,4])
>>> a
<map object at 0x10cccd400>
>>> next(a)
4
>>> next(a)
9
>>> next(a)
16
```


## reduce

reduce 把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算

```python
>>> from functools import reduce
>>> reduce(add,[1,2,3,4])
10
```


## filter

ilter 也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素

```python
>>> def big_then_six(x):
...     if x > 6 :
...         return True
...     return False
... 
>>> filter(big_then_six,[1,2,3,4,5,6,7,8,9,10])
<filter object at 0x10ccaa208>
```


## sorted

sorted 函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序

```python
>>> L=[('b',2),('a',1),('c',3),('d',4)]
>>> sorted(L, cmp=lambda x,y:cmp(x[1],y[1]))   # 利用cmp函数
[('a', 1), ('b', 2), ('c', 3), ('d', 4)]
>>> sorted(L, key=lambda x:x[1])               # 利用key
[('a', 1), ('b', 2), ('c', 3), ('d', 4)]
>>> sorted(students, key=lambda s: s[2], reverse=True)       # 按降序
[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
```


# 匿名函数

```python
>>> list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
[1, 4, 9, 16, 25, 36, 49, 64, 81]
```


# 装饰器

```python
#coding:utf-8
import functools
cert = {
    "username":"test",
    "password":"qwe123"
}
def authentication(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        if cert["username"] == "test" and cert["password"] == "qwe123":
            return func(*args,**kw)
        else:
            print("auth failed")
    return wrapper
@authentication
def user_profile():
    print("Hello Here is user profile")
if __name__ == "__main__":
    user_profile()
```


# 面向对象

Python面对对象的实现，采用的是“鸭子模型”的方式，什么是鸭子模型，一个动物，只要它叫声像鸭子，走路像鸭子，行为举止动作思想等等方面像鸭子，那么在python里面，就说明这是一只鸭子。 怎么理解呢？ 比如说，Iterator 对象是因为内部有一个**iter**方法，所以才被称之为Iterator 对象，所以在python里面，只要声明一个对象，并且实现了**iter** 方法，那么声明的这个对象就是 Iterator 对象。


## 声明对象

```python
class Student(object):
    # 构造函数，创建实例需要用到
    def __init__(self):
        pass
```


## 访问限制

封装性是面向对象的一大特点，如果要内部属性不被外部调用，需要加上 __ 两个下划线

```python
class Student(object):
     def __init__(self,name):
         self.__name = name
```

这样就没办法直接通过实例来访问这个变量了

```python
>>> bart = Student('Bart Simpson')
>>> bart.__name
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute '__name'
```

因为这个时候，`__name` 变量已经被隐式的变成了 `_Student__name`


## 继承

继承的一般写法为：

```python
class Animal(object):
    pass
class Cat(Animal):
    pass
```

所有的类都继承于 object 这个类。所要注意的是，在继承父类的时候，也会同时继承其构造函数，但是如果要给子类添加一些新的属性时候要怎么办？ 比如说父类是一个比较模糊的名词，Animal，创建的实例Cat要有一个名字 name，这个时候，name就是子类新的属性。例子：

```python
class Animal(object):
    def __init__(self,feather):
        self.feather = feather
    # 是否有羽毛
    def is_feather(self):
        return self.feather
class Bird(Animal):
    def __init__(self,name,age,*args,**kw):
        self.name = name
        self.age = age
        super(Bird,self).__init__(*args,**kw)
    
    def is_feather(self):
        return self.feather
```


## 使用**slots**

使用 **slots** 可以 限制类的实例赋值，比如，要限制 Student 的实例，只能添加 name 和 age 两个属性，其他的不允许,就可以这么做:

```python
# coding: utf-8 
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
    def __init__(self):
        pass
   
if __name__ =="__main__":
    s = Student()
    s.scope = 100
# 输出：  AttributeError: 'Student' object has no attribute 'scope'
```


## [property ]()

这个属性主要是针对对象的封装性的，对象的属性一般是不应该通过实例直接来设置，一般还需要设置 get 和 set 方法。 [property ]() 就是这么来使用的。例子

```python
class Student(object):
    @property
    def score(self):
        return self._score
        
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
```

# 文件读写

文件读写有几种方式，一种是使用 `with` 写法，一种是打开文件的做法

## with
读取文件
```python
with open('test.txt','r',encoding='utf-8') as f:
  f.read()
```
写入文件 
```python
with open('test.txt','w',encoding='utf-8')as f:
  f.write('hello')
  
# 追加形式写入文件
with open('test.txt','a',encoding='utf-8')as f:
  f.write('Hello.world')
```


## 打开文件
一般如果我们要持续写入文件内容，这个时候不需要每一次打开立马关闭，可以使用如下的做法：
```python
f = open("test.txt",'w')
for r in result:
  f.write(r)
f.close()
```


## Tips
如果在打开文件的时候，遇到个别字符的编码错误，不影响大局的情况下,可以忽略错误，使用如下做法
```python
with open("Log201904.txt",'r',errors='ignore')as f:
    content = f.read()
```


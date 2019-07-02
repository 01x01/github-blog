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


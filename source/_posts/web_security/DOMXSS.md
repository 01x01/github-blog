---
title: DOM XSS
date: 2019-07-01 16:42:24
tags: 
category: websec
---
DOM XSS 介绍
<!-- more -->
# 区别
DOM XSS 属于反射型 XSS 的一种，跟正常的反射型 XSS区别在于：

1. 其操作的是浏览器 DOM 环境
1. 利用的是客户端的环境，也就是说反射型 XSS 是作为网页返回的一部分，但是 DOM XSS 并不是网页返回的一部分，而是因为开发的失误，在客户端基于用户输入构造了 DOM 结构，从而造成了 xss 漏洞
1. 传统的 xss 是因为服务器返回的内容含有非法的脚本，在页面加载的时候执行，所以这个时候浏览器能够解析得知漏洞，并基于黑名单过滤，而 DOM XSS 不一样，它是基于合法的脚本，因为在客户端错误处理了用户的输入，所以造成的漏洞，是在页面加载后的一段时间内构造完成的，浏览器无法拦截


# 演示
安装 juice soup
```
docker pull bkimminich/juice-shop
docker run --rm -p 3000:3000 bkimminich/juice-shop 
打开 http://127.0.0.1:3000
```

在搜索栏键入 `<img src="#" onerror=alert(1)>` 
![image.png](https://cdn.nlark.com/yuque/0/2019/png/290091/1557327306632-d989f2be-9d81-4f81-bde3-c574644c936d.png#align=left&display=inline&height=361&name=image.png&originHeight=722&originWidth=2488&size=303238&status=done&width=1244)

查看源代码，可以看到搜索页面返回的 html  并没有含有相关的 js 代码，说明这是一个 DOM 型的 XSS


# 参考
[https://www.4hou.com/technology/12234.html](https://www.4hou.com/technology/12234.html) 
[http://qingbob.com/Excess-XSS/](http://qingbob.com/Excess-XSS/) 

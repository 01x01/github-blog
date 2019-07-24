---
title: apache httpd 小结
date: 2019-07-24 23:27:24
tags: 
category: websec
---
<!-- more -->
# 安装
```shell
# Fedora/CentOS/Red Hat Enterprise Linux
sudo yum install httpd
sudo systemctl enable httpd
sudo systemctl start httpd

# Ubuntu/Debian
sudo apt install apache2
sudo service apache2 start
```

# 配置文件语法
## 基本语法
1. 每一行代表一个指令，如果需要写到下一行，就需要在末尾加上 `\`
2. 配置文件之间使用空格进行隔开 `key value`
3. 使用 `#` 作为注释
4. 指令在配置文件中大小写不敏感，但是指令的参数是大小写敏感的
5. 可以使用 `${var}` 来取得系统环境变量，也可以自己在配置环境中定义环境变量，只要使用 `<IfDefine variable></IfDefine>`

## 模块
apache 可以动态启用模块来实现功能，所以对于模块的配置可以使用 `<IfModule>` 来进行定义，如
```conf
<IfModule log_config_module>
    ...
    LogFormat "%a %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"" combined
    LogFormat "%h %l %u %t \"%r\" %>s %b" common

    <IfModule logio_module>
      # You need to enable mod_logio.c to use %I and %O
      LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\" %I %O" combinedio
    </IfModule>

    ...
    CustomLog "/var/log/httpd/access_log" common

    ...
</IfModule>
```
## 指令的作用范围
如果指令是声明在全局的配置文件中，那么就是范围就是全局，如果想作用在局部的范围之中，可以使用如下几个指令
```
<Directory>
<DirectoryMatch>
<Files>
<FilesMatch>
<Location>
<LocationMatch>
<VirtualHost>
```
# 配置文件
## 容器
配置文件中有两种基本的容器，一种是作用于全部的请求，一种是只作用于满足条件的请求。` <IfDefine>, <IfModule>, <IfVersion>`三个容器命令只作用于服务启动或者称其的时候，如果条件为真，则里面的指令应用于所有的请求，如果条件为否，则忽略

## 文件系统，webspace和真假表达式
首先要明确文件系统和 webspace 的区别：
> 文件系统指的是操作系统上具体的文件路径，而 webspace 则指的是网站的相对路径，如文件系统指的是 `/var/web/dir1`,而 webspace 中 `/dir2` 则会指向 `/usr/local/apache2/htdoc/dir2`

文件系统的配置
```conf
<Directory "/var/web/dir1">
    <Files "private.html">
        Require all denied
    </Files>
</Directory>
```
webspace 的配置
```conf
<LocationMatch "^/private">
    Require all denied
</LocationMatch>

<Location "/foo">
</Location> 
```



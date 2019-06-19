---
title: httpd文档
date: 2019-06-19 14:36:44
tags: httpd
category: apache-httpd
---
To Be Continue...


# 关键字： httpd，httpd conf
# 概述
Apache httpd 是世界上流行的 http 服务器，简单记录一下对官方文档的理解。
httpd 的配置文件为 `httpd.conf` 通常情况下，这个文件会存储一些公用的配置，对于站点会新建一份 conf 文件来进行配置。最后再通过 `Include` 命令在 `httpd.conf` 中进行引入。

# 安装
## 源码安装

## yum 安装

## httpd.service
```conf
[Unit]
Description=The Apache HTTP Server
After=network.target remote-fs.target nss-lookup.target
Documentation=man:httpd(8)
Documentation=man:apachectl(8)

[Service]
Type=forking
ExecStart=/usr/local/apache/bin/apachectl start
ExecReload=/usr/local/apache/bin/apachectl graceful
ExecStop=/bin/kill -WINCH ${MAINPID}
PIDFile=/usr/local/apache/logs/httpd.pid
PrivateTmp=true

[Install]
WantedBy=multi-user.target
```

# 配置
## 绑定地址和端口
在 `httpd.conf` 中可以进行 IP 地址和端口的配置，默认配置是监听在 80 端口
```conf
Listen 80
```
需要注意的是，这个 http 服务器的监听地址和端口，跟虚拟主机是无关的。一般这个配置不进行改动
## 配置文件的语法
`httpd.conf` 里面一行代表一个指令, 如果需要多行需要加一个 `\` 来连接，同时，参数使用空格表示，因此如果你的参数包含空格，最好通过 `""` 括起来。


# 总结



# 参考
[官方文档](https://httpd.apache.org/docs/2.4)

---
title: 虚拟机安装CentOS
date: 2019-06-17 11:08:25
tags: Linux
category: Linux 
---
安装CentOS7, 安装完之后会出现上不了网的情况，需要更改网络配置

```
cd /etc/sysconfig/network-scripts 
vi ifcfg-en33
将 ONBOOT=no 改为 ONBOOT=yes
```
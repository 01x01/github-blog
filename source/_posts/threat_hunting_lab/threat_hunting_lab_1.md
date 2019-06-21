---
title: threat hunting lab part 1 
date: 2019-06-17 22:16:24
tags: threat-hunting-lab
category: [threat-hunting-lab,security]
---
# 关键字： 威胁猎杀，威胁猎杀实验室，windows server，pfsense，ESXI
# 概述
设置一个实验室，模拟企业管理，使用默认的 VM 网络管理作为我们的 WAN 口，新建一个新的交换机作为内网通信的 LAN 口。
<!-- more -->
# 准备
1. 需要安装 [vSphere](https://my.vmware.com/cn/group/vmware/details?downloadGroup=ESXI67U2&productId=742&rPId=33333#errorCheckDiv). 截止目前是 `6.7U2` 版本. 
2. Windows server2012 镜像 / windows 7 镜像 / CentOS 镜像
3. 架构图
![img](/postimg/LabNetwork.png)

# 安装 pfsense
![lab1](/postimg/lab1.jpg)
![lab2](/postimg/lab2.jpg)
这里有一个疏忽，需要配置一下交换机。
![lab3](/postimg/lab1-1.jpg)
![lab2](/postimg/lab3.jpg)
![lab4](/postimg/lab4.jpg)
![lab5](/postimg/lab5.jpg)
![lab6](/postimg/lab6.jpg)
![lab7](/postimg/lab7.jpg)
![lab8](/postimg/lab8.jpg)
![lab9](/postimg/lab9.jpg)
![lab10](/postimg/lab10.jpg)
![lab11](/postimg/lab11.jpg)
![lab12](/postimg/lab12.jpg)
![lab15](/postimg/lab15.jpg)
# 验证 pfsense
如下图所示， windows7 在内网里面，可以通过 pfsense 来发送请求，而我们在外面的机器访问不到这一台 windows7
![lab13](/postimg/lab13.jpg)
![lab14](/postimg/lab14.jpg)
![lab16](/postimg/lab16.jpg)
![lab17](/postimg/lab17.jpg)

 # 总结
 至此，我们就完整的安装一套内外网分离的架构。
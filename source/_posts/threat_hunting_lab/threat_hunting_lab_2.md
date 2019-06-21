---
title: threat hunting lab part 2
date: 2019-06-18 21:48:14
tags: threat-hunting-lab
category: [threat-hunting-lab,security]
---
如何一步步搭建一个 active directory lab
<!-- more -->
关键字： Windows server 2012；Active Directory;
# Active Directory
baidu百科的解释： 
> 活动目录（Active Directory）是面向Windows Standard Server、Windows Enterprise Server以及 Windows Datacenter Server的目录服务。（Active Directory不能运行在Windows Web Server上，但是可以通过它对运行Windows Web Server的计算机进行管理。）Active Directory存储了有关网络对象的信息，并且让管理员和用户能够轻松地查找和使用这些信息。Active Directory使用了一种结构化的数据存储方式，并以此作为基础对目录信息进行合乎逻辑的分层组织 

其功能：
① 服务器及客户端计算机管理：管理服务器及客户端计算机账户，所有服务器及客户端计算机加入域管理并实施组策略。
② 用户服务：管理用户域账户、用户信息、企业通讯录（与电子邮件系统集成）、用户组管理、用户身份认证、用户授权管理等，按省实施组管理策略。
③ 资源管理：管理打印机、文件共享服务等网络资源。
④ 桌面配置：系统管理员可以集中的配置各种桌面配置策略，如：用户使用域中资源权限限制、界面功能的限制、应用程序执行特征限制、网络连接限制、安全配置限制等。
⑤ 应用系统支撑：支持财务、人事、电子邮件、企业信息门户、办公自动化、补丁管理、防病毒系统等各种应用系统。

# 准备 
1. Windows server2012

# 基于 Windows2012 配置域管理

![img](/postimg/lab2-1.jpg)
![img](/postimg/lab2-2.jpg)
![img](/postimg/lab2-3.jpg)
![img](/postimg/lab2-4.jpg)
![img](/postimg/lab2-5.jpg)
![img](/postimg/lab2-6.jpg)
![img](/postimg/lab2-7.jpg)
![img](/postimg/lab2-8.jpg)
![img](/postimg/lab2-9.jpg)
![img](/postimg/lab2-10.jpg)

# 总结
至此，我们就安装了一台域服务器，下一篇记录如何使用域服务器。


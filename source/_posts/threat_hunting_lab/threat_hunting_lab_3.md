---
title: threat hunting lab part 3
date: 2019-06-19 20:25:26
tags: threat-hunting-lab
category: threat-hunting-lab,security
---
设置 Windows server 2012 为 domain controller 和 DHCP 服务器
<!-- more -->
关键字： Active Directory;domain forests;
# Active Directory 结构
|元素|描述|
| ----|----|
| Organizational Units (OUs)| 是可以将用户、组、计算机和其它组织单位放入其中的AD(Active Directory，活动目录)容器，是可以指派组策略设置或委派管理权限的最小作用域或单元。
| Domains | Domains 是一个容器对象，也就是 域。 是一组管理上定义的对象，他们与其他域共享一个公共目录数据库，安全策略和信任关系, 每个域都是对象的管理边界，一个域可以跨越多个物理位置和站点，并且可以包含数百万个对象
| Domain Trees | domain trees 是一组 domain 的组合，分为父域和子域
| Forests | Forests 是一个 Active Directory 完整的实例，是最顶层的容器，里面包含了一个或者多个的域容器，共享逻辑结构，全局目录，目录模式和目录配置，以及自动双向传递信任关系。第一个域称之为森林的根域，域名为这个森林的名字，默认情况下，信息仅仅在林中共享，因此，forests 是active directory 的信息安全边界
| Site Objects | 站点是叶子和容器对象。站点容器是用于管理和实现Active Directory复制的对象层次结构中的最顶层对象。站点容器存储知识一致性检查器(KCC)用于影响复制拓扑的对象层次结构。站点容器中的一些对象包括NTDS站点设置对象、子网对象、连接对象、服务器对象和站点对象(林中每个站点一个站点对象)。层次结构显示为Sites容器的内容，它是配置容器的一个子容器。 


# 实验
![img](/postimg/lab3-1.jpg)
![img](/postimg/lab3-2.jpg)
![img](/postimg/lab3-3.jpg)
![img](/postimg/lab3-4.jpg)
![img](/postimg/lab3-5.jpg)
![img](/postimg/lab3-6.jpg)
![img](/postimg/lab3-7.jpg)
![img](/postimg/lab3-8.jpg)
![img](/postimg/lab3-9.jpg)
![img](/postimg/lab3-11.jpg)
![img](/postimg/lab3-12.jpg)
![img](/postimg/lab3-13.jpg)
![img](/postimg/lab3-14.jpg)
![img](/postimg/lab3-15.jpg)
![img](/postimg/lab3-16.jpg)
![img](/postimg/lab3-17.jpg)
![img](/postimg/lab3-18.jpg)
![img](/postimg/lab3-19.jpg)
![img](/postimg/lab3-20.jpg)
![img](/postimg/lab3-21.jpg)
![img](/postimg/lab3-22.jpg)
![img](/postimg/lab3-23.jpg)
![img](/postimg/lab3-24.jpg)
![img](/postimg/lab3-25.jpg)

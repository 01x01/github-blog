---
title: SSH
date: 2019-06-24 15:12:21
tags: 
category: Linux
---
SSH 安全配置
<!-- more -->
# 创建用于登陆的 SSH 用户
## 安装 sudo
Debian
```sh
apt-get install sudo -y
```
CentOS
```sh
yum install sudo -y
```
FreeBSD
```sh
cd /usr/ports/security/sudo/ && make install clean
或者
pkg install sudo
```
## 添加用户到 sudoer
Debain/CentOS/FreeBSD
```s
adduser newUserName
```
## 添加用户到 wheel 用户组
用户处于 wheel 用户组即可使用 su 命令执行 root 命令， 在 debian 系列的 Linux 里面常常使用 sudo  用户组来代替。

Debian
```sh
usermod -aG sudo newUserName
```
CentOS/FreeBSD
```sh
usermod -aG wheel newUserName
```
## 确保 sudoers 文件配置合理
使用 visudo 命令，确保下列配置存在
```sh
# debian
# Allow members of group sudo to execute any command
%sudo   ALL=(ALL:ALL) ALL

# CentOS
# Allow members of group sudo to execute any command
%wheel   ALL=(ALL:ALL) ALL
```
## 重启 ssh
Debian
```sh
/etc/init.d/sshd restart
```
CentOS 6
```sh
/etc/init.d/sshd restart
```
CentOS 7
```sh
systemctl restart sshd.service
```
FreeBSD
```sh
/etc/rc.d/sshd start
```
## 测试
```sh
sudo uptime
sudo whoami
sudo su -
sudo -i
sudo -S
```
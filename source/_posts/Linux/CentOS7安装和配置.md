---
title: CentOS7安装和配置
date: 2019-06-24 15:07:20
tags: 
category: Linux
---
CentOS 7 安装和配置
<!-- more -->
# 使用虚拟机安装 CentOS 7 
安装完以后进行网络配置
```shell
cd /etc/sysconfig/network-scripts 
vi ifcfg-en33
将 ONBOOT=no 改为 ONBOOT=yes
```
# 设置 python 3 环境
## 安装 pyenv
```shell
$ curl https://pyenv.run | bash
```
## pyenv 常见命令
```sh
# 查看可安装版本
pyenv install -l

# 安装
pyenv install 2.7.13
pyenv install 3.7.6

# 卸载
pyenv uninstall 2.7.13

# 全局设置
pyenv global 2.7.13 (一般设置)
pyenv local 2.7.13 
pyenv shell 2.7.13

# 优先级
shell > local > global
```
# 安装 Java
1. 首先下载 [JDK](https://www.oracle.com/technetwork/java/javase/downloads/index.html)
2. 解压缩
```sh
tar -zxvf jdk.tar.gz -C /usr/local/java/
```
3. 配置环境变量
```sh
vim /etc/profile.d/java.sh
---
export JAVA_HOME=/usr/local/java/jdk
export PATH=$JAVA_HOME/bin:$PATH
---
source /etc/profile.d/java.sh
```
4. 验证
```sh
java --version
```
# 安装 NodeJS
```sh
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash
```
## 使用说明
1. 查看 node 版本
```sh
nvm ls-remote
```
2. 安装 node
```sh
nvm use node
```


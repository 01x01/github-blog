---
title: docker
date: 2019-06-28 21:27:55
tags: docker
category: devOps
---
docker 安装

<!-- more -->

# 环境
CentOS

# 安装

```shell
sudo yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2

sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
    
yum list docker-ce --showduplicates | sort -r

yum install <FULLY-QUALIFIED-PACKAGE-NAME>

安装最新版本：
yum install docker-ce

systemctl enable docker 

vim /etc/systemd/system/multi-user.target.wants/docker.service 

ExecStart=/usr/bin/dockerd --registry-mirror=https://rpwutt5n.mirror.aliyuncs.com

sudo systemctl daemon-reload
sudo systemctl restart docker
```


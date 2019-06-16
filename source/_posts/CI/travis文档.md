---
title: travis文档
date: 2019-06-16 22:39:45
tags: travis
category: CI
---
# 准备
1. 一个 github 账号
2. 一个托管在 github 上的项目
3. 在项目下添加 .travis.yml 文件

# 选择项目语言
目前 travis 支持下列语言
```
language: ruby
language: java
language: node_js
language: python
language: php
...
```
如果你的项目需要 macos 来运行测试，你还可以选择
```
os: osx
```
详见： https://docs.travis-ci.com/user/languages/

# job 的生命周期

Travis CI 在接受到请求的时候，会创建一个虚拟机，然后 clone 你的项目，安装依赖，最后运行 build 脚本，所以 job 的生命周期可以分为主要的两部分：
1. install ： 安装任何需要的依赖
2. script： 运行 build 脚本

所以一个 `.travis.yml` 可以有以下部分
```
before_install: 安装依赖之前执行的操作
install： 安装依赖
before_script: 运行 build 脚本之前的操作
script: 运行 build 内容
after_success/after_failure: 成功或失败需要发送提醒之类的操作
deploy： 部署操作
after_deploy: 部署之后的操作
after_script: script 结束的操作
```
如果 build 失败，那么 deploy 将不会进行。比较重要的是，为了防止 deploy 的时候清空你当前的工作目录（比如说 build 期间产生的改动），需要设置 
```
deploy:
    skip-cleanup: true
```

# 其他
除此之外， 脚本还有两种指定下载的项目的方式
```
# blocklist
branches:
  except:
  - legacy
  - experimental

# safelist
branches:
  only:
  - master
  - stable
```

# github page 的部署
最后给出 github page 的部署文件供参考
```yml
language: node_js

sudo: false

branches:
  only:
  - master

cache:
  - npm

node_js:
  - "stable"

install:
  - npm install

script:
  - hexo clean 
  - hexo generate

deploy:
  provider: pages
  skip-cleanup: true
  github-token: $GITHUBTOKEN
  local-dir: public
  keep-history: false
  on:
    branch: master
```
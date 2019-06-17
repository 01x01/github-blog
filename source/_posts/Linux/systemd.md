---
title: systemd
date: 2019-06-17 11:18:45
tags: Linux
category: Linux
keyword: systemd
---
# 概述
Systemd 是用来启动守护进程的，可以用于 Linux 服务器的自启动，简单记录一下其用法。一般 systemctl 命令的配置文件放置于 `/usr/lib/systemd/system`  里面. 分为三个部分， `Unit`  `[Service]` `[Install]` 

# Unit
`Unit` 区块主要定义启动顺序和依赖关系，一个常见的示例
```shell
[Unit]
Description=OpenSSH Server Daemon
Documentation=man:sshd(8)
After=network.target sshd-keygen.service
Wants=sshd-keygen.service
```

这里 After / Wants 分别是定义了顺序和依赖关系，有以下两种<br />`After/Before` : 顾名思义，启动这个服务的时候，需要其他服务先启动<br />`Wants/Requires` : Wants 表示依赖的服务没启动，这个服务也不会失败，是弱依赖。而Requires 则是会失败，是强依赖<br />其常见参数
```shell
Description：简短描述
Documentation：文档地址
Requires：当前 Unit 依赖的其他 Unit，如果它们没有运行，当前 Unit 会启动失败
Wants：与当前 Unit 配合的其他 Unit，如果它们没有运行，当前 Unit 不会启动失败
BindsTo：与Requires类似，它指定的 Unit 如果退出，会导致当前 Unit 停止运行
Before：如果该字段指定的 Unit 也要启动，那么必须在当前 Unit 之后启动
After：如果该字段指定的 Unit 也要启动，那么必须在当前 Unit 之前启动
Conflicts：这里指定的 Unit 不能与当前 Unit 同时运行
Condition...：当前 Unit 运行必须满足的条件，否则不会运行
Assert...：当前 Unit 运行必须满足的条件，否则会报启动失败
```


# Service
主要字段
```shell
Type：定义启动时的进程行为。它有以下几种值。
Type=simple：默认值，执行ExecStart指定的命令，启动主进程
Type=forking：以 fork 方式从父进程创建子进程，创建后父进程会立即退出
Type=oneshot：一次性进程，Systemd 会等当前服务退出，再继续往下执行
Type=dbus：当前服务通过D-Bus启动
Type=notify：当前服务启动完毕，会通知Systemd，再继续往下执行
Type=idle：若有其他任务执行完毕，当前服务才会运行
ExecStart：启动当前服务的命令
ExecStartPre：启动当前服务之前执行的命令
ExecStartPost：启动当前服务之后执行的命令
ExecReload：重启当前服务时执行的命令
ExecStop：停止当前服务时执行的命令
ExecStopPost：停止当其服务之后执行的命令
RestartSec：自动重启当前服务间隔的秒数
Restart：定义何种情况 Systemd 会自动重启当前服务，可能的值包括always（总是重启）、on-success、on-failure、on-abnormal、on-abort、on-watchdog
TimeoutSec：定义 Systemd 停止当前服务之前等待的秒数
Environment：指定环境变量
```

# Install
主要字段
```shell
WantedBy：它的值是一个或多个 Target，当前 Unit 激活时（enable）符号链接会放入/etc/systemd/system目录下面以 Target 名 + .wants后缀构成的子目录中
RequiredBy：它的值是一个或多个 Target，当前 Unit 激活时，符号链接会放入/etc/systemd/system目录下面以 Target 名 + .required后缀构成的子目录中
Alias：当前 Unit 可用于启动的别名
Also：当前 Unit 激活（enable）时，会被同时激活的其他 Unit
```


# 参考

[http://www.ruanyifeng.com/blog/2016/03/systemd-tutorial-commands.html](http://www.ruanyifeng.com/blog/2016/03/systemd-tutorial-commands.html)[https://www.ruanyifeng.com/blog/2016/03/systemd-tutorial-part-two.html](https://www.ruanyifeng.com/blog/2016/03/systemd-tutorial-part-two.html)
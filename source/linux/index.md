记录一些 Linux 常用命令
<!-- more -->
# 传输文件
```shell
scp <filename> <username>@<servername>:<server_path>
```
# 传输一个文件夹
```shell
scp -r <foldername> <username>@<servername>:<server_path>
```
# 追加内容到某一个文件
```shell
cat >> ~/.bashrc << EOF
> export JAVA_HOME=/data/jdk
> export PATH=$JAVA_HOME/bin:$PATH
> EOF
```
# ssh 使用 socks 代理
```shell
# 第一种方法
ssh -o ProxyCommand="nc -X 5 -x 127.0。0.1:1080 %h %p" user@server.net

# 第二种方法
# 写入 ~/.ssh/config 文件

host server.test.com
HostName server.test.com
ProxyCommand nc -X 5 -x 127.0.0.1:1080 %h %p
ServerAliveInterval 30
```
# 使用 curl 下载文件
```shell 
curl -O https://xxxx.xxxx.com/download.xxx
```

# curl 通过代理
```shell
curl --socks5 127.0.0.1:1086 -O https://download3.vmware.com/software/fusion/file/VMware-Fusion-11.1.0-13668589.dmg
```

# 查询PID
```shell
ps -ef | grep xxx | grep -v grep | awk '{print$2}'
```

---
title: httpd文档
date: 2019-06-19 14:36:44
tags: httpd
category: apache-httpd
---
To Be Continue...


# 关键字： httpd，httpd conf
# 概述
Apache httpd 是世界上流行的 http 服务器，简单记录一下对官方文档的理解。



# 安装
## 源码安装

## yum 安装

## httpd.service
```conf
[Unit]
Description=The Apache HTTP Server
After=network.target remote-fs.target nss-lookup.target
Documentation=man:httpd(8)
Documentation=man:apachectl(8)

[Service]
Type=forking
ExecStart=/usr/local/apache/bin/apachectl start
ExecReload=/usr/local/apache/bin/apachectl graceful
ExecStop=/bin/kill -WINCH ${MAINPID}
PIDFile=/usr/local/apache/logs/httpd.pid
PrivateTmp=true

[Install]
WantedBy=multi-user.target
```

# 配置
## 绑定地址和端口
在 `httpd.conf` 中可以进行 IP 地址和端口的配置，默认配置是监听在 80 端口
```conf
Listen 80
```
需要注意的是，这个 http 服务器的监听地址和端口，跟虚拟主机是无关的。一般这个配置不进行改动
## 配置文件的语法
。
httpd 的配置文件为 `httpd.conf` 通常情况下，这个文件会存储一些公用的配置，对于站点会新建一份 conf 文件来进行配置。最后再通过 `Include` 命令在 `httpd.conf` 中进行引入。`#` 通常被认为是注释，与代码级别的注释不同的是，不能写在同一行内。指令在配置中并不是大小写敏感的，但是参数往往是大小写敏感。
`httpd.conf` 里面一行代表一个指令, 如果需要多行需要加一个 `\` 来连接，同时，参数使用空格表示，因此如果你的参数包含空格，最好通过 `""` 括起来

## 动态和静态
除了以上之外， httpd 还是一个模块化的服务器，可以动态加载第三方模块，在编译的时候，你可以选择是静态还是动态，当然各有优缺点，比如静态，其性能高，但是拓展性差；动态拓展性高，但是性能就差了。这里简单记录一下动态加载，httpd 动态加载采用了 DSO (Dynamic Shared Object (DSO) Support) 的方式，只要在编译的时候指定即可，一个比较懒的方式就是直接指定为 `all`

```conf
./configure --enable-mods-shared=all
```
上面的命令会将全部的 module 变为动态，但是在载入的时候，只会载入核心的模块，其他模块需要自己开启。这显然符合我遇到的多数情况。在 conf 里面，静态加载的模块写在 `<IfModules>`, 动态模块写在 `LoadModule`

## Directory
Directory 有几个常见的参数
1. Require
2. Allowoverride
3. Options
4. DirectoryIndex


### Require
可以看到这个指令的意思是权限控制
```
Require all granted
Access is allowed unconditionally.

Require all denied
Access is denied unconditionally.

Require env env-var [env-var] ...
Access is allowed only if one of the given environment variables is set.

Require method http-method [http-method] ...
Access is allowed only for the given HTTP methods.

Require expr expression
Access is allowed if expression evaluates to true.
Some of the allowed syntaxes provided by mod_authz_user, mod_authz_host, and mod_authz_groupfile are:

Require user userid [userid] ...
Only the named users can access the resource.

Require group group-name [group-name] ...
Only users in the named groups can access the resource.

Require valid-user
All valid users can access the resource.

Require ip 10 172.20 192.168.2
Clients in the specified IP address ranges can access the resource.
```

[require 参数](https://httpd.apache.org/docs/2.4/zh-cn/mod/mod_authz_core.html#require)

### allowoverride
表示是否可以被 `.htaccess` 文件重写。有几个常见的参数
```
AuthConfig
Allow use of the authorization directives (AuthDBMGroupFile, AuthDBMUserFile, AuthGroupFile, AuthName, AuthType, AuthUserFile, Require, etc.).

FileInfo
Allow use of the directives controlling document types (ErrorDocument, ForceType, LanguagePriority, SetHandler, SetInputFilter, SetOutputFilter, and mod_mime Add* and Remove* directives), document meta data (Header, RequestHeader, SetEnvIf, SetEnvIfNoCase, BrowserMatch, CookieExpires, CookieDomain, CookieStyle, CookieTracking, CookieName), mod_rewrite directives (RewriteEngine, RewriteOptions, RewriteBase, RewriteCond, RewriteRule), mod_alias directives (Redirect, RedirectTemp, RedirectPermanent, RedirectMatch), and Action from mod_actions.

Indexes
Allow use of the directives controlling directory indexing (AddDescription, AddIcon, AddIconByEncoding, AddIconByType, DefaultIcon, DirectoryIndex, FancyIndexing, HeaderName, IndexIgnore, IndexOptions, ReadmeName, etc.).

Limit
Allow use of the directives controlling host access (Allow, Deny and Order).

All
可以全部重写

None
不可以重写
```

[allowoverride 参数](https://httpd.apache.org/docs/2.4/zh-cn/mod/core.html#allowoverride)

### Options
对于特殊的文件夹指定一些特殊的功能，默认是 `Options FollowSymlinks`
```
FollowSymlinks: 将遵循目录中的符号链接
Indexes: 如果请求一个映射到目录的URL，而该目录中没有DirectoryIndex(例如index.html)，那么mod_autoindex将返回该目录的格式化列表。如果有 DirectoryIndex 那么就会返回指定的值
```
[Options 参数](https://httpd.apache.org/docs/2.4/zh-cn/mod/core.html#Options)

### DirectorIndex
列出目录下面的资源，默认是 `DirectoryIndex index.html`
```conf
# Example A: Set index.html as an index page, then add index.php to that list as well.
<Directory "/foo">
    DirectoryIndex index.html
    DirectoryIndex index.php
</Directory>

# Example B: This is identical to example A, except it's done with a single directive.
<Directory "/foo">
    DirectoryIndex index.html index.php
</Directory>

# Example C: To replace the list, you must explicitly reset it first:
# In this example, only index.php will remain as an index resource.
<Directory "/foo">
    DirectoryIndex index.html
    DirectoryIndex disabled
    DirectoryIndex index.php
</Directory>
```
[DirectoryIndex](https://httpd.apache.org/docs/2.4/zh-cn/mod/mod_dir.html#directoryindex)
# 总结



# 参考
[官方文档](https://httpd.apache.org/docs/2.4)

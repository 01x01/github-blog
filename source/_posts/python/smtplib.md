---
title: smtplib
date: 2019-06-28 21:03:01
tags: 
category: python
---
如何使用 python 发送邮件

<!-- more -->

代码示例：

```python
#!/usr/bin/env python 
#-*- coding:utf-8 -*-
import smtplib
import email.mime.multipart
import email.mime.text

def sendEmail(email_msg):
    sender = '<your-email>@163.com'
    password = '<password>'
    receiver = ['<recevier>@163.com']
    subject = '<subjec>'
    message = email.mime.multipart.MIMEMultipart()
    message['From'] = sender
    message['To'] = ','.join(recevier)
    message['Subject'] = subject
    content = email.mime.text.MIMEText(email_msg,'html','utf-8')
    message.attach(content)
    try:
       smtpObj = smtplib.SMTP('smtp.163.com')
       smtpObj.login(sender, password)
       smtpObj.sendmail(sender, receiver, message.as_string())
       print('邮件发送成功')
    except smtplib.SMTPException:
       print('Error: 无法发送邮件')


if __name__ == '__main__':
    sendEmail("<h1>如何才能取到最新的一个值？</h1>")
```


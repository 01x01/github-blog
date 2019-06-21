---
title: datetime 
date: 2019-06-21 16:48:56
tags: 
category: python
---
时间模块
<!-- more -->
## 时间转字符串
在我们的使用中，我们常常需要将时间转换为字符串，用来作为文件的名字或者用于加密字符的输出等等。例子：
```py
from datetime import datetime 
datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S")
```
## 字符转时间
有时候我们需要将一个字符给转换为时间对象
```
from datetime import datetime 
>>> datetime.strptime('2018-09-09',"%Y-%m-%d")
datetime.datetime(2018, 9, 9, 0, 0)
```
## 时间戳的转换
```
import time 
from datetime import datetime 
stamp = time.time()
datetime.fromtimestamp(stamp)
```
## timedelta
```
import datetime
print('microseconds:', datetime.timedelta(microseconds=1))
print('milliseconds:', datetime.timedelta(milliseconds=1))
print('seconds :', datetime.timedelta(seconds=1))
print('minutes :', datetime.timedelta(minutes=1))
print('hours :', datetime.timedelta(hours=1))
print('days :', datetime.timedelta(days=1))
print('weeks :', datetime.timedelta(weeks=1))
```
加 就是 延后几秒; 减 就是提前几秒
## 转换格式
| Symbol | Meaning | Example |
| :--- | :--- | :--- |
| %a | Abbreviated weekday name | 'Wed' |
| %A | Full weekday name | 'Wednesday' |
| %w | Weekday number: 0 (Sunday) through 6 (Saturday) | '3' |
| %d | Day of the month (zero padded) | '13' |
| %b | Abbreviated month name | 'Jan' |
| %B | Full month name | 'January' |
| %m | Month of the year | '01' |
| %y | Year without century | '18' |
| %Y | Year with century | '2018' |
| %H | Hour from 24-hour clock | '17' |
| %I | Hour from 12-hour clock | '05' |
| %p | AM/PM | 'PM' |
| %M | Minutes | '00' |
| %S | Seconds | '00' |
| %f | Microseconds | '000000' |
| %z | UTC offset for time zone–aware objects | '-0500' |
| %Z | Time zone name | 'EST' |
| %j | Day of the year | '013' |
| %W | Week of the year | '02' |
| %c | Date and time representation for the current locale | 'Wed Jan 13 17:00:00 2016' |
| %x | Date representation for the current locale | '01/13/16' |
| %X | Time representation for the current locale | '17:00:00' |
| %% | A literal % character | '%' |

## tips
工作中经常需要用到美国时间，做一个记录。 utc晚了8个小时，所以要减去即是美国时间
```
datetime.strftime(datetime.utcnow()-timedelta(hours=8),'%Y-%m-%d %H:%M:%S')
```
GMT时间格式
```
GMT_FORMAT =  '%a, %d %b %Y %H:%M:%S GMT'
```
# 参考
《The Python3 Standard Library By Example》

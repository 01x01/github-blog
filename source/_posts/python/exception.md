---
title: exception
date: 2019-07-01 16:58:02
tags: 
category: python
---
捕捉异常并写入文件
<!-- more -->


```py
import traceback 
msg = traceback.format_exc()
exc_type, exc_value, exc_traceback_obj = sys.exc_info()    
traceback.print_exception(exc_type, exc_value, exc_traceback_obj, limit=2, file=open(os.path.join('exceptions','except.log'),'w'))
```

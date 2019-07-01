---
title: tqdm
date: 2019-07-01 16:52:25
tags: 
category: python
---
命令行进度条工具
<!-- more -->
# Manual
```py
with tqdm(total=100,ascii=True)as bar:
    i = 0
    while i < 100:
        r = requests.get(root_url + "/status") # 查询状态
        ri = int(r.json().get('scanPercentage')) # 得到目前进度
        process = ri - i # 目前已完成进度 - i 
        i = ri  # 替换成目前进度
        bar.update(process)  # 更新进度
``` 

# 参考
https://github.com/tqdm/tqdm
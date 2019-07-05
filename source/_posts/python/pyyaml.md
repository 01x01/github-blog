---
title: pyyaml
date: 2019-07-05 17:31:03
tags: 
category: python
---
使用 python 解析 yaml
<!-- more -->
```python
import os 
try:
    from yaml import CLoader as Loader, CDumper as CDumper
except ImportError:
    from yaml import Loader, CDumper
from yaml import load

file = os.path.join(os.getcwd(),"testcase","Auth-Digest","DigestAuth.yaml")
with open(file,'r') as loadfile:
    y = load(loadfile,Loader=Loader)
    print(y)

```
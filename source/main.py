# coding: utf-8 
# author: John.W
import os 
from datetime import datetime 
import random
article_name = input("Please enter your article name: ")
tag = input("Please enter your tag name: ")
category = input("Please enter your category name: ")


with open(os.path.join("_posts",article_name+".md"),'w') as f:
    f.write("""---
title: {}
date: {}
tags: {}
category: {}
---
<!-- more -->
""".format(article_name,datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S"),tag,category))
# coding: utf-8 
# author: John.W
import os 
from datetime import datetime 
import random
article_name = input("Please enter your article name: ")
tag = input("Please enter your tag name: ")
category = input("Please enter your category name: ")
img = [i for i in os.listdir('img')]
img = random.choice(random.shuffle(img))

with open(os.path.join("_posts",article_name+".md"),'w') as f:
    f.write("""---
title: {}
date: {}
tags: {}
category: {}
---
![img](https://raw.githubusercontent.com/01x01/github-blog/master/source/img/{})""".format(article_name,datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S"),tag,category,img))
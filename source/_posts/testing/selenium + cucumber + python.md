---
title: selenium + cucumber + python
date: 2019-07-23 16:01:16
tags: 
category: testing
---
使用python实现基于 selenium + cucumber 的 UI 自动化  
<!-- more -->

# 项目组织
```
tests
    - data: 存放页面元素位置，比如 xpath，id 等等
    - features： 自然语言定义测试用例
    - settings： 项目配置
    - steps： 实现步骤
    - utils：封装 selenium 操作以及其他功能，例如发邮件，生成 report 等等
main.py: 运行项目的入口
```

# 项目依赖
## python 依赖
```shell
pip install selenium behave 
```
## 浏览器驱动
[chromedriver下载地址](http://chromedriver.chromium.org/downloads)
[Firefox driver下载地址](https://github.com/mozilla/geckodriver/releases)

# selenium 常见的用法总结
```<input type="text" name="passwd" id="passwd-id" />```
命令 | 含义
--- | ---
`element = driver.find_element_by_id("passwd-id")`|按照id 来寻找元素
`element = driver.find_element_by_name("passwd")`|按照name 属性来寻找元素
`element = driver.find_element_by_xpath("//input[@id='passwd-id']")`|按照xpath 来寻找元素
`element.send_keys("some text")` | 填充数据
`element.clear()`| 清除表格数据


# 封装 selenium
```py
from selenium import webdriver
from setting.config import settings
import os 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time 

class Browser(object):
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Browser()
        
        return cls.instance

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        self.driver_path = os.path.join(os.getcwd(),"tests","utils",'chromedriver.exe')
        if str(settings['browser']).lower() is "firefox":
            self._driver = webdriver.Firefox()
        elif str(settings['browser']).lower() is "chrome":
            self._driver = webdriver.Chrome(self.driver_path,chrome_options=chrome_options)
        else:
            self._driver = webdriver.Chrome(self.driver_path,chrome_options=chrome_options)
            
    def get(self,url):
        self._driver.get(url)
    
    def click(self,element):
        self._driver.find_element_by_xpath(element).click()

    def dynamic_wait(self,element,seconds=10):
        WebDriverWait(self._driver,seconds).until(EC.presence_of_element_located((By.XPATH, element)))
    
    def static_wait(self,seconds=3):
        time.sleep(seconds)
    
    def find_element(self,element):
        self._driver.find_element_by_xpath("//*[contains(text(),\"{}\")]".format(element))
    
    def find_element_by_name(self,element):
        self._driver.find_element_by_name
    
    def find_element_by_id(self,id):
        self._driver.find_element_by_id(id)
    
    def send_keys(self,element,value):
        self._driver.find_element_by_xpath(element).send_keys(value)
    
    def quit(self):
        self._driver.close()

    def get_driver(self):
        return self.driver
    

browser = Browser.get_instance()

```


---
title: selenium
date: 2019-06-21 15:04:21
tags: 
category: python
---
浏览器自动化测试框架 selenium 
<!-- more -->
# 下载 driver
[chromedriver下载地址](http://chromedriver.chromium.org/downloads)
[Firefox driver下载地址](https://github.com/mozilla/geckodriver/releases)

# 初始化
```py
from selenium import webdriver
import requests 
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--proxy-server=http://127.0.0.1:8083")
driver = webdriver.Chrome('chromedriver.exe',chrome_options=chrome_options)
driver.get("https://www.qa.ehealthinsurance.com")
```
# 下载文件
```py
options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': os.getcwd()+'\\report'}
options.add_experimental_option('prefs', prefs)
self.driver = webdriver.Chrome(executable_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),'chromedriver.exe'),options=options)
```
# 执行js
```py
self.driver.execute_script("return document.documentElement.outerHTML")
```
# 无头浏览器
```py
options = webdriver.ChromeOptions()
options.set_headless()
self.driver = webdriver.Chrome(executable_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),'chromedriver.exe'),options=options)
```
# 浏览器最大化
```py
options.add_argument('start-maximized')
```
# 智能等待元素
```py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 等待元素出现在DOM
WebDriverWait(self._driver).until(EC.presence_of_element_located((By.ID, value)))

# 等待元素显示在页面
WebDriverWait(self._driver,10).until(EC.visibility_of_element_located((By.NAME, value)))

# 等待元素从页面消失
WebDriverWait(self._driver, 10, 0.2).until_not(EC.visibility_of_element_located((By.CLASS_NAME, value))))

# 等待页面的title显示
WebDriverWait(self._driver, 5,0.2).until(EC.title_contains(title))
```
# 多层定位
```py
# 先定位到iframe
frame = self.driver.find_element_by_xpath('//table/tbody/tr[2]/td[2]/iframe')
# 再切换
self.driver.switch_to_frame(frame)
```
# 常见的寻找元素的方法
```py
find_element_by_id
find_element_by_css_selector
find_element_by_xpath
####################################
find_elements_by_id
find_elements_by_css_selector
find_elements_byxpath
```

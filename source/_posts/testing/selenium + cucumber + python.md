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

## 常见的输入框
以 `<input type="text" name="passwd" id="passwd-id" />` 为例
命令 | 含义
--- | ---
`element = driver.find_element_by_id("passwd-id")`| 按照 id 来寻找元素
`element = driver.find_element_by_name("passwd")`| 按照 name 属性来寻找元素
`element = driver.find_element_by_xpath("//input[@id='passwd-id']")`| 按照 xpath 来寻找元素
`element.send_keys("some text")` | 填充数据
`element.clear()`| 清除表格数据

## Select 表单
```py
from selenium.webdriver.support.ui import Select
select = Select(driver.find_element_by_name('name'))
select.select_by_index(index)
select.select_by_visible_text("text")
select.select_by_value(value)
```

清除选择
```py
select = Select(driver.find_element_by_id('id'))
select.deselect_all()
```

## 拖动页面元素
```py
element = driver.find_element_by_name("source")
target = driver.find_element_by_name("target")

from selenium.webdriver import ActionChains
action_chains = ActionChains(driver)
action_chains.drag_and_drop(element, target).perform()
```
## iFrame 和 Windows 窗口切换处理
```py
driver.switch_to_frame("frameName")
driver.switch_to_window("windowName")
alert = driver.switch_to_alert()
```

## 下载文件
```py
options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': os.getcwd()+'\\report'}
options.add_experimental_option('prefs', prefs)
self.driver = webdriver.Chrome(executable_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),'chromedriver.exe'),options=options)
```

## 执行js
```py
self.driver.execute_script("return document.documentElement.outerHTML")
```

## 浏览器配置
```py
# 无头浏览器
options = webdriver.ChromeOptions()
options.set_headless()
self.driver = webdriver.Chrome(executable_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),'chromedriver.exe'),options=options)
```

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
# features 
一般以 3 个词开头：`Given`, `When`, `Then`. 一个普通的测试用例如下所示：
```features
Feature: register 
        In order to login website
        As a user
        I want to register user
    Scenario: Successful register
        Given I visit the website 
        When I click register button 
        Then I fill the forms
        Then I register suceessful

```
一旦你需要定义其中某个字段的时候，需要使用 `Scenario Outline`
```
Feature: Login Github 

    Scenario Outline: I want to login github 
        Given I visit the github 
        when I click login button
        Then I enter "<username>" and "<password>" and click submit
        Then I quit
    Examples:
        | username | password      | 
        | admin    | qwer1234      | 
        | 01x01    | xxxxxxxx      | 
```

# Steps 定义示例
```py
from behave import given, when, then 
from utils.browser import browser
from data.elements import operator,assertor

@when('I click login button')
def step_impl_click_login_button(context):
    browser.click(operator['Sign in'])
    browser.static_wait()
    browser.find_element(assertor["SignInText"])

@then('I enter "{username}" and "{password}" and click submit')
def step_impl_enter_username_passwd(context,username,password):
    browser.send_keys(operator["login"],username)
    browser.send_keys(operator["password"],password)
    browser.click(operator['commit']) 
```




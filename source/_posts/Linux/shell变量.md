---
title: shell变量
date: 2019-06-24 15:40:46
tags: 
category: Linux
---
shell 脚本基础语法 - 变量
<!-- more -->
# 变量
## 定义变量
变量名不加 `$`,如
```bash
variable_name="variable name"
```
## 使用变量
需要加上 `$`, 如：
```bash
echo ${variable_name}
```
## 只读变量
```bash
readonly variable_name
```
## 删除变量
```bash
unset variable_name
```
# 单引号和双引号
1. 单引号里的任何字符都会原样输出，单引号字符串中的变量是无效的；
```bash
echo '${your_name}'

# 输出
${your_name}
```
2. 单引号字串中不能出现单独一个的单引号（对单引号使用转义符后也不行），但可成对出现，作为字符串拼接使用
```bash
echo 'Hello, ' ${your_name} '! '
```
等于说不用加号连接字符串

3. 双引号里可以有变量，并且变量是有效的
```bash
echo "${your_name}"

# 输出
john
```
# 字符串
## 字符串长度
```bash
string="abcd"
echo ${#string} #4
```
## 提取字符串
```bash
echo ${string:1:4}  # 第 2 个字符开始截取 4 个字符 [2,4)
```
## 查找字符串
```bash
string="runoob is a great site"
echo `expr index "$string" io`  # 输出 4
```
注意： 以上脚本中 ` 是反引号，而不是单引号 '，不要看错了。


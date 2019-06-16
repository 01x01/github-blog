---
title: subprocess
date: 2019-06-16 16:05:23
tags: 
category: 
---
![img](https://raw.githubusercontent.com/01x01/github-blog/master/source/img/Wall_Fables_II.png)
# Concurrency - subprocess


# 概述
subprocess 模块包装了一个子进程用来执行系统命令。


# 运行外部命令

```python
completed = subprocess.run(['ls','-al'])
print("return code: ",completed.returncode) # return code:  0c
```


# shell

```python
completed = subprocess.run("ls -al",shell=True)
print("return code: ",completed.returncode) # return code:  0c
```


# 错误处理,添加 check参数

```python
try:
    completed = subprocess.run(['false'],check=True)
except subprocess.CalledProcessError as err:
    print("Err:",err)  #Err: Command '['false']' returned non-zero exit status 1.
```


# 捕捉输出

```python
complete = subprocess.run(['ls','-al'],stdout=subprocess.PIPE)
print("return code : ",complete.returncode)
print("stdout: ",complete.stdout.decode("utf-8"))
# python3.7 只需要加一个关键参数 capture_output
>>> a = subprocess.run(['ls','-al'],capture_output=True)
>>> a.stdout
```


# 捕捉错误输出

```python
completed = subprocess.run(["false"],stderr=subprocess.PIPE)
print("Error:",completed.stderr)
```


# 直接使用Popen函数

```python
completed = subprocess.Popen(["echo","Hello World"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
stdout = completed.communicate()[0].decode('utf-8')
print("stdout: ",stdout)
# 使用communicate的原因
# communicate 是一个管道，用来输出输入消息
```


# 不使用communicate也可以

```python
completed = subprocess.Popen(["echo","Hello World"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
print("stdout: ",completed.stdout.readline().decode("utf-8"))
```


# 使用communicate进行输入

```python
completed = subprocess.Popen(["cat"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
msg = "cat Hello World \n"
stdout = completed.communicate(msg.encode("utf-8"))[0] # 返回一个tuple
print(stdout.decode())
```


# 管道流

```python
cat = subprocess.Popen(['cat','README.md'],stdout=subprocess.PIPE)
grep = subprocess.Popen(["grep","testing"],stdin=cat.stdout,stdout=subprocess.PIPE)
print(grep.stdout.readline())
```



# 参考
[https://dothinking.github.io/blog/2018/01/12/%E4%BD%BF%E7%94%A8subprocess%E6%A8%A1%E5%9D%97%E8%B0%83%E7%94%A8%E5%AD%90%E8%BF%9B%E7%A8%8B%E5%B9%B6%E8%8E%B7%E5%8F%96%E8%BE%93%E5%87%BA.html](https://dothinking.github.io/blog/2018/01/12/%E4%BD%BF%E7%94%A8subprocess%E6%A8%A1%E5%9D%97%E8%B0%83%E7%94%A8%E5%AD%90%E8%BF%9B%E7%A8%8B%E5%B9%B6%E8%8E%B7%E5%8F%96%E8%BE%93%E5%87%BA.html)

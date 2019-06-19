---
title: pytest
date: 2019-06-16 21:48:14
tags: python第三方模块
category: python
---
# 安装
```python
pip install pytest
```

# 脚本命名

1. 测试脚本必须命名为 `test_<name>.py` 或者 `<name>_test.py` 
1. 测试方法或者测试函数，需要以 `test_<name>` 开头
1. 测试的类需要以 `Test<name>` 开头

# 命令行参数说明

## 只运行一个文件里面的一个函数
```python
pytest -v tasks/test_one.py::test_default.py
```

## --collect-only
查看收集到的测试用例有几个。两个测试函数，两个测试用例
```python
(test-KsxmWhQY) C:\test>pytest --collect-only
================================================= test session starts =================================================
platform win32 -- Python 3.6.4, pytest-4.4.1, py-1.8.0, pluggy-0.9.0
rootdir: C:\test
collected 2 items
<Module tasks/test_three.py>
  <Function test_defaults>
  <Function test_member_access>

============================================ no tests ran in 0.04 seconds =============================================
```

## -k
当我们命名一个函数的时候，使用的是 `test_<name>` 的方法，这里 `<name>` 是对这个测试用例的简单描述，我们可以直接通过函数名进行运行测试

```python
(test-KsxmWhQY) C:\test>pytest -v -k "default"
================================================= test session starts =================================================
platform win32 -- Python 3.6.4, pytest-4.4.1, py-1.8.0, pluggy-0.9.0 -- c:\users\johnw\.virtualenvs\test-ksxmwhqy\scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\test
collected 2 items / 1 deselected / 1 selected

tasks/test_three.py::test_defaults PASSED                                                                        [100%]

======================================= 1 passed, 1 deselected in 0.04 seconds ========================================
```
只运行了 `test_default` 的测试用例。

## -m
给测试用例加上一个 label，然后通过 lable 来运行测试，见例子

```python
# 测试脚本
import pytest 

@pytest.mark.run_these_please
def test_mark():
  assert 1 == 2


(test-KsxmWhQY) C:\test>pytest -v --tb=no -m run_mark_test
=================================================================== test session starts ===================================================================
platform win32 -- Python 3.6.4, pytest-4.4.1, py-1.8.0, pluggy-0.9.0 -- c:\users\johnw\.virtualenvs\test-ksxmwhqy\scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\test
collected 3 items / 2 deselected / 1 selected

tasks/test_three.py::test_mark FAILED                                                                                                                [100%]

========================================================= 1 failed, 2 deselected in 0.15 seconds ==========================================================
```
可以看到，我们只运行测试了我们标记的测试用例

## -x 
正常的情况下，如果一个测试用例失败了，那么测试还是会继续进行下去的，但是有一种情况是你在调试脚本的时候，你需要确切的知道在哪个步骤错了，需要使用这个参数

```python
(test-KsxmWhQY) C:\test>pytest -v -x --tb=no
=================================================================== test session starts ===================================================================
platform win32 -- Python 3.6.4, pytest-4.4.1, py-1.8.0, pluggy-0.9.0 -- c:\users\johnw\.virtualenvs\test-ksxmwhqy\scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\test
collected 3 items

tasks/test_three.py::test_defaults PASSED                                                                                                            [ 33%]
tasks/test_three.py::test_member_access FAILED  
```
三个item，只执行了两个

## --maxfail=num
顾名思义就是最大失败次数，没啥好说的

## lf --last-failed
重新运行最近一次运行时所有失败的 case

```python
> pytest -v --tb=no --lf


tasks/test_one.py::test_two FAILED                                                                                                                   [ 33%]
tasks/test_three.py::test_member_access FAILED                                                                                                       [ 66%]
tasks/test_three.py::test_mark FAILED                                                                                                                [100%]

========================================================= 3 failed, 2 deselected in 0.19 seconds ==========================================================

```

## --ff 
先运行上次失败的case，通过的case 最后运行

```python
>>pytest -v --tb=no --ff
tasks/test_one.py::test_two FAILED                                                                                                                   [ 20%]
tasks/test_three.py::test_member_access FAILED                                                                                                       [ 40%]
tasks/test_three.py::test_mark FAILED                                                                                                                [ 60%]
tasks/test_one.py::test_oneone PASSED                                                                                                                [ 80%]
tasks/test_three.py::test_defaults PASSED                                                                                                            [100%]

=========================================================== 3 failed, 2 passed in 0.20 seconds ============================================================
```

## --tb=no
设置不输出错误堆栈

## -v 
```python
(test-KsxmWhQY) C:\test>pytest -v
=================================================================== test session starts ===================================================================
platform win32 -- Python 3.6.4, pytest-4.4.1, py-1.8.0, pluggy-0.9.0 -- c:\users\johnw\.virtualenvs\test-ksxmwhqy\scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\test
collected 5 items

tasks/test_one.py::test_oneone PASSED                                                                                                                [ 20%]
tasks/test_one.py::test_two FAILED                                                                                                                   [ 40%]
tasks/test_three.py::test_defaults PASSED                                                                                                            [ 60%]
tasks/test_three.py::test_member_access FAILED                                                                                                       [ 80%]
tasks/test_three.py::test_mark FAILED                                                                                                                [100%]
```

## --duration=num
展示出耗时最慢的几个测试用例

# 参考
《python testing with pytest》

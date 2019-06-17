---
title: headpq
date: 2019-06-17 09:55:36
tags: python内建模块
category: python
---
# 概述
headpq 是堆结构，是一种树状的数据结构，每个子节点跟父节点都是**有序存储 [按数值大小排列] **的关系，所以其增加和移除都不需要额外的内存. 一个很常听说的算法就是堆排序，只不过这里帮你实现了。<br />python 中的堆，可以帮你移除，替换，排序你传入的数据。 如下代码所示：


# 创建堆
下面的代码可以看出，使用了堆模块，快速帮我们排序好了值。
```python
import heapq

data = [19, 9, 4, 10, 11]
heap = []
print("random:",data)
print()

for n in data:
    print("add {:>3}".format(n))
    heapq.heappush(heap,n)
    #show_tree(heap)

print(heap) # [4, 10, 9, 19, 11] 
```


# 获取堆中的内容 

## 移除
移除堆中的内容，可以使用  `heappop()` 来进行移除，比较需要注意的点是，这里的移除操作，需要接收一个列表之类的数据. 移除的是第一个数据

```python
a = heapq.heappop([10,2,3,4,5])
print(a) # 10
```

## 获取值
堆还可帮助你统计数值，如下代码所示

```python
print("all data:",data)
print("最大的三个数:", heapq.nlargest(3,data))
print("最小的三个数：", heapq.nsmallest(3,data))

# 输出
# all data: [1, 6, 4, 13, 12, 5, 19]
# 最大的三个数: [19, 13, 12]
# 最小的三个数： [1, 4, 5]
```


# 更有效的排序
关于堆排序，主要的是堆排序注重的排序中的模块来排序，而不是按照，每个模块中的数据进行排序。见代码

```python
import random 
random.seed(2016)
data = []

for i in range(4):
    new_data = list(random.sample(range(1,101),5))
    new_data.sort()
    data.append(new_data)
    
    
print(data)
for i in heapq.merge(*data):
    print(i,end=" ")
    
# 输出
[[33, 58, 71, 88, 95], [10, 11, 17, 38, 91], [13, 18, 39, 61, 63], [20, 27, 31, 42, 45]]
10 11 13 17 18 20 27 31 33 38 39 42 45 58 61 63 71 88 91 95 
```
可以看到，代码先进行了每个列表数值的选取，一旦第一个数是最小，那么这个列表就会被排到最前面。


# 总结
python 中 堆模块跟其他列表，字典比较不一样，它是一种算法的呈现，是一种操作过程。

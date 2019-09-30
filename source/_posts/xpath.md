# 选取节点
一般只使用 `//` 来选取根节点，不考虑 DOM 节点在 html 中的位置，然后使用 `/` 来选取子节点

# 结合属性选取节点 

```
//a[@target="_top" and @title="XPath 语法"]
//a[@title="XPath 运算符" or @title="XPath 语法"]
//div/a[1] 第一个 
//div/a[last()] 最后一个
```

# 函数

./node() 根节点 <!DOCTYPE html> 节点
//div/a[last()]
//div/a[position() != 2]
//div/a[count(//div/a)]
//div/button[text() = string(//div/button)]
//div[text()="hello"]
//div[contain(@id, 'idname')]
//div[starts-with(@class, 'pre_classname')]




### Python 拷贝相关 

#### 赋值
> 赋值（=）是创建了对象的一个新的引用，修改其中任意一个变量都会影响到另一个。
 
```
>>> a = 1
>>> b = 'aaa'
>>> c = []
>>> d = {'a':a, 'b':b, 'c':c}
>>> id(e) == id(d)
True
>>> e['c'].append('aaaa')
>>> d['c']
['aaaa']
>>> id(e) == id(d)
True
>>> c
['aaaa']
```
> 上面可以看到，修改dictionary e 中key为c的值时，d也跟着发生改变。

#### 浅拷贝
> 浅拷贝：创建一个新的对象，但它包含的是对原始对象中包含项的引用（如果用引用的方式修改其中一个对象，另外一个也会修改改变）  

- 完全切片方法
- 工厂函数，如list()
- copy模块的copy()函数

```
>>> import copy
>>> f = copy.copy(d)
>>> id(f) == id(d)
False
>>> id(f['c']) == id(d['c'])
True
>>> f['c']
['aaaa']
>>> f['c'].append('bbbbb')
>>> c
['aaaa', 'bbbbb']
>>> d['c']
['aaaa', 'bbbbb']


>>> cc=c[:]    # 避免浅拷贝
>>> id(c)==id(cc)
False
>>> cc.append('cccc')
>>> c
['aaaa', 'bbbbb']
>>> cc
['aaaa', 'bbbbb', 'cccc']

```


#### 深拷贝
> 深拷贝：创建一个新的对象，并且递归的复制它所包含的对象（修改其中一个，另外一个不会改变）  
copy模块的deep.deepcopy()函数
```
>>> g=copy.deepcopy(d)
>>> id(g)==id(d)
False
>>> id(g['c'])==id(d['c'])
False
>>> g['c'], d['c']
(['aaaa', 'bbbbb'], ['aaaa', 'bbbbb'])
>>> id(g['c'][0])==id(d['c'][0])
True
>>> id(g['a'])==id(d['a'])
True

```
> 从上面可以看到，不可变对象的内存地址相同，深拷贝之后如list的可变对象内存地址不同。


#### 引用和copy(),deepcopy()的区别
```pythonstub
import copy
a = [1, 2, 3, 4, ['a', 'b']]  #原始对象

b = a  #赋值，传对象的引用
c = copy.copy(a)  #对象拷贝，浅拷贝
d = copy.deepcopy(a)  #对象拷贝，深拷贝

a.append(5)  #修改对象a
a[4].append('c')  #修改对象a中的['a', 'b']数组对象

print('a = ', a)
print('b = ', b)
print('c = ', c)
print('d = ', d)

"""
输出结果：
a =  [1, 2, 3, 4, ['a', 'b', 'c'], 5]
b =  [1, 2, 3, 4, ['a', 'b', 'c'], 5]
c =  [1, 2, 3, 4, ['a', 'b', 'c']]
d =  [1, 2, 3, 4, ['a', 'b']]
"""

```

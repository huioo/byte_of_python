# 理解MRO与多继承
> 《编写高质量代码——改善Python程序的91个建议》 建议58

Python同其他编程语言一样，也支持多继承。
> 在Python 3.x中取消了经典类，默认都是新式类，并且不必显式的继承object，也就是说：  
> - class Person(object):pass  
> - class Person():pass  
> - class Person:pass    
  三种写法并无区别，推荐第一种

> 但是在Python2.x中，默认都是经典类，只有显式继承了object才是新式类，即：
> - class Person(object):pass 新式类写法
> - class Person():pass 经典类写法
> - class Person:pass 经典类写法

## 多继承经典问题——菱形继承
假如有如下继承关系，当用古典类实现的时候，如果有实例`d=D()`，当调用`d.getvalue()`和`d.show()`方法的时候分别对应哪个父类中的方法？当改用新式类来实现时，结果又将会是怎样的呢？

具体实现：
```python
class A():
    def getvalue(self):
        print "return value of A"

    def show(self):
        print "I can show the information of A"

class B(A):
    def getvalue(self):
        print "return value of B"

class C(A):
    def getvalue(self):
        print "return value of C"

    def show(self):
        print "I can show the information of C"

class D(B, C):
    pass

```
实例`d=D()`，调用`d.getvalue()`和`d.show()`方法时：
- 当用古典类实现的时候，分别调用的是**B类的getvalue()方法**和`A类中的show()方法`。输出如下：
    ```
    return value of B
    I can show the information of A
    ```
- 当用新式类实现的时候，分别调用的是**B类的getvalue()方法**和`C类中的show()方法`。输出如下：
    ```
    return value of B
    I can show the information of C
    ```

## 结果不同的原因
> 根本原因在于古典类和新式类之间所采取的`MRO（Method Resolution Order，方法解析顺序）`的实现方式存在差异。

- 古典类  
  > MRO搜索采用简单地自左至右的深度优先方法，即按照多继承声明的顺序形成继承树结构，自顶向下采用深度优先的搜索顺序，当找到所需要的属性或者方法的时候就停止搜索。
  >> 调用`d.getvalue()`时，其搜索顺序是`D->B`，所以调用的是B类中对应的方法。
  >> 
  >> 调用`d.show()`时，其搜索顺序是`D->B->A`，所以调用的是A类中对应的方法。
- 新式类
  > 采用C3 MRO搜索方法，该算法描述如下：
  >> 假定，C1C2..CN表示C1到CN的序列，其中序列头部元素(head)=C1，序列尾部(tail)定义为=C2..CN。  
  C继承的基类自左向右分别表示为B1,B2,..,BN；  
  L(C)表示C的`线性继承关系`，其中L[object]=object。  
  >>    
  >> 算法具体过程如下：  
  `L[C(B1 ... BN)] = C + merge(L[B1] ... L[BN], B1 ... BN)`   
  >> 
  >> merge方法里面的元素，指每个父类自身的线性继承关系，以及该类自己的父类线性关系。  
  >> 其中merge方法的计算规则如下：   
  在`L[B1] ... L[BN], B1 ... BN`中，取L[B1]的head，如果该元素不在`L[B2] ... L[BN], B1 ... BN`的尾部序列中，则添加该元素到C的线性继承序列中，同时将该元素从所有列表中删除（该头元素也叫good head），否则取`L[B2]`的head。继续相同的判断，直至整个列表为空或者没有办法找到任何符合要求的头元素（此时将引发一个异常）。  
  >
  > 结合上面的例子来说明C3 MRO 算法的具体计算方法，以新式类实现的上述菱形继承关系（class O, class A(O), class B(A), class C(A), class D(B, c)）
  ```
  算法规则关系表达式如下：
  L[O] = O; L[A] = AO；
  则：
  L[B] = B + merge(L[A]) = B + merge(AO) = B + A + merge(O, O) = B + A + O
  L[C] = C + merge(L[A]) = C + merge(AO) = C + A + merge(O, O) = C + A + O
  L[D] = D + merge(L[B],L[C],BC)
       = D + merge(BAO, CAO, BC)
       = D + B + merge(AO, CAO, C)   # 下一个计算取AO的头A，但A包含在CAO的尾部，因此不满足条件
                                     # 跳到下一个元素CAO继续计算
       = D + B + C + merge(AO, AO)
       = D + B + C + A + O
       = D,B,C,A,O
  当D的实例d调用`getvalue()`和`show()`方法时按照`D->B->C->A->O`的顺序进行搜索，在第一次找到该方法时停止并调用该类对应的方法。
  ```
  > 关于MRO的搜索顺序，我们也可以通过查看 `__mro__` 属性得到证实。`D.__mro__`的输出如下：
    ```python
    >>> D.__mro__
    (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
    ```
  > 实际上MRO虽然叫方法解析顺序，但是它不仅是针对方法搜索，对于类中的数据属性也适用。  
  新式类多继承搜索顺序(广度优先): 先在水平方向查找，然后再向上查找。

## C3 MRO 死锁

根据C3 MRO算法的描述，如果找不到满足条件的good head，则会摒弃该元素从而对下一个元素进行查找。但如果找遍了所有的元荤素都找不到符合条件的good head会怎么样呢？
 
来看一个具体的例子：
```python
class A(object): pass
class B(object): pass
class C(A, B): pass     # 基类顺序是A，B
class D(B, A): pass     # 基类顺序是B，A
class E(C, D): pass
```  
运行程序我们会发现这种情况下有异常抛出。
```python
Traceback (most recent call last):
  File "<input>", line 5, in <module>
TypeError: Cannot create a consistent method resolution
order (MRO) for bases A, B
```
根据上述代码的继承关系和MRO算法可以得出：
```
L[E] = E + maerge(L[C],L[D],CD)
     = E + maerge(CABO,DBAO,CD)
     = E + C + maerge(ABO,DBAO,D)
     = E + C + D + maerge(ABO,BAO)
```
当算法进行到最后一步的时候再也找不到满足条件的head了，因为当选择ABO的头A元素时，发现其包含在BAO的尾部AO中；同理。B包含在BO中，此时便形成了一个`死锁`。Python解释器此时不知道如何处理这种情况，便直接抛出异常，这就是上述例子有异常抛出的原因。

菱形继承我会死我们在多继承设计的时候需要尽量避免的一个问题。


# 更多知识
""""""

# 传递元组
"""
你曾经希望能从函数中返回两个不同的值吗？ 这当然可以。
你所要做的就是使用一个元组。

>>> def get_error_details():
...     return 2, 'details'
...
>>> errnum, errstr = get_error_details()
>>> errnum
2
>>> errstr
'details'


请注意， a, b = <某些表达式> 会将表达式的结果解析为两个值组成的元组。

这也意味着在 Python 中交换两个变量的最快方法是：
>>> a = 5; b = 8
>>> a, b
(5, 8)
>>> a, b = b, a
>>> a, b
(8, 5)
"""

# 魔术方法
"""
有一些方法，如 __init__和__del__ 方法，它们在类中具有特殊意义。

魔术方法用于模仿内置类型的某些行为。
例如，如果你想为你的类使用 x[key] 索引操作（就像你列表和元组使用它一样），那么你所要做的就是实现 __getitem __() 方法，这样你的工作就已经完成了。
如果你思考一下，这就是 Python 本身为 list 类所做的事情！

下表列出了一些有用的魔术方法。 如果你想了解所有的魔术方法，
  参考手册(http://docs.python.org/3/reference/datamodel.html#special-method-names)。
  
    __init__(self, ...)
        在返回新创建可以使用的对象之前调用此方法。
    
    __del__(self)
        在对象被销毁之前调用（具有不可预测时机，所以避免使用它）
    
    __str__(self)
        当我们使用 print 函数或使用 str() 时调用。
    
    __lt__(self, other)
        使用小于（ less than ）运算符（<）时调用。 同样，所有运算符都有特殊的方法（+，>等）
    
    __getitem__(self, key)
        使用 x[key] 索引操作时调用。
    
    __len__(self)
        当内置的 len() 函数用于序列对象时调用。

"""

# 单个语句块
"""
我们已经看到，每个语句块都通过其自己的缩进级别与其余语句区分开来。
但有一点需要注意，如果你的语句块只包含一个语句，那么您可以在条件语句或循环语句的同一行上指定它。

以下示例应该说明这一点:
>>> flag = True
>>> if flag: print('Yes')
...
Yes

请注意，单个语句是就地使用的，而不是作为单独的块使用。
虽然，你可以使用它来使你的程序更小，但我强烈建议避免使用这种快捷方法，除了错误检查。主要是因为如果使用适当的缩进，添加额外的语句将更容易。
"""

# Lambda 格式
"""
lambda 语句用于创建新的函数对象。
基本上， lambda 采用一个参数，后跟一个表达式。
Lambda 成为函数的函数体，新函数返回此表达式的值。


示例 （保存为 more_lambda.py ）：
points = [{'x': 2, 'y': 3},
          {'x': 4, 'y': 1}]
points.sort(key=lambda i: i['y'])
print(points)

输出：

$ python more_lambda.py
[{'y': 1, 'x': 4}, {'y': 3, 'x': 2}]


请注意， list 的 sort 方法可以采用 key 参数来确定列表的排序方式（通常我们只知道升序或降序）。
在我们的例子中，我们想要进行自定义排序，为此我们需要编写一个函数。
我们使用 lambda 表达式创建一个新函数，而不是为仅在这一个地方使用的函数编写单独的 def 块。
"""

# 列表推导
"""
列表推导用于从现有列表中导出新列表。
假设你有一个数字列表，并且你希望获得一个相应的新列表，其中所有数字仅在数字本身大于2时乘以2。
列表推导是这种情况的理想选择。

示例（保存为 more_list_comprehension.py ）：

listone = [2, 3, 4]
listtwo = [2*i for i in listone if i > 2]
print(listtwo)

输出：

$ python more_list_comprehension.py
[6, 8]

这里，我们通过在满足某些条件时指定要完成的操作（ 2*i ）来推导出一个新的列表（ if i > 2 ）。 请注意，原始列表保持不变。

使用列表推导的优点是，当我们循环处理列表的每个元素并将其存储在新列表中时，它减少了所需样板代码的量。
"""

# 在函数中接受元组和字典
"""
有一种特殊的方法可以分别使用 * 或 ** 前缀将参数作为元组或字典接收到函数中。
当在函数中使用可变数量的参数时，这很有用。

因为我们在`args`变量上有一个`*`前缀，所有传递给函数的额外参数都作为元组存储在`args`中。
如果使用了`**`前缀，那么额外的参数将被认为是字典的键/值对。

>>> def powersum(power, *args):
...     '''返回每个参数指定幂次的总和。'''
...     total = 0
...     for i in args:
...         total += pow(i, power)
...     return total
...
>>> powersum(2, 3, 4)
25
>>> powersum(2, 10)
100
"""

# assert 语句
"""
assert语句用于断言某值为 True 。
例如，如果您非常确定您正在使用的列表中至少有一个元素并且想要检查它，并且如果不是 True 则引发错误，那么 assert 语句在这种情况下是理想的。
当 assert 语句失败时，会引发 AssertionError 。

pop（） 方法删除并返回列表中的最后一项。

>>> mylist = ['item']
>>> assert len(mylist) >= 1
>>> mylist.pop()
'item'
>>> assert len(mylist) >= 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError

assert 语句应该是明智地使用。 大多数情况下，最好能捕获异常、处理问题或向用户显示错误消息然后退出。
"""

# 装饰器
"""
装饰器是用于包装函数的快捷方式。
这有助于一遍又一遍地使用相同的代码『包装』功能。
例如，我为自己创建了一个 retry 装饰器，我能应用于任何函数，如果在运行期间抛出任何异常，则会再次重试，直到最多 5 次并且每次重试之间有间隔。
这对于你尝试向远程计算机进行网络连接的情况特别有用：
"""
from time import sleep
from functools import wraps
import logging

logging.basicConfig()
log = logging.getLogger("retry")
counter = 0


def retry(f):
    @wraps(f)
    def wrapper_function(*args, **kwargs):
        max_attempts = 5
        for attempt in range(1, max_attempts + 1):
            try:
                return f(*args, **kwargs)
            except:
                log.exception("Attempt %s/%s failed : %s",
                              attempt,
                              max_attempts,
                              (args, kwargs))
                sleep(10 * attempt)
        log.critical("All %s attempts failed : %s",
                     max_attempts,
                     (args, kwargs))
    
    return wrapper_function


@retry
def save_to_database(arg):
    print("Write to a database or make a network call or etc.")
    print("This will be automatically retried if exception is thrown.")
    global counter
    counter += 1
    # 这将在第一次调用中抛出异常
    # 并且在第二次调用中工作正常（即重试）
    if counter < 2:
        raise ValueError(arg)


if __name__ == '__main__':
    save_to_database("Some bad value")

"""
输出：

$ python more_decorator.py
Write to a database or make a network call or etc.
This will be automatically retried if exception is thrown.
ERROR:retry:Attempt 1/5 failed : (('Some bad value',), {})
Traceback (most recent call last):
  File "more_decorator.py", line 14, in wrapper_function
    return f(*args, **kwargs)
  File "more_decorator.py", line 39, in save_to_database
    raise ValueError(arg)
ValueError: Some bad value
Write to a database or make a network call or etc.
This will be automatically retried if exception is thrown.

"""

"""
http://www.ibm.com/developerworks/linux/library/l-cpdecor.html

http://toumorokoshi.github.io/dry-principles-through-python-decorators.html
"""


# Python 2 与 Python 3 的不同
"""
参见：

    "Six" 库
        (http://pythonhosted.org/six/)
    Porting to Python 3 Redux by Armin
        (http://lucumr.pocoo.org/2013/5/21/porting-to-python-3-redux/)
    Python 3 experience by PyDanny
        (http://pydanny.com/experiences-with-django-python3.html)
    Official Django Guide to Porting to Python 3
        (https://docs.djangoproject.com/en/dev/topics/python3/)
    Discussion on What are the advantages to python 3.x?
        (http://www.reddit.com/r/Python/comments/22ovb3/what_are_the_advantages_to_python_3x/)

"""

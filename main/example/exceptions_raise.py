class ShortInputException(Exception):
    """用户定义的异常对象"""
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    text = input('Enter something --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
    # 其他程序可以在这里正常执行
except EOFError:
    print('Why did you do an EOF on me?')
except ShortInputException as ex:
    print(('ShortInputException: The input was ' +
           '{0} long, expected at least {1}')
          .format(ex.length, ex.atleast))
else:
    print('No exception was raised.')

"""
$ python exceptions_raise.py
Enter something --> a
ShortInputException: The input was 1 long, expected at least 3

$ python exceptions_raise.py
Enter something --> abc
No exception was raised.
"""

"""
这里，我们创建了一个我们自己的异常类型这个新的异常类型被命名为 ShortInputException 。
它有两个字段， length 是给出输入的长度， atleast 是程序所期望的最小长度。

在 except 子句中，我们注意到错误的类通过 as 把错误或异常对应的对象储存到了命名的变量中。
这类似于函数调用中的变量和参数。

在特定的 except 子句中，我们用异常对象的 length 和  atleast 字段向用户输出适当的信息。
"""

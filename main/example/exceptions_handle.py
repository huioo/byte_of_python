try:
    text = input('Enter something --> ')
except EOFError:
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the operation.')
else:
    print('You entered {}'.format(text))
 
 
"""
# 按下 ctrl + d
$ python exceptions_handle.py
Enter something --> Why did you do an EOF on me?

# 按下 ctrl + c
$ python exceptions_handle.py
Enter something --> ^CYou cancelled the operation.

$ python exceptions_handle.py
Enter something --> No exceptions
You entered No exceptions
"""

"""
我们将所有可能引发异常或错误的语句放入 try 语句块中，然后将对应错误或异常的处理程序放入  except 子句（程序块）中。
except 子句会处理单个特定的错误或异常，或是一个带括号的错误或异常列表。
如果没有提供错误或异常的名字， 它将处理 所有的 错误和异常。

请注意，每个 try 子句之后，至少要有一个与之关联的 except 子句。否则， 一个单独的 try 语句块有什么意义？

如果有任何未处理的错误和异常，默认的 Python 处理程序将被调用，它只会终止程序运行并打印出一条异常信息。

你可以使用一个与 try..except 语句块关联的 else 子句。
else 子句在没有错误发生时将会执行。

"""

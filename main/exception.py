# 异常
"""
当意外的 情况在你的程序中发生时就会产生异常。
例如，当你尝试读取一个文件但它并不存在时，会发生什么？或者，当程序还在运行的时候，你删除了它会怎么呀？这类情况会通过引发异常来处理。

相似地，如果你的程序有一些无效的语句会发生什么？ 这由 Python 进行处理，它会举手并告诉你这里有一个错误。

"""


# 错误
"""
考虑一个简单的 print 函数调用。当 print 被错误拼写成 Print 会发生什么？注意字母大写。
这种情况下， Python 将会 引发（ raise ） 一个语法错误。

>>> Print("Hello World")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Print' is not defined
>>> print("Hello World")
Hello World

对这个错误的处理是，观察到 NameError 错误被引发并打印出这个错误发生的位置。
"""


# 异常
"""
我们将尝试读取用户的输入。我们输入下面的第一行代码并按下 Enter 执行。
当你的计算机提示你输入时，在 Mac 上按下 [ctrl-d] 或者在 Windows 上按下 [ctrl-z] 来观察会发生什么
（如果你使用的是 Windows 系统而以上两个选择都无效时，你可以尝试在命令行窗口使用 [ctrl-c] 来产生 KeyboardInterrupt 错误）。

>>> s = input('Enter something --> ')
Enter something --> Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
EOFError

Python 引发了一个名为 EOFError 的错误，它的意思是发现了一个不该出现的 文件末尾（ end of file） 符号（可以用 ctrl-d 表示）。
"""


# 处理异常
"""
我们可以用 try..except 语句来处理异常。
我们简单地把正常语句放入 try 语句块，并把所有错误处理程序放入 except 语句块。
"""
# 示例（保存为 exceptions_handle.py ），详见./example/exceptions_handle.py


# 引发异常
"""
你可以用 raise 语句 引发（ raise ） 异常，需要提供错误或异常的名字以及被 抛出（ thrown ） 的异常对象。

你用于引发异常的错误和异常应该是一个直接或间接地派生自 Exception 类的类。
"""
# 示例（保存为 exceptions_raise.py ），详见./example/exceptions_raise.py


# try .. finally
"""
假设你要在你的程序中读取一个文件。如何保证无论是否引发错误，文件对象都被正确关闭？
可以使用 finally 语句块来完成。
"""
# 把这段程序保存为 exceptions_finally.py ，详见./example/exceptions_finally.py


# with语句
"""
在 try 语句块中获取资源，并最终在 finally 语句块中释放资源是一种常见做法。
因此使用 with 语句可以以更清晰的代码风格实现以上过程：

with open("poem.txt") as f:
    for line in f:
        print(line, end='')
"""
# 保存为 exceptions_using_with.py ，详见./example/exceptions_using_with.py

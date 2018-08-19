# 输入输出
"""
这将会是解决你的项目与用户交互的办法。
例如，你想要从用户处得到输入，然后打印其中的一些结果。我们可以通过分别通过 input() 函数和 print 函数来实现。

对于输出，我们也可以使用 str 类中的方法。
例如，你可以使用 rjust 方法得到一个右对齐、有明确宽度的字符串。可以通过 help(str) 来查看更详细的信息。

输入/输出另一个常用的方式就是处理文件。
创建、读取、写入文件的能力对于很多程序来说都很重要。

"""


# 用户输入
# 以 io_input.py 保存这个项目，参考 ./example/io_input.py


# 文件
"""
你可以创建一个 file 类的对象来打开文件以供读写，使用 read, readline 或 write 中的恰当方法可以读取或写入文件。
对文件的读写能力取决于你打开文件时选择的模式。当你处理完文件后，你可以使用 close 方法告诉 Python 你已经使用完文件了。
"""
# 示例（另存为 io_using_file.py），参考 ./example/io_using_file.py


# Pickle
"""
Python 提供了一个标准模块 pickle，你可以使用该模块将任何加简单的 Python 对象存储在文件中，然后可再次取回。
这个过程也被称为持久化存储对象。
"""
# 以 io_pickle.py 保存这个项目，参考 ./example/io_pickle.py


# Unicode
"""
到目前为止，当我们编写和使用字符串或者读取和写入文件时，我们只使用了简单的英文字符。
英语和非英语字符都可以用 Unicode 码表示（请参阅本节末尾的文章了解更多信息），
默认情况下 Python 3 使用 Unicode 存储字符串变量（想想所有我们用单或双或三重引号包裹的文本引号）。

注意：
    如果你使用的是 Python 2 ，并且我们希望能够读取和编写其他非英语语言，我们需要使用 unicode 类型，
    所有内容都以字符 u 开头，例如：u"hello world" 。

>>> "hello world"
'hello world'
>>> type("hello world")
<class 'str'>
>>> u"hello world"
'hello world'
>>> type(u"hello world")
<class 'str'>
"""
"""
当数据通过网络发送时，我们需要以字节为单位发送数据......这是计算机易于理解的方式。
将 Unicode 码（这是 Python 在存储字符串时使用的）转换为字节的规则称为编码。
一种流行的编码方式是 UTF-8 。 我们可以通过在 open 函数中使用一个简单的关键字参数来读写 UTF-8 。

# encoding=utf-8
import io

f = io.open("abc.txt", "wt", encoding="utf-8")
f.write(u"Imagine non-English language here")
f.close()

text = io.open("abc.txt", encoding="utf-8").read()
print(text)

我们使用 io.open 然后在第一个 open 语句中使用 encoding 参数对信息进行编码，然后在解码信息时再在第二个 open 语句中使用该参数。
请注意，我们应该只在文本模式下使用 open 语句时的使用编码。

每当我们编写一个使用Unicode文字的程序（通过在字符串之前放置一个 u ）就像我们上面使用的那样，
我们必须确保 Python 本身被告知我们的程序使用UTF-8，我们必须把 ＃encoding=utf-8 注释在我们程序的顶部。
"""

# 模块
"""
你已经看到了如何在你的程序中重复使用代码——只需定义一次函数就可以对其重复调用了。
如果你想在其他程序中复用你写的大量的函数时，怎么办？可能你已经猜到了，答案就是模块。

编写模块的方式有很多，但是最简单的方式就是创建一个包含很多方法和变量并以 .py 为扩展的文件。
另一种方法就是用编写 Python 解释器的语言来编写模块。
例如，你可以用 C 语言 来写模块，在使用标准 Python 解释器中进行编译时，这些模块会从你的 Python 代码中调用。

一个模块会被引入到一个程序来使用它的功能。这就是我们使用 Python 标准库的方法。首先，我们会了解如何使用标准库模块。
"""
import sys

"""
我们利用 import  引入 sys 模块，这基本上会告诉 Python ，我们想使用这个模块。
sys 模块包含着与 Python 解释器和它的环境（即系统）有关的函数。
如果它不是一个编译模块（即用 Python 编写的模块），那么 Python 解释器会在它的 sys.path 变量中列出来的目录中寻找它。
如果模块被找到，则运行该模块主体中的语句，这个模块就会被设为 可用 供你使用。
注意初始化在我们 第一次 引入这个模块时就会完成。

sys 模块中的 argv 变量可以通过点表示法，即 sys.argv 访问。
它清晰地指出这个名字就是 sys 模块的一部分。
这种访问方式的另一种优点就是这个名字不会与你程序中的任何 argv 的变量发生冲突。

sys.argv 这个变量就是一个字符串 列表。具体来说，sys.argv 包含 命令行参数 列表，即那些使用命令行传递给程序的参数。
"""

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', *sys.path, sep='\n')

"""
当我们执行 python module_using_sys.py we are arguments 命令的时候，
我们使用 python 命令行运行模块 module_using_sys.py。
后面的字符串 we are arguments 被作为参数传递给模块。Python 会把这些参数储存在 sys.argv 变量里以供后续使用。

记住，当前运行的模块名总储存在 sys.argv 列表的第一个元素中。所以执行以上语句后，
sys.argv[0] 中存放着 'module_using_sys.py'，'we' 放在 sys.argv[1],
'are' 放在 sys.argv[2] 而 'arguments' 放在 sys.argv[3]。
注意到 Python 中，数组引索从 0 开始计数而不是从 1 开始。

sys.path 是模块导入时要搜索的目录列表。我们可以看到 sys.path 的第一个字符串是空的，
空字符串意味着当前目录也是 sys.path 的一部分，这与 PYTHONPATH 环境变量是相同的。
这意味着你可以直接从当前目录下导入模块。不然你还需要把你要导入的模块放到 sys.path 中的一个目录里。

注意：当前目录指的是你的程序启动的目录。你可以通过执行 import os; print(os.getcwd())，来查看你的程序的当前目录
"""


# 字节码文件 .pyc
"""
导入模块是一个相对而言开销较大的操作，因此，Python 试用了一些手段来使得导入模块的操作更加快速。
其中一个方法，就是创建以 .pyc 为扩展名的 字节码 文件，它是一种中间形式，Python 会把程序代码转换成这样的形式
当你下一次想要在另外一个程序代码中导入模块的时候，这个 .pyc 文件就很有用 —— 导入操作会很快完成，
这是因为导入模块所必须的一部分操作已经被事先完成了。此外，这些字节码文件都是平台无关的。

注意：这些 .pyc 文件一般会被创建在与它对应的 .py 文件相同的文件目录下。
如果 Python 没有在该文件夹下写文件的权限，那么 .pyc 文件将不会被创建。
"""


# from .. import .. 语句
"""
如果你希望直接把 argv 变量导入到你的程序中（以避免每次都要键入 sys.），那么你就可以使用 from sys import argv 语句。
"""
from math import sqrt

print("Square root of 16 is", sqrt(16))


# 模块的 __name__
"""
每个模块都有一个名称，在模块中我们可以通过判断语句来确定模块的名称。

这在一种情形下特别有用：确定模块被导入了？还是在独立的运行。
如之前提到过的，当模块第一次被导入的时候，模块的代码将被执行。
我们可以通过这一点，让模块在被导入和独立运行时执行不同的操作。
通过模块的 __name__ 属性可以实现这个功能。

每一个 Python 模块都定义了各自的 __name__。如果其值为 '__main__'，这说明用户正在单独运行这个模块，这时我们可以进行合适的操作。
"""

if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')


# 创建自己的模块
"""
创建你自己的模块还是很容易的，你从一开始就在做这件事！这是因为每一个 Python 程序都是一个模块。
你只需要保证这个程序以 .py 作为扩展名就行了。下面这个例子将会说明这件事。
"""
# 保存为mymodule.py
__version__ = '0.1'


def say_hi():
    print('Hi, this is mymodule speaking.')


"""
保存为mymodule_demo.py
这个模块的位置有两种选择：1、导入它的程序所处的文件夹下；2、sys.path 所列出的文件夹下。

import mymodule

mymodule.say_hi()
print('Version', mymodule.__version__)


保存为mymodule_demo2.py

from mymodule import say_hi, __version__

say_hi()
print('Version', __version__)


mymodule_demo2.py 的输出和 mymodule_demo.py 是相同的。
需要注意的是，如果如果导入 mymodule 的模块中已经被有一个 __version__ 名称被声明了的话，那么这里就会产生命名冲突。
这种情况是很可能出现的，因为一种常见的实践方式就是对每一个模块都使用这个名称来声明它自己的版本号。
因此，尽管 import 语句可能会让你的程序代码稍微有点冗长，但是我们更加推荐你使用它。

你也可以使用：
from mymodule import *

这将会导入所有的诸如 say_hi 这样的公开名称（public names），但是不会导入 __version__，因为它以 2 个下划线作为前缀。



    警告：记住，你应该避免使用 * 导入，比如像 from mymodule import * 这样。

    Python 之禅

    Python 的指导原则之一，就是「显式优于隐式」。你可以运行 import this 来了解更多的相关内容。

"""


# dir函数
"""
内置的 dir() 函数能以列表的形式返回某个对象定义的一系列标识符。
如果这个对象是个模块，返回的列表中会包含模块内部所有的函数、类和变量。

这个函数接收一个可选的参数。当参数是模块名时，函数会返回对应模块的标识符列表。没有参数时则会返回当前模块的标识符列表。


$ python
>>> import sys

# 获取 sys 模块内所有属性的标识符
>>> dir(sys)
['__displayhook__', '__doc__', 'argv', 'builtin_module_names', 'version', 'version_info', ...]
# 这里只列出了部分输出

# 获取当前模块内属性的标识符
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'sys']

# 创建一个新的变量 'a'
>>> a = 5

>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'sys', 'a']

# 删除变量 'a'
>>> del a
# 用于 删除 一个变量或标识符。

>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'sys']

注意 dir 函数 对任 何对象都有效。例如：dir(str) 会列出 str (String) 类的属性。
还有一个 vars() 函数，它有时能给你对象的属性和它们的值，但这个函数并不总是有效。
"""


# 程序包
"""
现在你一定已经开始观察组织程序的结构层次了。
变量通常在函数的内部。全局变量和函数通常在模块的内部。
如何组织模块呢？这就是程序包出场的时候了。

程序包就是一个装满模块的文件夹，它有一个特殊的 __init__.py 文件，这个文件告诉 Python 这个文件夹是特别的，
因为它装着 Python 的模块。


让我们假设你想创建一个叫做 world 的程序包，它有很多子程序包 asia、africa 等。这些子程序包依次包含 india、madagascar 等模块。

以下是一种组织文件夹的方式：

- <some folder present in the sys.path>/
    - world/
        - __init__.py
        - asia/
            - __init__.py
            - india/
                - __init__.py
                - foo.py
        - africa/
            - __init__.py
            - madagascar/
                - __init__.py
                - bar.py

"""


# 标准库
"""
标准库

Python 标准库包含超大量的实用模块，同时其实是每个 Python 标准安装的一部分。
熟悉 Python 标准库是非常重要的，因为如果你了解这些库可以完成事情的范围，很多问题刻可以快速解决。

我们将探索库中一些很常用的模块。你可以在 Python 安装所带的文档的 「代码库参考」章节 中找到 Python 标准库所有模块的完整细节。
https://docs.python.org/3/library/
"""


# sys 模块
"""
sys 模块包含特定系统的功能。我们已经见过

假设我们想要检查当前使用的 Python 版本， sys 模块给出我们以下信息。

>>> import sys
>>> sys.version_info
sys.version_info(major=3, minor=6, micro=5, releaselevel='final', serial=0)
>>> sys.version_info.major == 3
True

sys 模块有一个给出版本信息的 version_info 元组。
第一个条目是主要版本。我们可以提取这些信息来使用它。
"""


# logging 模块
"""
如果你希望将一些调试消息或重要消息存储在某个地方，以便你可以检查你的程序是否按照预期运行，该怎么办？
你怎样将这些信息「存在某地」，这可以用 logging 模块收集。
"""
# 保存为 stdlib_logging.py，参考./example/stdlib_logging.py


# Module of the Week 系列

"""
标准库中还有很多需要探索的地方，例如
    调试(http://docs.python.org/3/library/pdb.html)
    处理命令行选项(http://docs.python.org/3/library/argparse.html)
    正则表达式(http://docs.python.org/3/library/re.html)
    以及更多.

进一步探索标准库的最佳方法是 Doug Hellmann 的 Python Module of the Week 系列（图书版本）以及阅读 Python 官方文档 。

    译者注：《Python Module of the Week》中文版请见 https://pythoncaff.com/docs/pymotw

"""

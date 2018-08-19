import os
import platform
import logging

if platform.platform().startswith('Windows'):
    print(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'))
    logging_file = os.path.join(os.getenv('HOMEDRIVE'),
                                os.getenv('HOMEPATH'),
                                'test.log')
else:
    print(os.getenv('HOME'))
    logging_file = os.path.join(os.getenv('HOME'),
                                'test.log')

print("Logging to", logging_file)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w',
)

logging.debug("Start of the program")
logging.info("Doing something")
logging.warning("Dying now")

"""

$ python stdlib_logging.py
Logging to /Users/swa/test.log

$ cat /Users/swa/test.log
2014-03-29 09:27:36,660 : DEBUG : Start of the program
2014-03-29 09:27:36,660 : INFO : Doing something
2014-03-29 09:27:36,660 : WARNING : Dying now

"""

"""
我们使用标准库中的三个模块——与操作系统进行交互的 os 模块，
与获得比如操作系统等平台信息的 platform 模块以及处理日志（log）信息的 logging 模块。

首先，我们查看 platform.platform() （查看 import platform; help(platform) 获得更多信息）返回的字符串来检查我们所用操作系统类型。
如果是Windows，我们找到要存储信息的主驱动器、用户根文件夹和文件名。把这三个部分放在一起，我们就得到了文件的完整位置。
对于其他平台，我们只需要知道用户的主文件夹，就可以得到文件的完整位置。

我们使用 os.path.join() 函数组合路径的三个部分。
使用特殊函数而不仅仅是将字符串拼接到一起的原因是，这个函数将确保完整位置与操作系统预期的格式相同。
注意：我们在这里使用的 join() 方法是 os 模块的一部分，它与我们使用的字符串方法 join() 不同。

我们可以配置 logging 模块将所有信息以特定格式写入指定文件。

最后，我们可以放置调试、信息、警告甚至严重问题的消息。
一旦程序运行，我们可以检查这个文件，我们将知道在程序中发生了什么，即使没有信息显示给运行程序的用户。
"""

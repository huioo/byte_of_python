# 解决问题的思路

"""

软件开发过程

现在我们已经经历了编写软件的不同 阶段。这些阶段可以概括成以下环节：

    需求（分析需求）
    规格（确定规格）
    编写（编写代码）
    测试（测试与调试）
    使用（操作或部署）
    维护（优化与重构）
    
上面编写备份脚本的过程是一种推荐的编写程序的流程：一开始进行需求分析和系统设计，然后实现一个简单的版本，对它进行测试，有 bug 就进行调试。
接着使用它，确保它能像设计的那样正常工作。再增加你想要的新功能，并继续重复编写-测试-使用的循环，直到软件实现预期的功能。

记住：

    软件是生长出来的，不是构建出来的。—— Bill de hÓra

"""

# 现在我们想要解决的问题：
#     写一个备份我们所有重要文件的程序

# 分析：
#     比如：我们如何界定重要文件，怎么进行存储，放在哪里，等等。

# 适当的分析之后，开始设计我们的程序：
#     一般列出我们需要做的事情。要解决上面的问题，列出以下几个我们想要做的事。
"""
  要备份的文件和目录放在一个列表中。
  备份必须存放在一个主要的备份目录中。
  备份的文件需要打包进 zip里。
  zip 文件的名字是当前的日期和时间。
  使用标准的 zip 命令作为默认打包方式，这样可以运行在所有标准的 GNU/Linux 或 Unix 发行版上。（你可以使用任何提供了命令行接口的归档命令）


    对于 Windows 用户的解决方案

    Windows 用户可以从 GnuWin32 project page 处 安装 zip 命令行，之后把 C:\Program Files\GnuWin32\bin
    放到系统 PATH 环境变量里即可，和 what we did for recognizing the python command itself 里讲的一样。

"""


# 解决方案
#      随着程序的设计意图逐渐清晰合理，我们就可以写出我们的解决方案。
#    新建 backup_ver1.py 文件，具体内容详见 ./example/backup_ver1.py

"""
现在我们处在 测试 阶段，这个阶段我们要做的是测试我们的程序是否运行良好。
如果程序不能如预期般运行，那我们需要进入 调试 阶段，需要修复一些 bugs （错误）。

如果上面的程序不能在你的电脑上运行，复制上面 Zip command is 后面那一行的输出，然后在你的 shell 中粘贴，
看看是否有报错如果有请尝试解决它。同时也查看一下 zip 命令行手册看看可能是什么导致的出错。如果命令行运行正确，
要注意上面的程序只能由 Python 运行，确认下是否准确的由 Python 执行了它。

根据命令的执行结果，我们打印出合适的信息来查看备份成功了还是失败了。

这就是我们目前为止所做的事了，我们成功的创建了一个可以备份我们重要文件的脚本！

现在我们有了一个可以工作的脚本，我们可以在任何我们想备份文件的时候用它。这个阶段称为软件的 运行 阶段或 部署 阶段。

上面的程序运行良好，但（通常）第一个程序并不能非常准确的契合预期。比如，如果没有做良好的设计可能会出问题，或在写代码时出了个错等等。
遇到这种情况的话你就不得不重返 设计 阶段或不得不进入 调试 阶段。
"""

# 修改版
#     第一版的脚本可以正常工作，但我们可以对它进行一些优化，让脚本能更好满足我们的日常需求。
#     这称作软件的 维护 阶段。
#    新建 backup_ver2.py 文件，具体内容详见 ./example/backup_ver2.py

"""
我认为备份文件的命名规则是一处值得改进的地方——使用 时间 作为文件名，而将 日期 作为目录名，文件夹都放在主备份目录下。
这样做的一个优点是备份文件分层存放，便于管理。
第二个优点是备份文件的文件名更短了。
第三个优点是每天独立的目录让你很容易就能知道今天是否进行了备份。因为只有完成了今天的备份，目录才会被建立。

修改版的大部分代码都是一样的。主要的改进之处是使用 os.path.exists 函数检查主备份目录下
有没有以当前日期命名的文件夹，如果没有，则通过 os.mkdir 函数创建一个。
"""


# 第三版
#    新建 backup_ver3.py 文件，具体内容详见 ./example/backup_ver3.py

"""
第二版解决了要做多次备份的问题，第三版要改进的目标是如果有许多需要备份的呢，因为我发现第二版不能区分我们备份的目的！
所以我要做些修改或者说是表现形式，之后的整改我想在 zip 的名字上体现出来。而且也很容易实现，只要把用于提供的名字也附到 zip 上就好了。
"""

# 第四版
#    新建 backup_ver4.py 文件，具体内容详见 ./example/backup_ver4.py

# 更多改进
"""
第四版的程序对大多数用户来说足够了，但程序总有改进的余地。
举个例子：你可以通过指定 -v 选项使 zip 命令具有 交互 级别，让你的程序更有交互性；或者增加一个 -q 选项，让程序能静默运行。

另一个可能的改进是允许通过命令行指定额外需要备份的文件和目录。我们可以通过 sys.argv 列表获得这些名字，然后用 list 类的 extend 方法把他们加到 source 列表里。

最重要的改进可能是不使用 os.system 来创建备份，而用内置的 zipfile 和 tarfile 模块来创建备份。它们是标准库的一部分，你可以直接使用它们，而不需要额外的 zip 程序依赖。

我在上面的示例程序中使用 os.system 纯粹是出于教学需要，因为这样示例足够简单，每个人都能理解，同时也足够真实有用。

你可以尝试编写使用 zipfile 模块而不是  os.system 调用的第五版程序吗？
"""

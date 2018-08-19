import os
import time


# 1. 将要备份的文件和目录分配到一个列表中
# Windows 例子
# source = ['"C:\\My Documents"']
# Mac OS X 和 Linux 例子:
source = ['/Users/swa/notes']
# 注意如果名字中包含空格我们需要用复数引号
# 或者用 raw 字符串  [r'C:\My Documents'].

# 2. 必须备份到主目录中
# Windows 例子:
# target_dir = 'E:\\Backup'
# Mac OS X 和 Linux 例子:
target_dir = '/Users/swa/backup'
# 记得改成你想放的目录

# 3. 文件需要备份到 zip 里。
# 4. zip 的名字需要是当前的日期+时间。
target = target_dir + os.sep +\
         time.strftime('%Y%m%d%H%M%S') + '.zip'

# 如果目录不存在则创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # 创建目录

# 5. 使用 zip 命令把文件放到 zip 里。
zip_command = 'zip -r {0} {1}'.format(target,
                                      ' '.join(source))

# 运行
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
    
"""
运行：
$ python backup_ver1.py
Zip command is:
zip -r /Users/swa/backup/20140328084844.zip /Users/swa/notes
Running:
  adding: Users/swa/notes/ (stored 0%)
  adding: Users/swa/notes/blah1.txt (stored 0%)
  adding: Users/swa/notes/blah2.txt (stored 0%)
  adding: Users/swa/notes/blah3.txt (stored 0%)
Successful backup to /Users/swa/backup/20140328084844.zip
"""

"""
你注意到我们是怎么一步步从 设计 变成 代码 的了吗？

我们利用 os 和 time 模块，所以首先把它们导入。之后，我们把要备份的文件和目录指定到 source 列表中。
我们存储备份的目标目录就放到 target_dir 变量里。我们要创建的 zip 归档文件的名字就用当前日期+时间，
利用 time.strftime() 函数可以完成。同样我们也指定了 .zip 扩展名，之后会被放到 target_dir 目录中。

注意 os.set 变量 - 它会根据你的操作系统变换目录分隔符，比如 GNU/Linux，Unix，macOS 下是 '/',
Windows 下就会是 '\\'。使用 os.sep 代替直接用某个分割符可以让我们的程序具有移植性，也就是可能跨所有平台使用。

time.strftime() 函数需要占位符，比如我们上面程序中写的那些。 %Y 会替换为当前的年份。 %m 则是月份（01~12）。
完整的占位符可以在这里找到 Python 参考手册.  http://docs.python.org/3/library/time.html#time.strftime

我们使用可以 连接 字符串的额外操作符创建目标 zip 文件，它所起的作用也是连接这些字符串并且返回一个新的。
之后我们创建 包含我们将要执行的命令的 zip_command 字符串。之后我们可以检测下这条命令是否可以在 shell 中运行（GNU/Linux 终端或 DOS 提示符）。

我们使用的 zip 命令其实有些额外的选项，其中一个选项是 -r。-r 选项表示 zip 命令应该以递归的方式创建目录，
也就会包含所有在给定目录中的子目录及文件。选项后面跟着的是我们要创建的归档文件名，在之后跟着的是要备份的列表。
同样我们用字符串的 join 方法把 source 列表转换成字符串。

接下来我们终于要 运行 命令了，os.system 函数可以让命令如在 系统 中运行一样。
如果命令运行正常那么会返回 0，否则返回的是错误代码。

Windows 用户注意事项
除了使用双反斜杠转义分隔符，同样可以用 raw 字符串。比如 'C:\\Documents' 或 r'C:\Documents'
都是可以的，但 不要 用 C:\Documents 因为这样会变成你用了一个不知道是什么的转义字符 \D。

上面的程序运行良好，但（通常）第一个程序并不能非常准确的契合预期。比如，如果没有做良好的设计可能会出问题，或在写代码时出了个错等等。
遇到这种情况的话你就不得不重返 设计 阶段或不得不进入 调试 阶段。
"""

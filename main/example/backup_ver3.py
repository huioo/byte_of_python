import os
import time

# 注释看上。
# 1. The files and directories to be backed up are
# specified in a list.
# Example on Windows:
# source = ['"C:\\My Documents"', 'C:\\Code']
# Example on Mac OS X and Linux:
source = ['/Users/swa/notes']
# Notice we had to use double quotes inside the string
# for names with spaces in it.

# 2. The backup must be stored in a
# main backup directory
# Example on Windows:
# target_dir = 'E:\\Backup'
# Example on Mac OS X and Linux:
target_dir = '/Users/swa/backup'
# Remember to change this to which folder you will be using

# Create target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # make directory

# 3. The files are backed up into a zip file.
# 4. The current day is the name of the subdirectory
# in the main directory.
today = target_dir + os.sep + time.strftime('%Y%m%d')
# The current time is the name of the zip archive.
now = time.strftime('%H%M%S')

# 让用户输出一个用于创建 zIp 文件的名字。
comment = input('Enter a comment --> ')
# 检查是否有 comment。
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
        comment.replace(' ', '_') + '.zip'

# Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

# 5. We use the zip command to put the files in a zip archive
zip_command = "zip -r {0} {1}".format(target, ' '.join(source))

# Run the backup
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')

"""
$ python backup_ver3.py
  File "backup_ver3.py", line 39
    target = today + os.sep + now + '_' +
                                        ^
SyntaxError: invalid syntax

这一版的（无法）运行情况。

这程序不能用！ Python 报告了一个语法错误，表示脚本中存在不能让 Python 满意的语法结构。当我们审视 Python 给出的错误时，
就会发现它已经给出错误发生的地方。所以我们要在那一行开始 调试 。

仔细观察后，就可以发现原本是一整行的逻辑链被我们分成了两行但并没指定它们是一起的。
本质上说，Python 发现了额外操作符 + 但并无任何可操作的逻辑行，所以就不知道该怎么继续了。
记住，如果我们要指定一个逻辑行需要与下一行接壤，我们可以在最后的部分使用一个反斜杠。
Ok，现在知道怎么修复了吧。当我们发现了错误并最终矫正程序的做法我们就称之为 修复 bug。
"""

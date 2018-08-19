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

# 如果目录不存在则创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # make directory

# 3. 文件需要备份到 zip 里。
# 4. 当前日期是子目录的名字
today = target_dir + os.sep + time.strftime('%Y%m%d')
# 当前时间是 zip 存档的名字
now = time.strftime('%H%M%S')

# 从用户获取注释作为 zip 文件名
comment = input('Enter a comment --> ')
# 检查用户是否有输入
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' +\
        comment.replace(' ', '_') + '.zip'

# 如果目录不存在则创建
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

# 5. 使用 zip 命令把文件放到 zip 存档里
zip_command = 'zip -r {0} {1}'.format(target,
                                      ' '.join(source))

# 运行备份程序
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')


"""
程序现在可以工作了！让我们回顾一下我们在第三版中做了什么实质性的改进：
我们用 input 函数获得用户输入的注释，并通过 len 函数获得用户输入的长度，以确定用户真的输入了注释。
如果用户什么都没有输入，只是按下了 enter 键，可能这只是一次日常的备份、没什么特别的，那么我们就像之前一样产生文件名。

当用户输入了注释时，注释会被用作 zip 存档的文件名，放在 .zip 扩展名之前。
注意到我们把文件名中的空格替换为下划线了，这是因为以后处理没有空格的文件名更简单。
"""

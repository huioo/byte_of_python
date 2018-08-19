import os
import time

# 1. 需要备份的文件和目录
# 以列表的形式指明
# Windows 的例子：
# source = ['"C:\\My Documents"', 'C:\\Code']
# Mac OS X 和 Linux 的例子：
source = ['/Users/swa/notes']
# 注意到当路径中有空格时
# 你需要使用双重引号

# 2. 备份文件存放路径
# 即主备份路径
# Windows 的例子：
# target_dir = 'E:\\Backup'
# Mac OS X 和 Linux 的例子：
target_dir = '/Users/swa/backup'
# 记得把对应的路径改成你想备份到的地方

# 如果目的目镜不存在，则创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)  # 创建文件夹

# 3. 备份文件被打包为一个 zip 文件
# 4. 当前日期是主备份目录下的一个子文件夹
today = target_dir + os.sep + time.strftime('%Y%m%d')
# 当前时间作为备份文件的文件名
now = time.strftime('%H%M%S')

# zip 文件名
target = today + os.sep + now + '.zip'

# 如果不存在，则创建子文件夹
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

# 5. 用 zip 命令打包文件
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
运行结果：
$ python backup_ver2.py
Successfully created directory /Users/swa/backup/20140329
Zip command is:
zip -r /Users/swa/backup/20140329/073201.zip /Users/swa/notes
Running:
  adding: Users/swa/notes/ (stored 0%)
  adding: Users/swa/notes/blah1.txt (stored 0%)
  adding: Users/swa/notes/blah2.txt (stored 0%)
  adding: Users/swa/notes/blah3.txt (stored 0%)
Successful backup to /Users/swa/backup/20140329/073201.zip
"""

"""
修改版的大部分代码都是一样的。主要的改进之处是使用 os.path.exists 函数检查
主备份目录下有没有以当前日期命名的文件夹，如果没有，则通过 os.mkdir 函数创建一个。
"""

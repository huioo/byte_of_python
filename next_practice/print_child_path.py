"""

循环递归打印给定目录中的子文件夹名即文件名
"""
import os


def print_directory_path(s_path, level=0):
    if level == 0:
        prefix = []
    else:
        prefix = ['  ']*(level-1)+['  +']
    print(*(prefix + [s_path]), ':')


def print_file_name(name, level=0):
    prefix = ['  ']*(level-1)+['  |']
    print(*(prefix + [name]))


def print_directory_contents(s_path, level=0):
    """
    这个函数接受文件夹的名称作为输入参数，
    返回该文件夹中文件的路径，
    以及其包含文件夹中文件的路径。

    """
    print_directory_path(s_path, level)
    for sChild in os.listdir(s_path):
        s_child_path = os.path.join(s_path, sChild)
        if os.path.isdir(s_child_path):
            print_directory_contents(s_child_path, level=level+1)
        else:
            print_file_name(sChild, level=level+1)


if __name__ == '__main__':
    print_directory_contents('F:/WorkSpace/PyCharm/byte_of_python/main')



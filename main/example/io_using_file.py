poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''

# 打开文件进行 'w'riting 写操作
f = open('poem.txt', 'w')
# 将文本写入到文件
f.write(poem)
# 关闭文件
f.close()

# 如果没有指定文件打开方式
# 默认使用 'r'ead 读模式
f = open('poem.txt')
while True:
    line = f.readline()
    # 零行意味着 EOF 文件结尾
    if len(line) == 0:
        break
    # `line` 中已经自带换行了
    # 因为它是从文件中读取出来的
    print(line, end='')
# 关闭文件
f.close()


"""
$ python3 io_using_file.py
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
"""

"""
通过 open 方法我们很容易就能创建新的文件对象。
我们指定文件名和打开方式，通过内置的 open 函数打开文件，当文件不存在时则创建文件。
文件有很多种打开模式，可以是：读模式（'r'），写模式（'w'）或追加模式（'a'）。
我们也可以指定以什么方式进行读、写和追加，是文本模式（'t'）还是二进制模式（'b'）。
还有很多打开模式的组合，你可以通过 help(open) 命令来查看详细的说明。默认情况下 open() 认为文件以文本模式打开进行读取操作。


在我们的例子里，第一次我们用 write 方法读取/创建了这个文件，并把字符串变量写入文件里，之后我们用 close 关闭了文件。
接下来我们再次打开同一个文件用于读取。我们不需要指定模式，因为默认的读取文件模式已经足够了。
我们在主循环中通过 readline 方法读取文件中的每一行。这个方法每次会返回包括换行符在内的一整行。
当读到 空 字符时，就说明已经到了文件的结尾，我们就可以跳出主循环了。
最后，我们用 close 关闭了文件。

从 readline 的输出中我们可以得知：这个程序已经成功地把小诗写入了 poem.txt 文件，并可以从中读取出来，打印到屏幕上。
"""

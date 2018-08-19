import sys
import time

f = None
try:
    f = open("poem.txt")
    # 我们通常读取文件的语句
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        sys.stdout.flush()
        print("Press ctrl+c now")
        # 让程序保持运行一段时间
        time.sleep(2)
        print()
except IOError:
    print("Could not find file poem.txt")
except KeyboardInterrupt:
    print("!! You cancelled the reading from the file.")
finally:
    if f:
        f.close()
    print("(Cleaning up: Closed the file)")

"""
$ python exceptions_finally.py
Programming is fun
Press ctrl+c now
^C!! You cancelled the reading from the file.
(Cleaning up: Closed the file)
"""

"""
我们做了正常的文件读取，但我们在每行输出之后用 time.sleep 函数特意加入了2秒的休眠，这样程序就会缓慢运行（通常 Python 运行很快）。
当程序还在运行时，按下 ctrl + c 来终止或取消程序运行。.

观察到 KeyboardInterrupt 异常被抛出以及程序退出。但是，在程序退出前， finally 子句被执行，文件对象总是被正确关闭。

请注意， Python 将变量中的 0 、 None 、空数组和空集合都视为 False 。
这就是为什么我们可以在上面的代码中使用  if: f 。

还要注意，我们在 print 之后使用 sys.stdout.flush() ，这样就可以立刻输出到屏幕上。
"""

with open("poem.txt") as f:
    for line in f:
        print(line, end='')

"""
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
"""

"""
输出应该与之前一个示例相同。这里的不同点是，我们将 with 语句和 open 函数一起使用——我们让 with open 自动完成文件关闭。

with 语句隐藏地使用了一个规则。它获取了 open 语句返回的对象，这里我们称之为 "thefile" 。

它开始它下面的这个代码块前 总是 调用 thefile.__enter__ 函数，在离开这个代码块后 总是 调用 thefile.__exit__ 。

因此，被我们写入 finally 语句块的代码会被 __exit__ 方法自动完成。这避免我们重复地显示使用 try..finally 语句。

www.python.org/dev/peps/pep-0343/
"""

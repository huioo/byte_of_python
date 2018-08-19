# 控制流
"""
通常一系列的语句被Python以精确的自上而下的顺序执行。
那么如何改变它的执行流程，例如需要程序根据不同的情况作出一些决定和做不同的事情，像是根据一天中的时间打印“早上好”或“晚上好”。

这可以通过控制语句来实现。在Python中，有 if、for 和 while 三个控制流语句。
"""


# if语句
def if_func():
    """
    if 语句用于检查一个条件：如果条件是真的，我们运行一个语句块（称为 if-block），
    否则我们执行另一个语句块（称为 else-block）。else 语句是可选的。
    
    if语句结尾处有一个冒号——表名后面跟着一个语句块。
    elif 从句，它将两个相关的 if else-if else 语句组合成一个 if-elif-else 语句。
    elif 和 else 语句必须在逻辑行的结尾处有一个冒号，后面跟着相应的语句块（当然，要有适当的缩进）。
    """
    number = 23
    # input()方法获得用户的猜测数
    guess = int(input('Enter an integer:'))
    
    if guess == number:
        # 新程序的开始块
        print('Congratulations, you guessed it.')
        print('(but you do not win any prizes!)')
        # 新程序块的结尾处
    elif guess < number:
        # 另一个程序块
        print('No, it is a little higher than that')
        # 你可以在程序块中“为所欲为”——做任何你想做的事情
    else:
        print('No, it is a little lower than that')
        # 只有当猜测数大于给定数的时候，才会执行此处
    
    print('Done')
    # 在 if 语句执行结束后，最后的这句语句总是会被执行。
    
    """
    在 Python 执行完完整的 if 语句以及相关的 elif 和 else 从句后，它会继续往下执行包含 if 语句的语句块中的下一个语句。
    
    在一个 if 语句的 if 语句块中还可以再嵌套一个 if 语句，我们称之为嵌套的 if 语句。
    记住， elif 和 else 部分是可选的。最迷你的合法有效的一个 if 语句为：
    """
    if True:
        print('Yes, it is true')


# while 语句
def while_func():
    """
    将 input 和 if 语句移动到 while 循环地内部，并在 while 循环之前将变量 running 设置为 True 。
    首先，我们检查变量 running 是否为 True ，然后继续执行相应的 while 语句块 。
    执行完该语句块以后，再检查条件是否成立，在本例中，条件是变量 running 。
    如果条件为真，我们就再次执行 while 语句块，否则我们将继续向下执行可选的 else 语句块，然后继续向下执行下一个语句。
    
    else 语句块会在 while 循环的条件变为 False 时执行——甚至有可能在第一次检查条件时，条件就是 False 。
    如果 while 循环中有一个 else 从句，它总是会执行到，除非用 break 语句跳出循环时，才不会执行到。
    """
    number = 23
    running = True
    
    while running:
        guess = int(input('Enter an integer : '))
    
        if guess == number:
            print('Congratulations, you guessed it.')
            # 这会导致 while 循环停止
            running = False
        elif guess < number:
            print('No, it is a little higher than that.')
        else:
            print('No, it is a little lower than that.')
    else:
        print('The while loop is over.')
        # 你可以在此处继续进行其它你想做的操作
    
    print('Done')


# for语句
def for_func():
    """
    for..in 语句是另一种循环语句，它会 迭代 对象序列，即会遍历序列中的的每个项。
    
    range()方法接受2个参数，返回从第一个数字开始到第二个数字结束的数字序列，例如range(1,5) 得到序列 [1, 2, 3, 4]。
    默认情况下，range 的步长为 1 .如果我们为 range 函数提供第三个数字，那么这就是步长。
    例如，range(1,5,2) 得到 [1,3] 。记住，返回的序列的范围 不 包含第二个数字。
    
    for 循环对这个范围进行遍历—— for i in range(1,5) 等价于 for i in [1, 2, 3, 4] ，
    就像是将序列中的每一个数字（或对象）分配给 i 一样，一次只分配一个。然后对 i 的每个值执行语句块。
    
    else 部分是可选的。如果程序有该部分，那么在 for 循环结束后一定会执行一次该部分。除非遇到 break 语句。
    """
    for i in range(1, 5):
        print(i)
    else:
        print('The for loop is over')
    

# break语句
def break_func():
    """
    break 语句是用来中断循环语句，即直接停止循环语句的执行，就算循环条件没有变为False或者序列没有迭代到最后一项。
    需要重点关注的是，如果你 中断 了一个 for 循环或者一个 while 循环，任何相应循环的 else 语句块都不会被执行。
    
    重复输入内容，然后打印每次输入的长度。输入“quit”，中断循环来终止程序，然后到达程序的结尾处。
    break也可以与for循环一起使用。
    """
    while True:
        s = input('Enter something : ')
        if s == 'quit':
            break
        print('Length of the string is', len(s))
    print('Done')


# continue语句
def continue_func():
    """
    continue 用来告诉Python跳过当前循环语句块中的其余部分，然后继续执行循环的下一个迭代。
    
    接受用户输入的内容，只处理长度至少为3的输入字符串。continue也可以和for一起使用。
    """
    while True:
        s = input('Enter something: ')
        if s == 'quit':
            break
        if len(s) < 3:
            print('Too small')
            continue
        print('Input is of sufficient length')
    
    print('Done')






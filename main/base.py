# 这里的文本，主要用作程序读者的注释
# 注释也可以使用 ''' 注释 ''' 或 """ 注释 """
"""
 注释
"""
'''
 注释
'''

# 例如：print是一个函数
print("help(len) 的结果信息：")
# help方法，获取帮助信息
help('len')

# print()函数参数：end表示结尾的字符，sep表示多个参数的中间连接字符
print('a', end='')
print('b', end=', ')
print('c', 'd', 'e', sep=' + ')
print('*'*20)

# 复制运算符（=）将常量5赋给变量i。称之为（陈述）语句，因为它陈述了需要完成的一些事情。
i = 5
print(i)

# 文字常量，值不能改变的为常量
print('文字常量:', '5', '1.23', '\n字符串:', 'This is a string', "It's a string")
# 字符串是 字符 的序列。字符串本质上是一堆单词。
# 指定字符串
# 1)单引号：
'Quote me on this'
# 2)双引号：
"What's your name?"
# 3)三引号：使用三引号——（""" 或 '''）指定多行字符串，可以在三引号中自由地使用单引号和双引号：
'''This is a multi-line string. This is the first line.
This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond."
'''
# 字符串是不可改变的
"""
 字符串含有 “'”，可以使用 “"”，例如："What's your name?"，而不能使用 'What's your name?'
 也可以使用 “\” 转义符号来实现，将单引号指定为 “\'”，例如 'What\'s your name?'
"""

# 指定两行字符串
# 1)使用换行符 \n
print('This is the first line\nThis is the second line')
# 2)使用三引号
print('''This is the first line
This is the second line''')
# 使用“\”，放在行尾表示字符串在下一行继续，单不添加换行符；
print('This is the first line \
This is the second line')
print(20*'*')

# 原始字符串
# 如果你需要指定一些没有特殊处理（转义）的字符串，那么你需要指定一个“原始”字符串，指定方法是在字符串前面加上“r”或“R”。
r"Newlines are indicated by \n"
print(20*'*')


# 数字，分为整数和浮点数
print('整数:', 2, sep='\t')
print('浮点数:', 3.23, 52.3E-4, 'floating point numbers，简称floats', sep='\t')


# 变量
# 变量的值可以变化，变量只是存储信息的计算机内存中的一部分。和文字常量不同的是，你需要一些方法来访问这些变量，因此你需要为它们命名。
# 变量可以直接通过赋值来使用，不需要任何声明活着数据类型定义。
i = i + 1
print(i)

# 标识符命名
# 变量是标识符的例子。标识符 是用来标识 某事物的名的名称。在命名标识符的时候必须遵循一些规则：
"""
 标识符的第一个字符必须是字母（大写 ASCII 或小写 ASCII 或 Unicode 字符）或者下划线 （_）。
 标识符的其余部分可以由字母、下划线 (_) 或者数字 (0-9) 组成。
 标识符的名称区分大小写。例如， myname 和 myName 是 不 相同的。注意前者中的小写 n 和后者中的大写 N 。
 有效标识符名称的例子有 i、name_2_3。 无效 标识符名称的例子有 2things、this is spaced out、my-name 以及 >a1b2_c3。

"""

# 数据类型
# 变量可以保存不同类型（数据类型）的值。基本类型是数字和字符串。

# 对象
# python中一切皆对象，从某种意义上来讲，Python的面相对象是非常纯粹的，因为一切皆对象，包括数字、字符串和函数。

# 逻辑行，物理行
"""
物理行是当你在写程序的时候，你眼睛可以看见的行。
逻辑行是Python看到的一个程序语句。Python默认每一个物理行对应一个逻辑行。
一个逻辑行的一个例子就是一个语句，如 print('hello world!')

默认情况下，Python推荐一行一个语句，这会使代码更具有可读性
如果你希望在单个物理行中编写更多的逻辑行，则必须使用分号 (;) 显式地指定此逻辑行/此语句的结尾。
例如：i = 5; print(i);
"""

# 缩进
"""
 空格在Python中非常重要。实际上，行首的空格非常重要。这就是所谓的缩进。
 逻辑行开头的前导空格（空格和制表符）用于确定逻辑行的缩进级别，然后用于确定语句的分组。
 这意味着同一组的语句 必须 有相同的缩进。每一个这样的语句集被称为 语句块 。

 需要牢记的一件事情是，错误的缩进会导致报错。例如：


i = 5
# 错误如下！注意，在行的开头处有一个空格
 print('Value is', i)
print('I repeat, the value is', i)

当你运行该程序时，你会得到下面的错误：

  File "whitespace.py", line 3
    print('Value is', i)
    ^
IndentationError: unexpected indent

 如何缩进
 使用四个空格进行缩进。这是Python的官方建议。
 Python将始终使用缩进进行分块，永远不会使用花括号。
"""

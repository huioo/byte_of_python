# 函数
"""
函数是程序中可以复用的部件。函数允许你为一个语句块取一个特定名字；通过使用这个特定的名字，你可以随时随地地调用这个语句块。
这个过程被称为 调用 这个函数。例如：len() 、 range()

使用关键字 “def” 来定义函数。紧接着这个关键字，我们定义该函数的 标识符 名称；然后跟上一对小括号，小括号中可能包含一些变量的名字；
最后，我们再在最后一行的末尾写上一个冒号。而接下来便会是一个语句块，它是该函数的一小部分。
"""


def say_hello():
    # 属于该函数的语句块
    print('hello world')
    

say_hello()     # 调用
say_hello()     # 再次调用


# 函数参数
"""
函数参数就是调用函数时你提供给函数的值，这样函数就可以用这些值做一些事情。
这些参数就像变量一样，只不过参数的值是在调用函数时定义的，在函数运行时参数已经被赋值了。
参数在函数定义时在圆括号内指定，并用逗号分分割， def func_name(para1, para2)。
当我们调用函数时，我们用同样的方式提供值。

形参：函数定义时括号内的参数叫做形参；
实参：调用函数时提供的参数叫实参；
"""


def print_max(a, b):
    # a, b 形参
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')


# 直接传递字面量
print_max(3, 4)
x, y = 5, 7
# 实参 x, y
print_max(x, y)


# 局部变量
"""
当你在一个函数中声明变量时，这些变量与函数外部使用的重名的其它变量没有关系——即，变量名对于函数来讲是 局部的（只在函数内部有效）。
我们称之为变量的 作用域 。从变量名被定义的地方开始，所有的变量都具有作用域，即声明变量时所处的语句块。

"""
x = 50


def func(x):
    """
    当我们在函数体的第一行中，第一次打印输出变量名为 x 的 值 的时候，
    Python 会将主语句块（位于函数定义的上面）中声明的参数值打印输出。
    
    接下来，我们将值 2 赋给 x 。对于我们定义的函数来讲， x 是局部的。
    因此，当我们改变函数中 x的值时，主语句块中定义的 x 不会受到任何影响。
    
    程序的最后一个 print 语句，我们用它来显示主语句块中定义的 x 的值，
    从而确认它实际上不会受到前面调用的函数中局部赋值的影响。
    """
    print('x is', x)
    x = 2
    print('Changed local x to', x)


func(x)
print('x is still', x)


# global语句
"""
不在任何函数或类的定义内的变量也叫做程序的顶级 top level 变量。
如果你要在函数内给这种变量赋值，你需要告诉Python这个变量并非本地变量，它是一个全局变量。
为此，我们需要使用global语句。不使用global语句你就不可能给在函数外定义的变量赋值。

如果函数内没有同名变量，你可以使用在函数外部定义的变量。不推荐这么做，容易疑惑，不知道该变量在哪儿定义。
如果使用global则可以清楚的表示变量是在函数外部定义的。

"""
x = 50


def func():
    """
    global 用于声明 x 是一个全局变量，因此当我们在函数内部为x赋值时，主程序块中x的值也改变了。
    可以在global语句中同时指定多个全局变量，就像这样：global x,y,z
    """
    global x
    print('x is', x)
    x = 2
    print('Changed global x to', x)


func()
print('Value of x is', x)


# 默认参数值
"""
对于某些函数，你可能想让某些形参是 可选的，并在用户没有指定这些形参的值时，使用默认值。你可以通过默认形参值来实现这个功能。
你可以在函数定义时给某些形参名后加上赋值操作符 = 与对应形参的默认值，这样就为形参指定了默认值。

注意，形参的默认值必须是常数。更准确的说，默认值是不可改变的。

只有形参列表末尾的参数才能指定默认值，即你不能在声明参数列表时先声明有默认值的形参，然后再声明没有默认值的形参。
这是因为给形参赋值时时按照实参的顺序进行的。
例如函数声明 def func(a, b=5) 是有效的，而函数声明 def func(a=5, b) 是 无效的。
"""


def say(message, times=1):
    """
    say 函数用于多次输出指定的的字符串。如果我们不指定输出次数，它只会默认打印一次。
    我们通过将默认值 1 赋给形参 times 来实现这一点。
    """
    print(message * times)


say('Hello')
say('World', 5)


# 关键字参数
"""
如果你的一些函数需要许多参数，而你只想指定其中的一部分。那么你可以通过为这些参数命名来给它们赋值，这叫做 关键字参数。
使用名字（关键字）而不是位置来给函数指定实参。这样做有两个优势：
其一，这样给函数传递参数时更加简单，因为我们不需要担心参数的位置。
其二，我们可以只给我们想要改变的参数赋值，让其他参数使用默认值。
"""


def func(a, b=5, c=10):
    """
    函数 func 共三个参数。一个没有默认值的参数，以及两个有默认值的参数。
    """
    print('a is', a, 'and b is', b, 'and c is', c)


func(3, 7)
func(25, c=24)
func(c=50, a=100)


# 可变参数
"""
有时候你可能想要定义一个能接收 任意个 数参数的函数。例如定义一个参数个数可变的函数，你可以通过使用星号 * 来实现这个功能。
"""


def total(a=5, *numbers, **phonebook):
    """
    当我们声明一个带星号的参数 *param 时，从这个参数开始，之后的的所有参数都会被收集进入一个名为 param 的元组中。
    类似的，当我们定义了一个带两个星号的参数 **param 时，从这个参数开始，之后的所有参数都会被收入名为 param 的字典中。
    """
    print('a', a)

    # 遍历元组中的所有项
    for single_item in numbers:
        print('single_item', single_item)

    # 遍历字典中的所有项
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))


# return 语句
"""
return 语句用于从一个函数返回，即跳出这个函数。我们也可以从函数跳出时返回一个值，返回值是可选的。
注意没有返回值的 return 语句等价于 return None。None 在 Python 是一种代表「没有任何东西」特殊的类型。
例如：如果一个变量的值是 None，则说明这个变量尚未被赋值或值已被清空。
如果你的函数没有 return 语句，系统会自己在函数的结尾添加 return None 语句。
"""


def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y


print(maximum(2, 3))


# pass 语句在Python中用于表示一个空的语句块，通常用于占位。
def some_function():
    pass


print(some_function())    # None


# 文档字符串————DocStrings
"""
Python 有一个十分美妙的特性 文档字符串 (documentation strings)，通常简称为 DocStrings。
DocStrings 是一个十分重要的工具，你应该多使用它，它能让你的程序变得更加简单易懂。
神奇的是，在程序运行时，我们也能查看 DocStrings。

DocStrings 的书写惯例是：首行首字母大写，结尾有句号；第二行为空行；第三行以后为详细的描述。
我们 强烈建议 你在编写任何非平凡函数时都遵守这种惯例，那些只有几行的平凡函数可以不遵守这个惯例。
"""


def print_max(x, y):
    """Prints the maximum of two numbers.
    
    The two values must be integers."""
    # 如果有必要，将参数转为整数
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')


print_max(3, 5)
print(print_max.__doc__)


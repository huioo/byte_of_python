# 面相对象编程

"""
使用函数、块语句来操作我们的数据，这叫做 面相过程 的方式进行编程。
然后还有另外一种方式来组织你的程序：把数据和函数结合起来，并将其置入一种叫作对象的东西。这叫做面相对象 编程范式。

在大多数情况下，你可以使用面向过程的编程，但是当写大型程序或者遇到了一些更加适合这种方法的时候，你可以使用基于对象的编程技术。

类和对象是面向对象编程的两个主要概念。一个类创造了一种新的 类型 ，而对象就是类的实例。
一种观点是：你可以把 int 类型的变量翻译为存储着整型的变量，这个变量是 int 类的一个实例。


对静态语言编程者的提示

    注意整型被看待为一个int类的对象。这一点与 C++ 和 Java ( 早于 1.5 版本）不同。在这些语言中，整型被看成一种基本数据类型。

    C# 和 Java 1.5 的使用者会发现这个非常类似装箱与拆箱的概念。

"""

"""
对象能够使用原始变量（ 属于 对象）存储数据。
属于对象或者类的变量被称作域。
一个对象可以通过使用 属于 类的函数实现一定的功能。这些函数被称作类的方法。
这个术语是非常重要的，因为它帮助我们区分独立的函数和变量及属于对象或者类的变量和函数。
总的来说，域和方法可以被看作类的属性。

域有两种类型 - 他们可以属于每一个类的实例（也就是对象），也可以属于类本身。他们被分别称作实例变量和类的变量。
使用 class 关键字来创建一个类。这个类的域和方法被列在一个代码块中。
"""

# self
"""
类的方法与普通的函数相比只有一个区别 - 他们在入口参数表的开头必须有一个额外的形式参数，但是当你调用这个方法的时候，
你不会为这个参数赋予任何一个值，Python 会提供给它。这个特别的参数指向对象 本身 ，约定它的名字叫做 self .

尽管你可以给这个参数起任何一个名字，但是这里 强烈推荐 使用 self —— 任何其他的名字绝对会引起不满。
使用一个标准的名字有许多优点 - 如果你使用 self ，任何程序的渲染器将会自动的识别它，
甚至一些特定的 IDEs (Integrated Development Environments) 可以给你提供额外的帮助。

给 C++/Java/C# 使用者的提示

    Python 中的 self 和 C++ 中的 this 指针以及 Java 和 C# 中的 this 引用等价。
"""

"""
你一定好奇 Python 是如何给 self 赋值的，以及为什么你不必给它赋值。一个例子将会把这些问题说明清楚。

假设你有一个类叫做 MyClass 以及这个类的一个对象叫做 myobject 。
当你需要这样调用这个对象的方法的时候：myobject.method(arg1, arg2) ，
这个语句会被 Python 自动的转换成 MyClass.method(myobject, arg1, arg2)
    这样的形式 —— 这就是 self 特殊的地方。

这也意味着如果你有一个不声明任何形式参数的方法，却仍然有一个入口参数 —— self 。
"""


# 类
"""
最简单的类可能如下代码所示（保存为文件  oop_simplestclass.py )。

class Person:
    pass  # 一个空的语句块

p = Person()
print(p)

输出:

$ python oop_simplestclass.py
<__main__.Person instance at 0x10171f518>

这是如何工作的

我们使用 class 语句和类名创建了一个类。在这之后跟着一个语句块形成了类的主体。
在这个例子中，我们使用 pass 语句声明了一个空的语句块。

之后，我们使用类的名字和一对括号创建了一个类的对象（实例）。我们通过简单地打印变量 p 的方法确认这个变量类型。
结果证明这是 __main__ 模块中 Person类的一个对象（实例）。

注意这个对象在内存中的地址也被显示出来。这个地址可能在你的电脑上有一个不同的值，这是由于 Python 只要找到空闲的内存空间就会在此处存放这个对象。
"""


# 方法
"""
我们已经讨论了类和对象可以拥有一些方法正如普通的函数。但是这些方法有一个额外的 self 变量。现在我们来看一个例子（保存为文件 oop_method.py ）。

class Person:
    def say_hi(self):
        print('Hello, how are you?')

p = Person()
p.say_hi()
# 上面两行也可以写成下面这种形式
# Person().say_hi()

输出：

$ python oop_method.py
Hello, how are you?

注意到在 say_hi 方法中没有取得任何一个参数，却在方法定义的时候仍然有一个 self 参数。
"""


# __init__ 方法
"""
对 Python 类来说，许多方法名有特别的重要性。现在，我们来考察一个重要的 __init__ 方法。

__init__ 方法将在类的对象被初始化（也就是创建）的时候自动的调用。
这个方法将按照你的想法 初始化对象（通过给对象传递初始值）。
请注意这个名字的开头和结束都是双下划线。

例子（保存为文件  oop_init.py ）：
class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Swaroop')
p.say_hi()
# 上面两行也可以写成下面这种形式
# Person().say_hi()

输出：

$ python oop_init.py
Hello, my name is Swaroop

"""

"""
这里，我们定义了 __init__ 方法。这个方法除了通常的 self 变量之外，还有一个参数 name 。
这里我们创建了一个新的也叫做 name 的域。注意这里有两个不同的变量却都被叫做 'name' 。
这是没有问题的，因为带点的标记 self.name 表示有一个叫做 "name" 的域是这个类的一部分，而另外一个 name 是一个局部变量。
这里我们显式地指出使用哪个变量，因此没有任何冲突。

当新建一个新的 Person 类的实例 p 的时候，我们通过调用类名的方式来创建这个新的实例，在紧跟着的括号中填入初始化参数：p = Person('Swaroop') 。

我们没有显式的调用 __init__ 这个方法，这是这个方法特殊之处。
正如 say_hi 方法所示的，现在我们在我们的方法之中可以使用 self.name 这个域了。
"""


# 类和对象中的变量
'''
我们已经讨论了关于类和对象中函数的部分（也就是方法），现在让我们来学习关于数据的部分。
数据的部分（也就是域）并不是什么特别的东西，只是一些 绑定 到类或者对象命名空间的普通的变量。
这意味着这些变量只在和这些类和对象有关的上下文中有效。
这就是为什么他们被称作 命名空间 。

有两种类型的 域 -- 类变量和对象变量。
这是通过他们是 属于 类还是 属于 对象这一点来区分的。

类变量是共享的 -- 他们可以通过所有这个类的对象来访问。
类变量只有一份拷贝，这意味着当一个对象改变了一个类变量的时候，改变将发生在所有这个类的对象中。

对象变量属于每一个对象（实例）自身。在这种情况下，每一个对象都有属于它自己的域（在不同的对象中，这些变量不是共享的，
它们也并不相关，仅仅是名称相同。

一个例子将会让这些便于理解（保存到文件  oop_objvar.py ）：
class Robot:
    """代表一个机器人，拥有一个名字属性"""

    # 类属性，统计机器人的个数
    population = 0

    def __init__(self, name):
        """初始化数据"""
        self.name = name
        print("(Initializing {})".format(self.name))

        # 当机器人被生产出来的时候
        # 机器人人口增加
        Robot.population += 1

    def die(self):
        """啊！我要死掉了。"""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(
                Robot.population))

    def say_hi(self):
        """来自机器人的问候

        是的，他们有这种功能"""
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        """显示当前人口数。"""
        print("We have {:d} robots.".format(cls.population))

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()

输出：

$ python oop_objvar.py
(Initializing R2-D2)
Greetings, my masters call me R2-D2.
We have 1 robots.
(Initializing C-3PO)
Greetings, my masters call me C-3PO.
We have 2 robots.

Robots can do some work here.

Robots have finished their work. So let's destroy them.
R2-D2 is being destroyed!
There are still 1 robots working.
C-3PO is being destroyed!
C-3PO was the last one.
We have 0 robots.


类变量和对象变量之间的区别：
population 属于 Robot 类，因此是一个类变量。
    population 类变量应当用 Robot.population 来访问，而非self.population。
    还可以通过 self.__class__.population 来访问这个类对象，因为每一个对象都通过 self.__class__ 属性指向自己的类。
name 变量属于每一个个体（使用 self 来指向）因此是一个对象变量。
    name 对象变量应当使用 self.name 来访问。
    
注意：
    一个与类变量同名的对象变量将会把这个类变量屏蔽。
    

how_many 实际上是一个属于类的方法，而非属于对象的方法。使用一个装饰器来标记 how_many 方法，并将其作为一个类方法。
装饰器可以被想象成为一个快捷的方式去调用一个包裹函数（一个包裹着另外一个函数的函数，因此可以在内部函数调用之前及之后做一些事情），
因此使用 @classmethod 装饰器和如下调用等价：
    how_many = classmethod(how_many)


__init__ 方法被用作初始化一个Robot实例，并给这个机器人取一个名字。在这个方法中，我们获得一个新的新机器人，就使得 population 增加1。
此外，注意到self.name变量的值会因对象的不同而不同，这就展现了对象变量的自然之处。


属性引用 (attribute reference):
请记住，你 只能 通过 self 来指向同一个对象的变量和方法。这被称为 属性引用 (attribute reference) 。


在这个程序中，我们还可以看到 文档字符串 (docstrings) 在类和方法值中的使用。
运行时，我们可以通过 Robot.__doc__ 来访问类的文档字符串以及通过  Robot.say_hi.__doc__ 来访问方法的文档字符串。


在 die 方法之中，我们单纯的使得 Robot.population 减少 1 。


所有的类成员都是公共的.
只有一种情况除外：如果你使用 双下划线前缀 （例如 __privatevar ）时，
Python 会使用命名粉碎规则 (name-mangling) 作用于这个变量，并使其变为私有变量。


因此，结论就是所有的仅在类和对象之中的变量应当使用一个下划线来开头，所有其他的命名都是公共的，可以被其他类和对象访问。
请记住这只是约定而非 Python 强制规定（使用双下划线除外）。
'''


# 继承
"""
面向对象编程的主要优势之一就是代码的重用，一种获得代码重用的主要方式就是继承体系。
继承可以被想象成为类之间的一种类型和子类型的关系的实现。

假设你想要写一个程序来跟踪一所大学之中的老师和同学。他们有一些共同的特征，比如名字、年龄、地址等。
他们还有一些独有的特征，比如对老师来说有薪水、课程、离开等，对学生来说有成绩和学费。

你当然可以为这两种类型构建两种独立的类来驱动程序。但是当需要添加一个共同的属性的时候，意味着需要在这两个独立的类中同时添加。这很快就会变得非常笨拙。

一个更好的办法就是构造一个共同的类  SchoolMember ，然后在让老师和学生分别 继承 这个类。
换句话说，他们都是这个类型（类）的子类型，之后我们也可以为这些子类型添加独有的属性。

这种方式有许多的好处。
如果我们想要添加或者改变 SchoolMember 类中的功能，这将也会自动地反映在子类型之中。
举个例子，你可以通过简单的修改 SchoolMember 类的方式来为学生和老师添加新的 ID 卡的域。然而，一个子类型之中的变化不能够反映在其他子类型之中。

另外一个好处就是你可以使用一个 SchoolMember 对象来指向任意一个老师或者学生的对象。这将会在某些情况下非常有用，比如统计学校中人的总数。
这被称作多态：如果有父类型的话，子类型可以在任何一种情况下被替代。也就是说，一个子类型的对象可以被当作父类型的实例。

此外，注意到我们重用了父类的代码。不需要在不同的类中重复这些代码，只要我们不使用独立的类的方式来实现。

 SchoolMember 类在这种情况下被称为基本类或者超类。而 Teacher 和 Student 类被成为派生类或者子类。
 
 
我们来看看这个例子（保存为 oop_subclass.py ）：

class SchoolMember:
    '''代表了学校中的任何一个成员'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        '''告诉我细节'''
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
    '''表征一个老师'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))

class Student(SchoolMember):
    '''表征一个学生'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

# 输出一个空行
print()

members = [t, s]
for member in members:
    # 所有的老师和学生都可用
    member.tell()

输出：

$ python oop_subclass.py
(Initialized SchoolMember: Mrs. Shrividya)
(Initialized Teacher: Mrs. Shrividya)
(Initialized SchoolMember: Swaroop)
(Initialized Student: Swaroop)

Name:"Mrs. Shrividya" Age:"40" Salary: "30000"
Name:"Swaroop" Age:"25" Marks: "75"


为了使用继承，我们在类名之后的括号中指明父类的类名。（举个例子， class Teacher(SchoolMember) ）。
之后我们可以看到在 __init__ 方法中，通过  self 变量显式的调用了父类的 __init__ 方法来初始化子类对象中属于父类的部分。
这非常重要，请记住 -- 既然我们在 Teacher 和 Student 子类中定义了 __init__ 方法，
Python 不会自动的调用父类 SchoolMember 中的构造方法，你必须显式的调用。

相反的，如果我们不定义子类的 __init__ 方法，Python 将会自动地调用父类中的构造方法。

当我们想把 Teacher 或者 Student 的实例当作 SchoolMember 的实例，并且想调用 tell 方法的时候，
只需要简单的输入 Teacher.tell 或者 Student.tell即可。

我们在每个子类之中定义了另一个新的 tell 方法（ 父类 SchoolMember 的 tell 方法作为其中的一部分）来定制子类的功能。
因为我们已经做了这样的工作，当我们调用 Teacher.tell 的时候， Python 将会使用子类中 tell 方法，而非父类的。
然而，如果我们没有在子类中定义 tell 方法，Python 将使用父类中的方法。
Python 总是首先在实际的子类中寻找方法，如果不存在，将会按照子类声明语句中的顺序，依次在父类之中寻找（在这里我们只有一个父类，但是你可以声明多个父类）。


注意术语 -- 如果有超过一个类被列在继承元组之中，这就叫做多重继承。

end 参数在父类 tell() 方法中调用的 print 函数中被使用，以使得打印完一句话之后，下一次打印紧接在第一句话之后，而不换行。
这个技巧可以使得 print 函数在输出结束时不打印 \n 符号（换行）。
"""


# 数据结构
"""
数据结构基本上是这样的 - 它们是能够将一些数据组合在一起的一种结构。换句话说，它们被用来存储相关数据的集合。

Python 中有四种内置的数据结构 - list, tuple, dictionary and set。

"""


# List
"""
List 是一种保存有序项集合的数据结构。也就是说，你可以在列表中存储一系列项。
这很容易想象，如果你有一系列的东西要买就会思考出一个购物清单，可能在你的购物清单中每一项都有一个单独的行，而在 Python 中你使用逗号隔开它们。

项目列表应该使用方括号扩起来，以便 Python 能够理解您正在定义一个列表。一旦创建了列表，你就可以在列表中增加，删除或者搜索列表中的项 。
正因为我们可以增加和删除项，所以我们称列表是一种 可变 数据类型，也就是说这个类型可以被改变。
"""


# 对象和类的简介
"""
当我们使用一个变量 i 并为它赋值时，例如将整数 5 赋值给它。我们可以将其看作是创建一个对象 i （即，实例）的过程，它对应的 类 （即，类型）为 int 。
实际上，你可以通过查看 help(int) 来更好地理解这一点。

一个类也可以有方法，即只能被该类调用的函数。只有当你拥有该类对象时，才能使用这些函数。例如，Python为列表提供了一个append函数，它允许你在列表的
末尾添加一个元素或项。例如，mylist.append('an item') 会把那个字符串添加到列表mylist中。
注意，我们使用点（.）来访问对象中的方法。

一个类也可以有字段，它们是为该类定义的变量。只有当你拥有该类的对象时，才可以使用这些变量名称。字段也可以用点访问，例如，mylist.field。


"""

# 这是我的购物清单，存储要购买的商品名称所对应的字符串
shoplist = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shoplist), 'items to purchase.')

print('These items are:', end=' ')
# for .. in 循环遍历列表中的项（元素），列表也是一个序列
for item in shoplist:
    print(item, end=' ')

print('\nI also have to buy rice.')
# 向列表中添加一个项（元素）
shoplist.append('rice')
print('My shopping list is now', shoplist)

print('I will sort my list now')
# 对列表进行排序。该方法影响自身，并且不会返回修改后的列表——这和字符串不一样。列表是可变的，字符串不可变。
shoplist.sort()
print('Sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
# 删除列表中的第一项
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)
print(20*'*')


# Tuple 元组
"""
元组用于将多个对象组合在一起。可以将它们近似看作列表，但是没有列表类提供的许多功能。元组的一个重要特征是，
它们和字符串一样是 不可变的 ，即你不能修改元组。

元组是由一些特殊的项定义的，这些项在一对可选的圆括号中，由逗号隔开。
元组通常用于这种情况，也就是语句或者用户自定义的函数可以安全地认为值的集合（即，值的元组）不会改变的情况。

包含 0 或 1 个项的元组

一个空的元组是由一对空的圆括号构成的，例如， myempty = () 。
只有一个项的元组，必须且仅在第一项的后面用一个逗号来指定元组，这样Python就可以区分一个元组和表达式中对象周围的一堆括号之间的区别了。
即，如果你想要一个元组只包含一个项：2，那么你就必须用 singleton = (2 , ) 。

Perl 程序员请注意

列表中的列表依旧是列表，不会丢失其特性，也就是说，列表并不会像 Perl 中的那样变平。这同样适用于元组中的元组、列表中的元组或者元组中的列表等等。
就 Python 而言，它们只是使用另一个对象存储的对象，仅此而已。
"""
# 尽管圆括号是可选的，
# 我还是建议使用圆括号，
# 来表示元组的开始和结束。
# 因为显式总比隐式要好。
zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))

new_zoo = 'monkey', 'camel', zoo    # parentheses not required but are a good idea
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
# 通过在一堆方括号中指定项的位置来访问元组中的项（元素），就像我们访问列表中的项一样。我们称之为 索引 操作符。
# 通过 new_zoo[2] 来访问 new_zoo 中的第三个项，我们通过 new_zoo[2][2] 来访问 new_zoo 元组中第三个项中的第三个项。
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is',
      len(new_zoo)-1+len(new_zoo[2]))
print(20*'*')

# dictionary 字典
"""
字典就像是一个地址簿，只要知道一个人的名字，你就可以找到他/她的地址或联系方式，即，我们将键 （名字）与 值 （详细信息）相关联。
注意，键必须是唯一的！
就好比是，如果有两个人重名，那就无法找到正确的详细信息一样。

注意，对于字典的键，你只能使用不可变对象（比如字符串），但是对于字典的值，不可变对象或者可变对象都可以使用。
这基本上就意味着，对于字典的键，你最好只使用简单点的对象。

通过 d = {key1 : value1, key2 : value2 } ，就可以指定字典中的键值对。
注意，一个键值对中的键与值由冒号隔开，
而不同键值对之间是由逗号隔开，所有的键值对以及冒号、逗号都包含在一对花括号中。

记住，字典中的键值对不以任何方式排序（不像列表中的像一样有从小到大递增的索引）。
如果你想要得到一个特殊的顺序。那么在使用字典之前，你必须自己对其进行排序。
"""
# 'ab' 是 'a'ddress'b'ook 的缩写，意思是地址簿
ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}
# 使用索引操作符来指定字典的键，以此访问键值对
print("Swaroop's address is", ab['Swaroop'])

# 删除一个键值对
del ab['Spammer']

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))
# 使用items()方法访问字典中的每一个键值对，该方法返回一个元组列表，其中每个元组包含一个键值对————键在前值在后
# 检索到某一个键值对，将其值赋给变量 name和address，相当于对每个键值对使用for..in循环
for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))

# 添加一个键值对
ab['Guido'] = 'guido@python.org'

# 使用 in 操作符检查键值对是否存在
if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])


# 序列
"""
列表元组和字符串都是序列的一种。
序列的主要特征是：成员测试（例如：in与not in表达式） 和 索引操作。这两种操作让我们可以直接从序列中提取特定部分。

上面提到了三种序列：列表、元组和字符串。它们还有另一种特殊的操作 —— 切片 ，切片操作让我们可以得到序列的一部分。
"""
shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

# 字符串引索，即下标操作
# 每当在序列上用方括号指定一个数字时，Python 会为你抓取序列中对应位置的元素。
# 记住 Python 从 0 开始计数。因此 shoplist[0] 抓取第一个元素，而 shoplist[3] 抓取 shoplist 序列中的第四个元素。
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
# 序列引索也可以是负数，这时位置从序列尾部开始计算。因此 shoplist[-1] 返回序列的最后一个元素，而 shoplist[-2] 返回倒数第二个元素。
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])

# 列表切片 #
"""
切片操作通过在序列名称的后面加上一个方括号，方括号中有一对可选的数字，用冒号分割。记住数是可选的，而冒号是必须的。
切片操作中冒号之前的第一个数表示切片开始的位置，冒号之后的第二个数表示切片到哪里终止。如果不指定第一个数，Python 会从序列首开始，
不指定第二个数则到序列尾结束。注意返回的切片从开始位置 开始，在结束位置之前 结束，即一个左闭右开区间。
seq[start:end] 即截取了 [start, end)，开始的位置包含在切片中，而结束位置不在。
因此 shoplist[1:3] 返回从位置 1 开始，包括位置 2，但不包括位置 3 ，只有两个元素的原序列切片。而 shoplist[:] 返回原序列的一个副本。
你也可以用负数位置做切片。负数从序列尾部开始计算位置。例如：shoplist[:-1] 会返回除了最后一个元素外的其余序列切片。
注意：当步长是 2 时，我们能得到位置 0, 2,... 上的字符。而步长是 3 时，我们得到 0, 3,... 上的字符。

>>> shoplist = ['apple', 'mango', 'carrot', 'banana']
>>> shoplist[::1]
['apple', 'mango', 'carrot', 'banana']
>>> shoplist[::2]
['apple', 'carrot']
>>> shoplist[::3]
['apple', 'banana']
>>> shoplist[::-1]
['banana', 'carrot', 'mango', 'apple']
"""

print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])

# 字符串切片 #
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])


# set 集合
"""
集合（set）是简单对象的 无序的 集合（collection）。
当对象在集合（collection）中的存在比对象在集合（collection）中的顺序或者比对象在集合（collection）中出现的次数更为重要时，
我们就会用到集合（set）。

你可以使用集合（set）来测试成员资格，看看它是否是另一个集合（set）的子集，找到两个集合之间的交集，等等。

>>> bri = set(['brazil', 'russia', 'india'])
>>> 'india' in bri
True
>>> 'usa' in bri
False
>>> bric = bri.copy()
>>> bric.add('china')
>>> bric.issuperset(bri)
True
>>> bri.remove('russia')
>>> bri & bric # 或者是 bri.intersection(bric)
{'brazil', 'india'}


集合论 / 维恩图

译者PS：关于 set 和 collection 的翻译。在数学上， set 和 collection 的区别是是否具有互异性，即，包含的元素是否可以重复出现。
set 中的元素具有互异性，而 collection 中的元素不具有互异性。比如，{1，2，3} 既是 collection 又是 set ，而 {1，2，3，3}
只是 collection 不是 set 。因为后者（即{1，2，3，3}）有重复的元素（就是那两个 3），这不符合 set 的互异性要求。但是，将两者
翻译成中文都是 “集合” ，译者能力有限，只能理解并翻译到这个程度了。
"""


# 引用
"""
当你创建一个对象，并把它赋值给一个变量时，这个变量只是引用了这个对象，变量并不能代表对象自身！
    因此，你也可以把变量名当作一个指针，它指向存储对象的那一块计算机内存。
    这称作绑定名称到对象。

通常来说，你不需要担心这一点，但你需要注意使用引用时的一些细微的差别。

如果你想要获得列表、或者类似的序列、或更复杂对象的副本，只要不是像整数一样简单的 对象，你都需要通过切片操作来获得它的副本。
如果你直接把一个变量名赋值给另一个，它们两个都会引用同一个对象。
在赋值时你需要注意这一点，不然可能会造成意想不到的结果，从而带来麻烦。
"""
print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
# mylist 只是指向同一个对象的另一个别名！
mylist = shoplist

# 我买下了第一件商品，所以把它从列表中移除
del shoplist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
# 注意到 shoplist 和 mylist 产生了同样的输出
# 输出的都是没有 'apple' 的相同列表
# 这验证了它们都指向着同一个对象

print('Copy by making a full slice')
# 通过全切片来获得一个副本
mylist = shoplist[:]
# 移除第一个元素
del mylist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
# 注意到现在这两个列表有差异了

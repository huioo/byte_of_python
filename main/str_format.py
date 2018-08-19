# format 方法
# 有时候我们想要从其他信息中构造字符串。这就是 format() 方法可以发挥作用的地方。

age = 20
name = 'Swaroop'

# {0}对应name，format方法的第一个参数
# {1}对应age，format方法的第二个参数
# 使用字符串连接实现相同的效果，name + ' is ' + str(age) + ' years old'
template = '{0} was {1} years old when he wrote this book.'
print(template.format(name, age))
template = 'Why is {0} playing with that python?'
print(template.format(name))


# 数字可选，可填可不填，如下：
print('{} was {} years old when he wrote this book'.format(name, age))
print('Why is {} playing with that python?'.format(name))

# python在 format() 方法中的作用就是将每一个参数值替换为规范的位置，可以有更详细的规范。
# 取十进制小数点后的精度为3，得到的浮点数为0.333
print('{0:.3f}'.format(1/3))

# 填充下划线(_)，文本居中
# 将 '__hello__' 的宽度扩充为 11
print('{0:_^11}'.format('hello'))

# 用基于关键字的方法打印显示 ‘Swaroop wrote A Byte of Python’
print('{name} wrote {book}'.format(
    name='Swaroop', book='A Byte of Python')
)

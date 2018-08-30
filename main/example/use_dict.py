#
"""



"""

# 1 直接创建
d = {'name': 'earth', 'port': '80'}

# 2 工厂方法
items = [('name', 'earth'), ('port', '80')]
d = dict(items)
items = (['name', 'earth'], ['port', '80'])
d = dict(items)

# 3 fromkeys()方法
d = {}.fromkeys(('x', 'y'), -1) == {'x': -1, 'y': -1}
d = {}.fromkeys(('x', 'y')) == {'x': None, 'y': None}
d = {}.fromkeys('x', 'y') == {'x': 'y'}
# {}.fromkeys('x', 'y', 'a', 'b') 异常
# TypeError: fromkeys expected at most 2 arguments, got 4


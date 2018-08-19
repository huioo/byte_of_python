import pickle

# 这里我们将存储对象的文件的名称
shoplistfile = 'shoplist.data'
# 要买的东西的清单
shoplist = ['apple', 'mango', 'carrot']

# 写入文件
f = open(shoplistfile, 'wb')
# 将对象存储到文件
pickle.dump(shoplist, f)
f.close()

# 销毁 shoplist 变量
del shoplist

# 从存储中读回
f = open(shoplistfile, 'rb')
# 从文件加载对象
storedlist = pickle.load(f)
print(type(storedlist), storedlist)

"""
$ python io_pickle.py
['apple', 'mango', 'carrot']
"""

"""
要将对象存储在文件中，必须先以二进制写入模式 open 文件，然后调用 pickle 模块的 dump 函数将对象保存到文件 file 中去，这个过程叫做 pickling。

之后，我们可使用 pickle 模块的 load 函数来检索对象并返回。此过程称为 unpickling 。
"""


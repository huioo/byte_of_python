import pickle


a = {'a':1, 'b':2}

with open('data/dict.data', 'wb') as fp:
    pickle.dump(a, fp)

with open('data/dict.data', 'rb') as fp:
    print(pickle.load(fp))

a = {'a':2, 'b':3}
a = [1,2,3,4]
with open('data/dict.data', 'wb') as fp:
    pickle.dump(a, fp)

with open('data/dict.data', 'rb') as fp:
    print(pickle.load(fp))

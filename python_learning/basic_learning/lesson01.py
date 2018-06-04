words = ['car', 'window', 'ddd']

print('------一般遍历------------')
for w in words[1:-1]:
    print(w, len(w))

print('------带索引的遍历1------------')
for index, w in enumerate(words):
    print(index, w)

print('------带索引的遍历2------------')
for index, w in enumerate(words, start=1):
    print(index, w)



maps = {'10': 'sun', '11': 'li', '12': 'cheng'}

print('------map遍历01------------')
for k, v in maps.items():
    print(k, v)

print('------带索引的map遍历------------')
for index, (k, v) in enumerate(maps.items()):
    print(index, k, v)

import itertools

k = ['a', 'b', 'c']
v = ['11', '22', '33', '44']

print('------zip遍历01------------')
for _k, _v in zip(k, v):
    print(_k, _v)

print('------zip遍历02------------')
for _k, _v in itertools.zip_longest(k, v):
    print(_k, _v)

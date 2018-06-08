def extendList(val, list=[]):
    list.append(val)
    return list


def extendList2(val, list=None):
    if list is None:
        list = []
    list.append(val)
    return list


list01 = extendList2(1)
list02 = extendList2(2)

print(id(list01))
print(id(list02))
print(list01)
print(list02)
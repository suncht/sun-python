class MyList(object):
    def __init__(self):
        self.size = 0
        self.container = []
        self._iterIndex = 0

    def add(self, obj):
        self.container.append(obj)
        self.size += 1

    def pop(self):
        obj = self.container.pop()
        self.size -= 1
        return obj

    def __len__(self):
        """
        长度
        :return:
        """
        return self.size

    def __iter__(self):
        """
        返回遍历的对象
        :return:
        """
        self._iterIndex = 0
        return self

    def __next__(self):
        """
        遍历下一次
        :return:
        """
        if self._iterIndex >= len(self.container):
            raise StopIteration()

        obj = self.container[self._iterIndex]
        self._iterIndex += 1
        return obj


if __name__ == '__main__':
    list = MyList()
    for i in range(100):
        list.add(i)
        if i % 3 == 0:
            list.pop()
    print(len(list))

    for item in list:
        print(item)

    print('------------------')
    for item in list:
        print(item)

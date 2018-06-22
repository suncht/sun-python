def singleton(cls):
    instances = {}
    def wapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wapper


@singleton
class MyClass:
    a = 1
    def __init__(self):
        self.id = "111"


if __name__ == '__main__':
    a = MyClass()
    b = MyClass()
    a.id = "22"
    print(a.id)
    print(b.id)

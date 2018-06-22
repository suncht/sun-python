class MyClass(object):
    def __new__(cls, *args, **kwargs):
        print("__new__")
        return object.__new__(cls, *args, **kwargs)

    def __init__(self):
        self.user_id = 'aaa'
        self.user_name = "suncht"


if __name__ == '__main__':
    myClass = MyClass()
    print(myClass.user_id)
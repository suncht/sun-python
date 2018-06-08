class User(object):
    # 限制添加的属性，只能添加'id', 'user_name', 'age'三个指定的属性
    __slots__ = ('id', 'user_name', 'age')

    def __init__(self, uid, user_name, age=-1):
        self.id = uid
        self.user_name = user_name
        self.age = age

if __name__ == '__main__':
    u = User(1, 'sunct', 30)

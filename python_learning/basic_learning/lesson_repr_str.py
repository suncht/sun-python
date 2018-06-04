class User(object):
    def __init__(self, user_id, user_name, age=15):
        self.userId = user_id
        self.userName = user_name
        self.age = age

    # def __repr__(self):
    #     return 'User_Repr[userId=%s, userName=%s, age=%d]' % (self.userId, self.userName, self.age)

    # def __str__(self):
    #     return 'User_Str[userId=%s, userName=%s, age=%d]' % (self.userId, self.userName, self.age)

if __name__ == '__main__':
    u = User(1, 'suncht', 32)
    print(u)
    u

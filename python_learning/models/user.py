class User(object):
    def __init__(self, id):
        self.id = id
        self.userName = '';
        self.age = -1
        self.idcode = ''

    def __str__(self):
        return 'id=%s, useName=%s, age=%s, idcode=%s' % (self.id, self.userName, self.age, self.idcode)
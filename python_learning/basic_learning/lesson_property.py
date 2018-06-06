class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
        self._age = 10

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score


if __name__ == '__main__':
    stu = Student('sunct', 80)
    print(stu.score)
    stu.score = 100
    print(stu.score)
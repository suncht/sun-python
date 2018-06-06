class Money(object):
    def __init__(self, yuan, jiao=0, fen=0):
        _total = yuan * 100 + jiao * 10 + fen
        _yuan, _jiao, _fen = Money.num_carry(_total)
        self.fen = _fen
        self.jiao = _jiao
        self.yuan = _yuan

    def __add__(self, other):
        """
        相加
        :param other:
        :return:
        """
        _total = (self.yuan + other.yuan) * 100 + (self.jiao + other.jiao) * 10 + (self.fen + other.fen)
        _yuan, _jiao, _fen = Money.num_carry(_total)
        return Money(_yuan, _jiao, _fen)

    # def __iadd__(self, other):
    #     """
    #     相加
    #     :param other:
    #     :return:
    #     """
    #     _total = (self.yuan + other.yuan) * 100 + (self.jiao + other.jiao) * 10 + (self.fen + other.fen)
    #     self.yuan, self.jiao, self.fen = Money.num_carry(_total)

    def __sub__(self, other):
        """
        相减
        :param other:
        :return:
        """
        _total = (self.yuan - other.yuan) * 100 + (self.jiao - other.jiao) * 10 + (self.fen - other.fen)
        if _total < 0:
            raise Exception('余钱不足')
        _yuan, _jiao, _fen = Money.num_carry(_total)
        return Money(_yuan, _jiao, _fen)

    def __mul__(self, other):
        """
        相乘
        :param other:
        :return:
        """
        if type(other) == Money:
            _yuan = self.yuan * other.yuan
            _jiao = self.jiao * other.jiao
            _fen = self.fen * other.fen
        elif type(other) == int or type(other) == float:
            _yuan = self.yuan * other
            _jiao = self.jiao * other
            _fen = self.fen * other
        else:
            raise Exception('类型错误')
        _total = 100 * _yuan + 10 * _jiao + _fen
        _yuan, _jiao, _fen = Money.num_carry(_total)
        return Money(_yuan, _jiao, _fen)

    def __truediv__(self, other):
        """
        相除  Python3中改名为__truediv__， Python2是__div__
        :param other:
        :return:
        """
        _total1 = self.yuan * 100 + self.jiao * 10 + self.fen
        _total2 = other.yuan * 100 + other.jiao * 10 + other.fen

        _total = _total1 // _total2
        _yuan, _jiao, _fen = Money.num_carry(_total)
        return Money(_yuan, _jiao, _fen)

    def __ge__(self, other):
        if type(other) == Money:
            return Money.convert(self) >= Money.convert(other)
        elif type(other) == int:
            return Money.convert(self) >= other
        else:
            raise Exception('类型异常')

    def __gt__(self, other):
        if type(other) == Money:
            return Money.convert(self) > Money.convert(other)
        elif type(other) == int:
            return Money.convert(self) > other
        else:
            raise Exception('类型异常')

    def __le__(self, other):
        if type(other) == Money:
            return Money.convert(self) <= Money.convert(other)
        elif type(other) == int:
            return Money.convert(self) <= other
        else:
            raise Exception('类型异常')

    def __lt__(self, other):
        if type(other) == Money:
            return Money.convert(self) < Money.convert(other)
        elif type(other) == int:
            return Money.convert(self) < other
        else:
            raise Exception('类型异常')

    def __eq__(self, other):
        if type(other) == Money:
            return Money.convert(self) == Money.convert(other)
        elif type(other) == int:
            return Money.convert(self) == other
        else:
            raise Exception('类型异常')

    def __ne__(self, other):
        if type(other) == Money:
            return Money.convert(self) != Money.convert(other)
        elif type(other) == int:
            return Money.convert(self) != other
        else:
            raise Exception('类型异常')

    def __str__(self):
        return 'Money[%d, %d, %d]' % (self.yuan, self.jiao, self.fen)

    def __repr__(self):
        return self.__str__()

    def __cmp__(self, other):
        """
        比较排序
        :param other:
        :return:
        """
        total_self = Money.convert(self)
        total_other = Money.convert(other)
        if total_self > total_other:
            return 1
        elif total_self == total_other:
            return 0
        else:
            return -1

    @staticmethod
    def num_carry(num):
        """
        判断数值是否进位
        :param num:
        :return:
        """
        if num >= 100:
            return (num // 100, (num // 10) % 10, num % 10)
        if num >= 10:
            return (0, num // 10, num % 10)
        else:
            return (0, 0, num)

    @staticmethod
    def convert(money):
        return money.yuan * 100 + money.jiao * 10 + money.fen


if __name__ == '__main__':
    m1 = Money(10, 13, 24)
    m2 = Money(3, 19, 58)
    m3 = Money(4, 5, 6)
    m4 = Money(10, 20, 4)
    list = [m1, m2, m3, m4]
    print(sorted(list))
    print(list)
    list.sort()
    print(list)

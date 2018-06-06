class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __int__(self):
        return self.p // self.q

    def __float__(self):
        return self.p * 1.0 / self.q


if __name__ == '__main__':
    r = Rational(12, 9)
    print(int(r))
    print(float(r))
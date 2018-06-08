import time
def stopWatch(func):
    print(func.__name__)
    def wrapper(self, *args, **kwargs):
        start = (int(round(time.time() * 1000)))

        result = func(self, *args, **kwargs)
        print('耗时：%d毫秒' % ((int(round(time.time() * 1000))) - start))
        return result
    return wrapper

class Util(object):
    def __init__(self, fromValue, toValue):
        self.fromValue = fromValue
        self.toValue = toValue

    @stopWatch
    def computeFunc(self):
        if self.fromValue > self.toValue:
            return 0

        total = 0
        for i in range(self.fromValue, self.toValue + 1):
            time.sleep(0.1)
            total = total + i

        return total



if __name__ == '__main__':
    util = Util(1, 10)
    print(util.computeFunc())
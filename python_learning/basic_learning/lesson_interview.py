#生成器的创建，区分迭代器、生成器、推导式、生成器表达式
l_01 = [x for x in range(10)]  #列表推导式
print(l_01)

l_02 = (x for x in range(10))  #列表生成器表达式
print(l_02)


class Fib:
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):  #Fib是迭代对象， 因为Fib实现了__iter__方法 -->类/对象
        return self

    def __next__(self):  #Fib是迭代器， 因为Fib实现了__next__方法 -->类/对象
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value


def fib():
    prev, curr = 0, 1
    while True:
        yield curr   #fib()是生成器，yield是关键字，生成器是一种特殊的迭代器  -->函数
        prev, curr = curr, curr + prev


def islice(fib, start, end):
    for i in range(start, end):
        yield next(fib)


f = fib()
l_03 = list(islice(f, 0, 10))
print(l_03)

#yield
print('--------------------')
y = 0
def g():
    global y
    print('1')
    for i in range(0, 10):
        yield i
        y = 5 + i
        print(y)
func_g = g()
print(func_g.__next__()) #等价于next(func_g)
print(func_g.__next__())
print(func_g.__next__())
print(func_g.send(10))
print(func_g.__next__())
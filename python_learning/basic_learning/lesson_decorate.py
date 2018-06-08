import time
import logging
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = (int(round(time.time() * 1000)))

        result = func(*args, **kwargs)
        print('耗时：%d毫秒' % ((int(round(time.time() * 1000))) - start))
        return result
    return wrapper

# 如果使用装饰器，那原来方法的元信息就被覆盖了
def logged(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == 'warn':
                logging.warning("%s is running" % func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return decorator


def logged2(level):
    def decorator(func):
        @wraps(func)    # 把原函数的元信息拷贝到装饰器函数
        def wrapper(*args, **kwargs):
            if level == 'warn':
                logging.warning("%s is running" % func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@timer
@logged2(level='warn')
def compute_func(from_value, to_value):
    if from_value > to_value:
        return 0

    total = 0
    for i in range(from_value, to_value + 1):
        time.sleep(0.1)
        total = total + i

    return total


if __name__ == '__main__':
    print(compute_func(1, 10))
    print(compute_func.__name__)


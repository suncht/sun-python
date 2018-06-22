import time
#from compute_model import foo


def foo():
    num = 0
    for i in range(100000001):
        num = num + i


start_time = time.time()
#for i in range(5):
foo()

end_time = time.time()
print('耗时:', end_time - start_time)

#30.93425750732422
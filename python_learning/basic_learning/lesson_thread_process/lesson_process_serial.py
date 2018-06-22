import time
import multiprocessing
from compute_model import foo

if __name__ == '__main__':
    #多进程串行
    t_list = []
    start_time = time.time()
    for i in range(5):
        i = multiprocessing.Process(target=foo, args=())
        t_list.append(i)
        i.start()
        i.join()
    end_time = time.time()
    print('耗时:', end_time - start_time)
    #耗时: 33.90458607673645
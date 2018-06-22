import time
import threading
from compute_model import foo

if __name__ == '__main__':
    #多线程并行
    t_list = []
    start_time = time.time()
    for i in range(5):
        i = threading.Thread(target=foo)
        t_list.append(i)
        i.start()

    for t in t_list:
        t.join()

    end_time = time.time()
    print('耗时:', end_time - start_time)
    #耗时: 32.29368734359741
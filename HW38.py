import time
from multiprocessing import Process, Pool
from threading import Thread

COUNT = 5000000000


def f(n):
    while n > 0:
        n -= 1


if __name__ == "__main__":
    start = time.time()
    pool = Pool(processes=2)
    pool.apply_async(f, args=(COUNT // 2,))
    pool.apply_async(f, args=(COUNT // 2,))

    pool.close()
    pool.join()
    end = time.time()
    print("Time:", end - start)

if __name__ == "__main__":
    start = time.time()
    th = Thread(target=f, args=(COUNT//2,))
    th1 = Thread(target=f, args=(COUNT//2,))
    th.start()
    th1.start()
    th.join()
    th1.join()
    end = time.time()
    print("Time", end - start)

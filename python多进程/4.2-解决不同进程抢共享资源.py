"""
# -*- coding: utf-8 -*-
@version: python3.7
@author: yuhaoyu
@software: PyCharm
@time: 2020/1/2
@PROJECT_NAME: yuyi
@file: 4.2-解决不同进程抢共享资源.py
Created for: 
"""

import multiprocessing as mp
import time


def job(v, num, l):
    l.acquire()  # 锁住
    for _ in range(5):
        time.sleep(0.1)
        v.value += num  # 获取共享内存
        print(v.value)
    l.release()  # 释放


def multicore():
    l = mp.Lock()  # 定义一个进程锁
    v = mp.Value('i', 0)  # 定义共享内存
    p1 = mp.Process(target=job, args=(v, 1, l))  # 需要将lock传入
    p2 = mp.Process(target=job, args=(v, 3, l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    '''
    需要主义的是上面可能仍然会发生冲突——p1先执行还是p2先执行的问题。
    为了解决这个问题我们可以在start,join中决定他们的顺序。
    '''
    # p1.start()
    # p1.join()
    # p2.start()
    # p2.join()


if __name__ == '__main__':
    multicore()

# 输出

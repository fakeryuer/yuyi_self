"""
# -*- coding: utf-8 -*-
@version: python3.7
@author: yuhaoyu
@software: PyCharm
@time: 2020/1/2
@PROJECT_NAME: yuyi
@file: 4.1-共享内存和进程锁.py
Created for: 
"""
'''
一般情况下，各个进程中的数据变量是无法发生交流的，但我们可以通过使用Value数据存储在一个共享的内存表中。
'''
import multiprocessing as mp
import time


def job(v, num):
    for _ in range(5):
        time.sleep(0.1)  # 暂停0.1秒，让输出效果更明显
        v.value += num  # v.value获取共享变量值
        print(v.value)


def multicore():
    v = mp.Value('i', 0)  # 定义共享变量
    p1 = mp.Process(target=job, args=(v, 1))
    p2 = mp.Process(target=job, args=(v, 3))  # 设定不同的number看如何抢夺内存
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == '__main__':
    multicore()

# 输出

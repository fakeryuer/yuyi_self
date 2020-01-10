"""
# -*- coding: utf-8 -*-
@version: python3.7
@author: yuhaoyu
@software: PyCharm
@time: 2020/1/2
@PROJECT_NAME: yuyi
@file: 1-简单多进程.py
Created for:
"""
'''
当我们任务数量确定而且比较少的时候，可以手动为每个任务指定一个进程来运行。
'''
import multiprocessing as mp

def f(a):
    print(a)

if __name__ == '__main__':
    # 这里有三个任务，手动指定3个进程
    p1 = mp.Process(target=f, args=(1,))
    p2 = mp.Process(target=f, args=(2,))
    p3 = mp.Process(target=f, args=(3,))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()

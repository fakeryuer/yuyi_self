"""
# -*- coding: utf-8 -*-
@version: python3.7
@author: yuhaoyu
@software: PyCharm
@time: 2020/1/2
@PROJECT_NAME: yuyi
@file: 2.1-使用进程池来处理多任务.py
Created for: 
"""
'''
当我们任务比较多而且不确定数量（又或者想使得代码更简洁）的时候可以使用进程池Pool来编写多进程。
'''
import multiprocessing as mp

def f(a):
    return a

if __name__ == '__main__':
    pool = mp.Pool()
    res = pool.map(f, (1, 2, 3, 4))
    print(res)
# 输出
[1, 2, 3, 4]
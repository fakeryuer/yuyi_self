"""
# -*- coding: utf-8 -*-
@version: python3.7
@author: yuhaoyu
@software: PyCharm
@time: 2020/1/2
@PROJECT_NAME: yuyi
@file: 2.2.1-使用进程池来处理多任务.py
Created for: 
"""
'''
Pool默认使用计算机所有cpu核来进行运算，也可使用Pool(process=4)来指定并行的进程数。
另一个可以储存结果的函数是apply_async()，但是这个函数只支持传入一个参数，也即运行一个任务，运行多个任务需要多次指定。
此外，他返回的结果是一个类似生成器的东西，需要通过get函数取出来。
'''
import multiprocessing as mp

def f(a):
    return a

if __name__ == '__main__':
    pool = mp.Pool()
    res = [pool.apply_async(f, (i,)) for i in range(4)]
    print([r.get() for r in res])

# 输出
[0, 1, 2, 3]
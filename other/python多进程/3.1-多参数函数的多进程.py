"""
# -*- coding: utf-8 -*-
@version: python3.7
@author: yuhaoyu
@software: PyCharm
@time: 2020/1/2
@PROJECT_NAME: yuyi
@file: 3.1-多参数函数的多进程.py
Created for: 
"""
'''
上面处理任务的函数都只有一个参数，在实际情况这种情况是很少的，一般我们的函数都需要传入多个参数。
python2中未能支持传多个参数，python3.3后则有starmap来支持传入多参数。
'''
import multiprocessing as mp

def f(a, b):
    return (a, b)

if __name__ == '__main__':
    pool = mp.Pool()
    res = pool.starmap(f, ((1, 2), ('a', 'b')))
    print(res)

# 输出
[(1, 2), ('a', 'b')]
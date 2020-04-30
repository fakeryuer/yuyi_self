"""
# -*- coding: utf-8 -*-
@version: python3.7
@author: yuhaoyu
@software: PyCharm
@time: 2019/12/26
@PROJECT_NAME: yuyi
@file: 分布式进程_服务端.py
Created for: 
"""

import queue
from multiprocessing import freeze_support
from multiprocessing.managers import BaseManager

# 任务个数
task_num = 10
# 定义收发队列
task_queue = queue.Queue(task_num)
result_queue = queue.Queue(task_num)

def get_task():
    return task_queue

def get_result():
    return result_queue

# 创建类似的QueueManager
class QueueManager(BaseManager):
    pass

def win_run():
    # windows下绑定调用接口不能使用lambda,所以只能先定义函数再绑定
    QueueManager.register('get_task_queue', callable=get_task)
    QueueManager.register('get_result_queue', callable=get_result)
    # 绑定端口并设置验证口令，windows下需要填写IP地址,Linux下不填，默认为本地
    manager = QueueManager(address=('127.0.0.1', 4000), authkey=b'qty')
    # 启动
    manager.start()
    # 通过网络获取任务队列和结果队列
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    try:
        # 添加任务
        for i in range(10):
            print('put task %s...' % i)
            task.put(i)
        print('try get result...')
        for i in range(10):
            print('result is %s' % result.get(timeout=10))
    except:
        print('manage error')
    finally:
        # 一定要关闭，否则会报管理未关闭的错误
        manager.shutdown()
        print('master exit!')

if __name__ == '__main__':
    # windows下多进程可能会出现问题，添加这句可以缓解
    freeze_support()
    win_run()

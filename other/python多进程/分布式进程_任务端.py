"""
# -*- coding: utf-8 -*-
@version: python3.7
@author: yuhaoyu
@software: PyCharm
@time: 2019/12/26
@PROJECT_NAME: yuyi
@file: 分布式进程_任务端.py
Created for: 
"""

from multiprocessing.managers import BaseManager

# 创建类似的QueueManager:
class QueueManager(BaseManager):
    pass

# 第一步：使用QueueManager注册用于获取Queue的方法名称
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 第二步：连接服务器
server_addr = '127.0.0.1'
print("Connect to server %s" % server_addr)
# 端口和验证口令注意保持与服务进程完全一致
m = QueueManager(address=(server_addr, 4000), authkey=b'qty')
# 从网络连接
m.connect()

# 第三步：获取Queue的对象
task = m.get_task_queue()
result = m.get_result_queue()

# 第四步:从task队列获取任务，并把结果写入result队列:
while not task.empty():
    index = task.get(True, timeout=10)
    print('run task download %s' % str(index))
    result.put('%s---->success ' % str(index))
# 处理结束
print('worker exit.')

"""
# -*- coding: utf-8 -*-
@version: python3.7
@author: yuhaoyu
@software: PyCharm
@time: 2020/1/10
@PROJECT_NAME: yuyi
@file: HTML标签处理.py
Created for: 
"""
from html.parser import HTMLParser


# 方法一：重定义方法输出
def strip_tags(html):
    """
    Python中过滤HTML标签的函数
    """
    html = html.strip()
    parser = HTMLParser()
    result = []
    parser.handle_data = result.append
    parser.feed(html)
    parser.close()
    return result


# 方法二：重写类
class MyHTMLParser(HTMLParser):

    # 构造方法,定义data数组用来存储html中的数据
    def __init__(self):
        HTMLParser.__init__(self)
        self.data = []

    # 覆盖starttag方法,可以进行一些打印操作
    def handle_starttag(self, tag, attrs):
        pass
        # print("Start Tag: ",tag)
        # for attr in attrs:
        #   print(attr)

    # 覆盖handle_data方法,用来处理获取的html数据,这里保存在data数组
    def handle_data(self, data):
        if data.count('\n') == 0:
            self.data.append(data)


with open('./20010984.txt', encoding='utf-8') as f:
    html = f.read()
    # 方法1
    # html = strip_tags(html)
    # print(html)
    # 方法2
    parser = MyHTMLParser()
    parser.feed(html)
    print(parser.data)

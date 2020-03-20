"""
# -*- coding: utf-8 -*-
@version: python3.7
@author: yuhaoyu
@software: PyCharm
@time: 2020/3/10
@PROJECT_NAME: yuyi
@file: givaudan_json数据处理.py
Created for: 
"""

import json, os, sys
from pprint import pprint

data_file = r'E:\Jupyter_yuyi\Panel Qaire_Product Test - CN\json\Json_result.json'
with open(data_file, 'r', encoding='utf-8') as f:
    data = json.load(f)
# pprint(data)
# pprint(data['question8'])

# 创建结果保存的字典
result = dict(zip(data['question8'].keys(),
                  {i for i in range(len(data['question8'].keys()))}))
for i in result:
    result[i] = {'average_score': 0,
                 'question2': dict(),
                 'question2-4': dict(),
                 'question5': dict(),
                 'question7': dict(),
                 'question8': dict(),
                 }


# 01 average_score 处理
def fun1():
    for code, code_value in data['average_score'].items():
        # print(code,code_value)
        result[code]['average_score'] = code_value


# 02 question2 处理
M_AD = ['Pleasantly sweet', 'Citrusy', 'Soapy', 'Fruity', 'Creamy/Milky', 'Spicy',
        'Edible', 'Mint', 'Floral', 'Sticky Sweet', 'Sour', 'Candy/Fruit candy',
        'Nature Green', 'Watery/Ocean', 'Herbal', 'Woody', 'Hygienic', 'Anti-bacteria']


def fun2():
    for code, code_value in data['question2-4'].items():
        for key, value in code_value.items():
            if key in M_AD:
                result[code]['question2'].update({key:
                                                      {'Fragrance Liking': value.split('|')[0],
                                                       'frequency': value.split('|')[1]}
                                                  })


# 03 question2-4 处理
M_BO = ['Pleasantly sweet',
        'Citrusy', 'Soapy', 'Fruity', 'Creamy/Milky', 'Spicy', 'Edible', 'Mint',
        'Floral', 'Sticky Sweet', 'Sour', 'Candy/Fruit candy', 'Nature Green',
        'Watery/Ocean', 'Herbal', 'Woody', 'Hygienic', 'Anti-bacteria',

        'Artificial', 'For children', 'Caring', 'Harsh', 'Cheap',
        'Smells like perfume', 'High quality', 'Soft', 'Clean',
        'Deodorizing (Not for Hair Care / Personal Care)', 'Moisturizing',
        'Dirty', 'Trendy', 'Masculine', 'Feminine', 'Mild', 'Natural',
        'For the whole family', 'For me', 'Fresh', 'Traditional', 'Premium',
        'Smells like cologne ', 'For baby',

        'Relaxing', 'Romantic', 'feel',
        'Safe', 'Delightful', 'Memorable', 'New', 'Energizing', 'Warm',
        'Familiar', 'Playful', 'Unusual']


def fun4():
    for code, code_value in data['question2-4'].items():
        for key, value in code_value.items():
            result[code]['question2-4'].update({key:
                                                    {'Fragrance Liking': value.split('|')[0],
                                                     'frequency': value.split('|')[1]}
                                                })


# 04 question5-7 处理
question_5_7 = ['question5', 'question7', 'question8']


def fun5_7():
    for question in question_5_7:
        for code, code_value in data[question].items():
            result[code][question].update(code_value)


if __name__ == '__main__':
    fun1()
    fun2()
    fun4()
    fun5_7()
    pprint(result)
    with open(r'E:\Jupyter_yuyi\Panel Qaire_Product Test - CN\json\givaudan_json.json', 'w+', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False)

"""
# -*- coding: utf-8 -*-
@version: python3.7
@author: yuhaoyu
@software: PyCharm
@time: 2020/3/2
@PROJECT_NAME: yuyi
@file: webdriver_chrome.py
Created for: 
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

login_user = ['ywycmonitor', 'haiermonitor']


for i in login_user:
    chrome_options = Options()
    # 禁止弹窗
    prefs = {
        'profile.default_content_setting_values':
            {
                'notifications': 2
            }
    }
    # 禁止弹窗加入
    chrome_options.add_experimental_option('prefs', prefs)
    browser = webdriver.Chrome(chrome_options=chrome_options)
    url = 'https://tool.yuyidata.com/login'
    browser.get(url)  # 打开浏览器预设网址
    b_name = '/html/body/div/div[1]/div[2]/div[1]/form/div[1]/div[1]/div/div/div/div/div/input'
    b_pwd = '/html/body/div/div[1]/div[2]/div[1]/form/div[1]/div[2]/div/div/div/div/div/input'
    b_login = '/html/body/div/div[1]/div[2]/div[1]/form/div[1]/div[4]/button'
    user = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
        (By.XPATH, b_name)
    ))
    psw = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
        (By.XPATH, b_pwd)
    ))
    login = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
        (By.XPATH, b_login)
    ))

    # 登陆信息
    user.clear()
    psw.clear()
    user.send_keys(i)
    psw.send_keys('pwdforstats')
    login.click()

    login_out = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app_toolbar"]/div/div[3]/div[1]/button/div/i')
    ))

    print(i.replace("\n", ''), browser.current_url)  # 打印网页源代码
    # login_out2 = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
    #     (By.XPATH, '//*[@id="inspire"]/div[1]/div/div[3]/a/div[1]/i')
    # ))
    # login_out2.click()
    browser.quit()
'//*[@id="inspire"]/div[1]/div/div[3]'
'//*[@id="inspire"]/div[1]/div/div[3]/a'
'//*[@id="inspire"]/div[1]/div/div[3]/a/div[1]'
'//*[@id="inspire"]/div[1]/div/div[3]/a/div[1]/i'
'//*[@id="inspire"]/div[1]/div/div[3]/a/div[2]'
'//*[@id="inspire"]/div[1]/div/div[3]/a/div[2]/div'

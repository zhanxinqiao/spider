import re
import time

import pymysql
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_data(url):
    #无界面模式
    options=Options()
    options.add_argument("-headless")
    # path = r'../chromedriver.exe'
    # brower=webdriver.Chrome(executable_path=path,options=options)
    brower=webdriver.Chrome(options=options)
    brower.get(url)
    time.sleep(3)
    # print(brower.page_source)
    return brower
    #有界面模式
    # driver = webdriver.Chrome(r'../chromedriver.exe')
    # driver.get(url)
    # time.sleep(3)
    # return driver


def XPath(driver1):
    name_list = driver1.find_elements_by_xpath('//div[@class="checi"]//tbody/tr/td[2]/a')
    # name  课程名
    name = []
    for n in name_list:
        a = n.text# 获取元素属性
        name.append(a)
        print(a)
    print(len(name))


if __name__ == '__main__':
    a=get_data("https://huoche.8684.cn/h_G101")
    XPath(a)
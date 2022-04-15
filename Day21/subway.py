import csv
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
    brower=webdriver.Chrome(options=options)
    brower.get(url)
    time.sleep(3)

    return brower



def XPath(driver1):
    name_list = driver1.find_elements_by_xpath('//ul[@class="ib-mn cm-mn"]//li[@class="sLink"]/a[1]')
    # name  课程名
    name = []
    for n in name_list:
        a = n.text# 获取元素属性
        name.append(a)
        print(a)
    print(len(name))
    for i in range(1,len(name)+1):
        values_list = driver1.find_elements_by_xpath('//ul[@class="ib-mn cm-mn"]//li[@class="sLink"]['+str(i)+']/a')
        j=1
        zz=[]
        for n in values_list:
            if j==1:
                j=2
            else:
                a=n.text
                zz.append(a)
        print(name[i-1],zz)
        down_load(name[i-1],zz)

def down_load(name, values):
    with open('./subway.csv', 'a+', encoding='utf-8') as f:
        f.write(name+"\t")
        for i in range(len(values)):
            f.write(values[i]+"\t")
        f.write("\n")
if __name__ == '__main__':
    a=get_data("https://dt.8684.cn/wh")
    XPath(a)
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
    # 商品名字
    name = []
    name_list1 = driver1.find_elements_by_xpath('//div[@class="g-slider"]//div[starts-with(@class,"item")]/div/a/img')
    for n in name_list1:
        a = n.get_attribute('alt') # 获取元素属性
        name.append(a)
    name_list2 = driver1.find_elements_by_xpath('//div[starts-with(@class,"g-box wow")]/div/a/img')
    for n in name_list2:
        a = n.get_attribute('alt') # 获取元素属性
        name.append(a)
        print(a)
    for i in range(len(name)):
        print(name[i])
    print(len(name))
    # 链接
    src = []
    src_list1 = driver1.find_elements_by_xpath('//div[@class="g-slider"]//div[starts-with(@class,"item")]/div/a')
    for s in src_list1:
        a = s.get_attribute('href')
        src.append(a)
    src_list2 = driver1.find_elements_by_xpath('//div[starts-with(@class,"g-box wow")]/div/a')
    for s in src_list2:
        a = s.get_attribute('href')
        src.append(a)
    for i in range(len(src)):
        print(src[i])
    print(len(src))
    teacher, image = [], []
    for i in src:
        driver = get_data(i)
        # # 老师
        price_list = driver.find_elements_by_xpath('//div[@class="teacher-info"]/ul/li/div[@class="r-cont"]/p[1]')
        for i in price_list:
            a = i.text
            print(a)
            teacher.append(a)
        # # image图片链接
        image_list = driver.find_elements_by_xpath('//div[@class="dp-guest"]//div[@class="l-wrap col-md-8 coverImage"]/img')
        for i in image_list:
            a = i.get_attribute('src')
            print(a)
            image.append(a)
        #http://dapengjiaoyu.cn/%E5%A4%A7%E9%B9%8F%E6%95%99%E8%82%B2JAVA%E5%B0%8F%E7%99%BD%E8%AF%95%E5%AD%A6%E7%B2%BE%E5%93%81%E8%AF%BE_%20%E5%A4%A7%E9%B9%8F%E6%95%99%E8%82%B2-%E9%AB%98%E5%93%81%E8%B4%A8%E7%9A%84%E8%AE%BE%E8%AE%A1%E5%B8%88%E5%9C%A8%E7%BA%BF%E6%95%99%E8%82%B2_files/jj89uw9n.jpg
        driver.close()
    print(len(name), len(src), len(teacher), len(image))
    driver1.close()
    return name, src, teacher, image


def INmysql(name, src,  teacher):
    db = pymysql.Connect(host='localhost', user='root', password='123456', port=3306, db='test')
    cursor = db.cursor()
    # try:
    for i in range(len(name)):
        cursor.execute("insert into dapeng(name,src,teacher) values(%s,%s,%s)",
                       (name[i], src[i], teacher[i]))
        db.commit()
    # except:
    #     print("出错啦！")
    cursor.close()
    db.close()



if __name__ == '__main__':
    url="http://dapengjiaoyu.cn/index.html"
    driver = get_data(url)
    name, src, teacher, image= XPath(driver)
    INmysql(name, src, teacher)
    # INMongo(name, present, image)

# https://www.dushu.com/book/1107.html
# https://www.dushu.com/book/1107_2.html

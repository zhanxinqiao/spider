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
    js = 'document.documentElement.scrollTop=100000'
    brower.execute_script(js)
    # print(brower.page_source)
    return brower
    #有界面模式
    # driver = webdriver.Chrome(r'../chromedriver.exe')
    # driver.get(url)
    # time.sleep(3)
    # return driver


def XPath(driver1):
    name_list = driver1.find_elements_by_xpath('//div[@class="video-list row"]//div[@class="bili-video-card"]/div[2]//div[@class="bili-video-card__info--right"]/a/h3')
    # name  课程名
    name = []
    for n in name_list:
        a = n.get_attribute('title')  # 获取元素属性
        name.append(a)
        print(a)
    print(len(name))
    # src书的链接
    src_list = driver1.find_elements_by_xpath('//div[@class="video-list row"]//div[@class="bili-video-card"]/div[2]//div[@class="bili-video-card__info--right"]/a')
    src = []
    for s in src_list:
        a = s.get_attribute('href')
        print(a)
        src.append(a)
    print(len(src))
    time_list=driver1.find_elements_by_xpath('//div[contains(@class,"video-list-item col_3 col_xs_1_5 col_md_2 col_xl_1_7")]//div[@class="bili-video-card"]/div[2]//div[@class="bili-video-card__mask"]//span[@class="bili-video-card__stats__duration"]')
    timed=[]
    for s in time_list:
        a=s.text
        print(a)
        timed.append(a)
    print(len(timed))

    # present=[]
    # for i in src:
    #     driver = get_data(i)
    #     # intr 书籍介绍
    #     present_list = driver.find_elements_by_xpath('/html/body/div[6]/div[1]/div[4]/div/div')
    #     for i in present_list:
    #         a = i.text
    #         print(a)
    #         present.append(a)
    #
    #
    #     driver.close()
    driver1.close()
    return name, src,timed


def INmysql(name, src,timed):
    db = pymysql.Connect(host='localhost', user='root', password='123456', port=3306, db='spider')
    cursor = db.cursor()
    # try:
    for i in range(len(name)):
        cursor.execute("insert into bilibili(name,src,time) values(%s,%s,%s)",
                       (name[i], src[i], timed[i]))
        db.commit()
    # except:
    #     print("出错啦！")
    cursor.close()
    db.close()

# def INMongo(name, src, present, author, price, image):
#     client=MongoClient('mongodb://localhost:27017')
#     database=client['my_test']
#     for i in range(len(name)):
#         database.sppider.insert_many([{'name':name[i], 'src':src[i], 'present':present[i],
#                                        'author':author[i], 'price':price[i], 'image':image[i]}])


if __name__ == '__main__':
    start_page = int(input("请输入开始爬取的页面："))
    end_page = int(input("请输入结束爬取的页面："))
    for i in range(start_page, end_page + 1):
        url = 'https://search.bilibili.com/all?keyword=%E5%A4%A7%E6%95%B0%E6%8D%AE%E8%AF%BE%E7%A8%8B&from_source=webtop_search&spm_id_from=333.1007&page=' + str(i)
        driver = get_data(url)
        XPath(driver)
        # name, src,timed = XPath(driver)
        # INmysql(name, src,timed)
        # INMongo(name, src, present, author, price, image)


#https://search.bilibili.com/all?keyword=%E5%A4%A7%E6%95%B0%E6%8D%AE%E8%AF%BE%E7%A8%8B&from_source=webtop_search&spm_id_from=333.1007
# https://search.bilibili.com/all?keyword=%E5%A4%A7%E6%95%B0%E6%8D%AE%E8%AF%BE%E7%A8%8B&from_source=webtop_search&spm_id_from=333.1007&page=2&o=36
# https://search.bilibili.com/all?keyword=%E5%A4%A7%E6%95%B0%E6%8D%AE%E8%AF%BE%E7%A8%8B&from_source=webtop_search&spm_id_from=333.1007&page=3&o=72
#to_hide_xs to_hide_md to_hide_xl video-list-item col_3 col_xs_1_5 col_md_2 col_xl_1_7

# link://div[@class="video-list row"]//div[@class="bili-video-card"]/div[2]//div[@class="bili-video-card__info--right"]/a/@href
# name://div[@class="video-list row"]//div[@class="bili-video-card"]/div[2]//div[@class="bili-video-card__info--right"]/a/h3/@title
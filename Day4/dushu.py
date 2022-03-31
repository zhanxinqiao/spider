import re
import time

import pymysql
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_data(url):
    #无界面模式
    # chrom_options=Options()
    # chrom_options.add_argument('--headless')
    # chrom_options.add_argument('--disable-gpu')
    # path = r'../chromedriver.exe'
    # # path=r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    # chrom_options.binary_location = path
    # brower=webdriver.Chrome(chrome_options=chrom_options)
    # driver=brower.get(url)
    # return driver
    #有界面模式
    driver = webdriver.Chrome(r'../chromedriver.exe')
    driver.get(url)
    time.sleep(3)
    return driver


def XPath(driver1):
    name_list = driver1.find_elements_by_xpath('//ul//div[@class="book-info"]//h3/a')
    # name书名
    name = []
    for n in name_list:
        a = n.get_attribute('title')  # 获取元素属性
        name.append(a)
        print(a)
    print(len(name))
    # src书的链接
    src_list = driver1.find_elements_by_xpath('//ul//div[@class="book-info"]//h3/a')
    src = []
    for s in src_list:
        a = s.get_attribute('href')
        print(a)
        src.append(a)
    print(len(src))
    present, author, price, image = [], [], [], []
    for i in src:
        driver = get_data(i)
        # intr 书籍介绍
        present_list = driver.find_elements_by_xpath('/html/body/div[6]/div[1]/div[4]/div/div')
        for i in present_list:
            a = i.text
            print(a)
            present.append(a)

        # # author作者
        author_list = driver.find_elements_by_xpath('/html/body/div[6]/div[1]/div[5]/div/div')
        for i in author_list:
            a = i.text
            print(a)
            author.append(a)

        # # price价格
        price_list = driver.find_elements_by_xpath('//*[@id="ctl00_c1_bookleft"]/p/span')
        for i in price_list:
            a = i.text
            print(a)
            price.append(a)

        # # image图片链接
        image_list = driver.find_elements_by_xpath('//div[@class="pic"]/img')
        for i in image_list:
            a = i.get_attribute('src')
            print(a)
            image.append(a)
        driver.close()
    print(len(name), len(src), len(present), len(author), len(price), len(image))
    driver1.close()
    return name, src, present, author, price, image


# def INmysql(name, src, present, author, price, image):
#     db = pymysql.Connect(host='localhost', user='root', password='123456', port=3306, db='spider')
#     cursor = db.cursor()
#     # try:
#     for i in range(len(name)):
#         cursor.execute("insert into dushubook(name,image,src,present,price,author) values(%s,%s,%s,%s,%s,%s)",
#                        (name[i], image[i], src[i], present[i], price[i], author[i]))
#         db.commit()
#     # except:
#     #     print("出错啦！")
#     cursor.close()
#     db.close()

def INMongo(name, src, present, author, price, image):
    client=MongoClient('mongodb://localhost:27017')
    database=client['my_test']
    for i in range(len(name)):
        database.sppider.insert_many([{'name':name[i], 'src':src[i], 'present':present[i],
                                       'author':author[i], 'price':price[i], 'image':image[i]}])


if __name__ == '__main__':
    start_page = int(input("请输入开始爬取的页面："))
    end_page = int(input("请输入结束爬取的页面："))
    for i in range(start_page, end_page + 1):
        url = 'https://www.dushu.com/book/1107_' + str(i) + '.html'
        driver = get_data(url)
        name, src, present, author, price, image = XPath(driver)
        # INmysql(name, src, present, author, price, image)
        INMongo(name, src, present, author, price, image)

# https://www.dushu.com/book/1107.html
# https://www.dushu.com/book/1107_2.html

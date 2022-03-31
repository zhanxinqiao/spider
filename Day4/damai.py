from selenium import webdriver
import time
#import pymysql
import re
import csv

def get_data(url,i):
    driver = webdriver.Chrome(r'../chromedriver.exe')
    driver.get(url)
    driver.maximize_window()
    time.sleep(3)
    if i==1:
        return driver
    else:
        for a in range(i-1):
            butten=driver.find_element_by_class_name('btn-next')
            butten.click()
        return driver
def XPath(driver):
    #演出名称
    name_list = driver.find_elements_by_xpath('//div[@class="items"]//div[@class="items__txt__title"]/a')
    name=[]
    for a in name_list:
        b=a.text
        name.append(b)
    print(len(name))
    print(name)
    #详情页网址
    src_list=driver.find_elements_by_xpath('//div[@class="items"]//div[@class="items__txt__title"]/a')
    src=[]
    for c in src_list:
        d=c.get_attribute('href')
        src.append(d)
    print(len(src))
    print(src)
    #演出描述
    describe_list=driver.find_elements_by_xpath('//div[@class="items"]//span[@class="items__img__tag"]')
    describe=[]
    for e in describe_list:
        f=e.text
        describe.append(f)
    print(len(describe))
    print(describe)
    #演出时间
    time,place=[],[]
    for i in range(len(src)):
        dri = get_data(src[i],1)
        time_list=dri.find_elements_by_xpath('//div[@class="address"]/div[@class="time"]')
        for t in time_list:
            z = t.text
            time.append(z)
        place_list=dri.find_elements_by_xpath('//div[@class="address"]/div[@class="place"]')
        for p in place_list:
            l=p.text
            place.append(l)
        dri.close()
    print(time)
    print(len(time))
    print(place)
    print(len(place))
    #票价
    price_list=driver.find_elements_by_xpath('//div[@class="items"]//div[@class="items__txt__price"]/span')
    price = []
    for p in price_list:
        i=p.text
        price.append(i)
    print(price)
    print(len(price))
    driver.close()
    return name,src,describe,time,place,price

if __name__ == '__main__':
    url = "https://search.damai.cn/search.htm"
    with open('./damai.csv','w+',encoding='utf-8') as pf:
        write=csv.DictWriter(pf,fieldnames=['name','src','describe','time','place','price'])
        write.writeheader()
        for i in range(1,4):
           a=get_data(url,i)
           name,src,describe,time,place,price=XPath(a)
           for i in range(len(name)):
               write.writerow({'name':name[i],'src':src[i],'describe':describe[i],'time':time[i],'place':place[i],'price':price[i]})



#1 https://search.damai.cn/search.htm?spm=a2oeg.home.category.ditem_0.ac2323e1H1wVG7&ctl=%E6%BC%94%E5%94%B1%E4%BC%9A&order=1&cty=
#2 https://search.damai.cn/search.htm?spm=a2oeg.home.category.ditem_0.ac2323e1H1wVG7&ctl=%E6%BC%94%E5%94%B1%E4%BC%9A&order=1&cty=
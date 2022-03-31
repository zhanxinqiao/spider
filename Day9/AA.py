import csv
import random
import urllib.request
from random import randint
from selenium import webdriver
from lxml import etree
from pymongo import MongoClient


def data_get(url):
    headers = {
        'Cookie': '_language=zh_CN; acw_tc=2f624a7916397202027533908e746d4aa5521fb5bbf1ef62b98b681aef3b31; JSESSIONID=2146FEF4A2ED023EBAFEB432B3F8D6B6',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    ip = [
        {'http': '111.77.97.148:47632'},
        {'http': '106.46.33.38:37150'}
    ]
    proxies = random.choice(ip)
    handler = urllib.request.ProxyHandler(proxies=proxies)
    opener = urllib.request.build_opener(handler)
    response = opener.open(request)
    content = response.read().decode('utf-8')
    return content


def XPath(content):
    jpg = []
    html = etree.HTML(content)
    name= html.xpath('//div[@class="home_product-list__2FH2V"]//div[@class="product_product-name__1wAJ0"]/text()')
    print(len(name))
    print(name)
    link_list= html.xpath('//div[@class="home_product-list__2FH2V"]/a/@href')
    for link in link_list:
        content2=data_get("https://mall.masadora.net"+link)
        html2=etree.HTML(content2)
        jpg1=html2.xpath('//div[@class="productDetail_cover__1AVEG"]/img/@src')
        print(jpg1[0])
        jpg.append(jpg1[0])
    print(name, len(name))
    print(jpg, len(jpg))
    return name, jpg

def INMongo(name, jpg):
    client=MongoClient('mongodb://localhost:27017')
    database=client['my_test']
    for i in range(len(name)):
        database.aa.insert_many([{'name':name[i], 'jpg':jpg[i]}])

if __name__ == '__main__':
    url = 'https://mall.masadora.net/?size=64&categoryId=54'
    content = data_get(url)
    name, jpg = XPath(content)
    INMongo(name,jpg)

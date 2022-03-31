import csv
import random
import urllib.request
from random import randint
from selenium import webdriver
from lxml import etree
from pymongo import MongoClient


def data_get(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 '
    }
    request = urllib.request.Request(url=url, headers=headers)
    ip = [
        {'http': '221.226.193.147:64161'},
        {'http': '119.49.185.30:42515'}
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
    name= html.xpath('//ul[@class="chart-dashed-list"]//div[@class="media__body"]/h2/a/text()')
    print(len(name))
    print(name)
    link_list= html.xpath('//ul[@class="chart-dashed-list"]//div[@class="media__img"]/a/@href')
    for link in link_list:
        content2=data_get(link)
        html2=etree.HTML(content2)
        jpg1=html2.xpath('//div[@class="subject clearfix"]//a/img/@src')
        print(jpg1[0])
        jpg.append(jpg1[0])
    print(name, len(name))
    print(jpg, len(jpg))
    return name, jpg

def INMongo(name, jpg):
    client=MongoClient('mongodb://localhost:27017')
    database=client['my_test']
    for i in range(len(name)):
        database.doubandushu.insert_many([{'name':name[i], 'jpg':jpg[i]}])

if __name__ == '__main__':
    url = 'https://book.douban.com/latest?tag=%E5%85%A8%E9%83%A8/'
    content = data_get(url)
    name, jpg = XPath(content)
    INMongo(name,jpg)

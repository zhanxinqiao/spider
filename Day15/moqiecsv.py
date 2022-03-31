import csv
import random
import re
import urllib.request
from random import randint

from bs4 import BeautifulSoup
from lxml import etree


def data_get(url):
    headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    ip = [
        {'http': '110.180.120.78:62155'},
        {'http': '202.110.6.213:59553'},
    ]
    proxies = random.choice(ip)
    handler = urllib.request.ProxyHandler(proxies=proxies)
    opener = urllib.request.build_opener(handler)
    response = opener.open(request)
    content = response.read().decode('utf-8')
    return content


def XPath(content):
    name, link= [], []
    html = etree.HTML(content)
    # print(html)
    # print(BeautifulSoup(content,'lxml'))
    #name=//div[@class="tab-content"]//dl//dd//a[@class="bigpic-book-name"]/text()
    #link=//div[@class="tab-content"]//dl//dd//a[@class="bigpic-book-name"]/@href
    nl_list = html.xpath('//ul[@class="chart-dashed-list"]//div[@class="media__body"]/h2/a')
    print(nl_list)
    for nl in nl_list:
        name1 = nl.xpath('.//text()')
        link1 = nl.xpath('.//@href')
        print(name1)
        print(link1)
        for i in range(len(name1)):
            # name=re.findall(r'([\u4e00-\u9fa5].*)',name1)[0]
            name.append(name1[i])
            link.append(link1[i])
    print(name, len(name))
    print(link, len(link))
    return name, link


def down_load(name, link):
    with open('dushu.csv', 'w+', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['name' '\t' 'link'])
        writer.writeheader()
        for i in range(len(name)):
            f.write(name[i] + '\t' + link[i] + '\n')


if __name__ == '__main__':
    url = 'https://book.douban.com/latest?tag=%E5%85%A8%E9%83%A8'
    content = data_get(url)
    name, link = XPath(content)
    down_load(name, link)

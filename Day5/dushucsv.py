import csv
import random
import urllib.request
from random import randint

from lxml import etree


def data_get(url):
    headers = {
        'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    ip = [
        {'http': '121.226.54.105:28566'},
        {'http': '111.76.144.55:35553'}
        # {},
    ]
    proxies = random.choice(ip)
    handler = urllib.request.ProxyHandler(proxies=proxies)
    opener = urllib.request.build_opener(handler)
    response = opener.open(request)
    content = response.read().decode('utf-8')
    return content


def XPath(content):
    name, link, author, present, state = [], [], [], [], []
    html = etree.HTML(content)
    print(html)
    nl_list = html.xpath('//div[@class="bookslist"]//li')
    for nl in nl_list:
        name1 = nl.xpath('.//h3/a/text()')
        link1 = nl.xpath('.//h3/a/@href')
        author1 = nl.xpath('.//p[1]/text()')
        present1 = nl.xpath('.//p[2]/text()')
        state1 = nl.xpath('.//p[3]/span/text()')
        for i in range(len(name1)):
            name.append(name1[i])
            link.append('https:'+link1[i])
            author.append(author1[i])
            present.append(present1[i])
            state.append(state1[i])
    print(name, len(name))
    print(link, len(link))
    print(author, len(author))
    print(present, len(present))
    print(state, len(state))
    return name, link, author, present, state


def down_load(name, link, author, present, state):
    with open('./dushu.csv', 'w+', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['name' '\t' 'link' '\t' 'author' '\t' 'present' '\t' 'state'])
        writer.writeheader()
        for i in range(len(name)):
            f.write(name[i] + '\t' + link[i] + '\t' + author[i] + '\t' + present[i] + '\t' + state[i]+'\n')


if __name__ == '__main__':
    start_page = int(input("请输入开始的页码："))
    end_page = int(input("请输入结束的页码："))
    for i in range(start_page, end_page + 1):
        url = 'https://www.dushu.com/book/1107_' + str(i) + '.html'
        content = data_get(url)
        name, link, author, present, state = XPath(content)
        down_load(name, link, author, present, state)

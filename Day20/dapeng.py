# http://category.dangdang.com/cp01.54.00.00.00.00.html
# http://category.dangdang.com/pg2-cp01.54.00.00.00.00.html
import re
import urllib.parse
import urllib.request

import pymysql
from lxml import etree
from pymongo import MongoClient


def create_request(url):
    header = {
        'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=header)
    return request


def get_context(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def Xpath(context):
    name,src=[],[]
    html = etree.HTML(context)
    name1 = html.xpath('//div[@class="g-slider"]//div[starts-with(@class,"item")]/div/a/img/@alt')
    print(name1)
    for n in name1:
        name.append(n)
    name2 = html.xpath('//div[starts-with(@class,"g-box wow")]/div/a/img/@alt')
    print(name2)
    for n in name2:
        name.append(n)
    src1 = html.xpath('//div[@class="g-slider"]//div[starts-with(@class,"item")]/div/a/@href')
    print(src1)
    for n in src1:
    #http://dapengjiaoyu.cn/aIFunction.html
    #./javatitle.html
        a="http://dapengjiaoyu.cn"+n[1:]
        print(a)
        src.append(a)
    src2 = html.xpath('//div[starts-with(@class,"g-box wow")]/div/a/@href')
    print(src2)
    for n in src2:
        a="http://dapengjiaoyu.cn"+n[1:]
        print(a)
        src.append(a)
    teacher,image=[],[]
    for i in range(len(src)):
        srci =src[i]
        request = create_request(srci)
        context = get_context(request)
        html1 = etree.HTML(context)
        teacher_list = html1.xpath('//div[@class="teacher-info"]/ul/li/div[@class="r-cont"]/p[1]/text()')
        image_list = html1.xpath('//div[@class="dp-guest"]//div[@class="l-wrap col-md-8 coverImage"]/img/@src')
        print(teacher_list)
        print(image_list)
        print("http://dapengjiaoyu.cn"+image_list[0][1:])
        images="http://dapengjiaoyu.cn"+image_list[0][1:]
        teacher.append(teacher_list)
        image.append(images)

    return name,src,teacher,image

def INMongo(name,src,teacher,image):
    client=MongoClient('mongodb://localhost:27017')
    database=client['my_test']
    for i in range(len(name)):
        database.dapeng.insert_many([{'name':name[i],'src':src[i],'teacher':teacher[i],'image':image[i]}])



if __name__ == '__main__':
    url = 'http://dapengjiaoyu.cn/index.html'
    request = create_request(url)
    context = get_context(request)
    name,src,teacher,image=Xpath(context)
    INMongo(name,src,teacher,image)
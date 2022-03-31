# http://category.dangdang.com/cp01.54.00.00.00.00.html
# http://category.dangdang.com/pg2-cp01.54.00.00.00.00.html
import re
import urllib.parse
import urllib.request

import pymysql
from lxml import etree


def create_request(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        'Cookie': '__permanent_id=20211127164456930982710436230689294; ddscreen=2; dest_area=country_id%3D9000%26province_id%3D111%26city_id%3D0%26district_id%3D0%26town_id%3D0; secret_key=a1169844a2507946b18ac1315c906eb2; __visit_id=20211127175502128289610167397866312; __out_refer=; sessionID=pc_1dc37a0954a12ffa55685301d295a2e74f77f350749ca04908f7bfe2b6cded5a; USERNUM=86XGWBkQQRY5kTl3yuCMkQ==; login.dangdang.com=.ASPXAUTH=4ndX2i1Jt416rqj7U9C4e2FybJFRfi9e1RQbcglVuy3C3zJYLC3Ypw==; dangdang.com=email=MTc2NzEwNTcxMjc0NjQ2M0BkZG1vYmlscGhvbmVfX3VzZXIuY29t&nickname=&display_id=1364430381126&customerid=2lEVqGLYXM2NpmY4kf+uVQ==&viptype=vXmNhKWpnes=&show_name=176****7127; __rpm=s_605253.451680112839%2C451680112840.54.1638007171547%7Clogin_page...1638007245992; LOGIN_TIME=1638007255460; __trace_id=20211127180055466285294466718519367'
    }
    request = urllib.request.Request(url=url, headers=header)
    return request


def get_context(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('gbk')
    return content


def down_load(context):
    db = pymysql.Connect(host="localhost", user="root", port=3306, password="123456", db="spider")
    cursor = db.cursor()
    html = etree.HTML(context)
    name_list = html.xpath('//ul[@id="component_59"]//p[@name="title"]/a/text()')
    print(name_list)
    src_list = html.xpath('//ul[@id="component_59"]//p[@name="title"]/a/@href')
    print(src_list)
    present_list2 = []
    for i in range(len(src_list)):
        src = 'https:' + src_list[i]
        request = create_request(src)
        context = get_context(request)
        html1 = etree.HTML(context)
        present_list = html1.xpath('//div[@class="name_info"]//h2/span[1]/text()')
        for i in range(len(present_list)):
            present_list1 = re.findall('\t\t(.*?)    \t', present_list[i])
            present_list2.append(present_list1)
    price_list = html.xpath('//ul[@id="component_59"]//p[@class="price"]/span[1]/text()')
    print(price_list)
    author_list = html.xpath('//ul[@id="component_59"]//p[@class="search_book_author"]//span[1]//a[1]/@title')
    print(author_list)
    image_list = []
    q=0
    if q == 0:
        image1 = html.xpath('//ul[@id="component_59"]//a[@class="pic"]/img/@src')
        for i in range(len(image1)):
            image_list.append(image1[i])
            q=q+1
            break
    if q!=0:
        image2 = html.xpath('//ul[@id="component_59"]//a[@class="pic"]/img/@data-original')
        for i in range(len(image2)):
            image_list.append(image2[i])
    print(image_list)
    try:
        for i in range(len(name_list)):
            name = name_list[i]
            image = 'https:' + image_list[i]
            print(image)
            src = 'https:' + src_list[i]
            present = present_list2[i]
            price = price_list[i]
            author = author_list[i]
            cursor.execute("insert into DDbook(name ,image,src,present,price,author) values (%s,%s,%s,%s,%s,%s)",
                           (name, image, src, present, price, author))
            db.commit()
    except:
        print("出错啦！！")
    cursor.close()
    db.close()


if __name__ == '__main__':
    start_page = int(input('请输入起始页面:'))
    end_page = int(input('请输入结束页面:'))
    for page in range(start_page, end_page + 1):
        url = 'http://category.dangdang.com/pg' + str(page) + '-cp01.54.00.00.00.00.html'
        request = create_request(url)
        context = get_context(request)
        down_load(context)

from bs4 import BeautifulSoup
import urllib.request
url='http://beijing.8684.cn/line1'
response = urllib.request.urlopen(url)
context = response.read().decode('utf-8')
soup=BeautifulSoup(context,'lxml')
print(soup)
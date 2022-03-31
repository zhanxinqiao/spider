from bs4 import BeautifulSoup
import urllib.request
url='https://www.starbucks.com.cn/'
response = urllib.request.urlopen(url)
context = response.read().decode('utf-8')
soup=BeautifulSoup(context,'lxml')
print(soup)
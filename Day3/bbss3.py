from bs4 import BeautifulSoup
soup=BeautifulSoup(open("./test.html",encoding='utf-8'),'lxml')
print(soup)
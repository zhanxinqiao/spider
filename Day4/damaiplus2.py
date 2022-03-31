from selenium import webdriver
import phantomjs
def get_data(url):
    path='../phantomjs.exe'
    browser=webdriver.PhantomJS(path)
    driver=browser.get(url)
    return driver

if __name__ == '__main__':
    url = "https://search.damai.cn/search.htm?spm=a2oeg.home.category.ditem_0.ac2323e1H1wVG7&ctl=%E6%BC%94%E5%94%B1%E4%BC%9A&order=1&cty="
    print(get_data(url))
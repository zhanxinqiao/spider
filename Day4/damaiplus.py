from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def share_brower(url):
    chrom_options=Options()
    chrom_options.add_argument('--headless')
    # chrom_options.add_argument('--disable-gpu')
    # chrom_options.add_argument('--disable-gpu')
    #浏览器安装路径
    path = r'../chromedriver.exe'
    # path=r'"C:\Program Files\Google\Chrome\Application\chrome.exe"'
    chrom_options.binary_location=path
    # chrom_options.binary_location=path
    brower=webdriver.Chrome(executable_path=path)#,chrome_options=chrom_options
    driver=brower.get(url)
    print(driver)
    return driver


if __name__ == '__main__':
    url = "https://search.damai.cn/search.htm?spm=a2oeg.home.category.ditem_0.ac2323e1H1wVG7&ctl=%E6%BC%94%E5%94%B1%E4%BC%9A&order=1&cty="
    # url='https://search.damai.cn/search.htm'
    driver=share_brower(url)
    # for a in driver:
    #     b=a.text
    #     print(b)
    # print(driver)
    # name_list = driver.find_elements_by_xpath('//div[@class="items"]//div[@class="items__txt__title"]/a')
    # print(name_list)
    # name=[]
    # for a in name_list:
    #     b=a.text
    #     name.append(b)
    # print(len(name))
    # print(name)
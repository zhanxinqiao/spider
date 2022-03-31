import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options=Options()
options.add_argument("-headless")
driver=webdriver.Chrome(options=options)
driver.get('https://stackoverflow.com/')
print(driver.page_source)

from selenium import webdriver
from lxml import etree
from time import sleep

bro = webdriver.Chrome(executable_path='./chromedriver.exe')
bro.get('http://fund.eastmoney.com/manager/')

page_text = bro.page_source

tree = etree.HTML(page_text)

manager_list = []

data_list = tree.xpath('//div[@class="datatable"]//a[contains(@title,"基金经理")]')

for data in data_list:
    manager =['http://' + data.xpath('@href')[0], data.xpath('text()')[0]]
    manager_list.append(manager)

print(manager_list)

sleep(5)
bro.quit()

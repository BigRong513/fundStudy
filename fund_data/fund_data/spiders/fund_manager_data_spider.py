# -*- coding = utf-8 -*-
# @Time : 2020/12/16 20:12
# @Author : BigRong
# @File : fund_manager_data_spider.py
# @Software : PyCharm
import  scrapy
from fund_data.items import FundDataItem
from selenium import webdriver

class FundManagerDataSpider(scrapy.Spider):
    name = 'fund_manager_data'

    start_urls = ['http://fund.eastmoney.com/manager/']
    page_number = 1

    def __init__(self):
        self.bro = webdriver.Chrome(executable_path=r'E:/project/fundStudy/chromedriver.exe')

    def parse(self, response):
        sel = scrapy.Selector(response)
        manager_list = sel.xpath('//div[@class="datatable"]/table[@id="datalist"]/tbody//tr')
        for manager in manager_list:
            #print(manager)
            item = FundDataItem()
            new_url = 'http:' + manager.xpath('./td[2]/a/@href').extract_first()
            item['name']        = manager.xpath('./td[2]/a/text()').extract_first()
            item['company']     = manager.xpath('./td[3]/a/text()').extract_first()
            item['work_time']   = manager.xpath('./td[5]/text()').extract_first()
            item['scope']       = manager.xpath('./td[6]/a/text()').extract_first()
            item['best_return'] = manager.xpath('./td[7]/a/text()').extract_first()

            print("before yield manager " + item['name'])
            yield scrapy.Request(url=new_url, callback=self.parse_detail, meta={'item':item})
            print("after yield manager " + item['name'])

        if self.page_number < 49:
            self.page_number += 1
            print("before yield page %d"%(self.page_number))
            yield scrapy.Request(url=response.url, callback=self.parse, dont_filter=True)
            print("after yield page %d"%(self.page_number))

    def parse_detail(self, response):
        item = response.meta['item']
        sel = scrapy.Selector(response)
        fund_list = sel.xpath('//table[@class="ftrs"]')[0].xpath('./tbody//tr')
        for fund in fund_list:
            item['fund_code']   = fund.xpath('./td[1]/a/text()').extract_first()
            item['fund_name']   = fund.xpath('./td[2]/a/text()').extract_first()
            item['fund_type']   = fund.xpath('./td[4]/text()').extract_first()
            item['fund_scope']  = fund.xpath('./td[5]/span[1]/text()').extract_first()
            item['fund_time']   = fund.xpath('./td[6]/text()').extract_first()
            item['fund_day']    = fund.xpath('./td[7]/text()').extract_first()
            item['fund_return'] = fund.xpath('./td[8]/text()').extract_first()

            if None == item['fund_code']:
                item['fund_code'] = ''
            if None == item['fund_name']:
                item['fund_name'] = ''
            if None == item['fund_type']:
                item['fund_type'] = ''
            if None == item['fund_scope']:
                item['fund_scope'] = ''
            if None == item['fund_time']:
                item['fund_time'] = ''
            if None == item['fund_day']:
                item['fund_day'] = ''
            if None == item['fund_return']:
                item['fund_return'] = ''
            print("before yield item " + item['fund_name'])
            yield  item
            print("after yield item " + item['fund_name'])

    def closed(self, spider):
        self.bro.quit()
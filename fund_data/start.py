# -*- coding = utf-8 -*-
# @Time : 2020/12/16 20:10
# @Author : BigRong
# @File : start.py
# @Software : PyCharm

from scrapy import cmdline
cmdline.execute("scrapy crawl fund_manager_data".split(' '))

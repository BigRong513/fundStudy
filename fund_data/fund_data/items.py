# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FundDataItem(scrapy.Item):
    # define the fields for your item here like:
    name        = scrapy.Field()
    company     = scrapy.Field()
    work_time   = scrapy.Field()
    scope       = scrapy.Field()
    best_return = scrapy.Field()
    fund_code   = scrapy.Field()
    fund_name   = scrapy.Field()
    fund_type   = scrapy.Field()
    fund_scope  = scrapy.Field()
    fund_time   = scrapy.Field()
    fund_day    = scrapy.Field()
    fund_return = scrapy.Field()

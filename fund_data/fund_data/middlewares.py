# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from time import sleep

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from scrapy.http import HtmlResponse


class FundDataDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.




    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        url = request.url

        if url in spider.start_urls:
            bro = spider.bro
            page_number = spider.page_number
            if page_number == 1:
                bro.get(url)
            else:
                next_page_label = bro.find_element_by_class_name('lastpage')
                next_page_label.click()
            sleep(2)
            page_text = bro.page_source
            new_response = HtmlResponse(url=url, body=page_text, encoding='utf-8',request=request)
            return new_response
        return response


import scrapy
import re
from ecb_scrapy.items import EcbScrapyItem
from scrapy.http import Request

class ecbSpider(scrapy.Spider):
    name = 'ecb'
    start_urls = ['https://www.ecb.europa.eu/press/pr/activities/mopo/html/index.en.html']

    def parse_detail(self, response):
        EcbScrapyItem = response.meta['part_items']
        detail_all = response.xpath('//article/p/text()').extract()
        content = ''
        for detail in detail_all:
            content = content + detail + '\n'
        EcbScrapyItem['content'] = content
        yield EcbScrapyItem

    def parse(self, response):
        item = EcbScrapyItem()
        dts = response.xpath('//dt').extract()
        dds = response.xpath('//dd/span/a').extract()
        n = 0
        date = {}
        for dt in dts:
            n += 1
            dt = dt[10:14] + '-' + dt[7:9] + '-' + dt[4:6]
            date[n] = dt

        m = 0
        for dd in dds:
            m += 1
            href = 'https://www.ecb.europa.eu' + re.findall(r'["](.*?)["]', dd)[0]
            title = re.findall(r'[>](.*?)[<]', dd)[0]
            item['date'] = date[m]
            item['title'] = title
            item['href'] = href
            yield Request(href, meta={'part_items':EcbScrapyItem(date=item['date'],\
                                      title=item['title'], href=item['href'])}, callback=self.parse_detail)
            if n == 1:
                break

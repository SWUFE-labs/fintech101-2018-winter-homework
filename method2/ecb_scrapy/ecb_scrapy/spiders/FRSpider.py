# import scrapy
# from ecb_scrapy.items import FRScrapyItem
# from scrapy.http import Request
#
# class FRSpider(scrapy.Spider):
#     name = 'FR'
#     start_urls = ['https://www.federalreserve.gov/feeds/press_monetary.xml']
#
#     def parse_detail(self, response):
#         FRScrapyItem = response.meta['part_items']
#         data_all = response.xpath('//div[@class="col-xs-12 col-sm-8 col-md-8"]/p/text()').extract()
#         content = ''
#         for data in data_all:
#             content = content + data + '\n'
#         FRScrapyItem['content'] = content
#         yield FRScrapyItem
#
#     def parse(self, response):
#         item = FRScrapyItem()
#         titles = response.xpath('//item/title/text()').extract()
#         hrefs = response.xpath('//item/link/text()').extract()
#         dates = response.xpath('//item/pubDate/text()').extract()
#         for n in range(len(titles)):
#             item['title'] = titles[n]
#             item['href'] = hrefs[n]
#             month_dict = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06',
#                           'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12',
#                           'ul ': '07', 'ug ': '08'}
#             try:
#                 month = month_dict[dates[n][8:11]]
#             except Exception as e:
#                 print(e)
#                 print(dates[n][8:11])
#             item['date'] = dates[n][12:16] + '-' + month + '-' + dates[n][5:7]
#             yield Request(hrefs[n], meta={'part_items': FRScrapyItem(date=item['date'],\
#                                           title=item['title'], href=item['href'])}, callback=self.parse_detail)
#             # if n == 1:
#             #     break

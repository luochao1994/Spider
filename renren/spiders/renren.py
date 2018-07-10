import json

from scrapy import Request
from scrapy.spiders import Spider
from scrapy.selector import Selector

from renren.items import RenrenItem

class RenrenSpider(Spider):
    name = 'renren'
    domains_url= 'https://www.renrenche.com/'
    start_renren_url ='https://www.renrenche.com/cd/ershouche/'

    def start_requests(self):
        yield Request(self.start_renren_url)

    def parse(self, response):
        sel = Selector(response)
        #  page = sel.xpath('/html/body/div[3]/div[5]/ul/li/a').extract()
        #  total_page = json.loads(page[1]).get('totalPage')
        total_page = sel.xpath('/html/body/div[3]/div[5]/ul/li[7]/a/text()').extract()[0]

        for i in range(1,int(total_page)+1):
            yield Request(self.start_renren_url+'/p'+str(i),
                          callback=self.parse_car)

    def parse_car(self, response):
        sel = Selector (response)
        lis = sel.xpath ('//*[@id="search_list_wrapper"]/div/div/div[1]/ul')
        for li in lis:
            item = RenrenItem ()
            item['car_code'] = li.xpath('./li/a/@data-car-id').extract()[0]
            item['img_src'] = li.xpath ('./li/a/div[1]/img/@src').extract()[0]
            item['title'] = li.xpath ('./li/a/h3/text()').extract()[0]
            item['carinfo'] = li.xpath ('./li/a/div[2]/span').extract()[0]
            item['price'] = li.xpath ('./li/a/div[4]/div').extract()
            item['firstpay'] = li.xpath ('./li/a/div[4]/div/div/div/text()').extract()[0]
            item['type'] = '二手车'
            item['city'] = '成都'

            yield item


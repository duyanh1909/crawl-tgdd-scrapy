# -*- coding: utf-8 -*-
from tgdd.items import TgddItem
from scrapy import Selector
from scrapy.spiders import Spider
from scrapy import Request
import pandas as pd

class Tgdd_crawl (Spider):
    name = "crawl_tgdd"
    allowed_domains = ["thegioididong.com"]
    file_link = pd.read_csv(r'C:\Users\ndduy\Desktop\NCKH_Tre\tgdd\link.csv').link
    start_urls = [url.strip() for url in file_link]
    #start_urls = ['https://www.thegioididong.com/dtdd/oppo-reno3/danh-gia',]
    def parse(self, response):
        root_page = response.url
        try:
            num_pages = int(response.xpath("//div[@class='pagcomment']/a/text()").getall()[-2])+1
            for i in range(1,num_pages,1):
                if i==1:
                    yield Request(url=root_page,dont_filter=(True),callback=self.page_item)
                else:
                    yield Request(url=root_page+'?p='+str(i),dont_filter=(True),callback=self.page_item)
        except:
            yield Request(url=root_page,dont_filter=(True),callback=self.page_item)

    def page_item(self,response):
        datas = Selector(response).xpath("//ul[@class='ratingLst']/li[@class='par ']")
        item = TgddItem()
        brand = response.xpath("//ul[@class='breadcrumb']/li[@class='brand']/a/text()").extract()
        phone = response.xpath("//ul[@class='breadcrumb']/li[4]/a/text()").extract()
        link = r'thegioididong.com'+''.join(response.xpath("//ul[@class='breadcrumb']/li[4]/a/@href").extract())
        for data in datas:
            item['name'] = data.xpath("div[@class='rh']/span/text()").extract()
            item['comment']=data.xpath("div[@class='rc']/p/i/text()").extract()
            item['brand']=''.join(brand)
            item['phone']=''.join(phone)
            item['link']=link
            yield item

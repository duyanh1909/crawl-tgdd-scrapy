import scrapy 
from tgdd.items import TgddItem

class TgddSpider (scrapy.Spider):
    name = 'get_link'
    allowed_domains = ['https://www.thegioididong.com']
    start_urls = ['https://www.thegioididong.com/dtdd',]
    
    def start_requests(self):
        script = """
        function main(splash)
            local url = splash.args.url
            assert(splash:go(url))
            assert(splash:wait(1))
            local element = assert(splash:select('.viewmore'))
            while element ~= nil do
                assert(element:mouse_click())
                assert(splash:wait(1))
                element = splash:select('.viewmore')
            end   
            return {
                html=splash:html(),
                }
        end
        """
        for url in self.start_urls:
            yield scrapy.Request(url,self.parse,meta={"splash":{"args": {"lua_source":script},"endpoint": "execute"}})
    
    def parse(self, response):
        item=TgddItem()    
        for data in response.xpath("//li[@class='item']"):
            item['link']=self.start_urls[0]+data.css('a::attr(href)').extract_first()[5::1]+'/danh-gia'
            yield item
            

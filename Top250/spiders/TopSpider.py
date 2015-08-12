import scrapy
from Top250.items import TopBook

class TopSpider(scrapy.Spider):
    name = "TopSpider"
    allowed_domains = "book.douban.com"

    start_urls = ['http://book.douban.com/top250?start=%s' % (25 * start) for start in range(0, 10)]

    def parse(self, response):
        items = response.css('.item')
        for item in items:
            topbook = TopBook()
            topbook['title'] = item.css('div[class=pl2] a::text').extract()[0]
            title = item.css('div[class=pl2] span::text').extract()
            if title:
                topbook['subtitle'] = title[0]
            topbook['url'] = item.css('div[class=pl2] a::attr(href)').extract()[0]
            meta = item.css('p[class=pl]::text').extract()[0].strip().split('/')
            print meta[-1]
            topbook['author'] = meta[0]
            topbook['publisher'] = meta[-3]
            topbook['pubdate'] = meta[-2]
            topbook['price'] = meta[-1]

            if len(meta) > 4: # if len == 4 , there is no translator
                topbook['translator'] = meta[1]

            yield topbook


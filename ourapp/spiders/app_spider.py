import scrapy


class OurAppSpider(scrapy.Spider):
    name = "first_app"
    allowed_domains = ["wikipedia.org", "it.wikipedia.org"]
    start_urls = [
        "http://it.wikipedia.org/wiki/Serie_A_2013-2014"
    ]

    def parse(self, response):
        for sel in response.xpath('//*[@id="mw-content-text"]/center/table'):
            for tr in sel.xpath('tr'):
                for td in tr.xpath('td'):
                    link = td.xpath('a/@href').extract()
                    print link
                    desc = td.xpath('text()').extract()
                    print desc
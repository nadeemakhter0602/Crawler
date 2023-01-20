import scrapy
from scrapy.selector import Selector


class AccentureSpider(scrapy.Spider):
    name = 'accenture'
    allowed_domains = ['accenture.com']
    start_urls = ['https://www.accenture.com/in-en/jobpostings-sitemap.xml']


    def parse(self, response):
        # inbuilt response.xpath() not working for some reason
        sel = Selector(text=response.text)
        job_posting_links = sel.xpath('//loc/text()').getall()
        pass

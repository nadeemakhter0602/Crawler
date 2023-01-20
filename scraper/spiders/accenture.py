import scrapy
from scrapy.selector import Selector


class AccentureSpider(scrapy.Spider):
    name = 'accenture'
    allowed_domains = ['accenture.com']
    start_urls = ['https://www.accenture.com/in-en/jobpostings-sitemap.xml']

    def parse(self, response):
        # inbuilt response.xpath() not working for some reason
        sel = Selector(text=response.text)
        for job_posting_link in sel.xpath('//loc/text()').getall():
            # follow link and get job posting data
            request = scrapy.Request(job_posting_link,
                                     callback=self.parse_job_posting)
            yield request

    def parse_job_posting(self, response):
        # job dictionary
        job_posting = {
            # get job title
            'job_title': response.xpath('//h1/text()').get(),
            # get job location city
            'job_city': response.xpath('//div/span/text()').get()
        }
        yield job_posting

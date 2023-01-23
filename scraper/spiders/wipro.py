import scrapy
from scrapy.selector import Selector


class WiproSpider(scrapy.Spider):
    name = 'wipro'
    allowed_domains = ['careers.wipro.com']
    start_urls = ['https://careers.wipro.com/sitemap1.xml']

    def parse(self, response):
        # inbuilt response.xpath() not working for some reason
        page_selector = Selector(text=response.text)
        for job_posting in page_selector.xpath('//url').getall():
            job_selector = Selector(text=job_posting)
            # job dictionary
            job_posting = {
                # get job title
                'job_posting_link': job_selector.xpath('//loc/text()').get(),
                # get job location city
                'last_modified': job_selector.xpath('//lastmod/text()').get()
            }
            yield job_posting

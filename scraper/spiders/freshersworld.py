import scrapy
from scrapy.selector import Selector


class FreshersworldSpider(scrapy.Spider):
    name = 'freshersworld'
    allowed_domains = ['www.freshersworld.com']
    start_urls = ['https://www.freshersworld.com/sitemap-activejobs.xml']

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

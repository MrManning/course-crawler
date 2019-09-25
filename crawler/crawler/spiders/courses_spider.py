# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
# from scrapy.crawler import CrawlerProcess
import crawler.items as items


class CoursesSpider(CrawlSpider):
    name = 'courses'
    allowed_domains = ['essex.ac.uk']
    start_urls = ['https://essex.ac.uk/subjects/']

    rules = (
        Rule(LinkExtractor(allow='subjects/'), callback="parse_subject", follow=True)
    )

    def parse_subject(self, response):
        sel = Selector(response)
        for elem in sel.css('div[class^="grid__item"]'):
            subject_item = items.SubjectItems()
            subject_item['subject'] = elem.css('div.subject__title::text').get()
            subject_item['link'] = elem.css('a::attr(href)').get()
            yield subject_item

    def parse_course(self):
        pass

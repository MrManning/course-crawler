# -*- coding: utf-8 -*-
import scrapy
import crawler.items as items

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector


class CoursesSpider(CrawlSpider):
    name = 'courses'
    allowed_domains = ['essex.ac.uk']
    start_urls = ['https://essex.ac.uk/']
    count = 0

    rules = (
        Rule(LinkExtractor(allow=r'/subjects'), callback='parse_subject', follow=True),
    )

    def parse_subject(self, response):
        sel = Selector(response)
        for subject in sel.css('div[class^="grid__item"]'):
            self.count = self.count + 1
            subject_item = items.SubjectItems()
            subject_item['count'] = self.count
            subject_item['subject'] = subject.css('div.subject__title::text').get()
            subject_item['link'] = subject.css('a::attr(href)').get()
            subject_item['courses'] = []

            next_url = response.urljoin(subject_item['link'])
            yield scrapy.Request(next_url, callback=self.parse_course, meta={'subject_item': subject_item})

    def parse_course(self, response):
        subject_item = response.meta['subject_item']
        sel = Selector(response)
        degree_types = [sel.xpath('//div[@id="related-courses-UG"]')]

        for index, type in enumerate(degree_types):
            for course in type.xpath('.//div[@class="grid__item"]'):
                course_title = course.css('h3::text').get().strip().split(" ", 1)

                course_item = items.CourseItems()
                course_item['name'] = course_title[1]
                course_item['degree_type'] = course_title[0]
                course_item['link'] = "load_more_link"

                subject_item['courses'].append(course_item)


            load_more_link = type.xpath('.//div[@id="load-more"]//a[contains(@href, "GetRelatedCourses")]/@href').get()
            if load_more_link is not None:
                next_url = response.urljoin(load_more_link)
                yield scrapy.Request(next_url, callback=self.parse_course, meta={'subject_item': subject_item})
            else:
                yield subject_item

        return
